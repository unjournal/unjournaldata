---
affiliation:
- id: 0
  organization: Goethe University Frankfurt
article:
  doi: 10.21428/d28e8e57.5411b150/640bb340
  elocation-id: e2naturalregeneration
author:
- Cannon Cloud
bibliography: /tmp/tmp-43a9GdBv07r3ZP.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 03
  month: 06
  year: 2025
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 2 of "Global potential for natural regeneration in
  deforested tropical regions"
uri: "https://unjournal.pubpub.org/pub/e2naturalregeneration"
---

# Abstract 

This paper aims to model and predict the global potential for natural
regeneration in deforested tropical regions for 2016 and 2030,
respectively, using a machine learning random forest (RF) approach. The
study's aim and methods are novel and important, given the potential
benefits of natural regeneration on carbon sequestration (amongst many
other ecological and environmental outcomes) and the lack of
pan-tropical analysis. The paper\'s current estimates are the first we
have for understanding the scope of natural regeneration as an effective
climate change mitigation measure.\
\
However, my review identifies several significant conceptual and
methodological concerns that fundamentally affect the validity and
interpretability of the results and predictions, particularly concerning
the paper\'s goal of informing restoration prioritization.

# Summary Measures

We asked evaluators to give some overall assessments, in addition to
ratings across a range of criteria. *See the *[*evaluation summary
"metrics"*](https://unjournal.pubpub.org/pub/evalsumnaturalregeneration#metrics "null")*
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
| **Overall         | 50/100            | 3 |
| assessment **     |                   | 0 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 8 |
|                   |                   | 0 |
+-------------------+-------------------+---+
| **Journal rank    | 4.5/5             | 3 |
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

# Claim identification and assessment 

## I. Identify the most important and impactful factual claim this research makes[^4] {#i-identify-the-most-important-and-impactful-factual-claim-this-research-makes}

\"We estimate that an area of 215 million hectares\... has potential for
natural forest regeneration\...\" (Williams et al. 2024, Abstract &
Results section)[@ne037gn4p3k]. They further estimate this area holds an
\"above-ground carbon sequestration potential of 23.4 Gt C (range,
21.1--25.7 Gt) over 30 years.\"

This claim is highly important because it provides the first spatially
explicit, high-resolution estimate of the *global biophysical potential*
for natural regeneration across the tropics. It quantifies a major,
often overlooked, cost-effective pathway for achieving large-scale
forest restoration, which is critical for meeting international climate
change mitigation and biodiversity conservation targets (like the Bonn
Challenge and the Global Biodiversity Framework). By mapping this
potential, the research aims to guide policy, investment, and planning
towards leveraging natural processes for restoration, complementing or
potentially replacing more expensive active tree-planting efforts in
suitable areas. It provides a crucial (though, as discussed in the
review, potentially overestimated and uncertain) baseline figure for
understanding the scale of this opportunity.

## II. To what extent do you \*believe\* the claim you stated above?[^5] {#ii-to-what-extent-do-you-believe-the-claim-you-stated-above}

Based on the significant methodological concerns outlined in the referee
report, particularly the unaddressed omission error in the input data
and the potential conflation of regrowth types, my belief in the
accuracy of the headline claim -- 215 Mha of potential natural
regeneration -- is low. A very rough back-of-the-envelope calculation
attempting to correct for these factors (detailed in the report)
suggests a more plausible credible interval for the *purely natural*
regeneration potential might be substantially lower, perhaps in the
range of **\~80 Mha to \~180 Mha, **and carry more uncertainty. This
reduced range reflects the expectation that correction for input data
errors and appropriate uncertainty propagation would revise the
authors\' point estimate downwards.

## III. Suggested robustness checks[^6] {#iii-suggested-robustness-checks}

The first minor point in the referee reports suggests using multiple
kinds of machine learning algorithms, such as Gradient Boosting Machines
or Neural Networks, for at least some regions, to compare sensitivity.

## IV. Important 'implication', policy, credibility[^7] {#iv-important-implication-policy-credibility}

The most important implication of the claim, as presented, is that there
exists a vast, globally significant area where cost-effective natural
regeneration could be prioritized to meet climate and biodiversity
goals, potentially redirecting substantial funding and policy focus
towards facilitating this process over more expensive active planting in
these regions. While the general principle that natural regeneration is
a crucial and cost-effective tool is undoubtedly true and highly
relevant for policy, my belief in the specific implication *derived from
the 215 Mha figure and the associated map* is medium (i.e., ballpark
correct but likely somewhat lower), due to the methodological concerns
outlined previously (especially the likely overestimation from
uncorrected omission errors and potential conflation). Therefore, while
policy *should* absolutely recognize and create mechanisms to support
natural regeneration, it should view the current 215 Mha estimate or the
specific map with a bit of skepticism for any large-scale funding
allocation or target setting.

# Written report

This paper aims to model and predict the global potential for natural
regeneration in deforested tropical regions for 2016 and 2030,
respectively, using a machine learning random forest (RF) approach. The
study's aim and methods are novel and important, given the potential
benefits of natural regeneration on carbon sequestration (amongst many
other ecological and environmental outcomes) and the lack of
pan-tropical analysis. The paper\'s current estimates are the first we
have for understanding the scope of natural regeneration as an effective
climate change mitigation measure.

However, my review identifies several significant conceptual and
methodological concerns that fundamentally affect the validity and
interpretability of the results and predictions, particularly concerning
the paper\'s goal of informing restoration prioritization. These major
concerns center on:

1.  The selection and use of predictor variables, including issues of
    **data leakage** and circularity, resulting in limitations in the
    model validation approach and its ability to assess predictive power
    for prioritizing future actions.

2.  Issues related to the **input data derived from Fagan et al.
    (2022)**[@nx4n4kw7305], including reliance on older source data,
    conflation of regrowth types, and high omission errors, which means
    prioritizing based on this map risks targeting areas already
    restored.

3.  The approach to **estimating uncertainty**, which overlooks key
    sources of error and potentially uses suboptimal methods for
    addressing known sources of error and uncertainty.

4.  The focus on **extensive tree growth** (i.e., gains in forest area)
    while neglecting **intensive regrowth** (i.e., canopy regeneration
    within existing forest pixels), meaning prioritization based solely
    on extensive gain ignores significant potential within existing
    forest areas.

While the overall approach has merit, offering a novel, global, and
scalable methodology for estimating natural regeneration potential, it
is currently under-developed but can be strengthened. Readily available
data and techniques exist to address these issues and help create better
estimates.

## Major Concerns:

**1. Data Leakage Concerns:**

-   **Definition:** Data leakage, also known as data contamination, is a
    critical issue in machine learning that can lead to overly
    optimistic estimates of model performance and poor generalization to
    new data. It occurs when information from outside the training
    dataset (e.g., from the validation or test set) is inadvertently
    used during the training process. This can take many forms, such as
    including predictor variables that are derived from the outcome
    variable itself, using future information to predict past events, or
    accidentally including validation data in the training data. Leakage
    leads to a model that appears to perform well during training and
    validation but fails to generalize to unseen data, as it has
    essentially \"memorized\" patterns that won\'t exist in a real-world
    predictive setting (see, e.g., Kuhn & Johnson, 2019, *Feature
    Engineering and Selection*; Kaggle Wiki on Leakage)[@n0wapq2ymwx].
    The implications of data leakage are particularly severe when the
    goal is prediction, as is the case in this study. In-sample
    performance metrics, such as those derived from cross-validation,
    will be unreliable indicators of how well the model will perform on
    truly independent out-of-sample data or in a future predictive
    scenario. Therefore, identifying and addressing potential sources of
    leakage is essential for ensuring the validity of any predictive
    model.\

-   **Specific Concerns with Predictor Variables:** I have some concerns
    about the predictor variables that fall into three categories:\

    -   **Variables potentially derived using outcome data:** The
        SoilGrids predictor variable appears to be from 2014 or 2016,
        potentially created using land cover classification data from
        2010 that includes forest classifications (related to the
        outcome variable, albeit from a different source than the
        primary Hansen GFC data). Extended Fig 3 shows this is the third
        most important variable.\

    -   **Variables potentially incorporating post-2000 outcome data:**
        Predictor variables averaged or derived from periods overlapping
        or extending beyond the 2000 start date of the regeneration
        outcome (e.g., NPP 2000-2015, burned area 2001--2017) may
        incorporate information influenced by the regeneration itself,
        creating temporal leakage. It is not explicitly stated they
        include data from recent years, but given they only update 3
        covariates (forest density, distance, and land cover) for
        prediction, it seems like not.\

    -   **Variables potentially limiting future prediction:** Predictors
        like human settlement and roads from post-2000 (arguably have
        less reverse causality though probably not none), would still
        threaten future prediction with the model, as they reflect
        conditions *during* the observed regeneration period. Using
        these to predict future (e.g., 2030) potential assumes these
        socioeconomic patterns remain stable or change predictably,
        which might not hold.\

-   **Implication:** Given the above issues with leakage, the reported
    model accuracy derived from validation likely does not reflect true
    predictive performance. Specifically:\

    -   Using predictors potentially derived from the outcome
        (Category 1) creates circularity, artificially inflating model
        performance metrics and compromising the model\'s ability to
        explain even the retrospective (2000-2016) regeneration
        patterns, as it may simply be learning the correlation rather
        than underlying drivers.\

    -   Using predictors whose values during the outcome period are
        influenced by the outcome itself (Category 2, e.g., NPP affected
        by regrowth) introduces temporal leakage and potential reverse
        causality within the model training. This inflates the apparent
        retrospective accuracy but obscures the true drivers of
        regeneration initiation and limits the model\'s explanatory
        power for the 2000-2016 period.\

    -   Using predictors reflecting conditions only during the outcome
        period (Category 3, e.g., post-2000 roads) fundamentally limits
        the reliability of the model for predicting future (2030)
        scenarios, as these conditions are likely to change.\

    -   Collectively, these issues mean that any references to accuracy
        derived from the current validation should not be extrapolated
        to future predictions (e.g., 2030) or necessarily be interpreted
        as reflecting true explanatory power even for the past (e.g.
        2016), requiring these concerns to be addressed. While the
        mechanisms differ (circularity vs. temporal feedback), both
        Category 1 and Category 2 leakage significantly compromise the
        model\'s explanatory power and predictive reliability.

**2. Input Data Concerns (GFC Gain & Fagan et al. Application):**

-   **(a) Reliance on Older GFC Gain Data:** The study relies on an
    older version of the Global Forest Change (GFC) gain data (v1.5,
    covering 2000-2012/2016). Since the initial analysis for Fagan et
    al. (2022), improved GFC datasets have been released (e.g., GMD 2022
    update using GEDI lidar, offering better canopy prediction;
    subsequent versions with multiple gain epochs). Link: [Global Forest
    Watch,
    2024](https://www.globalforestwatch.org/blog/data-and-tools/new-gfw-tree-cover-gain-net-change-data/ "null")
    [@nikk4s32isu]. There is even a newer version showing gains for
    2005, 2010, 2015, and 2020.\

    -   **Recommendation:** Re-running the analysis using the most
        current and improved GFC gain data (potentially over multiple
        distinct time periods like 2000-2005, 2005-2010, 2010-2015,
        2000-2010, etc.) is recommended. This would provide more
        accurate input data and allow for testing model sensitivity to
        predictor variables potentially causing leakage (e.g., excluding
        soil data for earlier periods where contemporaneous versions
        aren\'t available).\

-   **(b) Definition of Natural Regrowth (Inherited from Fagan et
    al.):** The model relies on Fagan et al.\'s definition, which treats
    all non-plantation gain as \"natural regrowth,\" which appears to
    conflate truly natural processes with human-assisted regeneration or
    diverse tree plantings not classified as monoculture plantations.
    Fagan et al. acknowledged this limitation: "Our product was also not
    designed to distinguish rarer land uses intermediate between tree
    plantations and natural regrowth, such as assisted natural
    regeneration." Given the scale of restoration commitments involving
    active planting (e.g., Initiative 20x20 claims 53 Mha planted in
    Latin America Link: [Initiative 20x20,
    2021](https://initiative20x20.org/publications/initiative-20x20-infographic "null"))
    [@nh9kqlgcj8a], this conflation significantly affects the
    interpretation. The authors must either attempt to disaggregate
    these categories or significantly temper their interpretation and
    claims regarding purely *natural* regrowth potential.\

-   **(c) Overestimation due to Omission Error (Inherited from Fagan et
    al.):** The analysis excludes areas *mapped* as regrowth by Fagan et
    al. to define the domain for potential regeneration. However, Fagan
    et al. [@npve34fucp9]\
    reported very high *omission* errors for regrowth (low area-based
    Producer\'s Accuracy of \~18.7%). This means the Fagan map used for
    exclusion missed a large area (\~26 Mha) of *actual* regrowth
    (estimated at 31.6 Mha). Consequently, the Williams et al.
    [@nsrh1gedpyb] potential area (215 Mha) includes these
    already-regrown areas, substantially overestimating the area truly
    available for *future* regeneration. This requires correction. While
    a precise spatial correction is challenging, this numerical
    adjustment highlights the scale of the overestimation, and the
    uncertainty associated with this correction must be addressed (see
    Point 3a). Prioritizing based on this map risks targeting areas
    already restored.

**3. Estimating Uncertainty:**

-   **(a) Underestimation of Uncertainty:** The necessary correction for
    the omission error (subtracting the \~26 Mha of omitted-but-actual
    regrowth, see Point 2c) carries significant uncertainty derived from
    the Fagan et al. [@nrijfuoil4p] accuracy assessment (31.6 ± 11.9 Mha
    for total regrowth). Propagating this uncertainty would result in a
    much wider confidence interval for the corrected potential
    regeneration estimate (\~189 Mha) than implied by the analysis of
    the 215 Mha figure. The current approach (reporting just minimal
    uncertainty from the RF model)  ignores this driving source of
    uncertainty.\

-   **(b) Stratification for Uncertainty Reduction:** The paper does not
    appear to leverage stratification techniques known to mitigate the
    impact of omission errors on area estimates, particularly for rare
    classes like forest gain (as demonstrated in Olofsson et al. 2020
    [@nroo6rq9lg2] for mitigating omission error impacts). While Fagan
    et al. [@nt2ox5ntm9b] suggested this is impossible for regrowth,
    Olofsson (2020)[@nap8pg7k68l] does not support that conclusion (from
    my reading). Williams et al.\'s [@n11x2lgdztf] own finding that most
    potential regrowth occurs near forest edges (within 300m: "For
    example, out of a random sample of 62,493 grid cells (of all 30 × 30
    m grid cells) across the study region, 98.1% of cells with a
    potential of \>0.5 (for illustrative purposes) occur within 300 m of
    a forest edge.") suggests a buffer-based stratification strategy
    could be feasible and potentially significantly reduce the
    uncertainty associated with omission errors by isolating them within
    smaller-area strata. Implementing such a stratification is
    recommended to improve the reliability of the underlying area
    estimates which compromise the bulk of the uncertainty (as compared
    to the minimal uncertainty from the RF model).\

-   **(c) Confidence Interval Construction for Rare Classes:**
    Additionally, while perhaps a secondary concern compared to the
    points above, the standard practice of constructing confidence
    intervals using the design-based SE and the Wald method (assuming
    normality) may be unreliable for rare land-use classes or metrics
    with low accuracy (like the Producer\'s Accuracy for regrowth). The
    underlying sampling distributions for these estimates are often
    skewed. Using bootstrap percentile confidence intervals, which
    empirically derive the interval from the data\'s distribution
    without assuming normality, can provide more realistic uncertainty
    bounds and likely achieve better coverage probability (i.e., capture
    the true value closer to the nominal 95% level). This is
    particularly important when estimates serve as baselines for
    monitoring, where reliable CIs are needed to detect future changes
    (example code demonstrating this comparison is provided).

\[*Note from manager:* *The evaluator provided an R script to compute
this, which we include in a \~code block below; we have checked that
this runs. We also host this on Google collab for those without R
installed --- *[*see
here.*](https://colab.research.google.com/drive/1-bFRNTgaHvNVAT3V7RlWSZO7u7g3quIm?usp=sharing "null")*\]*

* *

**4. Neglect of Intensive Margin Regrowth:**

-   The study focuses exclusively on the extensive margin (new forest
    area gain). It completely overlooks the intensive margin -- canopy
    regeneration and forest recovery *within* existing, potentially
    degraded, forest pixels (e.g., areas increasing from \<30% to \>60%
    canopy cover as an arbitrary threshold). Data exists to analyze this
    (e.g., Hansen GFC tree cover percentage layers for 2000/2010 Link:
    [Global Land Analysis & Discovery,
    2013](https://glad.umd.edu/dataset/global-2010-tree-cover-30-m "null")
    [@nnsu9v0yq2m]Sexton et al. [@nt80imzeb65] canopy data for multiple
    epochs [Link:
    https://e4ftl01.cr.usgs.gov/MEASURES/GFCC30TC.003/](https://e4ftl01.cr.usgs.gov/MEASURES/GFCC30TC.003/)).
    Looking at extensive gains alone does not allow for a complete
    estimate of natural regrowth potential. Perhaps this is outside the
    scope of this paper, but at a minimum the paper needs to reframe the
    results with this extensive-intensive caveat. For example, the
    abstract statement "We estimate that an area of 215 million
    hectares---an area greater than the entire country of Mexico---has
    potential for natural forest regeneration, representing an
    above-ground carbon sequestration potential of 23.4 Gt C (range,
    21.1--25.7 Gt) over 30 years..." makes it sound like this is all
    potential regrowth, not just extensive gain potential, and
    prioritization based solely on extensive gain ignores significant
    potential within existing forest areas.

## Minor Points:

-   **Sensitivity Analysis:** To assess the robustness of the potential
    regeneration predictions, it would be valuable to conduct a
    sensitivity analysis by comparing the results obtained from the
    Random Forest model with those from alternative high-performing
    algorithms. Could the authors provide a brief comparison of
    predictions using either Gradient Boosting Machines or Neural
    Networks for subsets of the study area? This comparison would help
    evaluate the stability of the predictions and the extent to which
    they are dependent on the specific modelling approach employed.\

-   **Socioeconomic Context:** The authors provide a clear rationale for
    basing their final spatial predictions of natural regeneration
    potential solely on biophysical variables, citing similar predictive
    accuracy compared to models including socioeconomic factors,
    alongside the greater temporal stability and spatial resolution of
    the biophysical data. This approach is understandable for mapping
    the *biophysical potential* for regeneration. However, translating
    this potential map directly into prioritization for restoration
    interventions requires careful consideration of socioeconomic
    context, including opportunity costs and factors influencing the
    persistence of regenerated areas, which the authors acknowledge in
    the discussion. For future refinements or applications aiming more
    directly at prioritization, it could be valuable to explore the
    integration of higher-resolution, spatially explicit socioeconomic
    proxy data that might overcome the limitations of the coarser
    datasets initially considered. For example, datasets such as
    nighttime lights, or potentially gridded indicators of relative
    wealth or sub-regional economic activity (where available at
    relatively fine scales, e.g. 375-750m), could offer additional
    spatial nuance regarding land-use pressure and the feasibility of
    regeneration persistence, complementing the biophysical potential
    mapped here.\

-   **Figure Reference:** The text references Extended Data Fig. 1 for
    Producer\'s Accuracy values (\"\...dropped to 18.7 (±5.4) when based
    on estimated area (Extended Data Fig. 1).\"). However, Extended Data
    Fig. 1 appears to show model accuracy versus the number of
    variables. Please verify the correct figure reference or provide the
    relevant accuracy data elsewhere.

## References

[@n7qa7h1sxrr] Williams, Brooke A, Hawthorne L Beyer, Matthew E Fagan,
Robin L Chazdon, Marina Schmoeller, Starry Sprenkle-Hyppolite, Bronson W
Griscom, et al. 2024. 'Global Potential for Natural Regeneration in
Deforested Tropical Regions'. *Nature*, 1--7.

[@nt81llwjf7s] Fagan, Matthew E, Do-Hyung Kim, Wesley Settle, Lexie
Ferry, Justin Drew, Haven Carlson, Joshua Slaughter, et al. 2022. 'The
Expansion of Tree Plantations across Tropical Biomes'. *Nature
Sustainability* 5 (8): 681--88.

[@nrfj1sro0ra] Johnson, Max Kuhn and Kjell. 2019. *Feature Engineering
and Selection: A Practical Approach for Predictive Models*. Data Science
Series. Taylor & Francis Group. <http://www.feat.engineering/>.

[@nijopdbs705] Weisse, Mikaela, Katie Reytar, Peter Potapov, Sarah
Carter, and Liz Goldman. 2024. 'Exploring New Tree Cover Gain and Net
Change Data \| GFW'. Global Forest Watch. 2024.
<https://www.globalforestwatch.org/blog/data-and-tools/new-gfw-tree-cover-gain-net-change-data/>.

[@n28r9st94ya] Olofsson, Pontus, Paulo Arévalo, Andres B. Espejo, Carly
Green, Erik Lindquist, Ronald E. McRoberts, and María J. Sanz. 2020.
'Mitigating the Effects of Omission Errors on Area and Area Change
Estimates'. *Remote Sensing of Environment* 236 (January):111492.
<https://doi.org/10.1016/j.rse.2019.111492>.

[@nxpelvaqa3a] Hansen, M.C., Potapov, P.V., Moore, R., Hancher, M.,
Turubanova, S.A., Tyukavina, A., Thau, D., Stehman, S.V., Goetz, S.J.,
Loveland, T.R., Kommareddy, A., Egorov, A., Chini, L., Justice, C.O.,
and Townshend, J.R.G., 2013, High-Resolution Global Maps of 21st-Century
Forest Cover Change: Science, v. 342, no. 6160, p. 850-853, at\
<http://www.sciencemag.org/content/342/6160/850.abstract>.

[@npsz5uyzo8b] Sexton, Joseph O., Min Feng, Chengquan Huang, Anupam
Anand, Saurabh Channan, Xiao-Peng Song, Dan-Xia Song, Do-Hyung Kim,
Praveen Noojipady, and John R. Townshend. 2016. 'Earth Science Data
Records of Global Forest Cover and Change: Assessment of Accuracy in
1990, 2000, and 2005 Epochs'. *Remote Sensing of Environment* 184
(October):73--85. <https://doi.org/10.1016/j.rse.2016.06.012>.

# Evaluator details

1.  How long have you been in this field?

    -   \[4-8\] years in a PhD program

2.  How many proposals and papers have you evaluated?

    -   0

# Accompanying R script, stratified bootstrap confusion matrix

    # Stratified Bootstrap for Accuracy Assessment Metrics
    # Based on Olofsson et al. (2014) methodology and user-provided data.
    # Uses Base R functions for data preparation.
    # v9: Added check before printing UA for 4th map class.

    # MANAGER NOTE: We also host this on Google collab for those without R installed — see https://colab.research.google.com/drive/1-bFRNTgaHvNVAT3V7RlWSZO7u7g3quIm?usp=sharing

    # --- 0. Required Packages ---
    # No external packages required for this version.

    # --- 1. Define Initial Data ---
    # Choose ONE dataset block below (uncomment the one you want to use)
    # IMPORTANT: Define the 'sample_counts' matrix and the NAMED 'stratum_weights' vector.
    #            Define 'ref_base_names' matching the columns of 'sample_counts'.
    #            Dimension names will be set automatically based on these in section 1E.

    # --- 1A: Dataset 1 (from image_ef6d5c.png) ---
    # Uncomment this block to use Dataset 1
    sample_counts <- matrix(c(
      43, 2, 5,   # Map_Deforestation (Stratum 1)
      0, 81, 9,   # Map_NonForest (Stratum 2)
      2, 10, 348  # Map_Forest (Stratum 3)
    ), nrow = 3, byrow = TRUE)
    # Define weights WITH names matching the intended Map Classes/Strata
    stratum_weights <- c(
      Map_Deforestation = 0.005,
      Map_NonForest = 0.195,
      Map_Forest = 0.800
    )
    # Define corresponding Reference Class base names (order must match columns)
    ref_base_names <- c("Deforestation", "NonForest", "Forest")
    # --- End Dataset 1 ---

    # --- 1B: Dataset 2 (from image_309bf7.png) ---
    # Comment this block out to use other datasets
    # sample_counts <- matrix(c(
    #   145, 7, 47,   # Map_Forest_c_loss (Stratum 1)
    #   0, 182, 29,   # Map_NonForest (Stratum 2)
    #   1, 40, 419  # Map_Forest (Stratum 3)
    # ), nrow = 3, byrow = TRUE)
    # # Define weights WITH names matching the intended Map Classes/Strata
    # stratum_weights <- c(
    #   Map_Forest_c_loss = 0.0037,
    #   Map_NonForest = 0.2835,
    #   Map_Forest = 0.7128
    # )
    # # Define corresponding Reference Class base names (order must match columns)
    # ref_base_names <- c("Forest_c_loss", "NonForest", "Forest")
    # --- End Dataset 2 ---

    # --- 1C: Dataset 3 - Fagan et al. (2022) - 3x3 simplified ---
    # Comment this block out to use other datasets
    # sample_counts <- matrix(c(
    #   160, 12,   1,  # Map_TP (Stratum 1)
    #    18, 150,  6,  # Map_REG (Stratum 2)
    #    25,  28, 1432 # Map_NG (Stratum 3)
    # ), nrow = 3, byrow = TRUE)
    # # Define weights WITH names matching the intended Map Classes/Strata
    # # Map Areas (Mha) from table for calculating weights: TP=9.9, REG=4.7, NG=875.4
    # total_map_area_3strata <- 9.9 + 4.7 + 875.4
    # stratum_weights <- c(
    #   Map_TP = 9.9 / total_map_area_3strata,
    #   Map_REG = 4.7 / total_map_area_3strata,
    #   Map_NG = 875.4 / total_map_area_3strata
    # )
    # # Define corresponding Reference Class base names (order must match columns)
    # ref_base_names <- c("TP", "REG", "NG")
    # --- End Dataset 3 ---

    # --- 1D: Dataset 4 - Fagan et al. (2022) - 4x3 FULL ---
    # Comment this block out to use other datasets
    # sample_counts <- matrix(c(
    #   # Ref: TP, REG, NG
    #   160, 12,   1,  # Map_TP (Stratum 1)
    #    18, 150,  6,  # Map_REG (Stratum 2)
    #    25,  28, 1432, # Map_NG (Stratum 3)
    #     0,   0, 1149  # Map_NGP (Stratum 4)
    # ), nrow = 4, byrow = TRUE)
    # # Define weights WITH names matching the intended Map Classes/Strata
    # # Map Areas (Mha) from table: TP=9.9, REG=4.7, NG=875.4, NGP=867.5
    # total_map_area_4strata <- 9.9 + 4.7 + 875.4 + 867.5
    # stratum_weights <- c(
    #   Map_TP = 9.9 / total_map_area_4strata,
    #   Map_REG = 4.7 / total_map_area_4strata,
    #   Map_NG = 875.4 / total_map_area_4strata,
    #   Map_NGP = 867.5 / total_map_area_4strata
    # )
    # # Define corresponding Reference Class base names (order must match columns)
    # ref_base_names <- c("TP", "REG", "NG")
    # --- End Dataset 4 ---


    # --- 1E: Calculate derived variables & SET NAMES AUTOMATICALLY ---

    # Check if sample_counts and stratum_weights are defined
    if (!exists("sample_counts") || !exists("stratum_weights")) {
      stop("ERROR: No active dataset found. Please uncomment one dataset block (1A, 1B, 1C, or 1D).")
    }
    # Check if ref_base_names is defined for the active dataset
    if (!exists("ref_base_names")) {
      stop("ERROR: 'ref_base_names' not defined for the active dataset block.")
    }

    # Get map class names directly from the *names* of the weights vector
    map_classes <- names(stratum_weights)
    if (is.null(map_classes)) {
      stop("ERROR: stratum_weights vector must have names corresponding to Map Classes / Strata.")
    }

    # Create reference class names by adding "Ref_" prefix to base names
    ref_classes <- paste0("Ref_", ref_base_names)

    # --- Assign dimension names to sample_counts matrix ---
    # Check dimensions match expectations
    if (nrow(sample_counts) != length(map_classes)) {
      stop(paste("ERROR: Number of rows in sample_counts (", nrow(sample_counts),
                 ") does not match number of strata defined by stratum_weights names (",
                 length(map_classes), ")."))
    }
    if (ncol(sample_counts) != length(ref_classes)) {
      stop(paste("ERROR: Number of columns in sample_counts (", ncol(sample_counts),
                 ") does not match number of reference classes defined by ref_base_names (",
                 length(ref_classes), ")."))
    }
    dimnames(sample_counts) <- list(
      MapClass_Stratum = map_classes,
      ReferenceClass = ref_classes
    )
    # --- End Automatic Naming ---


    # Calculate samples per stratum (ni)
    stratum_n <- rowSums(sample_counts)
    # Reorder weights to match current sample_counts rows just in case
    stratum_weights <- stratum_weights[map_classes]


    # Verify data setup
    print("--- Active Initial Data (Names Assigned) ---")
    print("Sample Counts (nij):")
    print(sample_counts)
    print("Stratum Weights (Wi):")
    print(round(stratum_weights, 4)) # Round for display
    print("Samples per Stratum (ni):")
    print(stratum_n)
    print(paste("Total Samples:", sum(stratum_n)))
    print(paste("Sum of Weights:", sum(stratum_weights))) # Should be close to 1
    print("------------------------------------------")


    # --- 2. Reconstruct Long Format Data using Base R ---

    # 1. Convert matrix to a frequency data frame using as.table() first
    counts_df <- as.data.frame(as.table(sample_counts))
    colnames(counts_df) <- c("map_class", "ref_class", "Freq") # Rename columns

    # 2. Expand rows based on frequency using rep()
    # Filter out zero freq rows first to avoid issues with seq_len
    counts_df_filtered <- counts_df[counts_df$Freq > 0, ]
    if(nrow(counts_df_filtered) > 0) {
      idx <- rep(seq_len(nrow(counts_df_filtered)), counts_df_filtered$Freq)
      # Select rows using the indices
      sample_data_long <- counts_df_filtered[idx, c("map_class", "ref_class")]
    } else {
      # Handle case where matrix is all zeros (e.g., in a bootstrap sample)
      sample_data_long <- data.frame(map_class=character(), ref_class=character())
    }


    # 3. Add stratum_id (same as map class in this design) and point_id
    sample_data_long$stratum_id <- sample_data_long$map_class
    sample_data_long$point_id <- 1:nrow(sample_data_long)

    # Reorder columns for better readability
    sample_data_long <- sample_data_long[, c("point_id", "stratum_id", "map_class", "ref_class")]

    # Verify the long format data
    print("--- Long Format Data Sample (Base R) ---")
    head(sample_data_long)
    print(paste("Total points in long format:", nrow(sample_data_long)))
    print("--------------------------------------")


    # --- 3. Function to Calculate Statistics (MODIFIED for Non-Square) ---
    # Takes a confusion matrix (like sample_counts) and weights (Wi)
    # Returns area proportions (p_dot_k), UA (Uk), PA (Pk) for relevant classes

    calculate_metrics <- function(conf_matrix, weights) {
      # Ensure input matrix has names for reliable indexing
      if (is.null(rownames(conf_matrix)) || is.null(colnames(conf_matrix))) {
        stop("Input confusion matrix must have row and column names.")
      }
      map_classes_func <- rownames(conf_matrix)
      ref_classes_func <- colnames(conf_matrix)
      n_strata_func <- nrow(conf_matrix)
      n_ref_classes_func <- ncol(conf_matrix)
      
      # Ensure weights have names matching matrix rows
      if (!identical(sort(names(weights)), sort(map_classes_func))) {
        stop("Names of weights must match row names of confusion matrix.")
      }
      # Reorder weights to match matrix rows if necessary
      weights_ordered <- weights[map_classes_func]
      
      stratum_n_func <- rowSums(conf_matrix) # ni for this sample
      
      # Calculate estimated area proportion matrix (p_ij_hat)
      p_ij_hat <- matrix(0, nrow = n_strata_func, ncol = n_ref_classes_func,
                         dimnames = list(map_classes_func, ref_classes_func))
      for (i in 1:n_strata_func) {
        stratum_name <- map_classes_func[i]
        # Check if stratum exists in the current bootstrap sample counts and has samples
        if (stratum_name %in% names(stratum_n_func) && stratum_n_func[stratum_name] > 0) {
          p_ij_hat[stratum_name, ] <- weights_ordered[stratum_name] * (conf_matrix[stratum_name, ] / stratum_n_func[stratum_name])
        } else {
          p_ij_hat[stratum_name, ] <- 0 # Assign 0 if stratum is empty or has 0 samples
        }
      }
      
      # Calculate Area Proportions (p_dot_k = column sums of p_ij_hat)
      p_dot_k <- colSums(p_ij_hat)
      names(p_dot_k) <- ref_classes_func # Assign names explicitly
      
      # Calculate Row Sums (p_k_dot)
      p_k_dot <- rowSums(p_ij_hat)
      names(p_k_dot) <- map_classes_func # Assign names explicitly
      
      # --- Calculate UA and PA ---
      # Identify base class names (e.g., TP, REG, NG) by removing prefixes
      base_class_names_map <- sub("^(Map_|Ref_)", "", map_classes_func)
      base_class_names_ref <- sub("^(Map_|Ref_)", "", ref_classes_func)
      # Common classes are those conceptually present in both map and reference
      common_base_classes <- intersect(base_class_names_map, base_class_names_ref)
      
      # Initialize results with NA
      UA_k <- setNames(rep(NA, length(map_classes_func)), map_classes_func)
      PA_k <- setNames(rep(NA, length(ref_classes_func)), ref_classes_func)
      
      # Extract "diagonal" elements where map/ref concepts match
      diag_elements <- setNames(rep(NA, length(common_base_classes)), common_base_classes)
      for (base_name in common_base_classes) {
        map_name <- map_classes_func[base_class_names_map == base_name]
        ref_name <- ref_classes_func[base_class_names_ref == base_name]
        # Check if unique map and ref classes exist for this base name
        if(length(map_name)==1 && length(ref_name)==1) {
          diag_elements[base_name] <- p_ij_hat[map_name, ref_name]
        }
      }
      
      # Calculate UA for ALL map classes
      for (map_name in map_classes_func) {
        base_name <- sub("^(Map_|Ref_)", "", map_name)
        # Check if this map class has a corresponding diagonal element (is a common class)
        # and if its row sum is > 0
        if ((base_name %in% common_base_classes) && (map_name %in% names(p_k_dot)) && !is.na(p_k_dot[map_name]) && p_k_dot[map_name] > 0 && !is.na(diag_elements[base_name])) {
          UA_k[map_name] <- diag_elements[base_name] / p_k_dot[map_name]
        } else if ((map_name %in% names(p_k_dot)) && !is.na(p_k_dot[map_name]) && p_k_dot[map_name] > 0) {
          # If row sum > 0 but no diagonal element, UA is 0
          UA_k[map_name] <- 0
        } # Else remains NA (e.g., if row sum is 0)
      }
      
      
      # Calculate PA for existing reference classes
      for (ref_name in ref_classes_func) {
        base_name <- sub("^(Map_|Ref_)", "", ref_name)
        # Check if this ref class has a corresponding diagonal element (is a common class)
        # and if its col sum is > 0
        if ((base_name %in% common_base_classes) && (ref_name %in% names(p_dot_k)) && !is.na(p_dot_k[ref_name]) && p_dot_k[ref_name] > 0 && !is.na(diag_elements[base_name])) {
          PA_k[ref_name] <- diag_elements[base_name] / p_dot_k[ref_name]
        } # Else remains NA
      }
      
      
      # Return all results
      return(list(
        p_dot_k = p_dot_k, # Area proportions (for Ref classes)
        UA_k = UA_k,     # User's Accuracies (for Map classes)
        PA_k = PA_k      # Producer's Accuracies (for Ref classes)
      ))
    }

    # Test the function on the original data (whichever is active)
    original_metrics <- calculate_metrics(sample_counts, stratum_weights)
    print("--- Original Estimated Metrics (Corrected Function) ---")
    print(original_metrics)
    print("-------------------------------------------------------")

    # --- 4. Stratified Bootstrap Loop ---
    set.seed(123) # for reproducibility
    # Set n_bootstrap: Use a low number for testing, higher (e.g., 5000+) for final results
    n_bootstrap <- 5000 # << SET NUMBER OF ITERATIONS HERE

    # Get strata names and reference class names from the active dataset
    strata_names <- rownames(sample_counts)
    ref_classes_names <- colnames(sample_counts)
    n_strata <- length(strata_names)
    n_ref_classes <- length(ref_classes_names)


    # Initialize storage for results (dimensions based on active data)
    bootstrap_results <- list(
      p_dot_k = matrix(NA, nrow = n_bootstrap, ncol = n_ref_classes, dimnames = list(NULL, ref_classes_names)),
      UA_k = matrix(NA, nrow = n_bootstrap, ncol = n_strata, dimnames = list(NULL, strata_names)),
      PA_k = matrix(NA, nrow = n_bootstrap, ncol = n_ref_classes, dimnames = list(NULL, ref_classes_names))
    )

    # --- Bootstrap Loop ---
    print(paste("Starting bootstrap with", n_bootstrap, "replicates..."))
    pb <- txtProgressBar(min = 0, max = n_bootstrap, style = 3) # Progress bar

    for (b in 1:n_bootstrap) {
      # Create an empty bootstrap sample confusion matrix
      bootstrap_sample_counts <- matrix(0, nrow = n_strata, ncol = n_ref_classes,
                                        dimnames = list(strata_names, ref_classes_names))
      
      # Perform stratified resampling
      for (stratum_name in strata_names) {
        n_i <- stratum_n[stratum_name] # Original sample size for stratum i
        
        if (n_i > 0) {
          # Get indices of original points belonging to this stratum
          original_indices_in_stratum <- which(sample_data_long$stratum_id == stratum_name)
          
          # Resample indices WITH replacement
          # Handle case where stratum might have only 1 sample in original data
          if(length(original_indices_in_stratum) == 1) {
            resampled_indices <- rep(original_indices_in_stratum, n_i)
          } else {
            resampled_indices <- sample(original_indices_in_stratum, size = n_i, replace = TRUE)
          }
          
          
          # Get the corresponding resampled points
          resampled_points_in_stratum <- sample_data_long[resampled_indices, ]
          
          # Tally the results into the bootstrap confusion matrix using table()
          # Need to ensure factors have all levels present for consistent table dimensions
          resampled_points_in_stratum$map_class_f <- factor(resampled_points_in_stratum$map_class, levels = strata_names)
          resampled_points_in_stratum$ref_class_f <- factor(resampled_points_in_stratum$ref_class, levels = ref_classes_names)
          # Use try to handle cases where table might be empty if n_i was 0 (shouldn't happen with check)
          tally <- try(table(resampled_points_in_stratum$map_class_f, resampled_points_in_stratum$ref_class_f), silent = TRUE)
          
          if (!inherits(tally, "try-error")) {
            # Add tally for this stratum to the overall bootstrap matrix
            # Note: Since map_class == stratum_id, the tally will only have one row corresponding to the current stratum.
            bootstrap_sample_counts[stratum_name, ] <- tally[stratum_name, ]
          }
        }
      } # End loop over strata
      
      # Calculate metrics for this bootstrap sample
      # Use tryCatch to handle potential errors in calculation for rare bootstrap samples
      current_metrics <- tryCatch({
        calculate_metrics(bootstrap_sample_counts, stratum_weights)
      }, error = function(e) {
        # print(paste("Error in bootstrap iteration", b, ":", e$message)) # Optional debug
        # Return NA values if calculation fails
        list(
          p_dot_k = setNames(rep(NA, n_ref_classes), ref_classes_names),
          UA_k = setNames(rep(NA, n_strata), strata_names),
          PA_k = setNames(rep(NA, n_ref_classes), ref_classes_names)
        )
      })
      
      
      # Store the results, ensuring names align if NAs were returned
      # Check if the result is valid before trying to access names
      if(is.list(current_metrics) && !is.null(current_metrics$p_dot_k)) {
        bootstrap_results$p_dot_k[b, names(current_metrics$p_dot_k)] <- current_metrics$p_dot_k
      } else {
        bootstrap_results$p_dot_k[b, ] <- NA
      }
      if(is.list(current_metrics) && !is.null(current_metrics$UA_k)) {
        bootstrap_results$UA_k[b, names(current_metrics$UA_k)] <- current_metrics$UA_k
      } else {
        bootstrap_results$UA_k[b, ] <- NA
      }
      if(is.list(current_metrics) && !is.null(current_metrics$PA_k)) {
        bootstrap_results$PA_k[b, names(current_metrics$PA_k)] <- current_metrics$PA_k
      } else {
        bootstrap_results$PA_k[b, ] <- NA
      }
      
      
      setTxtProgressBar(pb, b) # Update progress bar
    } # End bootstrap loop
    close(pb) # Close progress bar
    print("Bootstrap finished.")
    print("-------------------------")

    # --- 5. Analyze Bootstrap Results ---

    # --- Standard Errors (SE) ---
    # Calculate standard deviation, removing NA results if any occurred
    SE_p_dot_k <- apply(bootstrap_results$p_dot_k, 2, sd, na.rm = TRUE)
    SE_UA_k <- apply(bootstrap_results$UA_k, 2, sd, na.rm = TRUE)
    SE_PA_k <- apply(bootstrap_results$PA_k, 2, sd, na.rm = TRUE)

    print("--- Bootstrap Standard Errors (SE) ---")
    print("SE Area Proportions (p_dot_k):")
    print(SE_p_dot_k)
    print("SE User's Accuracies (UA_k):")
    print(SE_UA_k)
    print("SE Producer's Accuracies (PA_k):")
    print(SE_PA_k)
    print("--------------------------------------")

    # --- Confidence Intervals (CI) ---
    # Using the percentile method (captures asymmetry)
    alpha <- 0.05 # for 95% CI
    lower_quantile <- alpha / 2
    upper_quantile <- 1 - alpha / 2

    # Calculate quantiles, removing NA results if any occurred
    CI_p_dot_k <- apply(bootstrap_results$p_dot_k, 2, quantile, probs = c(lower_quantile, upper_quantile), na.rm = TRUE)
    CI_UA_k <- apply(bootstrap_results$UA_k, 2, quantile, probs = c(lower_quantile, upper_quantile), na.rm = TRUE)
    CI_PA_k <- apply(bootstrap_results$PA_k, 2, quantile, probs = c(lower_quantile, upper_quantile), na.rm = TRUE)

    print("--- Bootstrap 95% Confidence Intervals (Percentile Method) ---")
    print("CI Area Proportions (p_dot_k):")
    print(CI_p_dot_k)
    print("CI User's Accuracies (UA_k):")
    print(CI_UA_k) 
    print("CI Producer's Accuracies (PA_k):")
    print(CI_PA_k)
    print("--------------------------------------------------------------")



    # --- Note on applying to other data ---
    # To switch between datasets:
    # 1. Comment out the block for the INACTIVE dataset(s) in Section 1.
    # 2. Uncomment the block for the ACTIVE dataset in Section 1.
    # 3. Ensure 'ref_base_names' is defined correctly for the active dataset.
    # 4. Set n_bootstrap to the desired number (e.g., 5000).
    # 5. Re-run the entire script.

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
