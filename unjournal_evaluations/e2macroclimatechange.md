---
article:
  elocation-id: e2macroclimatechange
author:
- Evaluator 2
bibliography: /tmp/tmp-44J9synL57prYg.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 11
  month: 01
  year: 2025
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: "Evaluation 2 of \"The Macroeconomic Impact of Climate Change:
  Global vs. Local Temperature\""
uri: "https://unjournal.pubpub.org/pub/e2macroclimatechange"
---

# Abstract 

The paper's empirical innovation is simple: estimating the impacts of
temperature on GDP using global time-series data, implicitly capturing
the relationship between global temperatures, extreme events, and GDP
without modelling all intermediate pathways. This idea, combined with
their rigorous analytic approach, may have far-reaching implications due
to the huge magnitude of the resulting estimates. \
\
Given the small sample size used to estimate their main results (N\<60),
robustness checks and cautious inference are essential. I recommend
additional checks, which may increase their uncertainty estimates, and
could result in either higher or lower estimated impacts.

# Summary Measures

We asked evaluators to give some overall assessments, in addition to
ratings across a range of criteria. *See the *[*evaluation summary
"metrics"*](https://unjournal.pubpub.org/pub/evalsummacroclimatechange#metrics "null")*
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
| **Overall         | 90/100            | 8 |
| assessment **     |                   | 0 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 1 |
|                   |                   | 0 |
|                   |                   | 0 |
+-------------------+-------------------+---+
| **Journal rank    | 4.7/5             | 4 |
| tier, normative   |                   | . |
| rating**          |                   | 5 |
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

# Written report

## Summary of the paper and its contributions

This paper has two parts. First, it uses reduced form regression
analysis to estimate the causal relationship between global temperature
and GDP. Second, it integrates these estimates into a neoclassical
growth model to calculate the Social Cost of Carbon.

The paper's primary contribution lies in its innovative approach to
estimating climate damages. Whilst a large and influential previous
literature uses country (or subnational) panel data on GDP and
temperature to estimate damages before aggregating to the global level
(Dell, Jones, and Olken, 2012[@n8z5h0cl9pm]; Burke, Hsiang, and Miguel,
2015[@nteqnkf8y6h]; Kalkuhl and Wenz, 2020)[@ncqa2n1qnkb], Bilal and
Kanzig (BK) take a different approach. They use time series regressions
to directly estimate the relationship between *global* temperature
shocks and *global* GDP, resulting in significantly larger damage
estimates[^4] (Berg, Curtis, and Mark, 2024[@nx4lw64plpj]; Nath, Ramey,
and Klenow, 2024)[@n3ueyzbajrg]. BK argue that their larger estimates
arise because global temperature is a stronger predictor of extreme
climate events than local, country level temperature, which is used in
previous studies. To support this claim, they examine how global and
local temperature influence the likelihood of four extreme climatic
events that cause economic damage: extreme heat, droughts, high winds,
and heavy precipitation. They find that global temperature strongly
predicts these extreme events, whilst local temperature does not.
Interestingly they find that ocean temperature, rather than land
temperature, is mostly responsible for the impacts of temperature on
GDP, since ocean temperature is a more direct driver of these extreme
events.

A secondary contribution relates to the method used to translate their
reduced form regression results into structural damage functions and
estimate the Social Cost of Carbon (SCC). While this section introduces
some technical refinements compared to previous studies, these
adjustments seem to have only a modest impact on the results. When BK
input estimates of local temperature impacts into their model, the
results align more closely with those of earlier research. The primary
driver of their larger SCC estimates is the significantly higher
empirical damage estimates derived from their global temperature
approach.

BK's SCC estimate is nearly an order of magnitude larger than those from
previous studies, with profound policy implications. For instance, BK
estimate a domestic SCC of \$273 for the United States, suggesting that
unilateral US decarbonization would be cost-effective (since this is
substantially higher than the costs of emissions abatement in the US).
Thus, if adopted by policymakers, this estimate could fundamentally
reshape our understanding of international climate negotiations. By
reducing the significance of the "free rider" problem---long seen as a
major obstacle to collective action---these findings could catalyse more
ambitious and unilateral climate policies, challenging the traditional
coordination challenges that have hindered global progress.

Overall, I believe this is an important contribution which the climate
impacts community should take seriously. However, in this review[^5] I
also outline some potential concerns (all of which I think the authors
would be likely to be able to address).

BK's main analysis is conducted with a small sample size (roughly 50-60
years) and their model contains many parameters (at least 8), which make
careful inference and extensive robustness checks crucial. I suggest a
variety of additional robustness checks, and that BK conduct a
simulation study to provide verification that their approach to
quantifying statistical uncertainty is likely to produce valid
confidence intervals. I suggest additional caveats that should be
incorporated into the welfare analysis and projections, especially
related to the possibility of non-linear impacts, climate tipping
points, or significant unmodeled adaptation.

Also, when BK compare their results to the previous literature, they
compare their results to those from a model that doesn't allow for
non-linear effects or for permanent growth effects, which contrasts with
the models used in those previous analyses. This may confound their
comparison to previous work.

Further, the approach in this paper assumes that the in-sample
relationships between temperature and extreme events is informative
about that covariance in a changing climate. If climate change alters
the relationship between global average temperature and extreme events,
this assumption is invalid. BK could analyse CMIP projections[^6] to get
a sense of how much of an impact this could have on their results. If
climate change does change the distribution of extreme events, then BK
would need to estimate and project damages from each extreme event type
separately.

In the rest of this review, I first outline some strengths, and then
some limitations and suggestions for BK's analysis.

## Strengths 

-   **Data**

    -   BK assemble a new dataset on climate and the economy.
        Temperature data is taken from BEST, extreme events from ISIMIP,
        and GDP data from the Penn World Tables, Work Bank, and
        Jordà-Schularick-Taylor Macro-history database. These are
        appropriate data sources and allow them to construct a longer
        series of data than most existing climate impact studies.
        Including ISIMIP allows them to test the mechanisms for their
        larger impacts, something that most previous temperature-GDP
        studies don't do.\

-   **Replicability**

    -   BK made the code and data used to estimate the key empirical
        regressions publicly available. This is unusually transparent
        for an economics paper, most of which do not make anything
        public until after publication.

    -   All the data used in this paper is publicly available, so BK
        presumably will publish a full replication package upon
        acceptance at a journal.\

-   **Empirical strategy**

    -   BK use local projections to estimate the impact of annual global
        temperature on GDP. This is likely to be more robust to
        misspecification than a more parametric approach, although BK
        also show they can obtain similar results using a VAR in their
        appendix.\

-   **Robustness Checks**

    -   BK conduct extensive robustness checks, paying particular
        attention to the possibility of omitted variables bias, reverse
        causality, and external validity (which they proxy for using the
        stability of their results across time periods).

    -   The additional appendix robustness checks in Appendix A are very
        impressive! They use multiple datasets, check for influential
        observations, and many other things.

## Limitations/suggestions 

### Comments on empirical analysis

#### 1.** **Inference with a (very) small sample[^7]

-   BK's main results are calculated using a regression of around 50
    observations. The regression appears to have at least 7 parameters.

-   In this setting, with the number of parameters a substantial portion
    of the sample size, it's not clear that the asymptotic
    approximations required to justify their frequentist confidence
    intervals are appropriate.

-   I would suggest providing simulation evidence to illustrate the
    validity of their confidence regions in their setting, with time
    series data, few observations, and lots of parameters.

    -   Corrections to the heteroskedasticity robust standard error
        estimator are available for cases where the number of parameters
        is a non-negligible proportion of the sample size, for example:
        Cattaneo, Jansson, and Newey (2018)[@nkn9muo7jlw]. Simulation
        evidence could help to confirm whether this type of correction
        is likely to lead to valid inference.

#### 2. Comparison to previous 'local' temperature estimates

-   BK's local temperature model (Equation 4a) doesn't allow the impacts
    of country level (local) temperature to be non-linear.

-   Further, BK's model does not allow for a permanent growth effect.

-   BK claim that previous studies (e.g. Dell, Jones, and Olken,
    2012;[@n4okylyfl6c]Burke, Hsiang, and Miguel, 2015[@n4xinpok4a7];
    Nath, Ramey, and Klenow, 2024)[@nq4xg5771du] find impacts of only 1%
    from a 1c shock, but those papers allow for non-linear impacts, or
    for permanent growth effect. Therefore, the comparison to the
    previous literature seems a bit artificial.

-   To make a valid comparison to the previous literature, BK could
    allow the local temperature model to have non-linear effects, and
    permanent growth effects.

    -   They could also check that when they do so, the local
        temperature model that they are comparing to reproduces the
        results (e.g. damage from climate change) in the underlying
        studies. This would likely require a (very short) separate
        analysis for each model they are comparing to.

#### 3. Levels vs growth effects

-   BK assume that the impacts of temperature shocks go to zero after 10
    periods. This is in contrast to some previous influential climate
    impacts studies (Burke, Hsiang, and Miguel 2015)[@ns76kyyduw6],
    which assume a permanent growth effect.

-   Qualitatively, GDP does not seem to have fully reverted to the mean
    after 10 years in BK's main figures. Some mechanisms are still
    persistent after 10 years, e.g. effect of drought, Figure A.13.
    Also, some regions seem to be facing significant impacts; SE Asia
    and Sub-Saharan Africa, Figure 12.

-   It would be good to show the impacts for more than 10 years out, and
    to include a robustness check SCC calculation which allows for
    longer run effects (this will come at a cost of using fewer
    observations).

#### 4. Extreme event thresholds

Extreme weather events are defined relative to thresholds, such that
'the extreme heat, drought, extreme precipitation and extreme wind
indices have a baseline probability of 0.05, 0.25, 0.01 and 0.01'. Where
do these come from? Are the results robust to other thresholds?

#### 5. Asymmetric effect of hot and cold shocks

BK include a robustness check (Figure A.9) which allows the impact of
hot and cold shocks to be different. It appears that hot shocks are more
damaging, which is in line with previous climate impacts literature.
However, this specification is not used apart from in this robustness
check. It would be good to see the country level impacts in this
specification, and the impacts on extreme events, given most empirical
work to date has found non-linear impacts of temperature.\

#### 6. Is the two-step procedure necessary?

-   BK use a two-step procedure to estimate the causal impact of temp on
    GDP. In the first step, they estimate temperature shocks as
    residuals from a 2 step ahead AR(2) forecast. However, this is found
    to be numerically very similar to using the regression residuals
    from a 1 step forecast.

-   This approach is quite confusing for those used to the climate
    impacts literature. As BK note, it is numerically equivalent to
    estimate the model in one step with appropriate controls (not for
    the main model used in the text, but for the robustness check model
    which uses AR(2) residuals as the temperature shocks). It could be
    easier to understand if the main model was swapped to this one, so
    it can be estimated in one step.

## Comments on SCC / welfare effects calculations

#### 7. Validity of using past covariances between temperature and extreme events to project future damages

-   Existing climate impact studies generally control for precipitation
    when estimating and projecting the impacts of temperature. One
    reason for doing this, rather than loading precipitation impacts
    onto the temperature damage estimates implicitly through their
    covariances in historical data, is that climate change may affect
    the covariance between temperature and precipitation and other
    extreme events. If this is the case, then damage projections would
    need to separately project extreme events from temperature, rather
    than assuming the past covariance to temperature is directly
    informative.

-   It would be good to include some citations or analysis of CMIP
    projections to check how / if this could bias projected estimates.
    Or, at a minimum, some sense of how projections of extreme events
    look. How are extreme events trending in sample? How are they
    expected to trend in projections?

-   Kotz, Levermann, and Wenz (2022)[@nx76jfnq1p1] provide projections
    for some extreme event indicators, which could be used in this
    analysis.\
    \

#### 8. Extrapolation

-   BK assume that the in-sample relationship between weather and GDP in
    \[the present in the sample\] are informative about those in the
    future, and can be extrapolated forward.

-   It's certainly possible that this is not the case: e.g. due to
    climate tipping points which could imply a big increase in extreme
    events after a relatively small temperature increase (increased
    impacts), or unexpected technology shocks facilitating cheaper
    adaptation (decreased impacts). Whilst there isn't much BK can do to
    incorporate these into their analysis, I think they are important
    caveats when interpreting the magnitude of their results in a policy
    context, and this isn't discussed much in the paper's current draft.

-   This is especially relevant since the identifying variation in BK's
    temperature shock measure is very small -- they are extrapolating
    the impacts of small deviations in weather to project the effect of
    large changes in climate.\

#### 9. Non-market damages

Other papers (Carleton et al. 2022;[@nhhnl7wmicz] Rennert et al.
2022)[@nlw891tvkci] have found that non-market impacts compose the
largest portion of the SCC. Therefore, using only GDP to estimate the
impacts of climate change may severely undercount total damages needed
for an SCC calculation.

## Clarifying questions

10. BK say that BHM (Burke, Hsiang, and Miguel, 2015[@nkywrrz3to9]) find
    impacts of 1C temp rise as 1-2% at most. But, BHM states that RCP8.5
    implies global damages of around 25% of global GDP (see their Fig.
    5D). It would be good to know how specifically how they calculate
    that BHM only find this smaller value (also for comparison to DJO
    and Nath et al) (Burke, Hsiang, and Miguel, 2015[@nu2o2z66pbd];
    Dell, Jones, and Olken, 2012[@nxhwqec01ke]; Nath, Ramey, and Klenow,
    2024)[@nki8vere2nz].\

11. Does running country level regressions (using panel regression
    models and non-linear effects) with the extra four extreme climate
    variables increase SCC estimates to a similar magnitude as when BK
    use global temperature directly? This would require projecting the
    four extreme climate variables (which is going on implicitly in the
    current approach).

    -   Or is it only when also applying the other machinery in this
        paper that the results get so large? This would help explain
        what exactly the key departure is from the previous literature.

## References

[@n2mmfa4vyrc]Dell, Melissa, Benjamin F Jones, and Benjamin A Olken.
2012. 'Temperature Shocks and Economic Growth: Evidence from the Last
Half Century'. *American Economic Journal: Macroeconomics* 4 (3):
66--95. https://doi.org/10.1257/mac.4.3.66.

[@nya47z8wyj1]Burke, Marshall, Solomon Hsiang, and Edward Miguel. 2015.
'Global Non-Linear Effect of Temperature on Economic Production'.
*Nature* 527 (7577): 235--39. <https://doi.org/10.1038/nature15725.>

[@nrjrf4c1iwj]Kalkuhl, Matthias, and Leonie Wenz. 2020. 'The Impact of
Climate Conditions on Economic Production. Evidence from a Global Panel
of Regions'. *Journal of Environmental Economics and Management* 103
(September):102360. <https://doi.org/10.1016/j.jeem.2020.102360.>

[@nqmvr9evfp3]Berg, Kimberly A., Chadwick C. Curtis, and Nelson C. Mark.
2024. 'GDP and Temperature: Evidence on Cross-Country Response
Heterogeneity'. *European Economic Review* 169 (October):104833.
<https://doi.org/10.1016/j.euroecorev.2024.104833.>

[@ngc8wvrw4bd]Nath, Ishan B, Valerie A Ramey, and Peter J Klenow. 2024.
'How Much Will Global Warming Cool Global Growth?'

[@ns27a048bb6]Cattaneo, Matias D., Michael Jansson, and Whitney K.
Newey. 2018. 'Inference in Linear Regression Models with Many Covariates
and Heteroscedasticity'. *Journal of the American Statistical
Association* 113 (523): 1350--61.
<https://doi.org/10.1080/01621459.2017.1328360.>

[@nvr2cxxptlu]Kotz, Maximilian, Anders Levermann, and Leonie Wenz. 2022.
'The Effect of Rainfall Changes on Economic Production'. *Nature* 601
(7892): 223--27. <https://doi.org/10.1038/s41586-021-04283-8.>

[@nugu91svokq]Carleton, Tamma, Amir Jina, Michael Delgado, Michael
Greenstone, Trevor Houser, Solomon Hsiang, Andrew Hultgren, et al. 2022.
'Valuing the Global Mortality Consequences of Climate Change Accounting
for Adaptation Costs and Benefits'. *The Quarterly Journal of
Economics*, April, qjac020. https://doi.org/10.1093/qje/qjac020.

[@np35dnefhji]Rennert, Kevin, Frank Errickson, Brian C. Prest, Lisa
Rennels, Richard G. Newell, William Pizer, Cora Kingdon, et al. 2022.
'Comprehensive Evidence Implies a Higher Social Cost of CO2'. *Nature*,
September, 1--3. <https://doi.org/10.1038/s41586-022-05224-9.>

# Evaluator details

1.  How long have you been in this field?

    -   7 years

2.  How many proposals and papers have you evaluated?

    -   Around 5

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

[^4]: Two other recent papers employ a similar approach [(Berg, Curtis,
    and Mark 2024; Nath, Ramey, and Klenow 2024)]{.citation
    cites="2873 2847"}. However, neither of these paper\'s estimates the
    effect of global average temperature on global GDP, they instead
    focus on the response of country level GDP to global and local
    temperature shocks.

[^5]: Manager: We refer to these as "evaluations", but they are meant to
    largely resemble a standard peer review referee report for an
    academic journal.

[^6]: Manager: I expect this stands for the Coupled Model
    Intercomparison Project --- see
    https://climateknowledgeportal.worldbank.org/cmip5.

[^7]: Manager: I added the numbering to these comments to help the
    authors respond.
