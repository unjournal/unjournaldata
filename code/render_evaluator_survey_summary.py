#!/usr/bin/env python3
"""Render approved historical survey aggregates; never reads individual responses."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
folder = root / "website/posts/evaluator-survey-insights"
s = json.loads((folder / "survey_aggregate_snapshot.json").read_text())
y, r, w = s["years"], s["prior_reviews"], s["reevaluation"]
for numerator, denominator in [(y["at_least_ten"], y["n"]), (r["at_least_hundred"], r["n"]), (w["contains_yes"], w["n"])]:
    if not 0 <= numerator <= denominator <= s["survey_records"]:
        raise ValueError("Invalid aggregate count")
text = f"""<!-- Generated from survey_aggregate_snapshot.json by code/render_evaluator_survey_summary.py. -->
## Evaluator experience

The original November 2025 survey snapshot contained **{s['survey_records']} evaluation records**. Among answers that the original analysis could parse:

- **Years in the field:** {y['n']} usable answers; median **{y['median']:g} years**, mean **{y['mean']:.1f} years**. Of these, {y['at_least_ten']} ({100*y['at_least_ten']/y['n']:.0f}%) gave values of at least ten years.
- **Previous reviewing experience:** {r['n']} retained answers; median **{r['median']:g} previous reviews**, mean **{r['mean']:.1f}**. Of these, {r['at_least_hundred']} ({100*r['at_least_hundred']/r['n']:.0f}%) gave values of at least a hundred.

These are historical results from subsets of the survey records, rather than counts of distinct people or an updated survey analysis. The original code extracted numeric values from free-text answers, excluded parsed years at or above a hundred, and retained prior-review counts only when they were at least five. Responses expressed as ranges or lower bounds were reduced to a single number. The prior-review question covered proposals, papers, and projects reviewed for journals, grants, or other peer review. These parsing choices and exclusions limit how representative and precise the summaries are.

## Fields represented

The original snapshot included **{s['field_responses']} nonempty field-of-expertise responses**. The broad areas included economics, policy, behavioral research, and environmental research. This count describes answers, rather than distinct disciplines or distinct people.

## Feedback on the evaluation process

The original snapshot included **{s['feedback_responses']} nonempty responses** about the template and process. Broad themes were:

- Appreciation for clear guidance, a helpful template, and the opportunity to combine written assessment with quantitative ratings.
- Requests for a shorter questionnaire and less form-filling after completing the written evaluation.
- Difficulty using sliders and interpreting ratings with uncertainty intervals.
- Requests for worked examples and clearer instructions.

These themes summarize the earlier post; they were not coded into mutually exclusive categories, and no response shares or ranking of themes are inferred. They describe feedback on the evaluation process rather than on particular papers.

## Willingness to consider a revised evaluation

Of **{w['n']} nonempty answers** to whether the evaluator would consider evaluating a revised version, **{w['contains_yes']} ({100*w['contains_yes']/w['n']:.0f}%)** contained “yes.” This reproduces the original simple text classification. Conditional answers may be included; it does not establish a firm commitment or measure satisfaction.

*The experience and feedback figures above preserve the original November 2025 computed snapshot. They use a different sample from the separately checked public hours export above. The [aggregate snapshot](survey_aggregate_snapshot.json) and [rendering script](https://github.com/unjournal/unjournaldata/blob/main/code/render_evaluator_survey_summary.py) reproduce the displayed historical summaries; the rendering script does not reanalyse individual survey answers.*
"""
(folder / "_survey-summary.md").write_text(text)
print("Rendered approved historical survey aggregates")
