---
article:
  elocation-id: eval3effectivenudge
author:
- Evaluator 3
bibliography: /tmp/tmp-60piMlZW2GIRjs.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 10
  month: 08
  year: 2024
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: "Evaluation 3 of \"Selecting the Most Effective Nudge: Evidence
  from a Large-Scale Experiment on Immunization\""
uri: "https://unjournal.pubpub.org/pub/eval3effectivenudge"
---

# Abstract 

The method is mostly a clever combination of existing methods; the main
contribution is showing \[the\] consistency and normality of their
estimator. These results need not always hold, as they depend on
assumptions, and so applicability is not universal. The authors provide
guidance by presenting simulations showing that for n \> 3000, normality
seems to hold. The field data reveal no surprise\[s\], and all the
interventions have been tested before. Yet, the paper is strong, and the
method will possibly remain relevant despite the recent advances in
adaptive experimental design, if the authors provide additional guidance
or software.

# Summary Measures

We asked evaluators to give some overall assessments, in addition to
ratings across a range of criteria. *See the *[*evaluation summary
"metrics"*](https://unjournal.pubpub.org/pub/evalsumeffectivenudge#metrics "null")*
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
| **Overall         | 85/100            | 7 |
| assessment **     |                   | 5 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 9 |
|                   |                   | 0 |
+-------------------+-------------------+---+
| **Journal rank    | 4.5/5             | 4 |
| tier, normative   |                   | . |
| rating**          |                   | 0 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 5 |
|                   |                   | . |
|                   |                   | 0 |
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

## Overall Summary

The paper presents a technique to select a (best) policy from a large
factorial design, including, for example, various dosages of a treatment
that can be ordered with respect to their intensity. Essentially, the
technique aims to aggregate variants of a treatment that yield
(effectively) the same effect, thereby reducing the dimensionality of
possible options, and consequently increasing \[the\] power and
precision of estimates for the effect sizes of truly effective
treatments. The technique is applied to a large-scale experiment, where
75 policies are tested that involve combinations of reminders,
incentives, and local ambassadors, with the aim of increasing the number
of child immunizations in the state of Haryana (India). A combination of
ambassadors and reminders \[leads to\] to the largest impact when paired
with incentives; without incentives, a very similar combination is
identified as the most cost-effective one (any form of ambassador paired
with reminders).

## The method

The method is mostly a clever combination of already existing --
sometimes more, sometimes less -- established methods. The true merit of
the paper with respect to the method lies in identifying those, putting
them together, and finally showing that under \"strong assumptions\" (p.
34), the method \"rules out some of the cases where model-selection
leads to invalid inferences\" (p. 34), and produces estimates that are
consistent and asymptotically normal. Specifically, in a first step, all
treatments and their interactions are included in a regression via
marginal effects (known from a staggered design, for example). Then, a
LASSO is performed. This, however, cannot be performed directly on the
marginal effects due to the high correlations. The authors identify a
\"Puffer transformation\" due to Jia and Rohe (2015)[@nlhhepn7q93] as a
suitable solution. The LASSO then identifies marginal effects that are
effective, and others that are not (essentially based on their
p-values). Only then the variant aggregation starts, such that dosages
that do not lead to different effects (according to the LASSO) are
grouped. Treatments that have no effect whatsoever are either \"pooled
or pruned (pooled with control)\". Scientifically, I am a bit unsure
whether this should be allowed; a discussion seems warranted. It is
obviously principled and data-driven, but conceptually, it seems wrong
to me.

Regarding the asymptotic results, I cannot fully assess them, as going
through all the proofs seems to be out of scope considered that this is
not the core of my work. Yet, it is clear that asymptotic arguments and
asymptotic results imply that they need not always hold (as they depend
on N). Hence, a limitation of the \"existence\" result (the correct
support of effective marginal effects is indeed selected by the LASSO),
as well as consistency and normality results is that applicability is
not universal. The authors provide guidance by presenting simulations
showing that normality is approximately fulfilled in the given setting.
Whether or not the strong assumptions are likely to be fulfilled in
different settings will remain a judgment call; in particular, finding a
penalty sequence for the LASSO that fulfills Assumption 5 seems
non-trivial. Unless I\'ve missed it, there seems no guidance in that
respect (even though there are robustness checks).

A suggestion would thus be to provide some more intuition about the
settings in which the assumptions can be expected to hold; after all,
the present paper may use thousands of data points, which is not
necessarily representative. Unless there will be no software
implementation, I am unsure how much practitioners will \[adopt\] the
technique; the Jia and Rohe (2015)[@nm62qlr2e3x] correction for
correlated regressors seems technical, too, and so does the Andrews et
al. (2021)[@n0jniv62kmz]-correction for the winner\'s curse. As a final
comment, it is to be seen whether adaptive designs or the current design
approach will become more prevalent in the future.

## The field intervention

The field data result from a collaboration with the government of the
state of Haryana in India, with the objective \[of\] improv\[ing\]
immunization rates. The data consists of about 300,000 children, and
about 60,000 households satisfied the eligibility criterion of having
children between the ages of 12 to 18 months. While this allows for an
impressive study, by now, the innovation of the tested tools is somewhat
limited. That is: all tested interventions have been studied before,
including by the authors, and including in this very same dataset
(Banerjee et al., 2019, \"Using Gossips to Spread Information: Theory
and Evidence from Two Randomized Controlled Trials\")[@nion1s2jjnj].
This fact is communicated only on page 28, which is a bit late for my
taste.

\[However\], previous research has ignored interactions between the
treatments (at least of the full set considered here), which is to be
seen as the main contribution of the field data. The tested
interventions are: i) incentives (in the combinations low/high and
flat/increasing with every immunization shot, where low corresponded to
about 500 minutes of mobile phone talk time for all five immunization
shots), ii) SMS reminders (no reminder, reminders to 33% of parents,
reminders to 66% of parents), and iii) ambassadors (randomly selected,
information hubs identified by fellow villagers, trusted advisors
regarding agriculture and health identified by fellow villagers, trusted
advisors who were identified as information hubs). In addition to
informing about possible interaction effects, and despite not being
particularly innovative with respect to the tested interventions from
today\'s perspective (\[the\] baseline data was collected mid-2016), the
study can contribute to our understanding of the relative merit of the
interventions, which is also extremely valuable, even today (see Figure
4 for the results; only high incentives (increasing with every vaccine)
are effective, and this to a similar degree \[as\] relying on
ambassadors - even more than on trusted ambassadors).

### **Comments on the field intervention:** [^3]

1.  On page 27, the authors refer to an online appendix, in which they
    report about their data quality checks. In the main text, they
    describe the data quality as \"excellent\". In the appendix (p. 92),
    we learn that children's names and date of birth were accurate in
    80% of the checks, and that there were \"almost no\" fake child
    records, which is, however, not quantified. Finally, for 71% of the
    children, the vaccines overlapped completely. I work with field data
    myself, and I know that these number\[s\] are realistic, but
    objectively, this cannot be described as excellent. Administrative
    data from Denmark or Norway is excellent, but 71% overlapping
    vaccines certainly are not. As the errors are not different across
    treatment groups, results should be unaffected, though.

2.  Substitution effects are analyzed in an online appendix, but the
    tables are in landscape format, but the relevant pages are not, and
    hence about half of the tables/pages seem to be cut. As a result,
    \[the\] notes are not informative, as half of the information is
    missing; several columns seem to be missing, too. The content of the
    table remains cryptic, making it difficult to assess whether the
    incentive-effects are actually substitution effects, or are indeed
    new immunization shots. It remains unclear how the dependent
    variable and the regressors are coded (i.e., whether the regressions
    predict showing up for an immunization under a given incentive
    scheme and having been immunized somewhere else before (as the main
    text would suggest), or whether the regressions predict showing up
    for immunization despite not being in the register (as the Table
    headings suggest)). Yet, what can be seen looks innocent, in the
    sense that the share is not different across treatments, and hence
    there is hope that this is also true for the missing columns.
    However, the control means look incredibly high (up to .69) should
    the dependent variable really equal 1 if a child is not in the
    register. If this were the case, this issue should deserve more
    discussion.

3.  Section 4 could benefit from proofreading and streamlining. At the
    end, as a reader one is confused which sub-set of the data is
    finally analyzed.

4.  According to the pre-registration/pre-analysis plan (first mentioned
    on page 29, footnote 27 \-- also a bit late), the authors were
    interested in (some) previously not analyzed interaction effects
    between incentives, reminders and ambassadors (called \"gossip\" in
    Banerjee et al., 2019)[@n7qn52kr17q]. A systematic approach like the
    current one did not seem to be the plan, however, not even in the
    updated pre-registration from 2018. The authors could comment on
    this change (which is completely legitimate, in my view).

## References

[@nig9qw4nakq]Jia, J., & Rohe, K. (2015). Preconditioning the Lasso for
sign consistency. *Electronic Journal of Statistics*, *9*(1).
<https://doi.org/10.1214/15-ejs1029>

[@nlve66j1eww]Andrews, I., Kitagawa, T., & McCloskey, A. (2019).
*Inference on Winners*. National Bureau of Economic Research.
<https://doi.org/10.3386/w25456>

[@n7zzi6p4slj]Banerjee, A., Chandrasekhar, A. G., Duflo, E., & Jackson,
M. O. (2019). Using Gossips to Spread Information: Theory and Evidence
from Two Randomized Controlled Trials. *The Review of Economic Studies*,
*86*(6), 2453--2490. <https://doi.org/10.1093/restud/rdz008>

# Evaluator details

1.  How long have you been in this field?

    -   10+ years

2.  How many proposals and papers have you evaluated?

    -   20+

[^1]: Note: if you are reading this before, or soon after this has been
    publicly released, the ratings from this paper may not yet have been
    incorporated into that data presentation.

[^2]: Manager's note: We made some very small grammatical corrections
    and added some further paragraph spacing.

[^3]: Manager: Numbering added (originally listed as bullet points)
