#!/usr/bin/env python3
"""Regenerate the data tables and headline counts in the interactive ratings report
(website/posts/ratings-reliability-2026/v2/index.html) from analyze_ratings_quality.py outputs.

Tables are located by the text of their first header row, so the prose around them is untouched.
Run: python3 code/refresh_report_tables.py --results <results dir> [--page <index.html>]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import pandas as pd

LABEL = {
    "overall": "Overall", "claims": "Claims and evidence", "methods": "Methods", "adv_knowledge": "Advancing knowledge",
    "logic_comms": "Logic and communication", "open_sci": "Open science", "real_world": "Real-world relevance",
    "gp_relevance": "Global-priorities relevance", "merits_journal": "Journal tier: should", "journal_predict": "Journal tier: will",
}
QUAL = ["overall", "claims", "methods", "adv_knowledge", "logic_comms", "open_sci", "real_world", "gp_relevance"]
TIER = ["merits_journal", "journal_predict"]


def pct(x, nd=0):
    return "" if pd.isna(x) else f"{100 * x:.{nd}f}%"


def num(x, nd=0):
    return "" if pd.isna(x) else f"{x:.{nd}f}"


def rows_html(rows):
    return "\n".join("<tr>" + "".join(f"<td{' class=\"l\"' if i == 0 else ''}>{c}</td>" for i, c in enumerate(r)) + "</tr>" for r in rows)


def replace_tbody(page, header_start, body):
    """Replace the <tbody> of the table whose <thead> contains header_start."""
    i = page.find(header_start)
    if i < 0:
        raise SystemExit(f"table header not found: {header_start}")
    a = page.find("<tbody>", i) + len("<tbody>")
    b = page.find("</tbody>", a)
    return page[:a] + "\n" + body + "\n" + page[b:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--page", default="website/posts/ratings-reliability-2026/v2/index.html")
    a = ap.parse_args()
    R = Path(a.results)
    page = Path(a.page).read_text(encoding="utf-8")
    res = json.loads((R / "results.json").read_text())
    n_eval = res["describe"]["n_evaluations"]
    n_pap = res["describe"]["n_papers"]

    # 1. coverage table
    cov = pd.read_csv(R / "tbl_criterion_coverage.csv").set_index("criteria")
    rows = [[LABEL[c], "0–100" if c in QUAL else "0–5", int(cov.loc[c, "n"]), pct(cov.loc[c, "share_of_evaluations"]), pct(cov.loc[c, "share_with_ci"])]
            for c in QUAL + TIER if c in cov.index]
    page = replace_tbody(page, "<th>Criterion</th><th>Scale</th><th>Ratings</th>", rows_html(rows))

    # 2. scale use
    su = pd.read_csv(R / "tbl_scale_use_percentile.csv").set_index("criteria")
    rows = [[LABEL[c], num(su.loc[c, "mean"]), num(su.loc[c, "median"]), pct(su.loc[c, "share_ge_80"]), pct(su.loc[c, "share_le_30"]), pct(su.loc[c, "share_mult5"])]
            for c in QUAL if c in su.index]
    page = replace_tbody(page, "<th>Criterion</th><th>Mean</th><th>Median</th><th>Share ≥ 80</th>", rows_html(rows))

    # 3. disagreement + alpha table
    rel = pd.read_csv(R / "tbl_reliability_all.csv").set_index("criteria")
    rows = []
    for c in QUAL + TIER:
        if c not in rel.index:
            continue
        r = rel.loc[c]
        ci = f"{r.alpha_interval:.2f} [{r.alpha_ci_lo:.2f}, {r.alpha_ci_hi:.2f}]"
        if c in QUAL:
            rows.append([LABEL[c], int(r.n_pairs), num(r.median_abs_gap, 1).rstrip("0").rstrip("."), num(r.mean_abs_pair_diff, 1), pct(r.share_gap_gt_20), pct(r.share_gap_gt_30), ci, pct(1 - r.alpha_interval)])
        else:
            rows.append([LABEL[c], int(r.n_pairs), f"{r.median_abs_gap:.2f} tier", num(r.mean_abs_pair_diff, 2),
                         f'<span class="l">&gt; 1 tier apart: {pct(r.share_gap_gt_1tier)}</span>', "", ci, pct(1 - r.alpha_interval)])
    html = []
    for r in rows:
        if r[5] == "":
            html.append("<tr>" + f'<td class="l">{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td colspan="2" class="l">{r[4][len("<span class=\"l\">"):-len("</span>")]}</td><td>{r[6]}</td><td>{r[7]}</td>' + "</tr>")
        else:
            html.append("<tr>" + "".join(f"<td{' class=\"l\"' if i == 0 else ''}>{c}</td>" for i, c in enumerate(r)) + "</tr>")
    page = replace_tbody(page, "<th>Criterion</th><th>Pairs</th><th>Median gap</th>", "\n".join(html))

    # 4. Spearman-Brown table (sorted by single-rater reliability)
    sb = rel.sort_values("icc1", ascending=False)
    rows = []
    for c, r in sb.iterrows():
        k2 = 2 * r.icc1 / (1 + r.icc1)
        k3 = 3 * r.icc1 / (1 + 2 * r.icc1)
        rows.append([LABEL[c], num(r.icc1, 2), num(k2, 2), num(k3, 2), int(round(r["raters_for_0.8"])) if pd.notna(r["raters_for_0.8"]) else ""])
    page = replace_tbody(page, "<th>Criterion</th><th>One evaluation</th><th>Mean of 2</th>", rows_html(rows))

    # 5. calibration table
    cal = pd.read_csv(R / "tbl_calibration_by_criterion.csv").set_index("criteria")
    rows = [[LABEL[c], int(cal.loc[c, "n_pairs"]), pct(cal.loc[c, "coverage_other_midpoint"]), pct(cal.loc[c, "expected_coverage_if_calibrated"]),
             pct(cal.loc[c, "share_disjoint_intervals"]), num(cal.loc[c, "implied_sd_from_intervals"]), num(cal.loc[c, "empirical_rater_noise_sd"])]
            for c in QUAL if c in cal.index]
    page = replace_tbody(page, "<th>Criterion</th><th>Pairs</th><th>Observed coverage</th>", rows_html(rows))

    # 6. should vs will by entry year
    sw = pd.read_csv(R / "tbl_should_will_by_year.csv")
    rows = [[int(r.year), int(r.n), pct(r.share_same_mid), pct(r.share_should_gt_will), pct(r.share_will_gt_should), f"{r.mean_should_minus_will:+.2f}".replace("+0.00", "0.00")]
            for _, r in sw.iterrows() if pd.notna(r.year)]
    page = replace_tbody(page, "<th>Entered</th><th>Evaluations</th><th>Same midpoint</th>", rows_html(rows))

    # headline counts in prose
    page = re.sub(r"\d+ evaluations of \d+ papers", f"{n_eval} evaluations of {n_pap} papers", page)
    page = re.sub(r'"Share of evaluations" is out of \d+', f'"Share of evaluations" is out of {n_eval}', page)
    Path(a.page).write_text(page, encoding="utf-8")
    print("refreshed", a.page, n_eval, n_pap)


if __name__ == "__main__":
    main()
