---
article:
  doi: 10.21428/d28e8e57.5411b150/6a67da7e
  elocation-id: e1naturalregeneration
author:
- Evaluator 1
bibliography: /tmp/tmp-59FJathaf821P8.json
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
title: Evaluation 1 of "Global potential for natural regeneration in
  deforested tropical regions"
uri: "https://unjournal.pubpub.org/pub/e1naturalregeneration"
---

# Abstract 

**Strengths**\
- Proposes an empirically novel approach to answer highly
policy-relevant questions\
- Provides a sound overall methodology which is tractable and
replicable\
\
**Critiques**\
- Trained model does not enable prediction into the future given
currently observed conditions\
- Predictions do not represent pure biophysical potential despite being
framed as such\
- Regrowth longevity is not addressed\
- Policy targeting implications qualified by additionality and
opportunity costs

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
| **Overall         | 50/100            | 4 |
| assessment **     |                   | 0 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 6 |
|                   |                   | 0 |
+-------------------+-------------------+---+
| **Journal rank    | 3.5/5             | 3 |
| tier, normative   |                   | . |
| rating**          |                   | 0 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 4 |
|                   |                   | . |
|                   |                   | 0 |
+-------------------+-------------------+---+

**Overall assessment **(See footnote[^2])

**Journal rank tier, normative rating (0-5): ** On a 'scale of
journals', what 'quality of journal' should this be published in?[^3]
*Note: 0= lowest/none, 5= highest/best. *

# Claim identification and assessment

## I. Identify the most important and impactful factual claim this research makes[^4] {#i-identify-the-most-important-and-impactful-factual-claim-this-research-makes}

The authors estimate that biophysical conditions can support natural
regeneration in tropical forests over 215 million hectares globally, and
five countries (Brazil, Indonesia, China, Mexico and Colombia) account
for 52% of this estimated potential (source: abstract and last paragraph
in p. 132). The estimation is based on spatially explicit machine
learning predictions of natural regeneration potential. The claim is
important due to ambitious forest restoration targets requiring
science-based guidance on spatial targeting.

## II. To what extent do you \*believe\* the claim you stated above?[^5] {#ii-to-what-extent-do-you-believe-the-claim-you-stated-above}

I have low confidence in the estimated 215 Mha being an accurate figure
on biophysical potential. It is likely a lower bound to the true value,
due to anthropogenic factors which moderate the results. Other
comparable estimates do not exist. However, the true value is certainly
well below the maximum area of opportunity estimated at 678 Mha in a
previous study. The spatial distribution of reported results is biased
towards higher potential in regions with low anthropogenic disturbance.

## III. Suggested robustness checks[^6] {#iii-suggested-robustness-checks}

The proposed method cannot uncover the pure biophysical potential which
is how the authors interpret the result. The results do, however,
represent locations where natural regeneration is likely to happen under
a business-as-usual scenario. For this latter quantity to be accurately
estimated, the most important modification to the method would be to
formulate the prediction as a prediction of future outcomes conditional
on currently observed covariates.

## IV. Important 'implication', policy, credibility[^7] {#iv-important-implication-policy-credibility}

The results imply information about the spatial distribution of low-cost
forest restoration opportunities. The predictions likely correctly
identify several regions with high potential (no false positives) but
anthropogenic factors mask others (false negatives likely exist). An
important caveat to interpreting the results is that the identified
regions with high regeneration potential may also provide the least
additionality from interventions. As such, these results alone should
not guide policy choices.

# Written report

## Introduction

In their analysis, Williams et al. (2024) [@Williams2024Global] train a
Random Forest model to predict the probability of natural forest
regeneration at pan-tropical scale. The model is trained from previously
identified natural regrowth patches (Fagan et al., 2022)
[@Fagan2022expansion] and various biophysical and socioeconomic
features. In contrast to previous literature where estimates of forest
regeneration potential are based on the maximum area of opportunity
[@Cook2020Mapping][@Bastin2019global][@Griscom2017Natural], the authors'
predictions characterize the *likelihood* of natural regeneration. Based
on the predictions, the authors estimate that an area of 215 million
hectares has potential for natural regeneration and that over half of
this potential is located within five countries.

The study is a timely contribution to an important policy and scientific
topic. Forest restoration is among the most cost-effective mitigation
options [@IPCC2022Working], and various global (the UN Decade on
Ecosystem Restoration, the Bonn Challenge) and national (e.g. Bolivia's
Nationally Determined Contribution to restore 1 million ha by 2030)
initiatives have set ambitious restoration targets that require
science-based guidance for effective implementation. The paper sets out
to provide novel estimates of the probability of forest regeneration,
based on observed regeneration patches.

The overall methodological approach is appropriate, tractable, and
replicable with readily available data sources. While more sophisticated
training algorithms are available [@Masolele2021Spatial][@Ball2022Using]
and they could lead to increased predictive accuracy, they also come
with a significant computational cost. Random Forest is appealing due to
its computational tractability while being robust against overfitting
when sufficient input data are available and shallow or pruned trees are
used [@Oshiro2012How][@Barrenada2024Understanding]. Uncertainty in the
results, arising from input data sources and the model prediction
accuracy, is quantifiable and discussed transparently and extensively.

Despite these strengths, there are several aspects in the implementation
of the method and the interpretation of the results that qualify the
results and the conclusions the authors provide, warranting this
commentary. In short: (1) the trained model does not enable prediction
into the future given currently observed conditions, (2) the predictions
do not represent pure biophysical potential, and (3) regrowth longevity
is not addressed. Even if methodological concerns were addressed,
considerations of intervention additionality further qualify the
provided discussion and policy implications. The model predictions can
provide only partial, and in some cases biased or even misleading
guidance.

In the following, I expand on these critiques, offer methodological
suggestions, and discuss the interpretation of the results. The goal of
this review is to identify methodological improvements which subsequent
research on the topic should adopt, as well as highlight caveats which
policymakers should consider when using the results from the present
study or similar analyses.

## Contemporaneous predictors

The outcome variable indicates patches of natural forest regeneration
which occurred between 2000--2012 and persisted to 2016. At least three
of the predictor variables seen by the training algorithm are also
recorded during this period rather than prior to it: net primary
production, burned area, and road density
[@Zhao2005Improvements][@Artes2019global][@Meijer2018Global]. In
addition, the authors use variables from the ESA CCI land cover dataset
as recorded in the year 2000, overlapping with the outcome.

Due to this temporal overlap, the predicted regrowth probabilities are
conditional on events that are contemporaneous with the outcome. As a
result, the model predicts the present rather than the future. When the
authors predict regrowth in the near future, they make assumptions about
unobserved future data which are not available at the time of
prediction. Importantly, these assumptions are not reflected in the
model accuracy metrics. The reported model accuracy thus likely
overstates the true predictive performance.

This is especially problematic for variables like net primary
production---a key driver of regrowth and an indicator that regrowth is
happening---since assuming its future trajectory effectively dictates
the predicted outcome. The same applies to burned area and road density,
both of which can be seen as causal determinants for (the absence of)
natural forest regeneration.

It is important to distinguish this problem from the usual assumption
that relationships between the predictors and the target variable
persist in a new domain. This assumption is inherent in any
out-of-domain prediction, be it prediction into future time periods or
geographic regions not seen by the training algorithm. In contrast, the
issue here stems from assuming knowledge of future predictor values
themselves.

A solution to this problem is to delimit predictors to those that are
either time invariant or observed before the year 2000. This is feasible
with the ESA CCI land cover data which are available since 1992, as well
as climatic data. Soil characteristics could be considered time
invariant for short- to medium-term predictions. With such adjustments,
the model would predict future outcomes conditional on presently
available data, and accuracy metrics would correctly reflect predictive
performance under this constraint.

## Biophysical vs socioeconomic determinants and interpretation

While the authors train models with biophysical and socioeconomic
predictors, their spatial predictions are derived from a model that
includes only biophysical variables. This is motivated as an attempt to
identify areas with \"biophysical conditions amenable to natural
regeneration regardless of whether socioeconomic conditions are
favorable\" and with \"potential for natural regeneration if
socioeconomic factors limiting regeneration are managed\".

However, inferring purely biophysical potential from observational data
is not feasible with the proposed method. The difficulty lies in the
fact that biophysical and socioeconomic conditions are deeply
interconnected and affect one another. Predictions of forest
regeneration reflect a joint outcome from both domains, even when only
biophysical predictors are used. In practice, the model will predict
high regeneration probability in locations where *both* factors are
favorable. While this prediction is useful in its own right, it does not
support the interpretation the authors propose.

This issue has direct implications for the main findings of the study.
The knowledge gap which the authors identify and propose to resolve is
estimating *the degree of biophysical potential*. Using their model, the
authors argue that biophysical conditions could support natural
regeneration over an area of 215 Mha. However, as discussed above---and
contrary to the authors' interpretation---socioeconomic factors
substantially influence this result. If socioeconomic factors were to be
moderated, biophysical conditions could likely support a substantially
larger area for natural regeneration.

Overcoming this fundamental empirical constraint would overstep the
methodological scope of the present study, but would indeed be a novel
although non-trivial empirical exercise. A starting point could be to
correlate the outcome with biophysical features in regions where
socioeconomic constraints are minimal. Taking a step further, a
quasi-experimental design could examine exogenous variation in
socioeconomic factors.

## Ephemerality of forest regrowth

Short-term increases in natural forest cover do not necessarily
translate into persisting forest cover and the longevity patterns are
spatially non-uniform [@n29uv456gbc][@no26z3cg5c6][@Crawford2022Rural].
Addressing this aspect would be an extension to the presented
methodology, yet implementing it would be feasible and desirable as
spatial variation in regrowth longevity is likely and has important
implications for policy design and targeting.

The outcome data of the analysis do not identify locations with very
short-lived forest regeneration lasting less than four years. The
implication is that these locations will receive low predicted
regeneration probabilities, even though they may be even more important
for policy targeting. As for forest regeneration that lasted for more
than four years, differentials in persistence still induce a
differential in targeting priority which the presented method does not
capture.

With data from Hansen et al., (2013)[@Hansen2013High] which underlie the
outcome variable in the analysis, one could differentiate between
regions based on the degree of deforestation that is concurrent with
forest regrowth in the same region. Arguably, where concurrent
deforestation is high, the detected natural forest regeneration is less
likely to persist. Alternatively, one could use annual data on forest
cover change, which are currently available for the neotropics
[@Souza2020Reconstructing] and becoming available globally
[@Zhang2023GLC_FCS30D][@Arevalo2022Global].

## Policy implications

A central motivation for the analysis is how the resulting predictions
can inform the planning and targeting of forest restoration efforts. The
spatial predictions provide explicit targeting advice, even if the
authors are mindful of the multitude of factors that should inform such
decision making and that their method should be considered only as one
input that reflects specific aspects.

The methodological issues discussed above have direct implications on
spatial bias in the provided estimates. In sum, assuming that present
patterns on predictors that are closely related to the outcome also
persist in the future will induce non-quantified and likely spatially
non-uniform prediction error; socioeconomic factors influence the
predictions which results in an understatement of biophysical potential;
the model does not capture the persistence of forest regrowth, deflating
(inflating) the targeting priority of short-lived (persisting) regrowth.

Given that the above critiques were addressed, the model predictions
could provide compelling insights for intervention targeting and
planning. The authors note that by identifying areas where natural
regeneration is already occurring under current conditions, the model
highlights regions where the required intervention effort is likely to
be lowest and intervention success rate is likely to be highest. This
conclusion is well-founded in the provided references
[@Brancalion2019What][@Crouzeilles2017Ecological][@Bodin2022standard][@Hua2022biodiversity].
But are these the regions where interventions should actually be
prioritized? The answer hinges crucially on two related aspects:
additionality and the opportunity cost of forest restoration.

Additionality is certainly difficult to quantify yet at the core of the
targeting problem [@West2023Action][@Probst2023Systematic]. For
achieving additionality, the provided predictions alone hardly provide
any straightforward guidance. This follows from how the predictions
represent a business-as-usual probability for forest regeneration which
would occur even in the absence of an intervention. The regions
highlighted by the model are precisely those where interventions
facilitating forest regrowth will have the lowest additionality.
However, as the authors note, protecting the emerged regrowth could
create additionality, but only where regrowth is short-lived in the BAU
scenario.

On opportunity costs, or the forgone benefits from competing land uses,
there is no clear empirical prior on whether they will be correlated
with the prediction. While agriculture abandonment leading to regrowth
could be more likely to occur where agriculture has low profitability,
empirical studies have also found an opposite pattern [@nezxhh8s47q].
Fortunately, a recent analysis provides spatially explicit estimates of
opportunity costs [@Busch2024Cost].

Conservation efforts should be directed towards areas where they provide
the highest additional net benefits---that is, where interventions lead
to the maximal benefits that would not have occurred otherwise, and
where costs are simultaneously minimized. Identifying these \"sweet
spots\"---based on implementation costs, opportunity costs, success
rates, and additionality---clearly falls outside of the scope of the
present study. A central message of this critique is to highlight the
importance of these other aspects and to caution that focusing on a
single dimension, in isolation, can lead to incomplete or potentially
misleading advice.

## References

[@n8sk4h6lxel] Williams, Brooke A, Hawthorne L Beyer, Matthew E Fagan,
Robin L Chazdon, Marina Schmoeller, Starry Sprenkle-Hyppolite, Bronson W
Griscom, et al. 2024. 'Global Potential for Natural Regeneration in
Deforested Tropical Regions'. *Nature*, 1--7.

[@n9px425134u]Fagan, Matthew E, Do-Hyung Kim, Wesley Settle, Lexie
Ferry, Justin Drew, Haven Carlson, Joshua Slaughter, et al. 2022. 'The
Expansion of Tree Plantations across Tropical Biomes'. *Nature
Sustainability* 5 (8): 681--88.

[@nsc83kq2lgw] Cook-Patton, Susan C, Sara M Leavitt, David Gibbs, Nancy
L Harris, Kristine Lister, Kristina J Anderson-Teixeira, Russell D
Briggs, et al. 2020. 'Mapping Carbon Accumulation Potential from Global
Natural Forest Regrowth'. *Nature* 585 (7826): 545--50.

[@n0kmwqss1tz] Bastin, Jean-Francois, Yelena Finegold, Claude Garcia,
Danilo Mollicone, Marcelo Rezende, Devin Routh, Constantin M Zohner, and
Thomas W Crowther. 2019. 'The Global Tree Restoration Potential'.
*Science* 365 (6448): 76--79.

[@ndp7ypqcd5t] Griscom, Bronson W, Justin Adams, Peter W Ellis, Richard
A Houghton, Guy Lomax, Daniela A Miteva, William H Schlesinger, et al.
2017. 'Natural Climate Solutions'. *Proceedings of the National Academy
of Sciences* 114 (44): 11645--50.

[@ny9a5cqwvtv] IPCC. 2022. 'Working Group III Contribution to the Sixth
Assessment Report of the Intergovernmental Panel on Climate Change'.
Springer.

[@nvc8u88jhkn]Masolele, Robert N, Veronique De Sy, Martin Herold, Diego
Marcos, Jan Verbesselt, Fabian Gieseke, Adugna G Mullissa, and
Christopher Martius. 2021. 'Spatial and Temporal Deep Learning Methods
for Deriving Land-Use Following Deforestation: A Pan-Tropical Case Study
Using Landsat Time Series'. *Remote Sensing of Environment* 264:112600.

[@nd6tbgi7nga] Ball, James GC, Katerina Petrova, David A Coomes, and
Seth Flaxman. 2022. 'Using Deep Convolutional Neural Networks to
Forecast Spatial Patterns of Amazonian Deforestation'. *Methods in
Ecology and Evolution* 13 (11): 2622--34.

[@n8t6jcaf409] Oshiro, Thais Mayumi, Pedro Santoro Perez, and José
Augusto Baranauskas. 2012. 'How Many Trees in a Random Forest?' In
*Machine Learning and Data Mining in Pattern Recognition: 8th
International Conference, MLDM 2012, Berlin, Germany, July 13-20, 2012.
Proceedings 8*, 154--68. Springer.

[@nuj5nfurn5r] Barreñada, Lasai, Paula Dhiman, Dirk Timmerman,
Anne-Laure Boulesteix, and Ben Van Calster. 2024. 'Understanding
Overfitting in Random Forest for Probability Estimation: A Visualization
and Simulation Study'. *Diagnostic and Prognostic Research* 8 (1): 14.

[@nqxfte1znp8] Zhao, M., Heinsch, F. A., Nemani, R. R., & Running, S. W.
(2005). Improvements of the MODIS terrestrial gross and net primary
production global data set. *Remote Sensing of Environment*, *95*(2),
164--176.

[@n9lxmobyn95] Artés, Tomàs, Duarte Oom, Daniele De Rigo, Tracy Houston
Durrant, Pieralberto Maianti, Giorgio Libertà, and Jesús
San-Miguel-Ayanz. 2019. 'A Global Wildfire Dataset for the Analysis of
Fire Regimes and Fire Behaviour'. *Scientific Data* 6 (1): 296.

[@nvglll2llby] Meijer, Johan R, Mark AJ Huijbregts, Kees CGJ Schotten,
and Aafke M Schipper. 2018. 'Global Patterns of Current and Future Road
Infrastructure'. *Environmental Research Letters* 13 (6): 064006.

[@nfqmi9sgpwq] Piffer, Pedro R., Adriane Calaboni, Marcos R. Rosa, Naomi
B. Schwartz, Leandro R. Tambosi, and María Uriarte. 2022. 'Ephemeral
Forest Regeneration Limits Carbon Sequestration Potential in the
Brazilian Atlantic Forest'. *Global Change Biology* 28 (2): 630--43.

[@nfrgofrrz92] Reid, J Leighton, Matthew E Fagan, James Lucas, Joshua
Slaughter, and Rakan A Zahawi. 2019. 'The Ephemerality of Secondary
Forests in Southern Costa Rica'. *Conservation Letters* 12 (2): e12607.

[@n2mp2vt9jzd] Crawford, Christopher L, He Yin, Volker C Radeloff, and
David S Wilcove. 2022. 'Rural Land Abandonment Is Too Ephemeral to
Provide Major Benefits for Biodiversity and Climate'. *Science Advances*
8 (21): eabm8999.

[@nqsvuwvtkzm] Hansen, M. C., Potapov, P. V., Moore, R., Hancher, M.,
Turubanova, S. A., Tyukavina, A., ... others. (2013). High-resolution
global maps of 21st-century forest cover change. *Science*, *342*(6160),
850--853.

[@nq5eh0nsdlo] Souza Jr, C. M., Z. Shimbo, J., Rosa, M. R., Parente, L.
L., A. Alencar, A., Rudorff, B. F., ... others. (2020). Reconstructing
three decades of land use and land cover changes in Brazilian biomes
with Landsat archive and Earth Engine. *Remote Sensing*, *12*(17), 2735.

[@n2ewk8x4aan] Zhang, Xiao, Tingting Zhao, Hong Xu, Wendi Liu, Jinqing
Wang, Xidong Chen, and Liangyun Liu. 2023. 'GLC_FCS30D: The First Global
30-m Land-Cover Dynamic Monitoring Product with a Fine Classification
System from 1985 to 2022 Using Dense Time-Series Landsat Imagery and
Continuous Change-Detection Method'. *Earth System Science Data
Discussions* 2023:1--32.

[@nr3z1dcd0ai] Arevalo, P, R Stanimirova, E Bullock, Y Zhang, K Tarrio,
K Turlej, K Hu, and others. 2022. 'Global Land Cover Mapping and
Estimation Yearly 30 m V001 \[Data Set\]'. *NASA EOSDIS Land Processes
Distributed Active Archive Center*.

[@n0mdwjaqjp8] Brancalion, Pedro HS, Paula Meli, Julio RC Tymus, Felipe
EB Lenti, Rubens M Benini, Ana Paula M Silva, Ingo Isernhagen, and Karen
D Holl. 2019. 'What Makes Ecosystem Restoration Expensive? A Systematic
Cost Assessment of Projects in Brazil'. *Biological Conservation*
240:108274.

[@nirkx5qcnaa] Crouzeilles, Renato, Mariana S Ferreira, Robin L Chazdon,
David B Lindenmayer, Jerônimo BB Sansevero, Lara Monteiro, Alvaro
Iribarrem, Agnieszka E Latawiec, and Bernardo BN Strassburg. 2017.
'Ecological Restoration Success Is Higher for Natural Regeneration than
for Active Restoration in Tropical Forests'. *Science Advances* 3 (11):
e1701345.

[@n4pfh2p4kpe] Bodin, Blaise, Valentina Garavaglia, Nathanaël Pingault,
Helen Ding, Sarah Wilson, Alexandre Meybeck, Vincent Gitz, Sara
d'Andrea, and Christophe Besacier. 2022. 'A Standard Framework for
Assessing the Costs and Benefits of Restoration: Introducing The
Economics of Ecosystem Restoration'. *Restoration Ecology* 30 (3):
e13515.

[@npnru3ohmxv] Hua, Fangyuan, L Adrian Bruijnzeel, Paula Meli, Philip A
Martin, Jun Zhang, Shinichi Nakagawa, Xinran Miao, et al. 2022. 'The
Biodiversity and Ecosystem Service Contributions and Trade-Offs of
Forest Restoration Approaches'. *Science* 376 (6595): 839--44.

[@nvg5gxarhzo] West, Thales AP, Sven Wunder, Erin O Sills, Jan Börner,
Sami W Rifai, Alexandra N Neidermeier, Gabriel P Frey, and Andreas
Kontoleon. 2023. 'Action Needed to Make Carbon Offsets from Forest
Conservation Work for Climate Change Mitigation'. *Science* 381 (6660):
873--77.

[@no6g5mu7hez] Probst, Benedict, Malte Toetzke, Andreas Kontoleon, Laura
Diaz Anadon, and Volker H Hoffmann. 2023. 'Systematic Review of the
Actual Emissions Reductions of Carbon Offset Projects across All Major
Sectors'.

[@nmsh6aiutwm] Busch, J., Bukoski, J. J., Cook-Patton, S. C., Griscom,
B., Kaczan, D., Potts, M. D., ... Vincent, J. R. (2024).
Cost-effectiveness of natural forest regeneration and plantations for
climate mitigation. *Nature Climate Change*, *14*(9), 996--1002.

Shen, Yicheng, I Colin Prentice, and Sandy P Harrison. 2025.
'Investigation of Factors That Affect Post-Fire Recovery of
Photosynthetic Activity at Global Scale'. *Ecological Indicators*
171:113206.

# Evaluator details

1.  How long have you been in this field?

    -   5 years

2.  How many proposals and papers have you evaluated?

    -   2

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
