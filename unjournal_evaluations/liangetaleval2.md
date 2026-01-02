---
article:
  doi: 10.21428/d28e8e57.97377fc8
  elocation-id: liangetaleval2
author:
- Anonymous
bibliography: /tmp/tmp-60wjbRejw6XWtF.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 17
  month: 07
  year: 2023
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: "Evaluation 2 (anon.) of \"The Environmental Effects of Economic
  Production: Evidence from Ecological Observations\" for The Unjournal"
uri: "https://unjournal.pubpub.org/pub/liangetaleval2"
---

This is an evaluation of Liang et al ([@temp_id_5500720427351802]).

# Summary measures

**Overall assessment**

Answer: 70

Confidence (from 0 - 5): 3

**Quality scale rating**

"On a 'scale of journals', what 'quality of journal' should this be
published in?: Note: 0= lowest/none, 5= highest/best"

Answer: 4

Confidence (from 0 - 5): 5

# Written report

*\[Evaluation manager/editor's note: I made some very copy-editing
corrections below.\]*

This paper makes an important step forward in our understanding of the
relationship between biodiversity and economic activity. The first key
contribution of this paper stems from the use of a novel dataset to
provide a broader picture compared to previous literature of the impact
of economic activity on biodiversity. The combined spatial, temporal,
geographic, and taxonomic scope of the dataset allows for a more macro
perspective on the GDP-biodiversity relationship compared to previous
papers, and enables the authors to study the degree to which this
relationship holds across a variety of contexts.

The paper's central result that increases in GDP are associated with
decreases in biodiversity is supported by a thorough exploration of the
nature of this relationship in terms of heterogeneity by taxa and
economic sector, distributional analysis, and dynamic effects. Moreover,
the authors demonstrate that this association is plausibly causal; using
state-level sensitivity to shocks in aggregate military spending as an
instrument for state GDP, they present a convincing case for the
argument that increases in economic activity cause a decline in
biodiversity. Overall, the robustness and thoroughness of the analysis
of the GDP-biodiversity relationship is good. The finding that economic
activity negatively affects biodiversity is not particularly surprising
on its own, but estimating the magnitude of this effect alongside
extensive robustness checks as well as an IV approach for causal
inference is an important contribution.

Like all studies that use biodiversity surveys, this paper faces the
unavoidable drawback that the external validity of its findings is
unclear, because surveys are not randomly assigned to locations and
species. However, the authors provide an extensive discussion of the
data and its potential weaknesses. As well as quantitative checks for
any red flags that might suggest issues with the data, they also make
the important point that at the very least their results are internally
valid (with respect to the biodiversity surveys included in the
dataset). Overall I think their discussion of the data and its inherent
limitations is thorough and well-communicated, and the potentially
limited external validity of the results does not undermine the
importance of the contribution in terms of global priorities.

The authors build on an already important contribution by estimating the
role of pollution in the GDP-biodiversity relationship as well as the
mitigation of this relationship by environmental regulation. These
analyses improve the overall impactfulness of the paper by providing
practical insights into how to mitigate the impact of economic activity
on GDP. Using a well-established IV strategy from the pollution
literature, they estimate the role that pollution plays in the
GDP-biodiversity relationship. Their findings shed light on the
potentially important role that pollution plays in the impact of human
activity on ecosystems. Finally, the authors offer an assessment of the
role of environmental regulation in reducing the impact of GDP on
biodiversity. Their findings suggest that the Clean Air Act may have
helped to reduce the impact of economic activity on biodiversity.

As it is, I think this paper is already publishable in a good field
journal, and so I do not have any comments that are necessary to address
to ensure publication. However, I provide some comments and suggestions
below which the authors may find helpful for further improvements to the
paper. The main area of focus of these comments relates to the section
on environmental regulation, which I think is the least robust section
of the paper. Given the applicability of this section to real-world
practice, improving its robustness would contribute to the overall
impactfulness of the paper.

## Specific comments and suggestions:

*\[Evaluation manager/editor note: I replaced the bullet points with an
enumerated list.\]*

1.  A suggestion to improve the abstract: The headline finding that
    economic activity decreases biodiversity is an important
    contribution but not particularly surprising or impactful on its
    own. Meanwhile, as illustrated by Figure 3, the paper provides some
    interesting insights into the nature of the GDP-biodiversity
    relationship, in particular that non-bird and especially mammal
    species are relatively more vulnerable, as are locations where
    biodiversity is already particularly low. Given that these insights
    are underpinned by the breadth of the novel data used and are
    therefore an important element of the paper's novel contribution, I
    would suggest mentioning them in the abstract.

2.  GDP is likely non-stationary; however, if the biodiversity outcome
    variables are stationary, then using a non-stationary variable (GDP)
    to explain these outcome variables may introduce a lot of noise into
    the specification. In so far as state-level GDP follows a similar
    trend as the national average trend in GDP, the year-fixed effects
    mitigate this issue. Nevertheless, state-level GDP trends are likely
    heterogeneous. The authors cannot include state-by-year fixed
    effects because these will absorb the effect of GDP, but perhaps
    they could reduce noise in the estimation by de-meaning the GDP
    variable relative to the state-specific long-term average.

3.  I appreciate that comparing and interpreting the magnitude of the
    estimates in this paper is difficult, but nevertheless, some further
    discussion could help guide the reader to understand how large these
    estimated impacts are and improve the real-world applicability of
    the paper. For example, what do we know from ecology about the
    magnitude of natural year-to-year variation in population and
    abundance? How does the population decline associated with a 1%
    increase in GDP compare to population declines that followed a
    specific natural disaster or other extreme event (for example)?

4.  Regarding the evaluation of the effect of the Clean Air Act on the
    GDP-biodiversity relationship, I would suggest providing some more
    detail to justify the empirical strategy and/or testing some
    alternative strategies as a robustness check. For example, why use
    the count of NA designations rather than a binary variable to
    indicate any positive number of NA designations? Also, why use an IV
    strategy rather than an alternative approach such as
    difference-in-differences? It looks like you could have sufficient
    data for a DiD-type design around 2005, when the NAAQS for PM2.5
    came into effect. [Sager and
    Singer](https://eprints.lse.ac.uk/115528/1/GRI_clean_identification_paper_376.pdf)
    ([@RePEc:ehl:lserod:115528]) might be helpful here - they provide an
    interesting discussion of the potential limitations of a simple DiD
    framework in the context of the Clean Air Act. Finally, it would be
    beneficial to have a more extensive discussion of the extent to
    which we can interpret these estimates as causal; how confident can
    we be that attainment only affects biodiversity through its effect
    on GDP?

5.  It may be helpful to readers to see the equation for section 5.1
    written out explicitly, rather than referring the reader to the
    previous section, to help make clear the empirical strategy and for
    ease of comparison with previous literature on the Clean Air Act.

6.  Similar to the approach illustrated in Figure 3, which explores the
    heterogeneity in the GDP-biodiversity association, it would be
    interesting to explore the heterogeneity in the pollution
    regulation-biodiversity association. Particularly given that the
    availability of public funds to improve biodiversity are limited,
    this analysis could yield important practical insights into how to
    most effectively target these funds. For example, are some taxa more
    protected by regulation than others? Are the taxa that are most
    protected by regulation also those that are most vulnerable to
    economic activity? Does the impact of regulation on the
    GDP-biodiversity relationship vary over the distribution of
    biodiversity?

## Evaluator details {#survey-questions}

1.  How long have you been in this field? \[*blurred for anonymity:
    *5-10 years\]

2.  How many proposals, papers, and projects have you evaluated/reviewed
    (for journals, grants, or other peer-review)? None.
