#!/usr/bin/env python3
"""Reanalysis of The Unjournal's quantitative evaluator ratings.

Sections
  1. describe      counts, coverage of each criterion, anonymity
  2. scale_use     distributions, heaping, straightlining, interval checks
  3. structure     criterion correlations, PCA, redundancy, halo, overall vs parts
  4. reliability   Krippendorff's alpha (interval, bootstrap CI), ICC(1), ICC(1,k)
  5. calibration   do 90% intervals behave like 90% intervals?
  6. journal       should vs will, and predictions against publication outcomes
  7. trends        by year, anonymity, cause area
  8. llm           (optional) agreement with LLM ratings from llm-uj-research-eval
  9. private       (optional) evaluator-level patterns from the private SQLite DB

Default inputs are the public export in data/ (per-paper generic evaluator
labels, no cross-paper identities). Outputs: results.json, CSV tables and PNG
figures in --out. Nothing written here identifies an evaluator.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy import stats  # noqa: E402

warnings.filterwarnings("ignore")
RNG = np.random.default_rng(20261016)

QUAL = ["overall", "claims", "methods", "adv_knowledge", "logic_comms",
        "open_sci", "real_world", "gp_relevance"]
CLASSIC7 = ["overall", "methods", "adv_knowledge", "logic_comms", "open_sci",
            "real_world", "gp_relevance"]
JOURNAL = ["merits_journal", "journal_predict"]
ALL = QUAL + JOURNAL
CANON = {
    "advancing_knowledge": "adv_knowledge", "claims_and_evidence": "claims",
    "claims_evidence": "claims", "open_science": "open_sci",
    "logic_communication": "logic_comms", "global_relevance": "gp_relevance",
    "tier_should": "merits_journal", "tier_will": "journal_predict",
    "journal_should": "merits_journal", "journal_will": "journal_predict",
}
LABEL = {
    "overall": "Overall assessment", "claims": "Claims & evidence",
    "methods": "Methods", "adv_knowledge": "Advancing knowledge",
    "logic_comms": "Logic & communication", "open_sci": "Open science",
    "real_world": "Real-world relevance", "gp_relevance": "Global-priorities relevance",
    "merits_journal": "Journal tier: should", "journal_predict": "Journal tier: will",
}
Z90 = stats.norm.ppf(0.95)  # 1.645
# Okabe-Ito, colour-blind safe, fixed order
PAL = ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#56B4E9", "#D55E00", "#F0E442", "#999999"]
plt.rcParams.update({"figure.dpi": 130, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.alpha": 0.25, "font.size": 9})


# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------
def norm_title(s: str) -> str:
    s = re.sub(r"\s+", " ", str(s)).strip().lower()
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"[^a-z0-9 ]", "", s)


def kripp_alpha_interval(groups):
    """Krippendorff's alpha, interval metric; groups = iterable of arrays (one per unit)."""
    units = [np.asarray(g, float) for g in groups if len(g) >= 2]
    if len(units) < 2:
        return np.nan
    allv = np.concatenate(units)
    n = len(allv)
    do = sum(((u[:, None] - u[None, :]) ** 2).sum() / (len(u) - 1) for u in units) / n
    de = ((allv[:, None] - allv[None, :]) ** 2).sum() / (n * (n - 1))
    return 1 - do / de if de > 0 else np.nan


def bootstrap_alpha(groups, reps=600):
    units = [np.asarray(g, float) for g in groups if len(g) >= 2]
    vals = []
    for _ in range(reps):
        idx = RNG.integers(0, len(units), len(units))
        vals.append(kripp_alpha_interval([units[i] for i in idx]))
    vals = np.array(vals)
    return np.nanpercentile(vals, 2.5), np.nanpercentile(vals, 97.5)


def icc_oneway(groups):
    """ICC(1) and ICC(1,k) from one-way random-effects ANOVA (unbalanced)."""
    gs = [np.asarray(g, float) for g in groups if len(g) >= 2]
    k = len(gs)
    if k < 2:
        return dict(icc1=np.nan, icc1k=np.nan, msw=np.nan, msb=np.nan, n0=np.nan)
    N = sum(len(g) for g in gs)
    grand = np.concatenate(gs).mean()
    ssb = sum(len(g) * (g.mean() - grand) ** 2 for g in gs)
    ssw = sum(((g - g.mean()) ** 2).sum() for g in gs)
    msb, msw = ssb / (k - 1), ssw / (N - k)
    n0 = (N - sum(len(g) ** 2 for g in gs) / N) / (k - 1)
    icc1 = (msb - msw) / (msb + (n0 - 1) * msw)
    icc1k = (msb - msw) / msb
    return dict(icc1=icc1, icc1k=icc1k, msw=msw, msb=msb, n0=n0)


def raters_needed(icc1, target):
    if not np.isfinite(icc1) or icc1 <= 0:
        return np.nan
    return target * (1 - icc1) / (icc1 * (1 - target))


def nan_corr(x, y, method="pearson"):
    m = np.isfinite(x) & np.isfinite(y)
    if m.sum() < 4:
        return np.nan, int(m.sum())
    if method == "pearson":
        return stats.pearsonr(x[m], y[m])[0], int(m.sum())
    return stats.spearmanr(x[m], y[m])[0], int(m.sum())


def jsonable(o):
    if isinstance(o, dict):
        return {str(k): jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else round(float(o), 4)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, pd.DataFrame):
        return jsonable(o.to_dict(orient="records"))
    return o


# ----------------------------------------------------------------------------
# loading
# ----------------------------------------------------------------------------
def load_ratings(path, research_path, extra=None):
    d = pd.read_csv(path)
    if extra is not None and Path(extra).exists():
        e = pd.read_csv(extra)
        d = pd.concat([d, e], ignore_index=True)
    d["criteria"] = d["criteria"].astype(str).str.strip().replace(CANON)
    d = d[d["criteria"].isin(ALL)].copy()
    for c in ["middle_rating", "lower_CI", "upper_CI"]:
        d[c] = pd.to_numeric(d[c], errors="coerce")
    d = d.dropna(subset=["research", "evaluator"])
    d["research"] = d["research"].astype(str).str.replace(r"\s+", " ", regex=True).str.strip()
    bad = d["research"].str.lower().str.contains("test paper|testing a submission|upload test|submission check")
    d = d[~bad]
    d = d.drop_duplicates(["research", "evaluator", "criteria"]).copy()
    d["created"] = pd.to_datetime(d["row_created_date"], errors="coerce", utc=True)
    d["year"] = d["created"].dt.year
    if "evaluator_is_anonymous" in d.columns:
        d["anon"] = d["evaluator_is_anonymous"].astype(str).str.lower().eq("true")
    else:
        d["anon"] = d["evaluator"].astype(str).str.match(r"^Evaluator \d+$")
    d["eval_id"] = d["research"] + " || " + d["evaluator"].astype(str)
    d["key"] = d["research"].map(norm_title)
    r = pd.read_csv(research_path)
    r["key"] = r["label_paper_title"].map(norm_title)
    r = r.drop_duplicates("key")
    d = d.merge(r[["key", "main_cause_cat_abbrev", "publication_status", "doi"]], on="key", how="left")
    d["has_ci"] = d["lower_CI"].notna() & d["upper_CI"].notna()
    d["width"] = d["upper_CI"] - d["lower_CI"]
    d["is_qual"] = d["criteria"].isin(QUAL)
    return d


def add_paper_meta(d, meta_path):
    if meta_path is None or not Path(meta_path).exists():
        d["stream"] = np.nan
        d["uj_pub_date"] = pd.NaT
        d["journal_title"] = np.nan
        return d
    m = pd.read_csv(meta_path)
    m["key"] = m["title"].map(norm_title)
    m = m[m["status"].astype(str).str.startswith("50")].drop_duplicates("key")
    m["stream"] = np.where(m["stream_flags"].astype(str).str.contains("Applied", case=False), "applied", "academic")
    m["uj_pub_date"] = pd.to_datetime(m["publication_date_unjournal"], errors="coerce")
    m = m.rename(columns={"journal_title_doi": "journal_title", "publication_status": "pub_status_coda"})
    d = d.merge(m[["key", "stream", "uj_pub_date", "journal_title", "pub_status_coda", "cause_abbrev"]], on="key", how="left")
    d["main_cause_cat_abbrev"] = d["main_cause_cat_abbrev"].fillna(d["cause_abbrev"])
    return d


def to_wide(d):
    mid = d.pivot_table(index="eval_id", columns="criteria", values="middle_rating", aggfunc="first")
    lo = d.pivot_table(index="eval_id", columns="criteria", values="lower_CI", aggfunc="first")
    hi = d.pivot_table(index="eval_id", columns="criteria", values="upper_CI", aggfunc="first")
    meta = d.groupby("eval_id").agg(research=("research", "first"), anon=("anon", "first"),
                                    year=("year", "min"), area=("main_cause_cat_abbrev", "first"),
                                    stream=("stream", "first"), uj_pub_date=("uj_pub_date", "first")).reset_index()
    meta = meta.set_index("eval_id").loc[mid.index].reset_index()
    return mid, lo, hi, meta


def pairs_table(d, crit):
    sub = d[(d.criteria == crit) & d.middle_rating.notna()]
    out = []
    for res, g in sub.groupby("research"):
        if len(g) < 2:
            continue
        rows = g[["eval_id", "middle_rating", "lower_CI", "upper_CI"]].values
        for i in range(len(rows)):
            for j in range(len(rows)):
                if i != j:
                    out.append((res, rows[i][0], rows[j][0], rows[i][1], rows[i][2], rows[i][3],
                                rows[j][1], rows[j][2], rows[j][3]))
    return pd.DataFrame(out, columns=["research", "i", "j", "mid_i", "lo_i", "hi_i", "mid_j", "lo_j", "hi_j"])


# ----------------------------------------------------------------------------
# 1. describe
# ----------------------------------------------------------------------------
def describe(d, mid, meta, out):
    res = {}
    res["n_ratings"] = int(len(d))
    res["n_papers"] = int(d.research.nunique())
    res["n_evaluations"] = int(d.eval_id.nunique())
    per_paper = d.groupby("research").eval_id.nunique()
    res["evaluations_per_paper"] = per_paper.value_counts().sort_index().to_dict()
    res["share_anonymous_evaluations"] = float(meta.anon.mean())
    res["n_papers_2plus"] = int((per_paper >= 2).sum())
    cov = d.groupby("criteria").agg(n=("middle_rating", "count"), n_ci=("has_ci", "sum")).reindex(ALL)
    cov["share_of_evaluations"] = cov["n"] / res["n_evaluations"]
    cov["share_with_ci"] = cov["n_ci"] / cov["n"]
    cov.to_csv(out / "tbl_criterion_coverage.csv")
    res["criterion_coverage"] = cov.reset_index().rename(columns={"index": "criteria"})
    yr = d.groupby("year").eval_id.nunique()
    res["evaluations_by_entry_year"] = {int(k): int(v) for k, v in yr.items() if pd.notna(k)}
    if meta.stream.notna().any():
        res["evaluations_by_stream"] = meta.stream.value_counts(dropna=False).to_dict()
    if meta.uj_pub_date.notna().any():
        res["evaluations_by_uj_publication_year"] = meta.uj_pub_date.dt.year.value_counts().sort_index().to_dict()
    return res


# ----------------------------------------------------------------------------
# 2. scale use
# ----------------------------------------------------------------------------
def scale_use(d, mid, lo, hi, meta, out):
    res = {}
    q = d[d.is_qual]
    g = q.groupby("criteria").middle_rating
    tab = pd.DataFrame({
        "n": g.count(), "mean": g.mean(), "sd": g.std(), "median": g.median(),
        "p10": g.quantile(0.1), "p90": g.quantile(0.9), "min": g.min(), "max": g.max(),
        "share_ge_90": g.apply(lambda s: (s >= 90).mean()),
        "share_ge_80": g.apply(lambda s: (s >= 80).mean()),
        "share_le_30": g.apply(lambda s: (s <= 30).mean()),
        "share_eq_50": g.apply(lambda s: (s == 50).mean()),
        "share_mult5": g.apply(lambda s: (np.isclose(s % 5, 0)).mean()),
        "share_mult10": g.apply(lambda s: (np.isclose(s % 10, 0)).mean()),
    }).reindex([c for c in QUAL if c in g.groups])
    tab.to_csv(out / "tbl_scale_use_percentile.csv")
    res["percentile_criteria"] = tab.reset_index()
    j = d[d.criteria.isin(JOURNAL)]
    gj = j.groupby("criteria").middle_rating
    tabj = pd.DataFrame({
        "n": gj.count(), "mean": gj.mean(), "sd": gj.std(), "median": gj.median(),
        "share_integer": gj.apply(lambda s: np.isclose(s % 1, 0).mean()),
        "share_half_steps": gj.apply(lambda s: (np.isclose(s % 0.5, 0) & ~np.isclose(s % 1, 0)).mean()),
        "share_ge_4": gj.apply(lambda s: (s >= 4).mean()), "share_le_1": gj.apply(lambda s: (s <= 1).mean()),
    })
    tabj.to_csv(out / "tbl_scale_use_journal.csv")
    res["journal_criteria"] = tabj.reset_index()

    # all-criteria mean distribution: is the overall percentile distribution plausible?
    ov = q[q.criteria == "overall"].middle_rating.dropna()
    res["overall_share_above_50"] = float((ov > 50).mean())
    res["overall_share_above_70"] = float((ov > 70).mean())
    res["overall_ks_vs_uniform_p"] = float(stats.kstest(ov / 100, "uniform").pvalue)

    # straightlining (percentile criteria only)
    qm = mid[[c for c in QUAL if c in mid.columns]]
    nq = qm.notna().sum(axis=1)
    rng_ = qm.max(axis=1) - qm.min(axis=1)
    sd_ = qm.std(axis=1)
    res["straightline"] = {
        "n_evaluations_with_4plus_percentile_criteria": int((nq >= 4).sum()),
        "n_all_identical": int(((sd_ == 0) & (nq >= 4)).sum()),
        "n_range_le_5": int(((rng_ <= 5) & (nq >= 4)).sum()),
        "n_range_le_10": int(((rng_ <= 10) & (nq >= 4)).sum()),
        "median_within_evaluation_range": float(rng_[nq >= 4].median()),
        "median_within_evaluation_sd": float(sd_[nq >= 4].median()),
    }

    # interval checks (percentile criteria)
    c = q.copy()
    c["missing_ci"] = ~c.has_ci
    c["misspecified"] = c.has_ci & ((c.lower_CI > c.middle_rating) | (c.upper_CI < c.middle_rating) | (c.lower_CI > c.upper_CI))
    c["degenerate"] = c.has_ci & (c.lower_CI == c.upper_CI)
    c["uninformative"] = c.has_ci & (c.width >= 100)
    c["touches_bound"] = c.has_ci & ((c.upper_CI >= 100) | (c.lower_CI <= 0))
    c["asym"] = (c.upper_CI - c.middle_rating) - (c.middle_rating - c.lower_CI)
    c["centered"] = c.has_ci & (c.asym.abs() <= 1)
    c["mid_at_lower_edge"] = c.has_ci & (c.middle_rating == c.lower_CI) & (c.width > 0)
    c["mid_at_upper_edge"] = c.has_ci & (c.middle_rating == c.upper_CI) & (c.width > 0)
    ok = c[c.has_ci & ~c.misspecified]
    res["interval_checks"] = {
        "n_percentile_ratings": int(len(c)),
        "n_missing_ci": int(c.missing_ci.sum()),
        "n_misspecified": int(c.misspecified.sum()),
        "n_degenerate": int(c.degenerate.sum()),
        "n_uninformative_0_100": int(c.uninformative.sum()),
        "n_touching_0_or_100": int(c.touches_bound.sum()),
        "share_centered_within_1pt": float(c[c.has_ci].centered.mean()),
        "share_mid_at_lower_edge": float(c[c.has_ci].mid_at_lower_edge.mean()),
        "share_mid_at_upper_edge": float(c[c.has_ci].mid_at_upper_edge.mean()),
        "mean_asymmetry_upper_minus_lower": float(ok.asym.mean()),
        "share_longer_lower_tail": float((ok.asym < -1).mean()),
        "share_longer_upper_tail": float((ok.asym > 1).mean()),
        "width_mean": float(ok.width.mean()), "width_median": float(ok.width.median()),
        "width_p10": float(ok.width.quantile(0.1)), "width_p90": float(ok.width.quantile(0.9)),
        "width_share_le_10": float((ok.width <= 10).mean()),
        "width_share_ge_40": float((ok.width >= 40).mean()),
    }
    wt = ok.groupby("criteria").width.agg(["count", "mean", "median"]).reindex([x for x in QUAL if x in ok.criteria.unique()])
    wt.to_csv(out / "tbl_interval_width_by_criterion.csv")
    res["width_by_criterion"] = wt.reset_index()
    # width by midpoint bin (ceiling effect)
    bins = pd.cut(ok.middle_rating, [-1, 50, 70, 85, 100], labels=["<=50", "51-70", "71-85", "86-100"])
    wb = ok.groupby(bins).width.agg(["count", "mean", "median"])
    wb.to_csv(out / "tbl_interval_width_by_midpoint.csv")
    res["width_by_midpoint_bin"] = wb.reset_index().rename(columns={"middle_rating": "bin"})
    res["width_vs_midpoint_spearman"] = float(stats.spearmanr(ok.middle_rating, ok.width).statistic)
    # within-evaluation width consistency: do evaluators use one width for everything?
    ww = ok.groupby("eval_id").width.agg(["count", "std", "nunique"])
    ww = ww[ww["count"] >= 4]
    res["share_evaluations_single_width"] = float((ww["nunique"] == 1).mean())
    res["share_evaluations_width_sd_le_2"] = float((ww["std"] <= 2).mean())
    # journal-tier intervals
    jj = d[d.criteria.isin(JOURNAL)]
    res["journal_interval"] = {
        "share_with_ci": float(jj.has_ci.mean()),
        "width_median": float(jj[jj.has_ci].width.median()),
        "width_mean": float(jj[jj.has_ci].width.mean()),
    }
    # legacy confidence_level field
    if "confidence_level" in d.columns:
        cl = pd.to_numeric(d.confidence_level, errors="coerce")
        res["n_ratings_with_legacy_confidence_level"] = int(cl.notna().sum())

    # figure: distributions
    crits = [x for x in QUAL if x in q.criteria.unique()]
    fig, axes = plt.subplots(2, 4, figsize=(11, 5), sharex=True)
    for ax, cr in zip(axes.flat, crits):
        v = q[q.criteria == cr].middle_rating.dropna()
        ax.hist(v, bins=np.arange(0, 101, 5), color=PAL[0], edgecolor="white", linewidth=0.6)
        ax.axvline(v.median(), color=PAL[5], lw=1.5)
        ax.set_title(f"{LABEL[cr]} (n={len(v)}, med={v.median():.0f})", fontsize=8)
        ax.set_xlim(0, 100)
    for ax in axes.flat[len(crits):]:
        ax.axis("off")
    fig.suptitle("Distribution of midpoint ratings, 0-100 percentile scale (orange line = median)", fontsize=10)
    fig.tight_layout()
    fig.savefig(out / "fig_distributions.png")
    plt.close(fig)
    # figure: width vs midpoint
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(ok.middle_rating + RNG.normal(0, 0.4, len(ok)), ok.width, s=8, alpha=0.35, color=PAL[0])
    med = ok.groupby(pd.cut(ok.middle_rating, np.arange(0, 101, 10))).width.median()
    ax.plot([i.mid for i in med.index], med.values, color=PAL[5], lw=2, marker="o", ms=4, label="median width per 10-pt bin")
    ax.set_xlabel("Midpoint rating (percentile)")
    ax.set_ylabel("Width of stated 90% interval")
    ax.legend(frameon=False)
    ax.set_title("Stated interval width against the midpoint", fontsize=10)
    fig.tight_layout()
    fig.savefig(out / "fig_width_vs_midpoint.png")
    plt.close(fig)
    return res


# ----------------------------------------------------------------------------
# 3. structure: correlations, PCA, redundancy, halo
# ----------------------------------------------------------------------------
def structure(d, mid, meta, out):
    res = {}
    cols = [c for c in QUAL if c in mid.columns]
    ev = mid[cols]
    corr_ev = ev.corr(min_periods=15)
    corr_ev.to_csv(out / "tbl_corr_evaluation_level.csv")
    pm = mid.join(meta.set_index("eval_id")[["research"]]).groupby("research")[cols].mean()
    corr_pm = pm.corr(min_periods=12)
    corr_pm.to_csv(out / "tbl_corr_paper_mean_level.csv")
    # within-paper deviations (rater halo)
    dev = ev - ev.join(meta.set_index("eval_id")[["research"]]).groupby("research")[cols].transform("mean")
    n_r = ev.join(meta.set_index("eval_id")[["research"]]).groupby("research")[cols].transform("count")
    dev = dev.where(n_r >= 2)
    corr_dev = dev.corr(min_periods=15)
    corr_dev.to_csv(out / "tbl_corr_within_paper_deviations.csv")

    def offdiag_mean(m):
        a = m.values.copy()
        a[np.diag_indices_from(a)] = np.nan
        return float(np.nanmean(a))

    res["mean_offdiag_corr"] = {"evaluation_level": offdiag_mean(corr_ev),
                                "paper_mean_level": offdiag_mean(corr_pm),
                                "within_paper_deviation (rater halo)": offdiag_mean(corr_dev)}
    # PCA on paper means of the classic 7 (complete cases)
    pcs = {}
    for name, cset in [("classic7", CLASSIC7), ("with_claims", QUAL)]:
        cc = pm[[c for c in cset if c in pm.columns]].dropna()
        if len(cc) >= 10:
            z = (cc - cc.mean()) / cc.std()
            u, s, vt = np.linalg.svd(z.values, full_matrices=False)
            var = s ** 2 / (s ** 2).sum()
            pcs[name] = {"n_papers": int(len(cc)), "variance_explained": var[:4].round(3).tolist(),
                         "pc1_loadings": dict(zip(cc.columns, vt[0].round(3).tolist())),
                         "pc2_loadings": dict(zip(cc.columns, vt[1].round(3).tolist()))}
    res["pca_paper_means"] = pcs
    # evaluation-level PCA too
    cc = ev[CLASSIC7].dropna()
    z = (cc - cc.mean()) / cc.std()
    u, s, vt = np.linalg.svd(z.values, full_matrices=False)
    res["pca_evaluation_level_classic7"] = {"n": int(len(cc)), "variance_explained": (s ** 2 / (s ** 2).sum())[:4].round(3).tolist()}

    # leave-one-out predictability (R2) of each criterion from the others, evaluation level
    rows = []
    for c in cols:
        others = [o for o in cols if o != c and o != "claims"] if c != "claims" else [o for o in cols if o != c]
        sub = ev[[c] + others].dropna()
        if len(sub) < 20:
            continue
        X = np.column_stack([np.ones(len(sub)), sub[others].values])
        y = sub[c].values
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        r2 = 1 - ((y - X @ beta) ** 2).sum() / ((y - y.mean()) ** 2).sum()
        # best single predictor
        best = max(others, key=lambda o: abs(nan_corr(sub[c].values, sub[o].values)[0]))
        rows.append({"criteria": c, "n": len(sub), "r2_from_others": r2,
                     "best_single_predictor": best, "r_best": nan_corr(sub[c].values, sub[best].values)[0],
                     "sd": float(ev[c].std())})
    loo = pd.DataFrame(rows)
    loo.to_csv(out / "tbl_redundancy_loo_r2.csv", index=False)
    res["redundancy_loo"] = loo
    # overall vs mean of the parts
    parts = [c for c in cols if c != "overall"]
    pmean = ev[parts].mean(axis=1)
    both = ev["overall"].notna() & (ev[parts].notna().sum(axis=1) >= 3)
    diff = (ev["overall"] - pmean)[both]
    res["overall_vs_parts"] = {
        "n": int(both.sum()), "mean_overall_minus_mean_parts": float(diff.mean()),
        "sd_diff": float(diff.std()), "corr_overall_parts_mean": float(nan_corr(ev["overall"].values, pmean.values)[0]),
        "share_overall_above_parts_mean": float((diff > 0).mean()),
        "share_overall_above_max_part": float(((ev["overall"] - ev[parts].max(axis=1))[both] > 0).mean()),
    }
    # standardized regression of overall on classic parts
    sub = ev[CLASSIC7].dropna()
    z = (sub - sub.mean()) / sub.std()
    X = np.column_stack([np.ones(len(z)), z[[c for c in CLASSIC7 if c != "overall"]].values])
    beta, *_ = np.linalg.lstsq(X, z["overall"].values, rcond=None)
    r2 = 1 - ((z["overall"].values - X @ beta) ** 2).sum() / ((z["overall"].values - z["overall"].mean()) ** 2).sum()
    res["overall_regression"] = {"n": int(len(z)), "r2": float(r2),
                                 "std_betas": dict(zip([c for c in CLASSIC7 if c != "overall"], beta[1:].round(3).tolist()))}
    # figure: correlation heatmaps
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.6))
    for ax, (m, t) in zip(axes, [(corr_ev, "Evaluation level"), (corr_pm, "Paper means"), (corr_dev, "Within-paper deviations (halo)")]):
        im = ax.imshow(m.values, vmin=-1, vmax=1, cmap="RdBu_r")
        ax.set_xticks(range(len(cols)))
        ax.set_xticklabels([LABEL[c] for c in cols], rotation=60, ha="right", fontsize=7)
        ax.set_yticks(range(len(cols)))
        ax.set_yticklabels([LABEL[c] for c in cols] if ax is axes[0] else ["" for _ in cols], fontsize=7)
        ax.grid(False)
        for i in range(len(cols)):
            for j in range(len(cols)):
                v = m.values[i, j]
                if np.isfinite(v) and i != j:
                    ax.text(j, i, f"{v:.2f}", ha="center", va="center", fontsize=6,
                            color="white" if abs(v) > 0.6 else "black")
        ax.set_title(t, fontsize=9)
    fig.colorbar(im, ax=axes, shrink=0.7, label="Pearson r")
    fig.savefig(out / "fig_correlations.png", bbox_inches="tight")
    plt.close(fig)
    return res


# ----------------------------------------------------------------------------
# 4. reliability
# ----------------------------------------------------------------------------
def reliability(d, meta, out, label="all"):
    rows = []
    for c in ALL:
        sub = d[(d.criteria == c) & d.middle_rating.notna()]
        groups = [g.middle_rating.values for _, g in sub.groupby("research") if len(g) >= 2]
        if len(groups) < 5:
            continue
        a = kripp_alpha_interval(groups)
        lo_, hi_ = bootstrap_alpha(groups)
        ic = icc_oneway(groups)
        pr = pairs_table(d, c)
        gaps = (pr.mid_i - pr.mid_j).abs()[pr.i < pr.j] if len(pr) else pd.Series(dtype=float)
        rows.append({
            "criteria": c, "n_papers": len(groups), "n_ratings": int(sum(len(g) for g in groups)),
            "n_pairs": int(len(gaps)), "median_abs_gap": float(gaps.median()) if len(gaps) else np.nan,
            "share_gap_gt_20": float((gaps > 20).mean()) if len(gaps) else np.nan,
            "share_gap_gt_30": float((gaps > 30).mean()) if len(gaps) else np.nan,
            "share_gap_gt_1tier": float((gaps > 1).mean()) if len(gaps) else np.nan,
            "alpha_interval": a, "alpha_ci_lo": lo_, "alpha_ci_hi": hi_,
            "icc1": ic["icc1"], "icc1k_mean_of_raters": ic["icc1k"], "mean_raters": ic["n0"],
            "rater_noise_sd": np.sqrt(ic["msw"]) if np.isfinite(ic["msw"]) else np.nan,
            "between_paper_sd": np.sqrt(max((ic["msb"] - ic["msw"]) / ic["n0"], 0)) if np.isfinite(ic["msb"]) else np.nan,
            "mean_abs_pair_diff": float((pr.mid_i - pr.mid_j).abs().mean()) if len(pr) else np.nan,
            "raters_for_0.7": raters_needed(ic["icc1"], 0.7), "raters_for_0.8": raters_needed(ic["icc1"], 0.8),
        })
    tab = pd.DataFrame(rows)
    tab.to_csv(out / f"tbl_reliability_{label}.csv", index=False)
    return tab


def reliability_subsets(d, meta, out):
    res = {}
    # by anonymity of the paper's raters is not well-defined; do by entry era and stream and area for 'overall'
    for name, mask in [("entry_before_2025", d.year <= 2024), ("entry_2025_on", d.year >= 2025)]:
        sub = d[mask]
        groups = [g.middle_rating.values for _, g in sub[(sub.criteria == "overall") & sub.middle_rating.notna()].groupby("research") if len(g) >= 2]
        if len(groups) >= 5:
            res[name] = {"n_papers": len(groups), "alpha_overall": kripp_alpha_interval(groups),
                         "icc1_overall": icc_oneway(groups)["icc1"]}
    if d.stream.notna().any():
        for s in ["academic", "applied"]:
            sub = d[d.stream == s]
            groups = [g.middle_rating.values for _, g in sub[(sub.criteria == "overall") & sub.middle_rating.notna()].groupby("research") if len(g) >= 2]
            if len(groups) >= 4:
                res[f"stream_{s}"] = {"n_papers": len(groups), "alpha_overall": kripp_alpha_interval(groups)}
    rows = []
    for area, sub in d.groupby("main_cause_cat_abbrev"):
        groups = [g.middle_rating.values for _, g in sub[(sub.criteria == "overall") & sub.middle_rating.notna()].groupby("research") if len(g) >= 2]
        if len(groups) >= 4:
            rows.append({"area": area, "n_papers": len(groups), "alpha_overall": kripp_alpha_interval(groups),
                         "mean_overall": float(sub[sub.criteria == "overall"].middle_rating.mean())})
    res["by_area_overall"] = pd.DataFrame(rows).sort_values("n_papers", ascending=False)
    return res


# ----------------------------------------------------------------------------
# 5. calibration of intervals
# ----------------------------------------------------------------------------
def calibration(d, out):
    res = {}
    rows = []
    allpairs = []
    for c in QUAL:
        pr = pairs_table(d, c)
        if len(pr) < 10:
            continue
        pr = pr[pr.lo_i.notna() & pr.hi_i.notna()].copy()
        pr["covered"] = (pr.lo_i <= pr.mid_j) & (pr.mid_j <= pr.hi_i)
        pr["h_i"] = (pr.hi_i - pr.lo_i) / 2
        pr["h_j"] = (pr.hi_j - pr.lo_j) / 2
        s_i = pr.h_i / Z90
        s_j = pr.h_j.fillna(pr.h_i.median()) / Z90
        pr["expected_if_calibrated"] = 2 * stats.norm.cdf(pr.h_i / np.sqrt(s_i ** 2 + s_j ** 2)) - 1
        pr["disjoint"] = pr.lo_j.notna() & ((pr.hi_i < pr.lo_j) | (pr.hi_j < pr.lo_i))
        pr["criteria"] = c
        allpairs.append(pr)
        emp_sd = float(((pr.mid_i - pr.mid_j) / np.sqrt(2)).std())
        implied_sd = float((pr.h_i / Z90).median())
        rows.append({
            "criteria": c, "n_pairs": len(pr), "n_papers": pr.research.nunique(),
            "coverage_other_midpoint": float(pr.covered.mean()),
            "expected_coverage_if_calibrated": float(pr.expected_if_calibrated.mean()),
            "share_disjoint_intervals": float(pr.disjoint.mean()),
            "median_halfwidth": float(pr.h_i.median()),
            "implied_sd_from_intervals": implied_sd, "empirical_rater_noise_sd": emp_sd,
            "noise_ratio_empirical_over_implied": emp_sd / implied_sd if implied_sd > 0 else np.nan,
            "mean_abs_disagreement": float((pr.mid_i - pr.mid_j).abs().mean()),
        })
    tab = pd.DataFrame(rows)
    tab.to_csv(out / "tbl_calibration_by_criterion.csv", index=False)
    res["by_criterion"] = tab
    ap = pd.concat(allpairs, ignore_index=True)
    res["pooled"] = {
        "n_pairs": int(len(ap)), "coverage_other_midpoint": float(ap.covered.mean()),
        "expected_coverage_if_calibrated": float(ap.expected_if_calibrated.mean()),
        "benchmark_two_calibrated_raters_normal": float(2 * stats.norm.cdf(Z90 / np.sqrt(2)) - 1),
        "share_disjoint_intervals": float(ap.disjoint.mean()),
        # do raters who state wider intervals actually disagree more with their co-rater? (self-knowledge)
        "spearman_own_halfwidth_vs_abs_disagreement": float(stats.spearmanr(ap.h_i, (ap.mid_i - ap.mid_j).abs()).statistic),
        "spearman_own_halfwidth_vs_abs_disagreement_p": float(stats.spearmanr(ap.h_i, (ap.mid_i - ap.mid_j).abs()).pvalue),
    }
    # coverage by width tercile (do wide intervals cover more?)
    ap["width_bin"] = pd.cut(ap.h_i * 2, [-1, 10, 20, 30, 200], labels=["<=10", "11-20", "21-30", ">30"])
    cw = ap.groupby("width_bin").agg(n=("covered", "size"), coverage=("covered", "mean"),
                                     expected=("expected_if_calibrated", "mean"))
    cw.to_csv(out / "tbl_coverage_by_width.csv")
    res["coverage_by_width"] = cw.reset_index()
    # what width would have been needed? scale factor so that coverage hits 90% of other-rater midpoints
    # (interpretable as 'intervals would need to be k times wider')
    ks = np.linspace(1, 4, 61)
    cov_k = [float((((pr_mid := ap.mid_i) - k * ap.h_i <= ap.mid_j) & (ap.mid_j <= pr_mid + k * ap.h_i)).mean()) for k in ks]
    k_needed = next((k for k, cv in zip(ks, cov_k) if cv >= res["pooled"]["benchmark_two_calibrated_raters_normal"]), np.nan)
    res["pooled"]["width_multiplier_to_reach_benchmark"] = float(k_needed)
    # per-evaluation coverage score: share of own intervals covering co-rater midpoints
    pe = ap.groupby("i").agg(n=("covered", "size"), coverage=("covered", "mean"), mean_width=("h_i", lambda s: 2 * s.mean()))
    pe = pe[pe.n >= 4]
    res["per_evaluation_coverage"] = {"n_evaluations": int(len(pe)),
                                      "share_evaluations_coverage_below_50pct": float((pe.coverage < 0.5).mean()),
                                      "share_evaluations_coverage_zero": float((pe.coverage == 0).mean()),
                                      "share_evaluations_full_coverage": float((pe.coverage == 1).mean()),
                                      "corr_width_coverage_spearman": float(stats.spearmanr(pe.mean_width, pe.coverage).statistic)}
    # figure
    fig, ax = plt.subplots(figsize=(7, 4))
    x = np.arange(len(tab))
    ax.bar(x - 0.2, tab.coverage_other_midpoint, 0.4, color=PAL[0], label="Observed: co-evaluator midpoint inside my 90% interval")
    ax.bar(x + 0.2, tab.expected_coverage_if_calibrated, 0.4, color=PAL[1], label="Expected if stated intervals were calibrated")
    ax.axhline(0.9, color="grey", ls="--", lw=1)
    ax.set_xticks(x)
    ax.set_xticklabels([LABEL[c] for c in tab.criteria], rotation=35, ha="right", fontsize=8)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Share of pairs")
    ax.legend(frameon=False, fontsize=7, loc="upper right")
    ax.set_title("Interval coverage: observed versus what calibration implies", fontsize=10)
    fig.tight_layout()
    fig.savefig(out / "fig_coverage.png")
    plt.close(fig)
    return res


# ----------------------------------------------------------------------------
# 6. journal tiers
# ----------------------------------------------------------------------------
JOURNAL_TIER_MANUAL = {
    # 0-5 scale as in the evaluator guidelines; values are our reading of the guidelines' tiers
    "american economic review": 5.0, "quarterly journal of economics": 5.0, "econometrica": 5.0,
    "journal of political economy": 5.0, "review of economic studies": 5.0,
    "american economic review insights": 4.0, "management science": 4.0, "the economic journal": 3.5,
    "economic journal": 3.5, "journal of public economics": 3.5, "aea papers and proceedings": 2.5,
    "the world bank research observer": 2.5, "world bank research observer": 2.5,
    "journal of environmental economics and policy": 2.0, "conservation letters": 3.0,
    "international journal of disaster risk reduction": 2.0, "cognition": 3.5,
    "proceedings of the national academy of sciences": 4.0, "nature human behaviour": 4.5,
    "journal of development economics": 4.0, "journal of the european economic association": 4.0,
    "review of economics and statistics": 4.0, "american economic journal: applied economics": 4.0,
    "journal of economic perspectives": 4.0, "journal of economic literature": 4.0,
    "world development": 3.0, "plos one": 1.5, "food policy": 2.5, "global food security": 3.0,
}
REPOSITORY_WORDS = ("ssrn", "arxiv", "repository", "working paper", "nber", "mimeo", "osf", "zenodo", "research square", "medrxiv", "biorxiv")


def journal(d, mid, lo, hi, meta, out, private_db=None):
    res = {}
    j = mid[JOURNAL].dropna()
    diff = j.merits_journal - j.journal_predict
    t = stats.ttest_rel(j.merits_journal, j.journal_predict)
    res["should_vs_will"] = {
        "n": int(len(j)), "mean_should": float(j.merits_journal.mean()), "mean_will": float(j.journal_predict.mean()),
        "mean_diff": float(diff.mean()), "sd_diff": float(diff.std()), "cohens_d": float(diff.mean() / diff.std()),
        "share_should_gt_will": float((diff > 0).mean()), "share_equal": float((diff == 0).mean()),
        "t": float(t.statistic), "p": float(t.pvalue), "corr": float(nan_corr(j.merits_journal.values, j.journal_predict.values)[0]),
    }
    # should vs will by data-entry year (identical answers are much more common in rows entered in 2024)
    jy = j.join(meta.set_index("eval_id")[["year"]])
    by = jy.groupby("year").apply(lambda g: pd.Series({
        "n": len(g), "share_same_mid": float((g.merits_journal == g.journal_predict).mean()),
        "share_should_gt_will": float((g.merits_journal > g.journal_predict).mean()),
        "share_will_gt_should": float((g.merits_journal < g.journal_predict).mean()),
        "mean_should_minus_will": float((g.merits_journal - g.journal_predict).mean())}))
    by.to_csv(out / "tbl_should_will_by_year.csv")
    res["should_vs_will_by_entry_year"] = by.reset_index()
    # relation to overall
    ov = mid["overall"]
    res["corr_with_overall"] = {c: float(nan_corr(mid[c].values, ov.values)[0]) for c in JOURNAL}
    # outcome check: published journal title from Coda meta (journal_title) + private bibliometrics
    pap = meta.set_index("eval_id")
    jt = d.groupby("research").agg(journal_title=("journal_title", "first"), pub_status=("publication_status", "first"),
                                   pub_status_coda=("pub_status_coda", "first") if "pub_status_coda" in d else ("publication_status", "first"),
                                   uj_pub_date=("uj_pub_date", "first"))
    if private_db and Path(private_db).exists():
        con = sqlite3.connect(private_db)
        bib = pd.read_sql("SELECT paper_title, published_journal, journal_type, publication_date FROM bibliometrics", con)
        con.close()
        bib["key"] = bib.paper_title.map(norm_title)
        jt["key"] = jt.index.map(norm_title)
        jt = jt.reset_index().merge(bib[["key", "published_journal", "journal_type", "publication_date"]], on="key", how="left").set_index("research")
        jt["journal_title"] = jt.journal_title.where(jt.journal_title.notna() & (jt.journal_title.astype(str).str.strip() != ""), jt.published_journal)
    jt["journal_norm"] = jt.journal_title.astype(str).str.lower().str.strip().str.replace(r"^the ", "", regex=True)
    jt["is_repository"] = jt.journal_norm.apply(lambda s: any(w in s for w in REPOSITORY_WORDS)) | jt.journal_norm.isin(["", "nan", "none"])
    jt["actual_tier"] = jt.journal_norm.map(lambda s: JOURNAL_TIER_MANUAL.get(s, JOURNAL_TIER_MANUAL.get("the " + s, np.nan)))
    jt.loc[jt.is_repository, "actual_tier"] = np.nan
    # paper-level mean predictions
    pm = mid.join(pap[["research"]]).groupby("research")[JOURNAL + ["overall"]].mean()
    jt = jt.join(pm)
    jt["any_journal"] = ~jt.is_repository
    status_txt = jt.pub_status.astype(str).str.lower()
    jt["status_group"] = np.select(
        [status_txt.str.contains("top"), status_txt.str.contains("decent|published") & ~status_txt.str.contains("working|not published|unpublished"),
         status_txt.str.contains("revise|r&r|forthcoming")],
        ["published ~top", "published other", "R&R/forthcoming"], default="working paper / other")
    jt.loc[jt.actual_tier.notna(), "status_group"] = jt.loc[jt.actual_tier.notna(), "status_group"].replace({"working paper / other": "published other"})
    grp = jt.groupby("status_group")[["journal_predict", "merits_journal", "overall"]].agg(["count", "mean"])
    grp.columns = ["_".join(c) for c in grp.columns]
    grp.to_csv(out / "tbl_journal_pred_by_outcome_status.csv")
    res["prediction_by_outcome_status"] = grp.reset_index()
    known = jt[jt.actual_tier.notna() & jt.journal_predict.notna()]
    res["n_papers_with_known_journal_tier"] = int(len(known))
    if len(known) >= 5:
        err = known.journal_predict - known.actual_tier
        res["known_tier_check"] = {
            "n": int(len(known)), "mean_pred": float(known.journal_predict.mean()), "mean_actual": float(known.actual_tier.mean()),
            "mean_error_pred_minus_actual": float(err.mean()), "mae": float(err.abs().mean()),
            "spearman_pred_actual": float(stats.spearmanr(known.journal_predict, known.actual_tier).statistic),
            "spearman_should_actual": float(stats.spearmanr(known.merits_journal, known.actual_tier).statistic) if known.merits_journal.notna().sum() >= 5 else np.nan,
            "spearman_overall_actual": float(stats.spearmanr(known.overall, known.actual_tier).statistic),
        }
        # evaluator-level interval coverage of the actual tier
        jp = d[(d.criteria == "journal_predict") & d.has_ci].copy()
        jp = jp.join(jt[["actual_tier"]], on="research")
        jp = jp[jp.actual_tier.notna()]
        if len(jp):
            res["known_tier_check"]["n_evaluator_intervals"] = int(len(jp))
            res["known_tier_check"]["share_intervals_covering_actual"] = float(((jp.lower_CI <= jp.actual_tier) & (jp.actual_tier <= jp.upper_CI)).mean())
            res["known_tier_check"]["share_actual_above_interval"] = float((jp.actual_tier > jp.upper_CI).mean())
            res["known_tier_check"]["share_actual_below_interval"] = float((jp.actual_tier < jp.lower_CI).mean())
    known[["journal_title", "actual_tier", "journal_predict", "merits_journal", "overall"]].round(2).to_csv(out / "tbl_journal_known_outcomes.csv")
    # figure should vs will
    fig, ax = plt.subplots(figsize=(4.5, 4.5))
    ax.plot([0, 5], [0, 5], ls="--", color="grey", lw=1)
    ax.scatter(j.journal_predict + RNG.normal(0, 0.03, len(j)), j.merits_journal + RNG.normal(0, 0.03, len(j)), s=14, alpha=0.5, color=PAL[0])
    ax.set_xlabel("Will be published (predicted tier)")
    ax.set_ylabel("Should be published (merited tier)")
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.set_title(f"Should vs will, n={len(j)} evaluations; {100 * (diff > 0).mean():.0f}% above the line", fontsize=9)
    fig.tight_layout()
    fig.savefig(out / "fig_should_vs_will.png")
    plt.close(fig)
    return res


# ----------------------------------------------------------------------------
# 7. trends and subgroup patterns
# ----------------------------------------------------------------------------
def trends(d, mid, lo, hi, meta, out):
    res = {}
    q = d[d.is_qual & d.middle_rating.notna()]
    # by UJ publication year if available, else entry year
    ycol = "uj_pub_year"
    d2 = q.copy()
    d2[ycol] = d2.uj_pub_date.dt.year if d2.uj_pub_date.notna().any() else d2.year
    d2[ycol] = d2[ycol].fillna(d2.year)
    by = d2[d2.criteria == "overall"].groupby(ycol).agg(n_evals=("eval_id", "nunique"), mean_overall=("middle_rating", "mean"),
                                                        sd_overall=("middle_rating", "std"))
    wid = d2[d2.has_ci].groupby(ycol).width.median().rename("median_width_all_percentile_criteria")
    by = by.join(wid)
    by.to_csv(out / "tbl_by_year.csv")
    res["by_year"] = by.reset_index()
    sl = stats.spearmanr(d2[d2.criteria == "overall"][ycol], d2[d2.criteria == "overall"].middle_rating)
    res["overall_vs_year_spearman"] = {"rho": float(sl.statistic), "p": float(sl.pvalue)}
    # anonymity
    rows = []
    for c in ALL:
        s = d[(d.criteria == c) & d.middle_rating.notna()]
        a, b = s[s.anon].middle_rating, s[~s.anon].middle_rating
        if len(a) >= 8 and len(b) >= 8:
            tt = stats.ttest_ind(a, b, equal_var=False)
            rows.append({"criteria": c, "n_anon": len(a), "n_named": len(b), "mean_anon": a.mean(), "mean_named": b.mean(),
                         "diff_anon_minus_named": a.mean() - b.mean(), "p": tt.pvalue,
                         "width_anon": s[s.anon].width.median(), "width_named": s[~s.anon].width.median()})
    an = pd.DataFrame(rows)
    an.to_csv(out / "tbl_anonymity.csv", index=False)
    res["anonymity"] = an
    # within-paper anonymity comparison (papers with one named and one anonymous rater)
    wp = []
    for c in QUAL:
        s = d[(d.criteria == c) & d.middle_rating.notna()]
        for _, g in s.groupby("research"):
            if g.anon.nunique() == 2:
                wp.append(g[g.anon].middle_rating.mean() - g[~g.anon].middle_rating.mean())
    if len(wp) >= 10:
        wp = np.array(wp)
        res["anonymity_within_paper"] = {"n_paper_criteria": int(len(wp)), "mean_anon_minus_named": float(wp.mean()),
                                         "p_wilcoxon": float(stats.wilcoxon(wp).pvalue)}
    # stream
    if d.stream.notna().any():
        rows = []
        for c in ALL:
            s = d[(d.criteria == c) & d.middle_rating.notna()]
            g = s.groupby("stream").middle_rating.agg(["count", "mean"])
            rows.append({"criteria": c, **{f"{k}_{i}": v for i, r in g.iterrows() for k, v in r.items()}})
        pd.DataFrame(rows).to_csv(out / "tbl_by_stream.csv", index=False)
        res["by_stream"] = pd.DataFrame(rows)
    # cause area means (overall, gp_relevance, methods)
    ar = q[q.criteria.isin(["overall", "gp_relevance", "methods"])].groupby(["main_cause_cat_abbrev", "criteria"]).middle_rating.mean().unstack()
    ar["n_papers"] = q[q.criteria == "overall"].groupby("main_cause_cat_abbrev").research.nunique()
    ar = ar[ar.n_papers >= 3].sort_values("n_papers", ascending=False)
    ar.to_csv(out / "tbl_by_area.csv")
    res["by_area"] = ar.reset_index()
    # figure: by year
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.plot(by.index, by.mean_overall, marker="o", color=PAL[0], label="Mean overall rating")
    ax.plot(by.index, by.median_width_all_percentile_criteria, marker="s", color=PAL[1], label="Median interval width")
    for xi, n in zip(by.index, by.n_evals):
        ax.annotate(f"n={n}", (xi, by.loc[xi, "mean_overall"]), textcoords="offset points", xytext=(0, 6), ha="center", fontsize=7)
    ax.set_xlabel("Year the evaluation was published (fallback: data-entry year)")
    ax.set_ylabel("Points (0-100)")
    ax.legend(frameon=False, fontsize=8)
    ax.set_title("Ratings and interval widths over time", fontsize=10)
    fig.tight_layout()
    fig.savefig(out / "fig_by_year.png")
    plt.close(fig)
    return res


# ----------------------------------------------------------------------------
# 8. LLM comparison
# ----------------------------------------------------------------------------
MODEL_DIRS = {
    "gpt5_pro_updated_jan2026": "GPT-5 Pro", "gpt52_pro_focal_jan2026": "GPT-5.2 Pro",
    "gpt_4o_mini_2024_07_18": "GPT-4o-mini", "claude_sonnet_4_20250514": "Claude Sonnet 4",
    "claude_opus_4_6": "Claude Opus 4.6", "gemini_2.0_flash": "Gemini 2.0 Flash",
}
PAPER_RECODE = {"Trammel and Aschenbrenner 2024": "Trammel and Aschenbrenner 2025", "Liang et al 2023": "Liang et al. 2021"}
DOI_LABELS = {"10.3386/w31162": "Walker et al. 2023", "10.3386/w32728": "Hahn et al. 2025",
              "10.3386/w30011": "Bhat et al. 2022", "10.1093/wbro/lkae010": "Crawfurd et al. 2023"}


def parse_llm_response(path, model):
    r = json.loads(Path(path).read_text(encoding="utf-8"))
    paper = path.name.replace(".response.json", "").replace("_", " ")
    paper = PAPER_RECODE.get(paper, paper)
    parsed = None
    if r.get("parsed"):
        parsed = r["parsed"]
    elif r.get("output_text"):
        txt = re.sub(r"^\s*```[a-z]*\s*\n?", "", r["output_text"])
        txt = re.sub(r"\s*```\s*$", "", txt)
        try:
            parsed = json.loads(txt)
        except json.JSONDecodeError:
            parsed = None
    elif r.get("output"):
        for m in r["output"]:
            if m.get("type") == "message":
                try:
                    parsed = json.loads(m["content"][0]["text"])
                except Exception:  # noqa: BLE001
                    parsed = None
                break
    if not parsed or "metrics" not in parsed:
        return []
    rows = []
    for k, v in parsed["metrics"].items():
        if not isinstance(v, dict):
            continue
        c = CANON.get(k, k)
        if c in JOURNAL:
            rows.append((paper, model, c, v.get("score"), v.get("ci_lower"), v.get("ci_upper")))
        elif c in QUAL:
            rows.append((paper, model, c, v.get("midpoint"), v.get("lower_bound"), v.get("upper_bound")))
    return rows


def llm_compare(d, mid, meta, llm_repo, research_path, out):
    llm_repo = Path(llm_repo)
    rows = []
    for dname, model in MODEL_DIRS.items():
        jd = llm_repo / "results" / dname / "json"
        if not jd.exists():
            continue
        for f in sorted(jd.glob("*.response.json")):
            rows.extend(parse_llm_response(f, model))
    llm = pd.DataFrame(rows, columns=["paper", "model", "criteria", "mid", "lo", "hi"])
    for c in ["mid", "lo", "hi"]:
        llm[c] = pd.to_numeric(llm[c], errors="coerce")
    # map paper label -> research title
    m = pd.read_csv(llm_repo / "data" / "UJ_map.csv", sep=";")
    label2key = {p.strip(): norm_title(t) for p, t in zip(m.paper, m.research)}
    r = pd.read_csv(research_path)
    r["doi_n"] = r.doi.astype(str).str.lower().str.replace(r"^https?://(dx\.)?doi\.org/", "", regex=True).str.replace(r"^doi\.org/", "", regex=True).str.strip()
    for doi, lab in DOI_LABELS.items():
        hit = r[r.doi_n == doi]
        if len(hit):
            label2key[lab] = norm_title(hit.label_paper_title.iloc[0])
    llm["key"] = llm.paper.map(label2key)
    llm = llm[llm.key.notna()]
    res = {"n_llm_rows": int(len(llm)), "n_llm_papers_mapped": int(llm.key.nunique())}
    # human per-paper means and per-rater
    hum = d[d.middle_rating.notna()][["key", "research", "eval_id", "criteria", "middle_rating", "lower_CI", "upper_CI", "width"]]
    hmean = hum.groupby(["key", "criteria"]).agg(h_mean=("middle_rating", "mean"), h_n=("middle_rating", "count"),
                                                 h_width=("width", "mean")).reset_index()
    mm = llm.merge(hmean, on=["key", "criteria"], how="inner")
    mm["llm_width"] = mm.hi - mm.lo
    rows = []
    for (model, c), g in mm.groupby(["model", "criteria"]):
        if len(g) < 8:
            continue
        rows.append({"model": model, "criteria": c, "n_papers": len(g),
                     "spearman": nan_corr(g.mid.values, g.h_mean.values, "spearman")[0],
                     "pearson": nan_corr(g.mid.values, g.h_mean.values)[0],
                     "bias_llm_minus_human": float((g.mid - g.h_mean).mean()),
                     "mae": float((g.mid - g.h_mean).abs().mean()),
                     "sd_llm": float(g.mid.std()), "sd_human_mean": float(g.h_mean.std()),
                     "llm_width_median": float(g.llm_width.median()), "human_width_median": float(g.h_width.median())})
    tab = pd.DataFrame(rows)
    tab.to_csv(out / "tbl_llm_agreement.csv", index=False)
    res["agreement"] = tab
    # LLM as an extra rater: for papers with >=2 humans, compare corr(LLM, H_a) with corr(H_b, H_a)
    rows = []
    for model in llm.model.unique():
        for c in QUAL + JOURNAL:
            lm = llm[(llm.model == model) & (llm.criteria == c)].drop_duplicates("key").set_index("key").mid
            hh = hum[hum.criteria == c]
            papers = [k for k, g in hh.groupby("key") if len(g) >= 2 and k in lm.index]
            if len(papers) < 10:
                continue
            r_lh, r_hh = [], []
            for _ in range(200):
                xa, xb, xl = [], [], []
                for k in papers:
                    v = hh[hh.key == k].middle_rating.values
                    idx = RNG.permutation(len(v))
                    xa.append(v[idx[0]])
                    xb.append(v[idx[1]])
                    xl.append(lm[k])
                xa, xb, xl = map(np.array, (xa, xb, xl))
                r_lh.append(stats.spearmanr(xl, xa).statistic)
                r_hh.append(stats.spearmanr(xb, xa).statistic)
            # alpha with llm added
            groups_h = [hh[hh.key == k].middle_rating.values for k in papers]
            groups_l = [np.append(hh[hh.key == k].middle_rating.values, lm[k]) for k in papers]
            rows.append({"model": model, "criteria": c, "n_papers": len(papers),
                         "spearman_llm_vs_one_human": float(np.mean(r_lh)), "spearman_human_vs_human": float(np.mean(r_hh)),
                         "alpha_humans_only": kripp_alpha_interval(groups_h), "alpha_humans_plus_llm": kripp_alpha_interval(groups_l)})
    extra = pd.DataFrame(rows)
    extra.to_csv(out / "tbl_llm_as_extra_rater.csv", index=False)
    res["llm_as_extra_rater"] = extra
    # within-paper profile agreement: does the LLM reproduce which criteria are relatively strong/weak
    # for a given paper? Compare LLM vs each single human evaluation, and human vs human, on the same footing.
    rows = []
    wide = hum[hum.criteria.isin(QUAL)].pivot_table(index=["key", "eval_id"], columns="criteria", values="middle_rating")
    for model in llm.model.unique():
        lw = llm[(llm.model == model) & llm.criteria.isin(QUAL)].drop_duplicates(["key", "criteria"]).pivot_table(index="key", columns="criteria", values="mid")
        prof = []
        for (k, _), hrow in wide.iterrows():
            if k not in lw.index:
                continue
            lrow = lw.loc[k]
            m_ = hrow.notna() & lrow.reindex(hrow.index).notna()
            if m_.sum() >= 5:
                prof.append(stats.spearmanr(hrow[m_], lrow.reindex(hrow.index)[m_]).statistic)
        prof = [p for p in prof if np.isfinite(p)]
        if len(prof) >= 8:
            rows.append({"model": model, "n_comparisons": len(prof), "mean_within_paper_profile_spearman": float(np.mean(prof)),
                         "share_positive": float(np.mean(np.array(prof) > 0))})
    prof = []
    for k, g in wide.groupby(level=0):
        if len(g) >= 2:
            for a_i in range(len(g)):
                for b_i in range(a_i + 1, len(g)):
                    a, b = g.iloc[a_i], g.iloc[b_i]
                    m_ = a.notna() & b.notna()
                    if m_.sum() >= 5:
                        prof.append(stats.spearmanr(a[m_], b[m_]).statistic)
    prof = [p for p in prof if np.isfinite(p)]
    rows.append({"model": "Human vs human", "n_comparisons": len(prof), "mean_within_paper_profile_spearman": float(np.mean(prof)),
                 "share_positive": float(np.mean(np.array(prof) > 0))})
    pr = pd.DataFrame(rows)
    pr.to_csv(out / "tbl_llm_profile_agreement.csv", index=False)
    res["profile_agreement"] = pr
    # figure: overall, per model
    models = [m for m in ["GPT-5 Pro", "Claude Opus 4.6", "Gemini 2.0 Flash", "GPT-4o-mini"] if m in mm.model.unique()]
    fig, axes = plt.subplots(1, len(models), figsize=(3.2 * len(models), 3.4), sharey=True)
    for ax, model in zip(np.atleast_1d(axes), models):
        g = mm[(mm.model == model) & (mm.criteria == "overall")]
        ax.plot([0, 100], [0, 100], ls="--", color="grey", lw=1)
        ax.scatter(g.h_mean, g.mid, s=14, alpha=0.6, color=PAL[0])
        rho = nan_corr(g.mid.values, g.h_mean.values, "spearman")[0]
        ax.set_title(f"{model}: rho={rho:.2f}, n={len(g)}", fontsize=8)
        ax.set_xlabel("Human mean overall")
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
    np.atleast_1d(axes)[0].set_ylabel("LLM overall")
    fig.suptitle("LLM overall rating versus human mean", fontsize=10)
    fig.tight_layout()
    fig.savefig(out / "fig_llm_vs_human.png")
    plt.close(fig)
    return res


# ----------------------------------------------------------------------------
# 9. private supplement (evaluator-level)
# ----------------------------------------------------------------------------
def private_supplement(private_db, research_path, out):
    con = sqlite3.connect(private_db)
    er = pd.read_sql("SELECT research, evaluator, criteria, middle_rating, lower_CI, upper_CI, row_created_date FROM evaluator_ratings", con)
    epl = pd.read_sql("SELECT evaluator, paper_title, evaluation_stream, years_in_field, papers_reviewed, time_spent, hours_spent, "
                      "overall_rating, methods_rating, adv_knowledge_rating, logic_comms_rating, open_sci_rating, real_world_rating, gp_relevance_rating, claims_rating, "
                      "overall_lower, overall_upper, methods_lower, methods_upper FROM evaluator_paper_level", con)
    con.close()
    er["criteria"] = er.criteria.astype(str).str.strip().replace(CANON)
    er = er[er.criteria.isin(ALL)]
    er["middle_rating"] = pd.to_numeric(er.middle_rating, errors="coerce")
    er["research"] = er.research.astype(str).str.replace(r"\s+", " ", regex=True).str.strip()
    er = er[~er.research.str.lower().str.contains("test paper|testing a submission|upload test|submission check")]
    er = er[~er.evaluator.astype(str).str.lower().isin(["anonymous", "david reinstein", "david reinstein again"])]
    er["named"] = ~er.evaluator.astype(str).str.match(r"^Evaluator \d+$")
    er["ev_hash"] = er.apply(lambda r: hashlib.sha256(r.evaluator.encode()).hexdigest()[:10] if r.named else "anon:" + hashlib.sha256((r.research + r.evaluator).encode()).hexdigest()[:10], axis=1)
    res = {}
    n_per = er[er.named].groupby("ev_hash").research.nunique()
    res["named_evaluators"] = int(n_per.size)
    res["named_evaluators_with_2plus_papers"] = int((n_per >= 2).sum())
    res["named_evaluators_with_3plus_papers"] = int((n_per >= 3).sum())
    res["max_papers_per_evaluator"] = int(n_per.max())
    # evaluator leniency: residual from paper mean, for papers with >=2 raters
    rows = []
    for c in ["overall", "methods", "adv_knowledge", "logic_comms", "gp_relevance"]:
        s = er[(er.criteria == c) & er.middle_rating.notna()].copy()
        cnt = s.groupby("research").middle_rating.transform("count")
        s = s[cnt >= 2]
        s["resid"] = s.middle_rating - s.groupby("research").middle_rating.transform("mean")
        s["resid"] = s.resid * np.sqrt(cnt[cnt >= 2] / (cnt[cnt >= 2] - 1))  # scale so 2-rater residuals are comparable
        g = s[s.named].groupby("ev_hash").resid.agg(["count", "mean"])
        multi = g[g["count"] >= 2]
        if len(multi) < 5:
            continue
        groups = [s[s.ev_hash == e].resid.values for e in multi.index]
        f = stats.f_oneway(*groups)
        # method-of-moments evaluator effect SD
        within = np.mean([v.var(ddof=1) for v in groups])
        between = multi["mean"].var(ddof=1)
        ev_sd = np.sqrt(max(between - within / multi["count"].mean(), 0))
        rows.append({"criteria": c, "n_evaluators_2plus": len(multi), "n_residuals": int(sum(len(v) for v in groups)),
                     "anova_F": float(f.statistic), "anova_p": float(f.pvalue), "evaluator_effect_sd": float(ev_sd),
                     "residual_sd": float(np.sqrt(within)), "max_abs_evaluator_mean_resid": float(multi["mean"].abs().max())})
    lt = pd.DataFrame(rows)
    lt.to_csv(out / "tbl_private_evaluator_effects.csv", index=False)
    res["evaluator_effects"] = lt
    # evaluator-level consistency of interval widths across their papers (do people have a 'house width'?)
    w = er[er.criteria.isin(QUAL) & er.named].copy()
    w["width"] = pd.to_numeric(w.upper_CI, errors="coerce") - pd.to_numeric(w.lower_CI, errors="coerce")
    w = w.dropna(subset=["width"])
    ev_w = w.groupby(["ev_hash", "research"]).width.mean().reset_index()
    multi = ev_w.groupby("ev_hash").research.nunique()
    ev_w = ev_w[ev_w.ev_hash.isin(multi[multi >= 2].index)]
    if len(ev_w) >= 10:
        groups = [g.width.values for _, g in ev_w.groupby("ev_hash")]
        res["width_icc_across_evaluators_papers"] = icc_oneway(groups)["icc1"]
        res["width_n_evaluators_2plus"] = int(len(groups))
    # experience and hours
    e = epl.copy()
    e["years"] = pd.to_numeric(e.years_in_field.astype(str).str.extract(r"(\d+(?:\.\d+)?)")[0], errors="coerce")
    e["n_reviews"] = pd.to_numeric(e.papers_reviewed.astype(str).str.replace(",", "").str.extract(r"(\d+)")[0], errors="coerce")
    e["hours"] = pd.to_numeric(e.hours_spent, errors="coerce")
    e["ov_width"] = pd.to_numeric(e.overall_upper, errors="coerce") - pd.to_numeric(e.overall_lower, errors="coerce")
    e["key"] = e.paper_title.map(norm_title)
    pmean = er[er.criteria == "overall"].assign(key=lambda x: x.research.map(norm_title)).groupby("key").middle_rating.agg(["mean", "count"])
    e = e.join(pmean, on="key")
    e["abs_dev_from_paper_mean"] = (e.overall_rating - e["mean"]).abs() * np.sqrt(e["count"] / (e["count"] - 1))
    e.loc[e["count"] < 2, "abs_dev_from_paper_mean"] = np.nan
    rows = []
    for xv in ["years", "n_reviews", "hours"]:
        for yv in ["overall_rating", "ov_width", "abs_dev_from_paper_mean"]:
            s = e[[xv, yv]].dropna()
            if len(s) >= 15:
                rho = stats.spearmanr(s[xv], s[yv])
                rows.append({"x": xv, "y": yv, "n": len(s), "spearman": float(rho.statistic), "p": float(rho.pvalue)})
    ex = pd.DataFrame(rows)
    ex.to_csv(out / "tbl_private_experience_hours.csv", index=False)
    res["experience_hours"] = ex
    res["hours_summary"] = {"n": int(e.hours.notna().sum()), "median": float(e.hours.median()), "mean": float(e.hours.mean())}
    return res


# ----------------------------------------------------------------------------
MD_TABLES = {
    "tbl_criterion_coverage.csv": (["criteria", "n", "share_of_evaluations", "share_with_ci"], "Coverage of each criterion"),
    "tbl_scale_use_percentile.csv": (["criteria", "n", "mean", "sd", "median", "share_ge_80", "share_le_30", "share_mult5", "share_mult10"], "Scale use, percentile criteria"),
    "tbl_interval_width_by_midpoint.csv": (["bin", "count", "mean", "median"], "Interval width by midpoint bin"),
    "tbl_reliability_all.csv": (["criteria", "n_papers", "alpha_interval", "alpha_ci_lo", "alpha_ci_hi", "icc1", "icc1k_mean_of_raters", "rater_noise_sd", "between_paper_sd", "raters_for_0.8"], "Inter-rater reliability"),
    "tbl_calibration_by_criterion.csv": (["criteria", "n_pairs", "coverage_other_midpoint", "expected_coverage_if_calibrated", "share_disjoint_intervals", "implied_sd_from_intervals", "empirical_rater_noise_sd", "noise_ratio_empirical_over_implied"], "Interval calibration"),
    "tbl_coverage_by_width.csv": (["width_bin", "n", "coverage", "expected"], "Coverage by stated width"),
    "tbl_redundancy_loo_r2.csv": (["criteria", "n", "r2_from_others", "best_single_predictor", "r_best"], "How well each criterion is predicted by the others"),
    "tbl_journal_pred_by_outcome_status.csv": (["status_group", "journal_predict_count", "journal_predict_mean", "merits_journal_mean", "overall_mean"], "Journal-tier predictions by current publication status"),
    "tbl_journal_known_outcomes.csv": (["journal_title", "actual_tier", "journal_predict", "merits_journal", "overall"], "Papers now published in a journal with a tier we could assign"),
    "tbl_anonymity.csv": (["criteria", "n_anon", "n_named", "mean_anon", "mean_named", "diff_anon_minus_named", "p"], "Anonymous versus named evaluators"),
    "tbl_by_area.csv": (["main_cause_cat_abbrev", "n_papers", "overall", "methods", "gp_relevance"], "Mean ratings by research area"),
    "tbl_llm_agreement.csv": (["model", "criteria", "n_papers", "spearman", "bias_llm_minus_human", "mae", "sd_llm", "sd_human_mean", "llm_width_median", "human_width_median"], "LLM agreement with the human mean"),
    "tbl_llm_as_extra_rater.csv": (["model", "criteria", "n_papers", "spearman_llm_vs_one_human", "spearman_human_vs_human", "alpha_humans_only", "alpha_humans_plus_llm"], "LLM as an extra rater"),
    "tbl_llm_profile_agreement.csv": (["model", "n_comparisons", "mean_within_paper_profile_spearman", "share_positive"], "Within-paper criterion-profile agreement"),
}


def write_markdown_tables(out):
    md = out / "md"
    md.mkdir(exist_ok=True)
    for name, (cols, title) in MD_TABLES.items():
        p = out / name
        if not p.exists():
            continue
        t = pd.read_csv(p)
        if "criteria" in t.columns:
            t["criteria"] = t["criteria"].map(lambda c: LABEL.get(c, c))
        keep = [c for c in cols if c in t.columns]
        if not keep:
            keep = list(t.columns)[:8]
        t = t[keep]
        for c in t.columns:
            if pd.api.types.is_float_dtype(t[c]):
                t[c] = t[c].map(lambda v: "" if pd.isna(v) else (f"{v:.2f}" if abs(v) < 10 else f"{v:.1f}"))
        lines = ["| " + " | ".join(str(c) for c in t.columns) + " |", "|" + "---|" * len(t.columns)]
        for _, r in t.iterrows():
            lines.append("| " + " | ".join(str(v) for v in r.values) + " |")
        (md / name.replace(".csv", ".md")).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ratings", default="data/rsx_evalr_rating.csv")
    ap.add_argument("--research", default="data/research.csv")
    ap.add_argument("--extra-ratings", default=None, help="CSV with additional ratings in the same schema")
    ap.add_argument("--paper-meta", default=None, help="CSV of paper-level fields exported from Coda (title, status, dates, stream flags)")
    ap.add_argument("--llm-repo", default=None, help="path to llm-uj-research-eval checkout")
    ap.add_argument("--private-db", default=None, help="path to private unjournal_data.db (evaluator-level supplement)")
    ap.add_argument("--out", default="website/posts/ratings-reliability-2026/results")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    d = load_ratings(args.ratings, args.research, args.extra_ratings)
    d = add_paper_meta(d, args.paper_meta)
    mid, lo, hi, meta = to_wide(d)
    results = {}
    results["describe"] = describe(d, mid, meta, out)
    results["scale_use"] = scale_use(d, mid, lo, hi, meta, out)
    results["structure"] = structure(d, mid, meta, out)
    rel = reliability(d, meta, out)
    results["reliability"] = {"table": rel, "subsets": reliability_subsets(d, meta, out)}
    results["calibration"] = calibration(d, out)
    results["journal"] = journal(d, mid, lo, hi, meta, out, args.private_db)
    results["trends"] = trends(d, mid, lo, hi, meta, out)
    if args.llm_repo:
        results["llm"] = llm_compare(d, mid, meta, args.llm_repo, args.research, out)
    if args.private_db and Path(args.private_db).exists():
        results["private"] = private_supplement(args.private_db, args.research, out)
    # reliability figure
    fig, ax = plt.subplots(figsize=(7, 3.8))
    x = np.arange(len(rel))
    ax.bar(x, rel.alpha_interval, color=[PAL[0] if c in QUAL else PAL[1] for c in rel.criteria], width=0.6)
    ax.errorbar(x, rel.alpha_interval, yerr=[rel.alpha_interval - rel.alpha_ci_lo, rel.alpha_ci_hi - rel.alpha_interval], fmt="none", ecolor="black", lw=1, capsize=2)
    ax.axhline(0.667, color="grey", ls="--", lw=1)
    ax.set_xticks(x)
    ax.set_xticklabels([LABEL[c] for c in rel.criteria], rotation=35, ha="right", fontsize=8)
    ax.set_ylabel("Krippendorff's alpha (interval)")
    ax.set_title("Inter-rater reliability by criterion, bootstrap 95% CI over papers", fontsize=10)
    fig.tight_layout()
    fig.savefig(out / "fig_reliability.png")
    plt.close(fig)
    (out / "results.json").write_text(json.dumps(jsonable(results), indent=1), encoding="utf-8")
    write_markdown_tables(out)
    print(json.dumps(jsonable(results), indent=1))


if __name__ == "__main__":
    main()
