---
article:
  elocation-id: e1urbanforests
author:
- Evaluator 1
bibliography: /tmp/tmp-59ZWF2b5NkE739.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 08
  month: 04
  year: 2025
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: "Evaluation 1 of \"Urban Forests: Environmental Health Values and
  Risks\""
uri: "https://unjournal.pubpub.org/pub/e1urbanforests"
---

# Abstract 

The paper tackles a very interesting and relevant question about the
environmental and health impact of urban forests i.e how human-led
greening of urban areas affects well-being through its impact on
pollution and pollen. The paper's strength lies in bringing together
several data sources with high spatial resolution and decomposing the
policy impact into vegetation density & greenery, air quality and
finally health. Moreover the discussion on health and environment trade
off is also new and insightful. The main critique is that claims of
causality in the paper are not substantiated within the current
estimation framework. However, I believe with the excellent data sources
available to the authors this can be addressed in the future.

# Summary Measures

We asked evaluators to give some overall assessments, in addition to
ratings across a range of criteria. *See the *[*evaluation summary
"metrics"*](https://unjournal.pubpub.org/pub/evalsumurbanforests#metrics "null")*
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
| **Overall         | 60/100            | 4 |
| assessment **     |                   | 5 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 6 |
|                   |                   | 5 |
+-------------------+-------------------+---+
| **Journal rank    | 2.5/5             | N |
| tier, normative   |                   | / |
| rating**          |                   | A |
+-------------------+-------------------+---+

**Overall assessment **(See footnote[^2])

**Journal rank tier, normative rating (0-5): ** On a 'scale of
journals', what 'quality of journal' should this be published in?[^3]
*Note: 0= lowest/none, 5= highest/best. *

# Claim identification and assessment

## I. Identify the most important and impactful factual claim this research makes[^4] {#i-identify-the-most-important-and-impactful-factual-claim-this-research-makes}

1.  Document a substantial greening up of Beijing by the MMP programme,
    specifically NDVI growth to accelerate after 2012, the year of the
    project implementation .\

2.  Quantify the impact of urban forests on downwind air quality
    improvement using a quasi-experimental research design i.e.
    increased vegetation growth by MMP reduces average PM2.5
    concentration at city population hubs by 4.2 percent and led to a
    7.4 percent increase in pollen exposure.

## II. To what extent do you \*believe\* the claim you stated above? {#ii-to-what-extent-do-you-believe-the-claim-you-stated-above}

I don't believe these claims are causal as stated by the authors. The
estimation framework is not rigorous enough to identify these impacts.
Currently, they are correlational evidence.

# Written report

I believe the paper addresses some very interesting questions. I
particularly like the idea of studying a relevant policy instrument like
'Urban Forests' which are feasible to implement on a large scale and
something that several Asian countries are increasingly considering.
Moreover, I like the structure of decomposing the policy impact into
vegetation density & greenery, air quality and finally health. The
primary claims of the paper are:

1.  We document a substantial greening up of a mega city and examine the
    contribution by a government-led mass afforestation.\

2.  We quantify the impact of urban forests on downwind air quality
    improvement using a quasi-experimental research design.\

3.  We investigate a commonly wondered negative externality -- pollen
    emissions resulting from urban afforestation -- and use medical
    claims data to provide some of the first direct estimates of the
    health burdens associated with these aeroallergens.

The paper does tackle each of these, but I am not convinced that these
results can be interpreted within a causal inference framework.
Additionally, the paper is doing too much and seems very busy,
especially the introduction which needs to be trimmed down and more to
the point. I'll tackle each empirical section below and end with some
miscellaneous comments.

## Sections 4.2: documenting the greening of the city[^5]  {#sections-42-documenting-the-greening-of-the-city}

1.  Why not utilize the temporal dimension of their data and policy and
    show a straightforward event study of the grids that were treated
    and non-treated between 2001-2020 using 2012 as intervention. Also
    do you have information on when the MMP areas were planted? Was it
    staggered manner across each area or all together? Considering that
    NDVI data is high frequency this can be utilized for a staggered
    Differences \[in\] Differences.\

2.  Second, it seems that what the authors are trying to achieve via \
    specification (3) is somewhat similar to spatial regression
    discontinuity design but without exactly implementing that -- I
    suggest the authors use spatial RDD as it will allow to establish a
    counterfactual based on distance measure complimenting the DiD above
    which creates a counterfactual based on treatment status. I believe
    the high spatial resolution of their data would make spatial RDD a
    good choice. Of course, for this identification the MMP planting
    areas must be exogenous to the outcome -- I believe the authors need
    to provide more information on how exactly was MMP implemented, how
    were these areas chosen?\

3.  As it currently stands, the estimation is not rigorous enough for
    the authors to make the claim of causality as seen on page 18.\

4.  Why no fixed effects? At the very least doesn't Beijing have 16
    districts which itself may be an important factor in how the MMP
    have an impact? Why the lack of any controls? I think even if causal
    inference is not the aim in this section, the specification would
    benefit from having fe and controls.\

5.  In this framework simply not addressing spatial autocorrelation
    because Conley is too computationally intensive can not be justified
    here -- I would like the authors to talk a bit more about this.\

6.  I'd like a little more discussion on how NDVI is the best for your
    purpose - why not use another index like leaf area index?

## Section 5: environmental and health effects 

1.  I enjoyed this section and I like the idea of using NDVI grids in
    the upwind cone -But my question is again why no controls? Wind
    direction can be a result of weather events which in turn also
    directly impact pollution and pollen.\

2.  Interesting that pollen and pollution monitoring sites don't overlap
    -- also what determines the location of these monitors? The location
    choice itself can be impacting your outcomes, for example if the
    monitors are placed in densely/sparsely populated areas. Basically,
    the equation still suffers from omitted variable bias. For an area
    the size of Beijing I expect there to be decent variation in climate
    exposure and population which can in fact be seen in Figure 4 Panel
    (a).\

3.  Figure 5 Plot (a) is not very convincing because even though there
    is a drop its not significant and same with a few of the figures in
    the appendix -- the pollen figure looks encouraging - I am not sure
    what is the need of event study here? Is there some literature
    stating 20 days prior and after there is an effect? What I would
    like to see is the baseline results of the equation (7) which don't
    seem to be presented.\

4.  Does the MMP patch size in the upwind cone matter? A heterogeneity
    analysis here would be interesting,

## Miscellaneous comments:

-   Equations 1 and 2 are unnecessary and are not really explained well
    enough at that point in the paper and simply confuse the readers. We
    understand that the marginal impact is being estimated but I
    wouldn't call that section as "Why marginalize?" But rather "threats
    to identification".\

-   I don't see the need for section 4.3 when you tackle it better in
    section 5.\

-   Many times, the time unit of analysis is not clear unless the reader
    takes a look at the figures or tables -- please state this clearly
    when describing the specification.\

-   Mu (unit of area) -- the authors should not use this measurement in
    the abstract as it is not universally understood. And in the main
    body should provide context on how this translates to
    hectares/square miles/square kms etc.\

-   Section 6.3 and 7.1 can be combined and discussed especially in
    terms of future policy relevance.

# Evaluator details

1.  How long have you been in this field?

    -   5 years

2.  How many proposals and papers have you evaluated?

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

[^4]: The evaluator was given the following instructions: Identify the
    most important and impactful factual claim this research makes --
    e.g., a binary claim or a point estimate or prediction.

    Please state the authors' claim precisely and quantitatively.
    Identify the source of the claim (i.e., cite the paper), and briefly
    mention the evidence underlying this. We encourage you to explain
    why you believe this claim is important, either here, or in the text
    of your report.

[^5]: Editor: we replaced bullet points with numbering here
