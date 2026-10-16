# What The Unjournal's ratings data says about ratings, intervals, reliability and calibration

*Reanalysis, 16 October 2026. Prepared with Claude Code (Fable 5.1) for David Reinstein. Code: `code/analyze_ratings_quality.py` in the `unjournaldata` repository; all tables and figures regenerate from the public data export plus two optional supplements (the LLM-evaluation repository and the private database, used only for aggregate evaluator-level checks). No evaluator is identified anywhere in this report.*

## Headline findings

1. **The data.** 61 evaluated papers, 114 evaluations, 1,018 numeric ratings. Fifty papers have two or more evaluations, so most reliability and calibration results rest on about 45 to 48 paper pairs. The public export now uses per-paper evaluator labels, which is right for privacy but means cross-paper evaluator effects can only be studied on the private side.

2. **A data-pipeline gap.** The three evaluation packages published on PubPub since February 2026 (the scanner-data price-elasticity paper, the Yellow Vests independent evaluation, and the existential-risk technical report) have no rows in the Coda ratings table or the public export. The existential-risk evaluation sits in the new form's `form_submissions` table on Linode as `pending_review` since July. I added its seven ratings by hand for this analysis. The other two could not be read (PubPub's bot protection blocks automated fetches).

3. **The published 2025 post contains an error.** Its conclusions say evaluators "consistently judge papers as meriting higher-tier publication than they predict", "statistically significant (p < 0.001)". Its own test section reports a mean difference of -0.03 tiers, p = 0.63. The hard-coded sentence was never updated. I changed the source so the sentence is computed; it will render correctly at the next publish. To be clear, the form still asks both questions separately; the point is about the answers. On average, evaluators' "should" and "will" tiers are nearly the same number, and 43% of evaluations give exactly the same midpoint. That share is 61% for rows entered in 2024 (mostly older evaluations transferred from PubPub) and 24% for 2025 entries, so part of the overlap may be a transfer artifact; this is being checked against the published evaluations.

4. **Scale use is top-heavy.** On a scale that is meant to be a percentile of "serious research in the same area", 90% of overall ratings are above 50 and 47% are 80 or above. Relevance criteria are higher still (medians 84 to 85). Some of this is selection; The Unjournal picks promising work. Some is probably leniency and a loose reference class. Ratings heap on multiples of 5 (77%) and 10 (41%), so the effective precision is about five points.

5. **Evaluators disagree a lot, and their intervals do not admit it.** Two evaluators of the same paper differ by 12 points on overall assessment on average, 14 on methods, 19 on advancing knowledge and 23 on open science. Their stated 90% intervals have a median half-width of 10. If those intervals were calibrated, a co-evaluator's midpoint would fall inside about 70% of the time; it falls inside 51% of the time. Intervals would need to be roughly 2.5 times wider to match the disagreement we observe. Nearly a quarter of evaluator pairs give intervals that do not overlap at all.

6. **Reliability is moderate for quality, poor for open science.** Krippendorff's alpha (interval) is 0.45 for overall assessment, 0.50 for methods, 0.43 for claims and evidence (18 papers), 0.40 real-world relevance, 0.32 global-priorities relevance, 0.30 logic and communication, 0.22 advancing knowledge, and 0.06 for open science. With two raters, the paper mean reaches a reliability of about 0.6 to 0.7 for overall and methods; five raters would be needed for 0.8. Open science as currently measured is close to noise: evaluators differ by 21 points on it while papers differ by only 6.

7. **Two criteria are redundant and one is doing most of the work.** Real-world relevance and global-priorities relevance correlate at 0.89 within an evaluation (the new form already dropped real-world relevance; the data support that). The overall assessment is predicted (R-squared 0.74) by methods, advancing knowledge and logic; the relevance criteria and open science get roughly zero weight. Evaluators' "overall" is a rigor and contribution judgment, not an importance judgment.

8. **Halo.** When one evaluator is more generous than the co-evaluator on one criterion, they tend to be more generous on all of them (within-paper deviations correlate 0.41 across criteria on average). Part of what the sub-criteria measure is the rater, not the paper.

9. **Anonymous evaluators are harsher.** On papers with one anonymous and one named evaluator, the anonymous one rates about 5 points lower across criteria (102 paper-criterion comparisons, p = 0.009). This could be selection into anonymity or disinhibition; either way, named and anonymous numbers are not on the same scale.

10. **Journal predictions have some validity.** For 13 papers now published in journals I could assign a tier to, the mean predicted tier correlates 0.71 (Spearman) with the realised tier, with a small optimism of 0.2 tiers; 61% of evaluators' intervals covered the outcome. Papers that later landed in top journals had been predicted at 4.1 versus 3.7 for those still unpublished.

11. **LLM ratings.** Consistent with the LLM-evaluation site: GPT-5 Pro's overall rating correlates 0.54 with the human mean (46 papers), and as a stand-in for a second human it agrees with a single human evaluator at least as well as another human does (0.52 versus 0.37 for overall; 0.51 versus 0.42 methods; 0.68 versus 0.48 predicted tier). But it rates 6 points high on average and compresses the scale (SD 10 versus 14 to 15 for humans), so it should be used after standardisation. Open science is where every model disagrees with humans most (GPT-5 Pro and Claude Opus 4.6 rate it 17 to 20 points lower than the evaluators).

## The data

| criteria | n | share_of_evaluations | share_with_ci |
|---|---|---|---|
| Overall assessment | 111 | 0.97 | 0.88 |
| Claims & evidence | 48 | 0.42 | 0.98 |
| Methods | 108 | 0.95 | 0.90 |
| Advancing knowledge | 109 | 0.96 | 0.89 |
| Logic & communication | 111 | 0.97 | 0.89 |
| Open science | 109 | 0.96 | 0.88 |
| Real-world relevance | 98 | 0.86 | 0.90 |
| Global-priorities relevance | 108 | 0.95 | 0.89 |
| Journal tier: should | 96 | 0.84 | 0.81 |
| Journal tier: will | 88 | 0.77 | 0.83 |


Claims and evidence was introduced in 2025 and appears in 41% of evaluations. Real-world relevance was dropped from the current form. About 11 to 13% of percentile ratings have no interval; journal-tier ratings lack intervals 17 to 21% of the time. A legacy "confidence level" field appears in four rows and can be retired.

Evaluations are 58% anonymous. Ninety-three evaluations are academic-stream and eleven applied-stream (eight unassigned). Evaluation packages were published from 2023 to 2026; the mean overall rating by publication year is flat (76, 75, 75, 70 for 2023 to 2026, the last on seven evaluations) and the median interval width moved from 20 to 15.5 and back.

## 1. The nature of the numbers

![Distribution of midpoint ratings](results/fig_distributions.png)

| criteria | n | mean | sd | median | share_ge_80 | share_le_30 | share_mult5 | share_mult10 |
|---|---|---|---|---|---|---|---|---|
| Overall assessment | 111 | 74.8 | 15.1 | 77.0 | 0.47 | 0.02 | 0.77 | 0.40 |
| Claims & evidence | 48 | 72.1 | 20.1 | 80.0 | 0.53 | 0.06 | 0.69 | 0.41 |
| Methods | 108 | 70.8 | 18.9 | 75.0 | 0.41 | 0.05 | 0.80 | 0.52 |
| Advancing knowledge | 109 | 72.9 | 19.4 | 80.0 | 0.51 | 0.06 | 0.78 | 0.50 |
| Logic & communication | 111 | 74.7 | 15.2 | 79.0 | 0.49 | 0.03 | 0.79 | 0.48 |
| Open science | 109 | 73.2 | 21.2 | 80.0 | 0.50 | 0.07 | 0.79 | 0.54 |
| Real-world relevance | 98 | 76.8 | 19.3 | 84.0 | 0.53 | 0.04 | 0.73 | 0.44 |
| Global-priorities relevance | 108 | 78.4 | 18.2 | 85.0 | 0.65 | 0.03 | 0.82 | 0.54 |


Every percentile criterion has a mean between 71 and 78 and a median between 75 and 85. A Kolmogorov-Smirnov test against the uniform distribution the percentile interpretation would imply for a representative sample rejects at any level. Only 2 to 7% of ratings are 30 or below. The two relevance criteria are the most inflated: 37 to 40% of ratings are at or above 90.

Straightlining is rare: 2 of 109 evaluations give the same number on every criterion, 5 have a range of five points or less, and the median within-evaluation range is 25 points. Evaluators do differentiate.

Journal tiers: mean 3.85 on both the should and will questions, about 59% at 4 or above, none at 1 or below. Non-integer answers are common (63%), as the guidelines encourage.

**Intervals.** Of 827 percentile ratings, 8 have an interval that excludes its own midpoint and 11 have zero width (for example "100 [100, 100]"). Fourteen percent of intervals touch 0 or 100. Two-thirds are symmetric about the midpoint; where they are not, the lower tail is usually the longer one (22% versus 12%). The median width is 20 points (10th to 90th percentile: 10 to 40). Widths shrink as midpoints rise: median 30 for midpoints at or below 50, 20 in the 50 to 85 range, and 11 above 85. Part of this is the ceiling, but it also means our most confident intervals sit exactly where the ceiling makes them cheapest to state.

| count | mean | median |
|---|---|---|
| 98 | 29.3 | 28.0 |
| 160 | 24.0 | 20.0 |
| 223 | 20.4 | 20.0 |
| 229 | 13.6 | 11.0 |


![Interval width against midpoint](results/fig_width_vs_midpoint.png)

Evaluators do not simply use one width for everything: only 7% of evaluations use a single width across criteria.

## 2. Structure, redundancy and halo

![Correlations at three levels](results/fig_correlations.png)

The average off-diagonal correlation between criteria is 0.48 within an evaluation and 0.53 between paper means. A principal-components analysis of the seven classic criteria on paper means puts 56% of the variance on a first component that loads evenly on everything except open science (loading -0.09), 19% on a second component that is mostly open science with logic and communication, and 13% on a third that separates relevance from the rest.

| criteria | n | r2_from_others | best_single_predictor | r_best |
|---|---|---|---|---|
| Overall assessment | 96 | 0.74 | methods | 0.77 |
| Claims & evidence | 45 | 0.73 | methods | 0.78 |
| Methods | 96 | 0.64 | overall | 0.77 |
| Advancing knowledge | 96 | 0.67 | real_world | 0.71 |
| Logic & communication | 96 | 0.57 | overall | 0.68 |
| Open science | 96 | 0.23 | logic_comms | 0.39 |
| Real-world relevance | 96 | 0.82 | gp_relevance | 0.89 |
| Global-priorities relevance | 96 | 0.80 | real_world | 0.89 |


Real-world relevance is 82% predictable from the other criteria, global-priorities relevance 80%, overall 74%, claims 73%. Open science is only 23% predictable, which would be interesting if it were reliable; it is not (see section 4).

Regressing overall on the other six classic criteria (standardised, n = 96, R-squared 0.74) gives weights of 0.42 methods, 0.30 advancing knowledge, 0.28 logic and communication, 0.13 real-world relevance, -0.04 open science and -0.10 global-priorities relevance. Overall is also within a point of the simple mean of the sub-criteria on average, and in only 2% of evaluations is it above the highest sub-criterion.

The third panel of the figure is the halo check: each rating minus the paper's mean on that criterion, correlated across criteria. The average is 0.41. The strongest rater-level co-movements are the two relevance criteria (0.91), overall with logic and communication (0.71), and advancing knowledge with real-world relevance (0.79). Claims and evidence stands apart: a rater's generosity on claims barely co-moves with their generosity on relevance (0.02).

## 3. Inter-rater reliability

![Reliability by criterion](results/fig_reliability.png)

| criteria | n_papers | alpha_interval | alpha_ci_lo | alpha_ci_hi | icc1 | icc1k_mean_of_raters | rater_noise_sd | between_paper_sd | raters_for_0.8 |
|---|---|---|---|---|---|---|---|---|---|
| Overall assessment | 48 | 0.45 | 0.10 | 0.67 | 0.45 | 0.62 | 11.4 | 10.3 | 4.96 |
| Claims & evidence | 18 | 0.43 | 0.00 | 0.74 | 0.44 | 0.61 | 15.2 | 13.4 | 5.13 |
| Methods | 46 | 0.50 | 0.09 | 0.71 | 0.50 | 0.67 | 12.9 | 13.0 | 3.94 |
| Advancing knowledge | 46 | 0.22 | -0.03 | 0.48 | 0.18 | 0.31 | 17.5 | 8.23 | 18.0 |
| Logic & communication | 47 | 0.30 | -0.05 | 0.60 | 0.30 | 0.47 | 13.0 | 8.45 | 9.45 |
| Open science | 47 | 0.06 | -0.34 | 0.45 | 0.06 | 0.12 | 21.0 | 5.53 | 57.6 |
| Real-world relevance | 41 | 0.40 | 0.01 | 0.70 | 0.41 | 0.58 | 15.3 | 12.7 | 5.83 |
| Global-priorities relevance | 45 | 0.32 | -0.12 | 0.63 | 0.33 | 0.50 | 15.3 | 10.7 | 8.26 |
| Journal tier: should | 41 | 0.31 | 0.05 | 0.54 | 0.30 | 0.47 | 0.66 | 0.44 | 9.28 |
| Journal tier: will | 35 | 0.41 | 0.14 | 0.64 | 0.38 | 0.55 | 0.55 | 0.43 | 6.61 |


Alpha is the interval-metric Krippendorff's alpha over all papers with at least two ratings; the confidence interval is a bootstrap over papers, and it is wide everywhere. ICC(1) is the one-way intraclass correlation, numerically similar; "icc1k" is the reliability of the paper mean with the average number of raters we actually have (about two). "Rater noise SD" is the within-paper standard deviation of ratings; "between-paper SD" is the estimated spread of true paper scores.

Three readings:

- Overall and methods carry a real signal. Rater noise (11 to 13 points) is roughly equal to the spread of papers (10 to 13 points), so a single evaluation tells you about half of what you want to know and the mean of two tells you about two-thirds.
- Advancing knowledge, logic and communication and both relevance criteria carry less: noise is 1.5 to 2 times the spread of papers.
- Open science as rated carries almost none. Papers differ by 6 points; evaluators differ by 21. The bootstrap interval includes zero comfortably.

By era (data-entry year 2024 versus 2025 and later) alpha for overall is 0.47 versus 0.42, so there is no sign the percentile re-framing or the calibration tool changed agreement. The academic stream alone gives 0.37 over 40 papers; the applied stream gives 0.91 but on five papers. By research area, agreement on overall is lowest in the two largest areas, global health (0.16, 13 papers) and development economics (-0.28, 11 papers), and highest in environment (0.69, 6 papers). Small cells, but it is at least not the case that the areas where we have the most practice agree the most.

The prior posts reported alphas of 0.4 to 0.6 and called the measures "moderately reliable". With confidence intervals attached, the honest statement is: overall and methods are moderately reliable, the rest are weakly reliable, and open science is unreliable.

## 4. Calibration of the 90% intervals

![Coverage: observed versus implied](results/fig_coverage.png)

| criteria | n_pairs | coverage_other_midpoint | expected_coverage_if_calibrated | share_disjoint_intervals | implied_sd_from_intervals | empirical_rater_noise_sd | noise_ratio_empirical_over_implied |
|---|---|---|---|---|---|---|---|
| Overall assessment | 89 | 0.62 | 0.72 | 0.13 | 6.08 | 11.7 | 1.92 |
| Claims & evidence | 35 | 0.49 | 0.70 | 0.23 | 6.08 | 15.0 | 2.47 |
| Methods | 88 | 0.56 | 0.66 | 0.23 | 6.08 | 12.4 | 2.04 |
| Advancing knowledge | 90 | 0.51 | 0.70 | 0.27 | 6.08 | 17.8 | 2.92 |
| Logic & communication | 92 | 0.51 | 0.70 | 0.17 | 6.08 | 13.7 | 2.25 |
| Open science | 85 | 0.39 | 0.70 | 0.38 | 6.08 | 21.4 | 3.52 |
| Real-world relevance | 76 | 0.53 | 0.71 | 0.18 | 4.56 | 14.0 | 3.08 |
| Global-priorities relevance | 88 | 0.50 | 0.71 | 0.23 | 5.93 | 15.3 | 2.58 |


The test here is the one the guidelines invite. Each evaluator states a 90% credible interval for the "true" percentile. If both evaluators of a paper were calibrated and independent, one evaluator's midpoint would fall inside the other's interval about 75% of the time under a normal model with equal noise; using each pair's actual stated widths, the implied figure for our data is 70%. The observed figure is 51% overall (62% for overall assessment, 39% for open science). Twenty-three percent of pairs state intervals that do not overlap at all. Scaling every interval by a common factor, they would need to be 2.5 times wider to reach the calibrated benchmark.

A second way to see the same thing: a median half-width of 10 implies an evaluator believes their own error has a standard deviation of about 6 points. The disagreement between evaluators implies a per-rater error standard deviation of 12 (overall) to 21 (open science) points. Evaluators are overconfident by a factor of two to three and a half.

| width_bin | n | coverage | expected |
|---|---|---|---|
| <=10 | 170 | 0.37 | 0.57 |
| 11-20 | 281 | 0.51 | 0.71 |
| 21-30 | 84 | 0.64 | 0.79 |
| >30 | 106 | 0.67 | 0.84 |


Wider intervals do cover more, so the number means something: evaluators who state 30-point intervals cover 67% of co-evaluator midpoints versus 37% for those at 10 or below. But the gap to the calibrated expectation is about the same at every width. The correlation between an evaluator's own half-width and how far they are from the co-evaluator is only 0.13: there is a little self-knowledge in the intervals, not much.

At the evaluation level, 45% of evaluations cover fewer than half of their co-evaluator's midpoints, 4% cover none, and 8% cover all.

Two caveats run the other way. The "true percentile" is an idealised quantity, and two evaluators can both be right about different things. And if evaluators share information (same seminar, same priors), coverage would be higher than the independence benchmark, not lower; so this is if anything a lower bound on overconfidence.

## 5. Journal-tier questions

![Should versus will](results/fig_should_vs_will.png)

Should and will are almost the same number (means 3.82 and 3.86, correlation 0.73, 43% identical midpoints). Identical midpoints are much more common among rows entered in 2024 (61%) than in 2025 (24%), which may partly reflect how older evaluations were transferred; the gap between "should" and "will" may therefore be understated. "Should" correlates 0.77 with the overall assessment; "will" 0.54. So "should" tracks the overall assessment closely, while "will" is the one question with a resolvable answer. The useful quantity is the difference between them (how much evaluators think the journal system will over- or under-reward a paper), which is why both are kept.

| status_group | journal_predict_count | journal_predict_mean | merits_journal_mean | overall_mean |
|---|---|---|---|---|
| R&R/forthcoming | 3 | 4.53 | 4.52 | 73.1 |
| published other | 8 | 3.58 | 3.79 | 75.0 |
| published ~top | 8 | 4.13 | 4.03 | 78.3 |
| working paper / other | 32 | 3.67 | 3.72 | 74.0 |


| journal_title | actual_tier | journal_predict | merits_journal | overall |
|---|---|---|---|---|
| AEA Papers and Proceedings | 2.50 | 4.00 | 4.50 | 79.7 |
| Conservation Letters | 3.00 | 2.75 | 3.00 | 75.0 |
| American Economic Review Insights | 4.00 | 4.00 | 4.00 | 75.0 |
| American Economic Review | 5.00 | 4.70 | 4.55 | 85.0 |
| The World Bank Research Observer | 2.50 | 3.60 | 2.75 | 72.5 |
| International Journal of Disaster Risk Reduction | 2.00 | 3.00 | 3.17 | 61.7 |
| American Economic Review Insights | 4.00 | 4.00 | 4.00 | 87.5 |
| Cognition | 3.50 | 4.35 | 4.35 | 71.0 |
| Econometrica | 5.00 | 4.70 | 4.60 | 90.0 |
| Management Science | 4.00 | 3.60 | 3.80 | 65.0 |
| Review of Economics and Statistics | 4.00 | 4.30 | 4.35 | 75.0 |
| The Economic Journal | 3.50 | 3.50 | 4.00 | 73.5 |
| American Economic Review | 5.00 | 4.20 | 3.85 | 85.5 |


The tier assignment for realised journals is my own reading of the guidelines' five tiers and should be checked. On those 13 papers the mean prediction correlates 0.71 with the outcome; the mean error is +0.2 tiers (optimism), the mean absolute error 0.5 tiers; 61% of the 18 evaluator intervals contained the outcome, with the outcome below the interval 28% of the time. The overall assessment alone correlates 0.65 with the realised tier.

## 6. Systematic patterns

| criteria | n_anon | n_named | mean_anon | mean_named | diff_anon_minus_named | p |
|---|---|---|---|---|---|---|
| Overall assessment | 65 | 46 | 74.0 | 76.0 | -1.93 | 0.52 |
| Claims & evidence | 27 | 21 | 67.1 | 78.5 | -11.3 | 0.04 |
| Methods | 64 | 44 | 69.4 | 72.8 | -3.38 | 0.36 |
| Advancing knowledge | 64 | 45 | 70.8 | 75.9 | -5.15 | 0.17 |
| Logic & communication | 65 | 46 | 76.2 | 72.6 | 3.59 | 0.24 |
| Open science | 65 | 44 | 73.4 | 72.8 | 0.54 | 0.90 |
| Real-world relevance | 62 | 36 | 76.1 | 78.1 | -2.00 | 0.61 |
| Global-priorities relevance | 64 | 44 | 77.6 | 79.6 | -2.03 | 0.56 |
| Journal tier: should | 58 | 38 | 3.83 | 3.85 | -0.02 | 0.91 |
| Journal tier: will | 52 | 36 | 3.96 | 3.69 | 0.27 | 0.11 |


In the pooled comparison only claims and evidence differs much by anonymity. The sharper test is within paper: for 102 paper-criterion cells where one evaluator was named and the other anonymous, the anonymous evaluator is 4.8 points lower on average (Wilcoxon p = 0.009).

| main_cause_cat_abbrev | n_papers | overall | methods | gp_relevance |
|---|---|---|---|---|
| Global health (LMICs) | 13 | 77.3 | 75.0 | 80.3 |
| Dev. econ/gov. (LMICs) | 11 | 77.0 | 69.3 | 77.8 |
| Environment | 6 | 75.2 | 67.2 | 86.8 |
| Catastrophic & X-risk, LT, forecasting | 5 | 67.8 | 63.7 | 82.0 |
| Econ., welfare, misc. | 5 | 61.3 | 68.1 | 56.7 |
| Innovation & meta-science | 5 | 73.1 | 68.4 | 69.3 |
| Animal welfare, markets | 4 | 74.6 | 57.9 | 82.6 |
| Attitudes, behaviors, psych, misinfo. | 3 | 81.0 | 82.0 | 73.3 |


Research areas differ more on the relevance criteria than on quality: animal welfare papers score 83 on global-priorities relevance and 58 on methods; existential-risk papers score 82 and 64; the economics and welfare catch-all scores 57 and 68.

On the private side, 58 named evaluators appear in the data and only 9 have evaluated two or more papers (5 have three or more; the most is seven). A one-way ANOVA of residuals (rating minus paper mean) across those repeat evaluators gives p = 0.05 for overall, with an estimated evaluator-effect standard deviation of about 5 points against a residual of 9. That is suggestive of stable leniency differences, but it is nine people. Hours spent (n = 33, median 8) and years in field (n = 16) show no relationship with ratings or widths at these sample sizes.

## 7. Consistency with LLM ratings

![LLM versus human](results/fig_llm_vs_human.png)

| model | criteria | n_papers | spearman_llm_vs_one_human | spearman_human_vs_human | alpha_humans_only | alpha_humans_plus_llm |
|---|---|---|---|---|---|---|
| GPT-5 Pro | Overall assessment | 39 | 0.52 | 0.37 | 0.52 | 0.40 |
| GPT-5 Pro | Claims & evidence | 12 | 0.28 | 0.49 | 0.44 | 0.27 |
| GPT-5 Pro | Methods | 38 | 0.51 | 0.42 | 0.56 | 0.39 |
| GPT-5 Pro | Advancing knowledge | 38 | 0.48 | 0.26 | 0.24 | 0.24 |
| GPT-5 Pro | Logic & communication | 39 | 0.32 | 0.27 | 0.36 | 0.17 |
| GPT-5 Pro | Open science | 39 | 0.15 | -0.05 | 0.03 | 0.05 |
| GPT-5 Pro | Global-priorities relevance | 38 | 0.35 | 0.19 | 0.38 | 0.25 |
| GPT-5 Pro | Journal tier: should | 35 | 0.47 | 0.25 | 0.32 | 0.30 |
| GPT-5 Pro | Journal tier: will | 29 | 0.68 | 0.48 | 0.42 | 0.50 |
| GPT-4o-mini | Overall assessment | 39 | 0.15 | 0.37 | 0.52 | 0.28 |
| GPT-4o-mini | Claims & evidence | 12 | 0.32 | 0.49 | 0.44 | 0.32 |
| GPT-4o-mini | Methods | 38 | 0.11 | 0.42 | 0.56 | 0.27 |
| GPT-4o-mini | Advancing knowledge | 38 | 0.14 | 0.26 | 0.24 | 0.20 |
| GPT-4o-mini | Logic & communication | 39 | -0.00 | 0.26 | 0.36 | 0.15 |
| GPT-4o-mini | Open science | 39 | -0.13 | -0.05 | 0.03 | -0.05 |
| GPT-4o-mini | Global-priorities relevance | 38 | 0.17 | 0.20 | 0.38 | 0.18 |
| GPT-4o-mini | Journal tier: should | 35 | 0.20 | 0.25 | 0.32 | 0.23 |
| GPT-4o-mini | Journal tier: will | 29 | 0.30 | 0.47 | 0.42 | 0.31 |
| Claude Opus 4.6 | Overall assessment | 29 | 0.48 | 0.39 | 0.54 | 0.59 |
| Claude Opus 4.6 | Methods | 27 | 0.43 | 0.28 | 0.33 | 0.31 |
| Claude Opus 4.6 | Advancing knowledge | 28 | 0.37 | 0.14 | 0.18 | 0.29 |
| Claude Opus 4.6 | Logic & communication | 28 | 0.24 | 0.36 | 0.50 | 0.36 |
| Claude Opus 4.6 | Open science | 28 | 0.04 | 0.17 | 0.25 | 0.07 |
| Claude Opus 4.6 | Global-priorities relevance | 28 | 0.29 | 0.25 | 0.46 | 0.30 |
| Claude Opus 4.6 | Journal tier: should | 27 | 0.50 | 0.22 | 0.28 | 0.40 |
| Claude Opus 4.6 | Journal tier: will | 22 | 0.63 | 0.33 | 0.29 | 0.47 |
| Gemini 2.0 Flash | Overall assessment | 39 | 0.33 | 0.37 | 0.52 | 0.38 |
| Gemini 2.0 Flash | Claims & evidence | 12 | 0.10 | 0.50 | 0.44 | 0.27 |
| Gemini 2.0 Flash | Methods | 38 | 0.18 | 0.42 | 0.56 | 0.33 |
| Gemini 2.0 Flash | Advancing knowledge | 38 | 0.21 | 0.26 | 0.24 | 0.16 |
| Gemini 2.0 Flash | Logic & communication | 39 | 0.14 | 0.27 | 0.36 | 0.17 |
| Gemini 2.0 Flash | Open science | 39 | -0.05 | -0.05 | 0.03 | -0.00 |
| Gemini 2.0 Flash | Global-priorities relevance | 38 | 0.15 | 0.19 | 0.38 | 0.22 |


| model | n_comparisons | mean_within_paper_profile_spearman | share_positive |
|---|---|---|---|
| GPT-5 Pro | 83 | 0.30 | 0.67 |
| GPT-5.2 Pro | 17 | 0.31 | 0.82 |
| GPT-4o-mini | 83 | 0.22 | 0.73 |
| Claude Sonnet 4 | 18 | 0.26 | 0.72 |
| Claude Opus 4.6 | 60 | 0.25 | 0.77 |
| Gemini 2.0 Flash | 83 | 0.21 | 0.69 |
| Human vs human | 49 | 0.18 | 0.73 |


The first table is the fair comparison: for papers with two human evaluations, how well does the LLM agree with one randomly chosen human, versus how well the other human agrees with that same person? GPT-5 Pro beats a second human on overall, methods, advancing knowledge, global-priorities relevance and both journal-tier questions; Claude Opus 4.6 beats a second human on overall, methods, advancing knowledge and journal tiers; the cheaper models do not. Adding GPT-5 Pro as a third rater lowers Krippendorff's alpha because of its level bias (it rates 6 points high and compresses the scale), while adding Opus raises it slightly (it rates 8 points low with a human-like spread). The second table asks whether a rater reproduces a paper's profile across criteria (which criteria are its strengths); GPT-5 Pro's profiles agree with a single human's (0.30) more than two humans agree with each other (0.18).

| model | criteria | n_papers | spearman | bias_llm_minus_human | mae | sd_llm | sd_human_mean | llm_width_median | human_width_median |
|---|---|---|---|---|---|---|---|---|---|
| Claude Opus 4.6 | Advancing knowledge | 33 | 0.38 | -1.89 | 11.6 | 16.6 | 14.5 | 24.0 | 18.8 |
| Claude Opus 4.6 | Claims & evidence | 10 | 0.30 | -13.7 | 16.5 | 19.9 | 14.1 | 26.5 | 17.0 |
| Claude Opus 4.6 | Global-priorities relevance | 34 | 0.34 | -4.48 | 14.1 | 14.5 | 16.2 | 25.0 | 20.0 |
| Claude Opus 4.6 | Journal tier: will | 30 | 0.65 | -0.17 | 0.46 | 0.72 | 0.65 | 1.50 | 1.15 |
| Claude Opus 4.6 | Logic & communication | 34 | 0.00 | -1.04 | 13.8 | 13.8 | 13.6 | 22.0 | 20.0 |
| Claude Opus 4.6 | Journal tier: should | 31 | 0.60 | -0.25 | 0.49 | 0.74 | 0.70 | 1.50 | 1.17 |
| Claude Opus 4.6 | Methods | 33 | 0.45 | -5.91 | 14.6 | 19.5 | 16.5 | 24.0 | 19.5 |
| Claude Opus 4.6 | Open science | 34 | -0.06 | -20.4 | 25.8 | 17.7 | 17.7 | 30.0 | 20.0 |
| Claude Opus 4.6 | Overall assessment | 34 | 0.47 | -7.66 | 12.4 | 18.5 | 13.3 | 25.5 | 20.0 |
| Claude Sonnet 4 | Advancing knowledge | 11 | 0.10 | 3.09 | 8.73 | 4.40 | 9.97 | 17.0 | 15.0 |
| Claude Sonnet 4 | Global-priorities relevance | 11 | 0.00 | -2.41 | 8.77 | 8.67 | 7.17 | 14.0 | 20.0 |
| Claude Sonnet 4 | Logic & communication | 11 | 0.58 | 5.00 | 7.82 | 4.37 | 9.60 | 14.0 | 18.0 |
| Claude Sonnet 4 | Methods | 11 | -0.50 | 6.32 | 15.5 | 5.30 | 19.0 | 20.0 | 15.0 |
| Claude Sonnet 4 | Open science | 11 | 0.37 | -0.41 | 10.3 | 11.9 | 9.55 | 14.0 | 20.0 |
| Claude Sonnet 4 | Overall assessment | 11 | 0.06 | 0.18 | 6.91 | 4.03 | 9.17 | 20.0 | 20.0 |
| GPT-4o-mini | Advancing knowledge | 45 | 0.10 | 0.21 | 13.5 | 16.0 | 15.5 | 20.0 | 17.2 |
| GPT-4o-mini | Claims & evidence | 17 | 0.31 | -3.56 | 14.9 | 13.7 | 16.8 | 20.0 | 16.0 |
| GPT-4o-mini | Global-priorities relevance | 46 | 0.11 | -2.14 | 14.9 | 15.3 | 15.2 | 20.0 | 20.0 |
| GPT-4o-mini | Journal tier: will | 41 | 0.34 | -0.21 | 0.60 | 0.47 | 0.70 | 1.00 | 1.00 |
| GPT-4o-mini | Logic & communication | 46 | -0.01 | -1.40 | 11.9 | 14.6 | 12.9 | 20.0 | 19.0 |
| GPT-4o-mini | Journal tier: should | 42 | 0.29 | 0.23 | 0.49 | 0.40 | 0.67 | 1.00 | 1.00 |
| GPT-4o-mini | Methods | 45 | 0.10 | -1.83 | 14.3 | 15.2 | 18.2 | 20.0 | 19.5 |
| GPT-4o-mini | Open science | 46 | -0.22 | -7.91 | 17.1 | 14.2 | 15.8 | 20.0 | 20.0 |
| GPT-4o-mini | Overall assessment | 46 | 0.14 | -0.51 | 12.8 | 16.7 | 13.8 | 20.0 | 20.0 |
| GPT-5 Pro | Advancing knowledge | 45 | 0.45 | 7.61 | 11.9 | 9.89 | 15.5 | 17.0 | 17.2 |
| GPT-5 Pro | Claims & evidence | 17 | 0.39 | 3.44 | 14.0 | 12.8 | 16.8 | 16.0 | 16.0 |
| GPT-5 Pro | Global-priorities relevance | 46 | 0.39 | 6.09 | 11.5 | 9.33 | 15.2 | 17.0 | 20.0 |
| GPT-5 Pro | Journal tier: will | 41 | 0.75 | 0.12 | 0.40 | 0.53 | 0.70 | 1.20 | 1.00 |
| GPT-5 Pro | Logic & communication | 46 | 0.28 | 9.43 | 12.5 | 6.80 | 12.9 | 14.0 | 19.0 |
| GPT-5 Pro | Journal tier: should | 42 | 0.51 | 0.28 | 0.49 | 0.44 | 0.67 | 1.10 | 1.00 |
| GPT-5 Pro | Methods | 45 | 0.56 | 4.42 | 12.0 | 12.3 | 18.2 | 19.0 | 19.5 |
| GPT-5 Pro | Open science | 46 | 0.10 | -17.2 | 22.5 | 17.1 | 15.8 | 27.0 | 20.0 |
| GPT-5 Pro | Overall assessment | 46 | 0.54 | 6.23 | 10.1 | 10.0 | 13.8 | 15.0 | 20.0 |
| GPT-5.2 Pro | Advancing knowledge | 9 | 0.15 | -2.91 | 15.1 | 16.1 | 16.7 | 27.0 | 17.5 |
| GPT-5.2 Pro | Claims & evidence | 9 | 0.32 | -5.06 | 18.7 | 17.6 | 21.4 | 28.0 | 17.5 |
| GPT-5.2 Pro | Global-priorities relevance | 9 | 0.36 | 1.44 | 7.44 | 7.91 | 9.56 | 21.0 | 20.0 |
| GPT-5.2 Pro | Journal tier: will | 8 | 0.97 | -0.29 | 0.56 | 0.74 | 1.12 | 1.65 | 1.40 |
| GPT-5.2 Pro | Logic & communication | 9 | -0.27 | -2.31 | 14.4 | 11.4 | 13.2 | 23.0 | 20.0 |
| GPT-5.2 Pro | Journal tier: should | 8 | 0.39 | -0.15 | 0.54 | 0.71 | 0.93 | 1.45 | 1.25 |
| GPT-5.2 Pro | Methods | 9 | 0.05 | -2.56 | 24.6 | 20.0 | 23.0 | 30.0 | 22.5 |
| GPT-5.2 Pro | Open science | 9 | -0.51 | -22.6 | 28.7 | 20.3 | 13.7 | 32.0 | 17.0 |
| GPT-5.2 Pro | Overall assessment | 9 | 0.47 | -2.67 | 14.7 | 17.0 | 17.6 | 25.0 | 20.0 |
| Gemini 2.0 Flash | Advancing knowledge | 45 | 0.14 | -2.08 | 12.2 | 5.82 | 15.5 | 25.0 | 17.2 |
| Gemini 2.0 Flash | Claims & evidence | 17 | 0.02 | -0.03 | 12.7 | 8.01 | 16.8 | 25.0 | 16.0 |
| Gemini 2.0 Flash | Global-priorities relevance | 46 | 0.13 | -0.28 | 12.4 | 7.28 | 15.2 | 25.0 | 20.0 |
| Gemini 2.0 Flash | Logic & communication | 46 | 0.08 | 6.04 | 10.9 | 4.98 | 12.9 | 20.0 | 19.0 |
| Gemini 2.0 Flash | Methods | 45 | 0.17 | -2.14 | 14.1 | 8.82 | 18.2 | 25.0 | 19.5 |
| Gemini 2.0 Flash | Open science | 46 | -0.12 | -1.93 | 14.6 | 9.79 | 15.8 | 30.0 | 20.0 |
| Gemini 2.0 Flash | Overall assessment | 46 | 0.29 | -5.70 | 12.0 | 8.44 | 13.8 | 30.0 | 20.0 |


Open science is the exception everywhere: the frontier models rate it 17 to 20 points below the evaluators with near-zero rank agreement. Models cannot check data and code availability from a PDF, and evaluators apparently judge it by something else again.

## 8. Which measures are underused or redundant

- **Real-world relevance** is 82% predictable from the other criteria and correlates 0.89 with global-priorities relevance within an evaluation. Dropping it from the form was right.
- **Open science** has no reliability and no loading on the general factor. It should be replaced by a short checklist of verifiable items (data public, code public, pre-registration, materials), scored yes/partly/no, rather than a percentile. The percentile is costing evaluator time and producing noise.
- **Journal tier "should"** correlates 0.77 with overall. Keep the should/will pair: the contrast is the point of the question, and "will" is the one rating that resolves. The overlap in answers suggests the form should explain the distinction more sharply (for example, ask "will" first, then "if journals judged only merit, where should it go?"), rather than dropping either.
- **Claims and evidence** is new, used in 41% of evaluations, reliability comparable to overall on 18 papers, and the least affected by rater halo. Worth keeping and worth making the structured claim assessment more central.
- **Advancing knowledge** and **logic and communication** have weak reliability (0.22, 0.30). Logic and communication is cheap and distinct; advancing knowledge overlaps heavily with overall and the relevance criteria.
- The legacy **confidence_level** field and the duplicate criterion keys in the new form's output (`advancing_knowledge`, `claims_and_evidence`, `global_relevance`, `open_science`) should be canonicalised at import.

## 9. Implications for the evaluation form, platform and reporting

Easy fixes, in rough order of value for effort:

1. **Fix the pipeline first.** Ratings from the new form never reach the ratings table; three published packages are missing. Add the import step (form_submissions to evaluator_ratings to Coda) and canonicalise criterion keys. Until then, the dashboard and this analysis undercount 2026.
2. **Tell evaluators what disagreement looks like.** Next to each slider: "Evaluators of the same paper typically differ by 12 to 20 points on this scale. A 90% interval narrower than plus or minus 10 is rarely justified." Show the empirical distribution of prior ratings for the criterion. This is the single cheapest calibration intervention and costs nothing in evaluator time.
3. **Warn on narrow and degenerate intervals.** The form already enforces lower <= midpoint <= upper. Add a soft warning for widths under 10 and a hard one for zero width, and a note at the top of the scale that an upper bound of 100 is a claim.
4. **Anchor the reference class.** "Serious research in the same area you have encountered in the last three years" lets everyone choose a flattering comparison set. Options: name a concrete set (a working-paper series, a journal's recent accepts), or ask the evaluator to place the paper among three or four named comparison papers, or show them where previous Unjournal ratings sit.
5. **Replace the open-science percentile with a checklist.** See above. It also makes the LLM comparison meaningful for this criterion.
6. **Report two numbers, not one.** Because "overall" is a rigor judgment that ignores relevance, summaries should present overall and global-priorities relevance side by side, not a single composite.
7. **Report ratings to the nearest 5 and intervals that reflect two-rater noise.** Heaping tells us the evaluators' precision; decimals in summaries overstate it. For a paper with two evaluations, the mean has a standard error of about 8 points on overall.
8. **Use an LLM rating as a standardised third signal.** Run a fixed frontier-model rating on every package and report it separately, rank-standardised against the model's own distribution (never pooled raw with humans, because of level bias). On current evidence it is at least as informative as a second human on overall and methods and much cheaper.
9. **Do not mix named and anonymous numbers casually.** Anonymous evaluators are about 5 points harsher on the same paper. If a composite score is reported, either adjust or note the composition.
10. **Repeat evaluators are the route to rater adjustment.** With only nine people having done two or more evaluations there is no way to estimate individual leniency. Inviting the same evaluators back, and recording an evaluator identifier in the private data, would make rater-adjusted scores possible within a year or two.

## 10. Other lessons about eliciting beliefs here

- A 90% interval is the wrong elicitation for most people: it yields plus or minus 10 almost regardless of the question. A 50% interval, or a direct question ("what is the chance the true percentile is above 80?"), is both easier to answer and easier to score.
- Ask for at least one resolvable prediction per evaluation that is not journal placement: citations at three years above a threshold, replication outcome, policy uptake. Journal placement resolves slowly and noisily and already looks informative; adding a second forecast gives a track record per evaluator.
- Order and framing matter: overall is the first question on the form and is well predicted by the sub-criteria, consistent with evaluators forming a global impression first and then filling in parts. Asking the sub-criteria (and the claim assessment) before overall would make the overall a synthesis rather than an anchor. This is testable with a randomised form order.
- Because much of the criterion variance is rater-level halo, the cheapest gain in paper-level information per evaluator-hour is more raters on fewer criteria, not more criteria per rater.

## Caveats

Fifty papers with two raters is small; every alpha has a confidence interval wider than the differences between criteria, so the ranking of criteria is suggestive. Evaluators are not randomly assigned to papers. The "true value" the intervals refer to is not observable; the co-evaluator benchmark assumes independent, unbiased evaluators. Data-entry dates are not evaluation dates (I used the package publication date where Coda has it). The journal-tier assignment is hand-made. The LLM comparison re-uses runs from the LLM-evaluation repository (Jan to Mar 2026 for the frontier models) and its paper mapping; 47 papers match.

## Reproducing

```
python3 code/analyze_ratings_quality.py \
  --extra-ratings website/posts/ratings-reliability-2026/extra_ratings_2026.csv \
  --paper-meta <coda research export> --llm-repo ../llm-uj-research-eval \
  --private-db ../unjournal-database/unjournal_data.db \
  --out website/posts/ratings-reliability-2026/results
```

Tables are written as CSV and Markdown, figures as PNG, every number as `results.json`. Without the optional supplements the script still produces sections 1 to 6 from the public export alone, which is what a scheduled run can do.
