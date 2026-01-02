---
article:
  doi: 10.21428/d28e8e57.50ee8ef7/cac9213e
  elocation-id: e1publicscience
author:
- Evaluator 1
bibliography: /tmp/tmp-60QRGJpP7yZ4Os.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 19
  month: 06
  year: 2025
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 1 of "The Effect of Public Science on Corporate R&D"
uri: "https://unjournal.pubpub.org/pub/e1publicscience"
---

# Abstract 

The paper provides evidence on a recently relevant issue in science
policy: the spillover effects of public science. However, these effects
are not well-identified. There are numerous issues likely distorting the
identification, including bad controls and a shift-share design with
endogenous shares.

# Summary Measures

We asked evaluators to give some overall assessments, in addition to
ratings across a range of criteria. *See the *[*evaluation summary
"metrics"*](https://unjournal.pubpub.org/pub/evalsumpublicscience#metrics "null")*
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
| **Overall         | 64/100            | 5 |
| assessment **     |                   | 8 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 7 |
|                   |                   | 0 |
+-------------------+-------------------+---+
| **Journal rank    | 2.8/5             | 2 |
| tier, normative   |                   | . |
| rating**          |                   | 4 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 3 |
|                   |                   | . |
|                   |                   | 2 |
+-------------------+-------------------+---+

**Overall assessment **(See footnote[^2])

**Journal rank tier, normative rating (0-5): ** On a 'scale of
journals', what 'quality of journal' should this be published in?[^3]
*Note: 0= lowest/none, 5= highest/best. *

# Claim identification and assessment

## I. Identify the most important and impactful factual claim this research makes[^4] {#i-identify-the-most-important-and-impactful-factual-claim-this-research-makes}

Increased exposure to public invention decreases a firm's private R&D
expenditure.

## II. To what extent do you \*believe\* the claim you stated above?[^5] {#ii-to-what-extent-do-you-believe-the-claim-you-stated-above}

In a binary sense, I believe neither the sign nor magnitude of this
estimated relationship. My prior is, however, moved by the theoretical
possibility that the relationship could be negative.

# Written report

This paper tries to identify the impact of three forms of public science
on corporate R&D:

1.  public invention (i.e., university patents)[^6]

2.  human capital (i.e., PhD dissertations), and

3.  public knowledge (i.e., non-corporate publications).

The headline results are that (1) crowds out corporate innovation, (2)
boosts corporate innovation, and (3) has no meaningful effect. \

The identification strategy relies on a shift-share design, where the
shifts are based on U.S. congressional subcommittee spending on public
science and the shares are based on firm exposure to specific
subcommittee's shocks (based on firms' exposure to expenditures from
specific government agencies and the subcommittees responsible for those
agencies' funding). To address potential exclusion restriction
violations, the paper does not use raw changes in subcommittee
appropriations as its primary shock variable, but instead uses the
changes in appropriations predicted by those subcommittees' party
shares. **This report identifies two key issues in the identification
strategy ***\[Manager: Bold emphasis added, here and below\] *\

**First, the paper's shift-share design likely yields biased results due
to the endogeneity of the shares.** The primary IV models shown in the
paper instrument firms' exposure to public science using a series of
shift-share formulas that, generally speaking, instrument a firm's
exposure to public innovation with a sum of the products of (1) the
share of a firms' exposure to a specific class of innovation (e.g.,
publication subfields, patent subclassifications, etc) and (2) the
predicted R&D expenditures from all federal agencies for that innovation
class. (1) is likely endogenous; the paper indeed finds a positive
correlation between firm R&D stock and agency R&D funding. Of course,
this is only one source of endogeneity, and many more may exist. This is
a general gripe with shift-share designs; much is discussed about how
exogenous the shocks are but little attention is paid to whether the
*shares* are endogenous, which they often are.

\
The paper attempts to address the endogeneity of shares by controlling
for lagged firm-level R&D stock, but this exposes the paper to a third
identification issue: **the main specifications all control for
colliders.** An often-overlooked issue in control specifications is
whether the controls are themselves outcomes of the main exposures of
interest (in this case, public science). Cinelli, Forney, & Pearl (2024)
show that if a covariate is (1) influenced by an exposure of interest
and (2) shares a common unobserved confounder with the outcome, then
controlling for the covariate will bias the estimated relationship
between the outcome and the exposure of interest. To illustrate,
consider the 'birth weight paradox' (Hernández-Díaz, Schisterman, &
Hernán 2006). Though maternal smoking is associated with higher infant
mortality and more incidence of low birth weight, when controlling for
birth weight, maternal smoking appears to decrease infant mortality.
This is not because maternal smoking actually decreases infant
mortality, but rather because newborns who are low birth weight *because
of maternal smoking* likely exhibit lower mortality rates than newborns
who are low birth weight *because of other health complications*.
Applying this concept to the paper's specifications, firm exposure to
public science may not decrease firm innovation; rather, it may be the
case that firms with more R&D stock *due to public science* innovate
less than firms who have more R&D stock *due to the inherent innovative
nature of their activities*.

\
These issues together place the entire identification strategy in a
bind. Firms with innovation profiles similar to those invested into by
public agencies likely have different levels of R&D investment for
reasons unrelated to public science, but controlling for these levels of
R&D investment yields bad control problems because private R&D
investment is inherently influenced by public science. The clear
endogeneity issues with the shift-share design do not seem like they can
be controlled away with observable covariates.\
\
With public science funding under threat both in the United States and
globally, the paper's findings could mislead policymakers on the
importance of public science for the private sector given the
credibility issues with the empirical design. The paper's findings
effectively imply that the research function of universities is, if
anything, negative for the private sector. Given that the only positive
relationship between university research activity and firm outcomes is
found in the graduation of new PhDs, the policy implications of this
paper taken at face value would imply that universities should
prioritize training PhDs while simultaneously cutting back on university
invention. Given that universities conduct the bulk of all basic
scientific research, such a reorientation of university priorities
should not arise without more credible evidence.

## References 

[@nsvy7yy0cgl] Cinelli, C., Forney, P., & Pearl, J. (2024). "A crash
course in good and bad controls." *Sociological Methods & Research*
53(3), 1071-1104. https://doi.org/10.1177/00491241221099552. \
\
[@nr03kumrrxl] Hernández-Díaz, S., Schisterman, E. F., & Hernán, M. A.
(2006). "The birth weight 'paradox' uncovered?" *American Journal of
Epidemiology* 164(11), 1115-1120.https://doi.org/10.1093/aje/kwj275.

[@nz2bizg6ewp] Arora, Ashish, Sharon Belenzon, Larisa C. Cioaca, Lia
Sheer, and Hansen Zhang. *The effect of public science on corporate
R&D*. No. w31899. National Bureau of Economic Research, 2023.

# Evaluator details

1.  How long have you been in this field?

    -   3 years

2.  How many proposals and papers have you evaluated?

    -   8

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

[^5]:

[^6]: Manager: reformated numbered list for clarity.
