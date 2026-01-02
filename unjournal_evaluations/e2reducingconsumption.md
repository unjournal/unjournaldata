---
affiliation:
- id: 0
  organization: University of Connecticut
article:
  elocation-id: e2reducingconsumption
author:
- Matthew B. Jané
bibliography: /tmp/tmp-58O462V0tqAFHe.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 24
  month: 07
  year: 2025
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: "Evaluation 2 of \"Meaningfully reducing consumption of meat and
  animal products is an unsolved problem: A meta-analysis\""
uri: "https://unjournal.pubpub.org/pub/e2reducingconsumption"
---

# Abstract 

Strengths: The study is highly transparent, with fully reproducible code
and open data. The analytic pipeline is well-documented and is an
excellent example of open science.\
\
Limitations: However, major methodological issues undermine the study\'s
validity. These include improper missing data handling, unnecessary
exclusion of small studies, extensive guessing in effect size coding,
lacking a serious risk-of-bias assessment, and excluding all-but-one
outcome per study. Overall, the transparency is strong, but the
underlying analytic quality is limited.

# Summary Measures

We asked evaluators to give some overall assessments, in addition to
ratings across a range of criteria. *See the *[*evaluation summary
"metrics"*](https://unjournal.pubpub.org/pub/evalsumreducingconsumption#metrics "null")*
for a more detailed breakdown of this. See these ratings in the context
of all Unjournal ratings, with some analysis, in our *[*data
presentation
here.*](https://unjournal.github.io/unjournaldata/chapters/evaluation_data_analysis.html#basic-presentation "null")[^1]*
*

+-------------------+-------------------+---+
|                   | **Rating**        | * |
|                   |                   | * |
|                   |                   | 9 |
|                   |                   | 0 |
|                   |                   | % |
|                   |                   | C |
|                   |                   | r |
|                   |                   | e |
|                   |                   | d |
|                   |                   | i |
|                   |                   | b |
|                   |                   | l |
|                   |                   | e |
|                   |                   | I |
|                   |                   | n |
|                   |                   | t |
|                   |                   | e |
|                   |                   | r |
|                   |                   | v |
|                   |                   | a |
|                   |                   | l |
|                   |                   | * |
|                   |                   | * |
+===================+===================+===+
| **Overall         | 39/100            | 1 |
| assessment **     |                   | 9 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 6 |
|                   |                   | 2 |
+-------------------+-------------------+---+
| **Journal rank    | 1.1/5             | 0 |
| tier, normative   |                   | . |
| rating**          |                   | 4 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 1 |
|                   |                   | . |
|                   |                   | 9 |
+-------------------+-------------------+---+

**Overall assessment **(See footnote[^2])

**Journal rank tier, normative rating (0-5): ** On a 'scale of
journals', what 'quality of journal' should this be published in?[^3]
*Note: 0= lowest/none, 5= highest/best. *

# Claim identification and assessment

## I. Identify the most important and impactful factual claim this research makes[^4] {#i-identify-the-most-important-and-impactful-factual-claim-this-research-makes}

The main claim of the study is: "We conclude that while existing
approaches do not provide a proven remedy to MAP consumption, designs
and measurement strategies have generally been improving over time, and
many promising interventions await rigorous evaluation."

The claim is based on the overall mean effect of \[a standardized mean
differences\] SMD = 0.07 \[0.02, 0.12\].[^5] The claim is central to
practitioners, because they are trying to evaluate interventions to
reduce MAP consumption and based on the evidence the authors are
concluding that there does not seem to be any clear way of doing so at
the moment.

## II. To what extent do you \*believe\* the claim you stated above?[^6] {#ii-to-what-extent-do-you-believe-the-claim-you-stated-above}

I agree with the claim because this is all I have read on this topic and
it does not appear that the evidence of effectiveness (or
ineffectiveness) is very compelling. Outside of this paper I have no
knowledge of this field, so based on this paper alone the evidence is
not convincing of an effective intervention.

## III. Suggested robustness checks[^7] {#iii-suggested-robustness-checks}

Obtain all relevant outcomes and studies (not \[filtering out\] sample
size \<25). Work with a librarian to make a supplementary systematic
search to ensure good coverage. Use proper missing data methods for
non-significant and unreported effects (an R package called `metansue`
does this exact thing). Add a rigorous risk-of-bias assessment that
includes glaring issues such as effect size approximations, outcome
relevance, attrition bias, selective outcome reporting, etc.

# Written report

## Summary

This study conducted a meta-analysis of behavioral interventions aimed
at reducing meat and animal product (MAP) and red and processed mean
(RPM) consumption. They found that, on average, interventions produced
null to small mean reductions in MAP and RPM consumption. While the
analysis was transparent and reproducible, limitations in study
selection, outcome coding, and review methodology may affect the
reliability of the findings.

## Overview of Reproducibility and Transparency

The study demonstrates exemplary transparency. All data are openly
shared, complete with codebooks, and the authors have made the full
analytic pipeline accessible via *CodeOcean* and *GitHub*. Reproducing
the results was straightforward, and all table statistics matched the
raw data outputs. There were no discernible anomalies or outliers in
effect sizes (all falling within the range of approximately --0.4 to
0.8), which supports confidence in data integrity.

One minor critique concerns usability: several key statistical functions
are implemented as custom scripts across different folders rather than
leveraging existing packages (e.g., `metafor`). This added complexity to
code tracing and debugging. While this choice doesn't compromise
reproducibility, it slightly reduces ease-of-use for secondary analysts.

## Comments

### Assigning an effect size of .01 for n.s. results where effects are incalculable {#assigning-an-effect-size-of-01-for-ns-results-where-effects-are-incalculable}

A central concern lies in the handling of studies for which effect sizes
were unreported but described narratively as "non-significant." The
authors imputed a fixed SMD of 0.01 for such cases. While this may
appear conservative, it introduces systematic bias into the analysis.
This practice treats an unknown effect as if it were known with
certainty, ignoring *imputation variance*---the uncertainty inherent in
the imputed value. The correct approach would acknowledge that:[^8]

$$V_{\text{total},i} = V_{\text{imp},i} + V_{\text{sampling},i} + \tau^{2}$$

Yet by setting $y_{i} = 0.01$ and $V_{\text{imp},i} = 0$,  the method
underestimates the total variance, thereby over-weighting imputed
studies. This distorts parameter estimates and artificially tightens
confidence intervals. Moreover, this practice distorts the funnel plot
(see Figure 3 of the manuscript), producing an artificial vertical
cluster of points at 0.01 that hinders interpretation of the standard
error--effect size relationship:

+----------------------------------------------------------------------+
| ![](                                                                 |
| https://assets.pubpub.org/f8r4jr0j/11753260233349.png){#nkpo0x46smf} |
|                                                                      |
| *Figure 1: Figure 3 of paper. Notice the vertical column of data     |
| points that are artificially assigned a value of .01*                |
+======================================================================+
+----------------------------------------------------------------------+

An option to mitigate this is through multiple imputation, which can be
done through the `metansue` (i.e., meta-analysis of non-significant and
unreported effects) package or with `metafor` and `mice` (generic
multiple imputation for meta-analytic models).

### Lack of prediction intervals and heterogeneity

Although prediction intervals are mentioned in the main analysis, they
are inconsistently reported across subgroup analyses. This is a missed
opportunity. Prediction intervals communicate the range of likely
effects in future studies, which is particularly important when the mean
effect is small and the effects are heterogeneous. Their omission makes
it harder to judge the practical utility of interventions, especially
for applied researchers or policymakers interested in expected
real-world effects. Moreover, when only confidence intervals are
reported, readers often misinterpret them as indicating the full range
of plausible effects, even though true effects may lie well outside that
interval; this misperception can lead to overconfidence in the precision
and directionality of observed results.

### Not including small studies

The exclusion of small-sample studies (i.e., \<25 per group) is
unwarranted. Often the idea is that it will better account for
publication bias because publication bias occurs most often at small
sample sizes by definition. However, this actually just makes
publication bias harder to correct for and harder to detect since you
are actively restricting the range of standard errors and thus
attenuating the correlation between effect sizes and standard errors.

Based on a manual count from the data of excluded studies provided,
there were at least 16 studies were excluded solely for having small
sample sizes with no other exclusion reasons.

### Selected only one effect from each intervention

The authors extract only a single effect per intervention: the outcome
with the longest follow-up measuring net MAP or RPM consumption. While
this rule ensures statistical independence, it comes at the cost of
discarding valuable data.

In the section *"Selecting an appropriate dependent variable from
studies with multiple outcomes,"* the authors describe a hierarchical
decision rule that selects the most preferred outcome when multiple
outcomes are reported. This approach introduces selection issues and
unnecessarily throws out data. For example, if a study reports both
outcomes A and B, the authors extract A based on their hierarchy. But if
another study reports only B, then B is extracted. This creates a
paradox where outcome B is treated as sufficient evidence in one context
but ignored in another, even when available.

Given that the authors employ multilevel meta-analytic methods and
robust variance estimation in other parts of the analysis, there is no
compelling reason to exclude valid outcome data. A more appropriate
strategy would be to include all relevant outcomes and effects per study
and account for dependence using multivariate, multilevel, or robust
variance estimation models. This would improve statistical power and
provide a clearer partitioning of effect heterogeneity.

### Unstructured risk of bias assessment without a clear definition of low/high risk of bias

The authors claim to conduct a risk of bias assessment, but it is
informal and incomplete. Instead of using a validated tool such as
Cochrane RoB 2.0, the paper restricts itself to meta-regressions based
on open data/pre-registration, publication status, and self-report
versus objective outcomes.

This approach omits critical sources of bias that are arguably much more
important such as:

-   Selective outcome reporting

-   Attrition and incomplete data

-   Approximate or reconstructed statistics

-   Lack of blinding

Without a structured risk-of-bias framework, it's difficult to evaluate
study quality or weigh evidence accordingly.

### No discussion of attrition bias in RCTs

Many included studies rely on complete-case analyses, ignoring
participants who dropped out post-randomization or failed to report
outcomes. This omission is especially concerning given the known
non-randomness of attrition in dietary interventions (e.g., due to
disinterest, dissatisfaction, or disinhibition). The meta-analysts
should have prioritized *intent-to-treat (ITT)* analyses since
complete-case analysis undermines causal inference, as the benefits of
randomization are lost when dropout is differential. ITT analysis should
be the default for RCTs to preserve internal validity.

## Heavy use of guesswork and approximation in effect size coding

The authors are commendably transparent about how they derived effect
sizes, but this very transparency reveals that many estimates involve
substantial reconstruction, approximation, or inference that were not
systematic or proper. This includes:

-   Coding of "null results" as 0.01 (discussed in a prior section)

-   Subjective decisions about which effect to extract when multiple
    results were reported

-   Improper conversions

-   Approximating missing standard deviations

-   Guessing sample sizes

Such practices are often necessary in meta-analytic work, especially
when dealing with legacy studies or poor reporting standards. However,
these approximations introduce non-trivial uncertainty that should be
formally incorporated into the analysis, either through model-based
sensitivity checks or risk-of-bias items. As it stands, the
meta-analysis appears to treat these derived estimates as fully known
point values with sampling error only.

Below are direct quotes from the coding notes that illustrate the extent
of approximation:

> "No SD given but we're told there was overall no effect." ---Note
> \[17\]
>
> "No SD given but we're told there was overall no effect. At posttest
> the affective focus group eats more meat than the control group and
> the cognitive group eats less. If we had SD information this would be
> recorded as a minor backlash." ---Note \[16\]
>
> "taking sample C as the sample but ultimately the results are all the
> same (nulls). Noting here that this study slipped through many
> systematic review cracks before. I was at first backing the SD out of
> confidence intervals but the regressions control for gender so that
> doesn't work." ---Note \[24\]
>
> "The Ns are a bit of guesswork, but the lead author emailed to give
> average numbers of meals per intervention period, whcih I multipled by
> the number of restaurants times the number of days times a slight
> discount (0.9) to account for potential repeat customers." ---Note
> \[33\]
>
> "Taking Ns from text on '1985 dinner parties.' Parties probably have,
> what, an average of 2 people per group? I'll just divide that by 2.
> This is, clearly, a lot of guesswork." ---Note \[102\]
>
> "We really want is proportion of vegetarian meals ordered on the
> treatment days minus proportion of vegetarian meals ordered on control
> days without covariates and we want both data points reported. Instead
> we have z scores which are beta / se and theoretically se = sd /
> sqrt(n) assuming no covariates (which there are) so hypothetically we
> can convert z to via z/sqrt(n). Close enough I think. I am also using
> Ns from the total number of pariticpants, subtracting the percentage
> that ordered multple meals or meals for others & dividing by two."
> ---Note \[105\]
>
> "The effect size is a bit of guesswork here, as is the sign.
> Apparently red meat reduced significantly in treatment vs control but
> what actually seems to have happened is that red meat stayed constant
> in treatment from 0 to 6 months and went up in control, but white meat
> went down in control by a lot but just by a little in treatment. So
> I'm just summing the numbers in table 4 and dividing by the pooled SD
> from table 3. Is this null? I think so, if you average them together.
> If you care about health this treatment 'worked' (maybe just prevented
> regression to the mean?) but really who can say and also the
> intervention is not described in much detail. I feel comfortable with
> this level of ambiguity, delta = 0.11 is probably about right for the
> overall changes." ---Note \[43\]

These examples suggest that a considerable fraction of the effect size
dataset is constructed through improper, approximate, and unsystematic
calculations.

### Unsystematic literature review

While the authors include a PRISMA flowchart, the review process lacks
sufficient detail and transparency to be considered systematic or
reproducible. Key elements such as a fully reproducible search strategy,
clearly articulated inclusion and exclusion criteria (which are
referenced inconsistently across the text and code), and justification
for screening decisions are not comprehensively documented in the
manuscript or supplement. The use of Google Scholar precludes
reproducible searches. And relying on prior reviews is convenient
although it inherits those reviews potentially unsystematic and
non-reproducible searches. While it may be possible to reproduce the
references used, the upstream decisions made by those earlier reviews
may themselves be opaque, inconsistent, or non-systematic.

Without a clearly reported and reproducible review protocol, it is
difficult to assess whether the evidence base is comprehensive or
unbiased. This uncertainty weakens confidence in the validity and
generalizability of the meta-analytic findings.

I would recommend having an academic librarian help build a more
transparent and reproducible systematic review.

## Conclusion

While the study is highly transparent and reproducible, with
well-documented data and code, it falls short in several important
methodological areas. The lack of a systematic review protocol, the use
of improper effect size coding, the exclusion of small studies, the
handling of missing data, lack of a serious risk-of-bias assessment, and
exclusion of all-but-one outcome per study all raise serious concerns.
Many analytic decisions, though openly reported, reflect unsound
practices that introduce bias and reduce the reliability of the
findings. These issues limit the applied usefulness of the
meta-analysis. Overall, aside from its commendable transparency, the
meta-analysis is not of particularly high quality.

# Evaluator details

1.   What is your research field or area of expertise, as relevant to
    this research?

    -   Meta-analysis

2.  How long have you been in your field of expertise?

    -   4 years

3.  How many proposals, papers, and projects have you evaluated/reviewed
    (for journals, grants, or other peer-review)?

    -   \>10

[^1]: Note: if you are reading this before, or soon after this has been
    publicly released, the ratings from this paper may not yet have been
    incorporated into that data presentation.

[^2]: We asked them to rank this paper "heuristically" as a percentile
    "relative to all serious research in the same area that you have
    encountered in the last three years." We requested they "consider
    all aspects of quality, credibility, importance to knowledge
    production, and importance to practice.

[^3]: See ranking tiers discussed
    [here](https://globalimpact.gitbook.io/the-unjournal-project-and-communication-space/policies-projects-evaluation-workflow/evaluation/guidelines-for-evaluators#journal-ranking-tiers).

[^4]: The evaluator was given the following instructions: Identify the
    most important and impactful factual claim this research makes --
    e.g., a binary claim or a point estimate or prediction.

    Please state the authors' claim precisely and quantitatively.
    Identify the source of the claim (i.e., cite the paper), and briefly
    mention the evidence underlying this. We encourage you to explain
    why you believe this claim is important, either here, or in the text
    of your report.

[^5]: Manager: The term in brackets represents a 95% CI. I presume this
    is a frequentist 'confidence interval' given the terminology in the
    rest of the paper, rather than a Bayesian 'credible interval'.

[^6]: "Feel free to express this in terms of the probability of the
    claim being true or as a credible interval for the parameter being
    estimated."

[^7]: *We asked:*

    \[Optional\] What additional information, evidence, replication, or
    robustness check would make you substantially more (or less)
    confident in this claim?

    Feel free to refer to the main body of your evaluation here; you
    don\'t need to repeat yourself. Please specify how you would perform
    this robustness check (etc.) as precisely as you are willing. E.g.,
    if you suggest a particular estimation command in a statistical
    package, this could be very helpful for future robustness
    replication work.

[^8]: Manager: I believer tau\^2 here refers to between-study
    heterogeneity variance
