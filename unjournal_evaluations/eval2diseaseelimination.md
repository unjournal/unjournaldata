---
article:
  elocation-id: eval2diseaseelimination
author:
- Evaluator 2 (Unjournal, anonymous)
bibliography: /tmp/tmp-46z05tLvm0aB0b.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 16
  month: 07
  year: 2024
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 2 of "Economic vs. Epidemiological Approaches to
  Measuring the Human Capital Impacts of Infectious Disease Elimination"
uri: "https://unjournal.pubpub.org/pub/eval2diseaseelimination"
---

# Abstract 

This paper presents an interesting comparison of two methods for
estimating the impact of measles on long-term health and economic
outcomes: an epidemiological model to estimate variation in measles
infection across cohorts and, as more standard in economics, a
reduced-form model that uses variation in pre-vaccination measles
mortality across place. It is a fascinating and important study that
highlights the strengths and weaknesses of the two approaches. However,
pushing a bit further on the assumptions and measurement issues
associated with each approach and having a fuller explanation of the
differences in the empirical results would make for an even stronger
contribution.

# Summary Measures

We asked evaluators to give some overall assessments, in addition to
ratings across a range of criteria. *See the *[*evaluation summary
"metrics"*](https://unjournal.pubpub.org/pub/evalsumdiseaseelimination#ndhjuwlebbv "null")*
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
| **Overall         | 80/100            | 6 |
| assessment **     |                   | 5 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 9 |
|                   |                   | 0 |
+-------------------+-------------------+---+
| **Journal rank    | 3.3/5             | 2 |
| tier, normative   |                   | . |
| rating**          |                   | 6 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 4 |
|                   |                   | . |
|                   |                   | 1 |
+-------------------+-------------------+---+

**Overall assessment: **We asked evaluators to rank this paper
"heuristically" as a percentile "relative to all serious research in the
same area that you have encountered in the last three years." We
requested they "consider all aspects of quality, credibility, importance
to knowledge production, and importance to practice."

**Journal rank tier, normative rating (0-5): **"On a 'scale of
journals', what 'quality of journal' should this be published in? (See
ranking tiers discussed
[here](https://globalimpact.gitbook.io/the-unjournal-project-and-communication-space/policies-projects-evaluation-workflow/evaluation/guidelines-for-evaluators#journal-ranking-tiers "null"))"
*Note: 0= lowest/none, 5= highest/best".*

*See
*[*here*](https://globalimpact.gitbook.io/the-unjournal-project-and-communication-space/policies-projects-evaluation-workflow/evaluation/guidelines-for-evaluators#metrics-overall-assessment-categories "null")*
for the full evaluator guidelines, including further explanation of the
requested ratings.*

# Written report[^2]

This well-written paper provides an interesting comparison of two
different approaches to estimating the long-term health, education, and
income impacts of measles in the United States. Both approaches center
around using variation in measles exposure generated by the rollout of
the measles vaccine in 1963. The first approach is epidemiology-based,
using state-year data on measles infections along with vaccination rates
to estimate the share-ever-infected of each cohort and then using this
as the independent variable of interest. The second approach, which the
authors rightly identify as the main approach within the economics
literature, uses variation in pre-vaccine measles severity, proxied by
measles mortality, interacted with a dummy for the pre-vaccination
period, as the key independent variable. Note that, following the
authors, I will refer to this second approach as the reduced-form
approach.

When using the reduced-form approach, the authors find significant
long-term impacts of measles in the expected ways: exposure to a higher
measles mortality environment was associated with lower levels of high
school completion, lower income, higher levels of unemployment, and
higher levels of welfare income and food stamp usage. The
epidemiological approach finds noticeably different impacts, with higher
shares of measles infection showing a statistically insignificant
relationship with later life outcomes. Additionally, these estimates
appear far more sensitive to model specification than the reduced-form
results.

The paper presents compelling evidence that epidemiological and
reduced-form approaches provide different perspectives on the long-term
impacts of infectious disease elimination. However, to properly
interpret those differences, I think the paper needs to dig a bit deeper
into the impacts of the different assumptions built into the two
approaches and offer more guidance as to how to interpret differences in
the results. I elaborate on these points in the comments below.

**\[Cases vs. deaths\]**

1.  One significant focus of the paper when interpreting results, and in
    my view one of the significant theoretical differences between
    taking epidemiological versus reduced-form approaches, is the
    difference between focusing on cases versus deaths. It is
    understandable that most reduced-form studies will inevitably rely
    on mortality statistics because the data are more readily available
    and more accurately measured. The underlying assumption of most of
    these reduced-form papers is that a worse disease environment in
    terms of mortality is likely highly correlated with a worse disease
    environment for those who survive. The paper would benefit from
    offering the reader more guidance about how likely this assumption
    is to hold both in terms of measles and more broadly.

    Figure 4 (a really helpful figure for understanding the three
    different measures of measles exposure) suggests that infection
    rates and mortality rates do not necessarily move in lockstep with
    one another. Note how Washington and Arkansas completely flip in
    terms of level of measles exposure when switching from *share
    infected* to *pre-vaccine mortality*. The reader needs more context
    for how a deadly outbreak of measles differs from a less lethal
    outbreak and how those differences likely translate into different
    patterns of human capital formation. This seems essential to both
    understanding the empirical results but also to understanding the
    value of the two different approaches to measurement and when we
    should favor one over the other.

    **\[Cohort trend vs cohort fixed effects: why are the 'epi' models
    so sensitive to this?\]**

2.  While the point above is primarily about the real-world aspects of
    more and less lethal measles outbreaks, the empirical results also
    make me wonder if \[there\] is a very different but important issue
    related to the econometrics of the epidemiological model versus the
    reduced-form model. I think both models and their assumptions are
    both well-motivated and well-explained in the current manuscript.
    However, the main results suggest that there is something missing on
    the econometrics side. In particular, it was surprising to see how
    sensitive the epidemiological estimates were to the choice of
    controlling for either cohort trends or cohort fixed effects. The
    reduced-form results were pretty much unchanged by this choice but
    the epidemiological results not only changed substantially but
    typically flipped signs. This is noted in the paper but never
    explained. In my view, it is essential to figure out what is going
    on here. What I suspect is that the method for calculating cohort
    exposure to measles by estimating the number of susceptible
    individuals in the cohort each successive year is generating a
    correlation by construction with the cohort trends that might be
    throwing off results through multicollinearity issues.

    **\[Doubts about cohort trends in epi model\]**

    I haven't thought that through fully but I think the paper needs to
    grapple with whether the inclusion of cohort trends is compatible
    with the way cohort exposure is calculated.

    **\[Puzzling 'sign flips' between results of epi and reduced-form
    models\]**

    While the econometrics of that remain a bit out of reach for me, it
    is far clearer to me that the cohort fixed effects results are both
    easier to interpret and seem more defensible. That being the case,
    the paper needs to do more to explain the opposite signs on the
    long-term effects results for the epidemiological results compared
    to the reduced-form results. All of the reasoning throughout the
    paper relates to different magnitudes of effects, not different
    signs. Coming up with an explanation for those sign flips is
    important for establishing the credibility of the epidemiological
    approach (note that the power of the approach to predict future
    outbreaks is really convincing evidence of the credibility of the
    approach, evidence that I think could be emphasized even more, but
    explaining the sign flips still seems essential as well). The only
    explanation for sign flips between infections and deaths that
    immediately comes to mind is if there is some sort of culling effect
    going on, leaving a healthier but smaller population in the wake of
    severe measles outbreaks.

    **\[Measurement issues for both approaches\]**

3.  There were a few places where I would like to see a bit more about
    measurement issues for both measures and whether those issues are
    likely to generate attenuation biases in the results. For the
    reduced-form approach, how accurately does *stated cause of death*
    capture measles deaths? Are deaths from related complications like
    pneumonia included? If not, do we have a sense of how much measles
    deaths are being underreported? If so, do we have a sense of how
    much they might be overreported?

    For the epidemiological approach, could you offer a bit more to get
    a handle on the variation in both reporting rates and immunization
    rates? For the reporting rates, I find the approach of allowing them
    to vary over time the most reasonable and would recommend that it be
    the main approach rather than relegated to the appendix. I'd also be
    curious as to how variation in reporting rates correlates with other
    relevant state statistics (from the map, it appears that higher
    reporting rates are potentially positively correlated with income
    and with school attendance, pretty relevant correlations). For the
    immunization rates, I understand the need to use national estimates
    given the lack of state-level data but we know that in recent years
    these rates vary substantially across states. From the October 18,
    2019 Morbidity and Mortality Weekly Report, the national average for
    MMR vaccination rate is 94.7% yet some states like some states like
    Idaho are below 90%. That would lead to some substantial measurement
    error in the measles exposure estimates. It would be useful to track
    down earlier data on variation in immunization rates across states
    or to at least point to sources that document a divergence in
    immunization rates being a more modern phenomenon.

    **\[Compare to Atwood (2022) more closely to unpack the source of
    the differences\]**

4.  While this paper highlights the differences in measuring infection
    versus mortality by comparing the epidemiological model results to
    the reduced-form results, and does so with solid discussions, it
    seems equally important to dive deeper into the differences in the
    reduced-form results in this paper and those in Atwood
    (2022)[@nb5e0cokpk4]. As noted in this paper, the Atwood results
    aren't exactly the same as they focus on measles cases rather than
    deaths. Given this, should we expect the Atwood results to more
    closely track the epidemiological results of this paper? Or is it
    really the methodology (epi versus reduced-form) that makes the
    biggest difference as opposed to the cases versus mortality, meaning
    the Atwood results should more closely align with this paper's
    reduced-form results? Doing more to address these questions would
    both help distinguish this paper's contribution from Atwood but also
    provide a lot more clarity about the broad goal of showing how the
    measurement of infectious disease impacts estimates of its long-term
    impacts.

## References

[@nzy58xud3t0]Atwood, A. (2022). The Long-Term Effects of Measles
Vaccination on Earnings and Employment. *American Economic Journal:
Economic Policy*, *14*(2), 34--60.
[https://doi.org/10.1257/pol.2](https://doi.org/10.1257/pol.20190509 "null")

# Evaluator details

1.  How long have you been in this field?

    -   \[Range-coded to preserve anonymity: 15-20 years\]

2.  How many proposals and papers have you evaluated?

    -   roughly 75

[^1]: Note: if you are reading this before, or soon after this has been
    publicly released, the ratings from this paper may not yet have been
    incorporated into that data presentation.

[^2]: Managers note: We made some very small typographical adjustments
    to the evaluator's text. We also added the bracketed 'headers' above
    the numbered comments and within some sections.
