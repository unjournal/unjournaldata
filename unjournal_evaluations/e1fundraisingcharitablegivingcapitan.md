---
affiliation:
- id: 0
  organization: Swedish University of Agricultural Sciences
article:
  elocation-id: e1fundraisingcharitablegivingcapitan
author:
- Tabaré Capitán
bibliography: /tmp/tmp-60Y6520EFxPvJo.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 1 of "Does online fundraising increase charitable
  giving? A nationwide field experiment on Facebook"
uri: "https://unjournal.pubpub.org/pub/e1fundraisingcharitablegivingcapitan"
---

# Abstract 

This is a large-scale, well-executed field experiment on Facebook ads
for charitable giving in Germany. Randomized at the postal code level,
the study finds that the campaign increased donations both short- and
medium-term, without reducing future giving to the same charity---but
possibly crowding out donations to others. Content and delivery method
had no differential effect. The design is strong and materials are fully
replicable.

# Summary Measures

We asked evaluators to give some overall assessments, in addition to
ratings across a range of criteria. *See the *[*evaluation summary
"metrics"*](https://unjournal.pubpub.org/pub/evalsumfundraisingcharitablegiving#metrics "null")*
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
| **Overall         | 92/100            | 8 |
| assessment **     |                   | 5 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 9 |
|                   |                   | 5 |
+-------------------+-------------------+---+
| **Journal rank    | 4.8/5             | 4 |
| tier, normative   |                   | . |
| rating**          |                   | 6 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 5 |
|                   |                   | . |
|                   |                   | 0 |
+-------------------+-------------------+---+

**Overall assessment **(See footnote[^2])

**Journal rank tier, normative rating (0-5): ** On a 'scale of
journals', what 'quality of journal' should this be published in?[^3]
*Note: 0= lowest/none, 5= highest/best. *

# Claim identification and assessment [^4]

## I. Identify the most important and impactful factual claim this research makes[^5] {#i-identify-the-most-important-and-impactful-factual-claim-this-research-makes}

Abstract: However, we also found some crowding out of donations to other
similar charities or projects.

Table 3 shows a negative change in revenue in 23 other similar charities
in response to the exogenous variation created by the campaign.

It is particularly important because, according to the authors, there is
a belief in this literature that charities are complements. In other
words, a new donor is good news for everyone. In contrast, this result
imply competition. If this is the case, then any funds spent on
fundraising may be simply re-distributing a fixed cake (and making it
smaller).

## II. To what extent do you \*believe\* the claim you stated above?[^6] {#ii-to-what-extent-do-you-believe-the-claim-you-stated-above}

Like 90%. They don't have the same level of data quality \[for the data
on similar charities\] as \[for\] their main dataset, but it is very
comprehensive.

# Written report

## Evaluation summary

This is a high-powered field experiment with little room to improve. In
partnership with a charity in Germany, the authors designed and deployed
a campaign in Facebook to increase donations to the partner charity.
They were able to reach, essentially, all of Germany, at the postal code
level. They randomized postal codes into five groups. One group was a
control. The next four groups come from a 2x2 factorial design, varying
the content of the (video) ad and the way in which the ad was shown to
Facebook users. Given randomization, simple comparison of means between
the control and pooled treatment groups yield causal estimates of the
effect of the campaign. The key result of this paper is that the ad
increased revenue both during the campaign and in the subsequent five
weeks. Importantly, the \"long-term\" increase, provided the well-timed
deployment around the holiday season, suggests that the increased
donations did not come at the expense of future planned donations to the
same charity. However, the same does not hold true for other charities.
External data suggests that the increased revenue crowded out donations
to other charities. Furthermore, using the 2x2 factorial design, the
authors show that neither the content of the video nor the impression
assignment strategy make a difference in the overall treatment effect.

The experimental design, methods, and robustness checks are appropriate;
making their causal estimates credible. Furthermore, the authors provide
a comprehensive supplement and replication materials. The replication
material detail how to obtain the data and it is indeed accesible; the
code is well organized and easy to use. In the remaining of this
evaluation I list the main claims of the paper, as well as some
lingering concerns or issues.

## Main claims

1\. Campaign increased donation revenue and frequency during the
campaign and in the subsequent five weeks.\
2. The campaign was profitable for the fundraiser. \
3. The effects were similar regardless of the content of the campaign or
the impression assignment strategy.\
4. The campaign crowds out donations from other charities.

## Concerns

**Is the campaign profitable?**

Comment on Profitability Estimates

The paper [@n83rua1y4yi] argues that the campaign was profitable, which
is a key practical claim and a major justification for scaling similar
interventions. Based on point estimates, this appears plausible: the
immediate return per euro spent is estimated at €1.45, rising to €1.75
when incorporating assumptions about future donations from new recurring
donors, and up to €2.53 when including revenue from all donors exposed
to the ad.

However, the claim rests on assumptions on top of significant
uncertainty, especially in the long-term estimate. The 95% confidence
interval for the €2.53 ROI is wide---ranging from €0.15 to €2.74. While
point estimates suggest the campaign may be profitable, the interval
includes values that wipe out profitability. In hypothesis testing, we
would treat the inclusion of zero in a confidence interval as evidence
of no statistically significant effect. By that logic, the inclusion of
low revenue values  in the CI should raise similar caution. For example,
€5000 in revenue is within the CI, as opposed to the €47726 point
estimate used to calculate their most conservative ROI of €1.45. At
most, the paper suggests that an online fundraiser may be profitable,
but it is a risky move.

Moreover, the analysis assumes a "lifetime" value for recurring donors
based on short-term behavior: about 30% of new donors chose recurring
donations. But without data on donation persistence, the assumption of
lifetime giving is strong. If recurring donations last for only 1--2
years, the actual return could be substantially lower. Additionally, the
extrapolation assumes that each donor's recurring amount equals their
initial donation adjusted for discounting, which may not reflect actual
donor trajectories, particularly if influenced by platform defaults or
one-off generosity.

Finally, the suggestion that profitability could be increased through
targeted campaigns is reasonable but incomplete. Targeted ads are
typically more expensive under Facebook's auction model, especially when
targeting higher-value individuals. If ad pricing internalizes the
predicted return per user, the margin for increased profitability may be
limited or negative. It would be constructive for the authors to
acknowledge that the ROI under algorithmic targeting depends on both
improved efficiency and potential increases in ad costs---something not
currently addressed.

In sum, the campaign appears profitable by point estimate, but the
confidence intervals and strong behavioral assumptions warrant a more
cautious interpretation. Highlighting this uncertainty
explicitly---especially in the abstract and introduction---would enhance
transparency without undermining the value of the findings.

**How external is the external validity?**

The external validity of the findings within Germany is strong by
design, as the sample covers essentially the entire country and includes
a large, heterogeneous population of potential donors. However,
generalizing these results to other national contexts---especially
outside Europe---requires more caution.

Donor behavior is shaped by cultural norms, institutional arrangements,
and the structure of the nonprofit sector. For instance, in the United
States, charitable giving is more prevalent as a share of GDP and
strongly incentivized through tax deductions. In contrast, Germany (and
much of continental Europe) tends to rely more on state-supported social
services, with relatively less individual-level charitable giving and
weaker tax incentives.

This implies that U.S. donors may respond differently to online
fundraising efforts, both in terms of volume and substitution patterns.
Additionally, competition among nonprofits is more intense in the U.S.,
and digital fundraising campaigns are more common and professionally
managed. These factors could affect both the baseline responsiveness to
ads and the degree of donor substitution between organizations.

To inform external validity, the paper could (have) usefully reflect on
how Germany compares to other contexts along key institutional and
behavioral dimensions: tax treatment, norms around giving, fundraising
saturation, and digital engagement. Comparative evidence on donor
behavior (e.g., Bekkers & Wiepking 2011 [@nd2bplnndv8]; Andreoni 2006
[@nz12gw5c2aa]) suggests that motivations such as empathy, perceived
impact, and social signaling are broadly shared, but their relative
strength may vary.

**Randomization is a process, not a result**

Table A1 is titled "Results of Randomization," yet what is shown is not
evidence of whether randomization occurred, but rather covariate balance
between treatment arms. Randomization is a design property---it either
happened or it did not---and cannot be inferred from the observed
balance in covariates. As such, interpreting covariate balance tables as
a test of randomization is conceptually incorrect.

Moreover, the use of t-tests to assess balance is misleading.
\$p\$-values are a function of both effect size and sample size. As the
number of observations increases, even trivial differences in means can
become statistically significant. Conversely, with small samples,
substantial imbalance may yield high \$p\$-values. This results in the
paradox where increased sample size suggests "worse" balance due to
lower p-values, despite the imbalance remaining constant.

See Freedman (2008) for a formal critique:

> [@nyk9qwbzp2u] Freedman, D.A. (2008). \"On regression adjustments to
> experimental data.\" \*Advances in Applied Mathematics\* 40(2):
> 180--193.

Freedman shows mathematically that balance tests do not provide evidence
for or against randomization, and that regression adjustments (including
t-tests) post-randomization can introduce bias in finite samples. (Which
is admittedly not the case for this paper). The key insight is that
under random assignment, any observed imbalance is due to chance, and no
correction or test is necessary to "validate" the assignment.

A more appropriate approach is to report standardized differences in
covariates without relying on hypothesis tests. This allows readers to
assess the magnitude of any chance imbalances without conflating
statistical significance with practical importance. Imbens & Rubin\'s
(2015 [@novz35070jh]) book on causal inference provide guidance in this
regard.

## References

[@nnmowcfvc5p] Adena, Maja, and Anselm Hager. 2025. 'Does Online
Fundraising Increase Charitable Giving? A Nationwide Field Experiment on
Facebook'. *Management Science* 71 (4): 3216--31.
<https://doi.org/10.1287/mnsc.2020.00596>.

[@n1k3z7u7a39] Bekkers, R., & Wiepking, P. (2011). A literature review
of empirical studies of philanthropy: Eight mechanisms that drive
charitable giving. *Nonprofit and voluntary sector quarterly,* 40 (5),
924-973.

[@nhxyf3f5q7x] Andreoni, J. (2006). Philanthropy. *Handbook of the
economics of giving, altruism and reciprocity*, 2, 1201-1269.

[@nqyhaotxn1x] Freedman, D.A. (2008). \"On regression adjustments to
experimental data.\" *Advances in Applied Mathematics* 40(2): 180--193.

[@nce7y4izuxb] Imbens, G. W., & Rubin, D. B. (2015). *Causal inference
in statistics, social, and biomedical sciences*. Cambridge university
press.

# Evaluator details

1.   What is your research field or area of expertise, as relevant to
    this research?

    -   Experimental and behavioral economics

2.  How long have you been in your field of expertise?

    -   10+

3.  How many proposals, papers, and projects have you evaluated/reviewed
    (for journals, grants, or other peer-review)?

    -   10+

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

[^4]: This comes from the form. If the author didn't do this, please
    skip this section.

[^5]: The evaluator was given the following instructions: Identify the
    most important and impactful factual claim this research makes --
    e.g., a binary claim or a point estimate or prediction.

    Please state the authors' claim precisely and quantitatively.
    Identify the source of the claim (i.e., cite the paper), and briefly
    mention the evidence underlying this. We encourage you to explain
    why you believe this claim is important, either here, or in the text
    of your report.

[^6]: "Feel free to express this in terms of the probability of the
    claim being true or as a credible interval for the parameter being
    estimated."
