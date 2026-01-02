---
article:
  doi: 10.21428/d28e8e57.ef6f66cd/3c5e0495
  elocation-id: e2demandfordemocracy
author:
- Evaluator 2
bibliography: /tmp/tmp-60oi6RtmXPZTzg.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 07
  month: 08
  year: 2025
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 2 of "Misperceptions and Demand for Democracy under
  Authoritarianism"
uri: "https://unjournal.pubpub.org/pub/e2demandfordemocracy"
---

# Abstract 

This paper makes a valuable contribution to research on authoritarianism
and democratic resilience by combining an online survey and a
large-scale field experiment in Turkey to test whether correcting
factual misperceptions about institutional decline can shift political
attitudes and electoral behavior. \
\
The study is theoretically ambitious, well-powered, and methodologically
transparent, with the field experiment demonstrating real-world
behavioral effects on opposition vote share. The paper could be improved
by addressing the mismatch between the authors' normative framing of
democracy and media freedom and the more instrumental, performance-based
content of their treatments. The authors could also do more to address
concerns about treatment spillover and compliance heterogeneity in the
field experiment. \
\
Overall, the study is rigorous and policy-relevant, and it offers a
strong foundation for future work on information-based interventions in
hybrid regimes.

# Summary Measures

We asked evaluators to give some overall assessments, in addition to
ratings across a range of criteria. *See the *[*evaluation summary
"metrics"*](https://unjournal.pubpub.org/pub/evalsumdemandfordemocracy#metrics "null")*
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
| **Overall         | 88/100            | 8 |
| assessment **     |                   | 0 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 9 |
|                   |                   | 5 |
+-------------------+-------------------+---+
| **Journal rank    | 4.5/5             | 3 |
| tier, normative   |                   | . |
| rating**          |                   | 5 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 5 |
+-------------------+-------------------+---+

**Overall assessment **(See footnote[^2])

**Journal rank tier, normative rating (0-5): ** On a 'scale of
journals', what 'quality of journal' should this be published in?[^3]
*Note: 0= lowest/none, 5= highest/best. *

# Claim identification and assessment 

## I. Identify the most important and impactful factual claim this research makes[^4] {#i-identify-the-most-important-and-impactful-factual-claim-this-research-makes}

The most important and impactful factual claim made in this paper is
that exposure to nonpartisan, factual messages about institutional
decline led to a measurable increase in opposition vote share in the
2023 Turkish presidential election. Specifically, the authors report
that treated neighborhoods experienced a 0.8 percentage point increase
in opposition vote share, which represents a 1.5% increase relative to
baseline support levels. This estimate is based on administrative data
from 1,887 ballot boxes across 554 neighborhoods in Izmir, comparing
treatment and control areas using a 2SLS design that instruments actual
treatment exposure (measured by completed household visits) with
randomized treatment assignment.

This claim is impactful because it provides novel real-world evidence
that factual, nonpartisan informational interventions can meaningfully
influence electoral behavior in a hybrid regime. It moves beyond
attitudinal outcomes, demonstrating that even modest corrections of
misperceptions can scale to population-level political effects. This is
an important finding for policymakers and scholars concerned with
democratic backsliding and information resilience under authoritarian
conditions.

## II. To what extent do you \*believe\* the claim you stated above?[^5] {#ii-to-what-extent-do-you-believe-the-claim-you-stated-above}

I am inclined to believe this claim as the field experiment is
well-powered, pre-registered, and analyzed using appropriate
instrumental variable (2SLS) methods, which lends credibility to the
causal inference. The use of administrative ballot-box data reduces
concerns about self-report bias, and the authors show that the result is
robust across multiple specifications. I am somewhat cautious due to 1)
potential spillover across adjacent neighborhoods; 2) variation in
treatment compliance and delivery success; 3) uncertainty about the
underlying mechanism as messages focused on performance outcomes rather
than normative democratic appeals.

## III. Suggested robustness checks[^6] {#iii-suggested-robustness-checks}

**Spillover Analysis:** Given the risk of treatment, conducting spatial
spillover checks would help validate the localized nature of the
treatment effect. For instance, the authors could re-estimate treatment
effects excluding neighborhoods adjacent to treated areas or include
spatial lags of treatment assignment as covariates. Tools such as
spatial autoregressive models or geographically weighted regressions
(e.g., using R packages like spdep [@10.32614/CRAN.package.spdep
] or spatialreg [@10.32614/CRAN.package.spatialreg
]) could help model and quantify potential diffusion effects.

**CACE Estimation: **The 2SLS approach accounts for partial compliance,
but presenting CACE estimates would clarify treatment effects among
those who received the intervention. This would be especially helpful
given variation in completion rates by canvasser affiliation. CACE can
be estimated using the same instrumental variable approach already
implemented, but with a focus on interpreting the LATE for compliers.
Reporting these estimates alongside covariate profiles of compliers
(households that opened doors or received pamphlets) would improve
transparency.

## IV. Important 'implication', policy, credibility[^7] {#iv-important-implication-policy-credibility}

The central implication of the paper's main claim is that nonpartisan,
factual messaging about institutional decline can meaningfully shift
electoral outcomes even under authoritarian or hybrid regimes,
suggesting that targeted information campaigns may be a cost-effective
strategy for bolstering democratic opposition and civic engagement. If
this effect generalizes beyond Turkey, it implies that donors,
prodemocracy NGOs, and election-monitoring organizations should invest
in informational interventions that highlight the performance
consequences of democratic erosion, especially in settings where direct
normative appeals to democracy may be less persuasive or politically
risky.

I believe this implication, especially in contexts where political
competition still exists and where the ruling regime has made clear
governance failures. However, generalizability may be limited. The
effect likely depends on contextual factors such as, salience of recent
scandals or disasters, and audience receptivity to nonpartisan
messengers.

# Written report

This paper examines whether correcting citizens' misperceptions about
democratic decline and the erosion of media freedom can shift political
attitudes and electoral behavior. The ambitious study focuses on Turkey
in the lead-up to the 2023 presidential election. It combines evidence
from an online survey experiment, which tests the effects of brief
informational messages on belief updating and self-reported intended
vote choice, with a large-scale field experiment in Izmir, where
canvassers initiated conversations and delivered pamphlets to over
400,000 registered voters across 554 neighborhoods. The treatments in
both experiments emphasized either the negative consequences of
authoritarian control over the media (enabling corruption) or democratic
backsliding (weakening disaster preparedness). In the online experiment,
both treatments increased agreement with statements linking
institutional quality to performance outcomes and produced statistically
significant increases in opposition vote intention. In the field
experiment, treated neighborhoods saw a 0.8 percentage point increase in
opposition vote share, measured using administrative ballot-box results.

The authors argue that citizens living under authoritarian or hybrid
regimes may support such systems in part due to correctable
misperceptions. They show that high-quality, factual, non-partisan
information can increase public demand for democracy. The combination of
theory-driven hypotheses, a well-powered online experiment capturing
belief updating and vote intentions, and a large-scale field experiment
measuring real-world behavioral outcomes makes this paper a valuable and
timely contribution to the literature on authoritarianism, information
effects, and democratic resilience. The online experiment allows for
fine-grained measurement of attitudinal change, while the field
experiment demonstrates that informational interventions can translate
into actual electoral shifts at scale.

Below I offer several suggestions for improving the manuscript. I would
particularly encourage the authors to be more explicit about conceptual,
measurement, and inference-related limitations, and to work toward
better aligning the theoretical framing with the empirical design.
Clarifying issues related to construct validity and generalizability
would also help strengthen the contribution and situate the findings
more precisely within broader debates about support for democracy under
hybrid and authoritarian regimes.

## Conceptual Framing and Construct Validity[^8] 

As currently written, there is a bit of a mismatch between the paper's
conceptual scope and the content of the experimental interventions and
outcomes. While the paper is framed as an investigation into how
correcting misperceptions about democratic backsliding and media freedom
shapes support for opposition, the actual treatments focus on
instrumental, performance-based framings of institutional decline.
Specifically, the democracy treatment highlights how democratic erosion
contributed to mismanagement of natural disasters, while the media
treatment frames state control of the press as a driver of corruption
(Sections 3.1 and 3.2). These framings are substantively compelling and
contextually salient in Turkey, but they do not isolate support for
democracy or media freedom as normative commitments.

The online experiment measures outcomes using an index of two agreement
statements: that "strengthening democracy will reduce the number of
people affected by natural disasters" and that "increasing media
independence will reduce corruption." These are beliefs about
performance consequences, rather than measures of democratic values or
support for media freedom. Moreover, Figure A8 shows that the democracy
treatment affects beliefs about media, suggesting that participants may
have interpreted the treatments as general signals about regime failure
rather than cleanly differentiated messages.

Similarly, the informational treatments in the field experiment also
emphasize performance-based themes. The authors argue that the observed
vote shift reflects a correction of authoritarian-era misperceptions,
but the underlying mechanisms (whether belief updating, emotional
reactions to disasters and corruption, or general anti-incumbent
sentiment) are difficult to disentangle. Without more direct evidence
linking treatment exposure to changes in institutional beliefs or
values, the conclusion that voters "demand democracy" is not clearly
supported.

Along these lines, the authors should discuss more explicitly how the
external validity of their findings may be limited by the highly
contextualized nature of the intervention. The treatments leveraged
timely, salient examples of corruption and disaster mismanagement. While
this likely improved effectiveness of the treatments in the Turkish
context, it limits generalizability to other regimes without similar
scandals or recent crises. Additionally, if public responsiveness is
driven more by outrage at regime incompetence than by principled
democratic beliefs, the broader claim about correcting misperceptions to
build democratic support should be caveated.

## Methodological Limitations

The field experiment is impressive as it is well-powered,
pre-registered, and uses behavioral outcome data from official election
returns. However, it would be useful to provide more detail on some
potential limitations. The authors should address potential spillover
across neighborhoods. Given Izmir's dense urban environment, adjacent
untreated neighborhoods may have been indirectly exposed to treatment
messages via word-of-mouth or sharing of pamphlets. If spillovers
occurred, the estimated treatment effects could be attenuated or biased.

While the authors acknowledge variation in completion rates in the field
experiment (only 35% of visits resulted in successful delivery of the
message) they argue this does not bias results, showing that completion
rates do not differ significantly across treatment arms and that their
2SLS design accounts for differences in treatment uptake. However, this
does not fully address concerns about heterogeneity in compliance.
Completion rates varied substantially by canvasser affiliation, with
non-affiliated canvassers achieving higher success rates. The authors
might consider reporting complier average causal effect (CACE) estimates
or further exploring how compliance heterogeneity may interact with
treatment responsiveness. Greater transparency about who complied, how
first-stage variation maps onto outcomes, and whether effects are driven
by specific subgroups (e.g., more persuadable households or more
credible messengers) would help clarify the mechanisms and improve
interpretability of the results.

## Reproducibility and Research Transparency:

The paper generally follows best practices for open science. The
experiments are pre-registered, and the main estimations are
pre-specified and clearly documented. The outcomes are based on
administrative data, and the authors provide thorough appendices
detailing treatment materials, implementation protocols, and robustness
checks. Ultimately, the authors should make their code and de-identified
administrative data processing scripts publicly available. This would be
especially helpful given the complexity of matching field implementation
logs to ballot-box election returns. Future research would also benefit
from more precise documentation of unit-level assignment, treatment
delivery, and any deviations from protocol (such as canvasser
substitutions, missing neighborhoods etc.).

## V-Dem data

While the authors use V-Dem indices to benchmark Turkey's institutional
decline, these expert-coded indicators have known limitations, including
issues of inter-coder reliability, conceptual overlap, and potential
bias in aggregation procedures. Recent work has raised concerns about
the replicability and independence of V-Dem\'s low-level indicators,
particularly in contexts of contested democratic status (Little and Meng
2024)[@n93sw9zlxno]. While this doesn't invalidate the use of V-Dem for
descriptive context or longitudinal comparisons, it is important not to
treat these measures as direct evidence of citizen misperceptions or
democratic backsliding without additional validation.

## References

[@ngbvqiy3nwp] Little, Andrew T., and Anne Meng. 2024. 'Measuring
Democratic Backsliding'. *PS: Political Science & Politics* 57 (2):
149--61. <https://doi.org/10.1017/S104909652300063X>.

[@n9ef7ca14wo] Acemoglu, Daron, Cevat Giray Aksoy, Ceren Baysan, Carlos
Molina, and Gamze Zeki. *Misperceptions and demand for democracy under
authoritarianism*. No. w33018. National Bureau of Economic Research,
2024.

# Evaluator details

1.   What is your research field or area of expertise, as relevant to
    this research?

    -   Political Science; Authoritarian Politics; MENA Politics;
        Experimental Methods

2.  How long have you been in your field of expertise?

    -   10 years

3.  How many proposals, papers, and projects have you evaluated/reviewed
    (for journals, grants, or other peer-review)?

    -   \~200

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

[^6]: *We asked:*

    \[Optional\] What additional information, evidence, replication, or
    robustness check would make you substantially more (or less)
    confident in this claim?

    Feel free to refer to the main body of your evaluation here; you
    don\'t need to repeat yourself. Please specify how you would perform
    this robustness check (etc.) as precisely as you are willing. E.g.,
    if you suggest a particular estimation command in a statistical
    package, this could be very helpful for future robustness
    replication work.

[^7]: *We asked:* \[Optional\] Identify the important \*implication\* of
    the above claim for funding and policy choices? To what extent do
    you \*believe\* this implication? How should it inform policy
    choices? Note: this 'implication' could be suggested by the
    evaluation manager in some cases. As an example of an
    \'implication\' \... in a global health context, the \'main claim\'
    might suggest that a vitamin supplement intervention, if scaled up,
    would save lives at a \$XXXX per life saved.

[^8]: Manager: We changed the inline bolded text into headers to aid
    readability and navigability
