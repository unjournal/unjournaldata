---
affiliation:
- id: 0
  organization: University of Texas at Dallas
article:
  doi: 10.21428/d28e8e57.2c870c01
  elocation-id: liangetaleval1
author:
- Elias Cisneros
bibliography: /tmp/tmp-60m0Ifdovz4agw.json
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
title: "Evaluation 1 of \"The Environmental Effects of Economic
  Production: Evidence from Ecological Observations\" for The Unjournal"
uri: "https://unjournal.pubpub.org/pub/liangetaleval1"
---

This is an evaluation of Liang et al ([@temp_id_5187546922896782]).

# Summary measures

**Overall assessment**

Answer: 88

Confidence (from 0 - 5): 5

**Quality scale rating**

"On a 'scale of journals', what 'quality of journal' should this be
published in?: Note: 0= lowest/none, 5= highest/best"

Answer: 4

Confidence (from 0 - 5): 5

[See here](https://unjournal.pubpub.org/pub/liangevalsum/ "null") for a
more detailed breakdown of the evaluators' ratings and predictions.

# Written report

*\[Evaluation manager/editor's note: I made some very copy-editing
corrections below.\]*

Thank you for the opportunity to read this paper. I truly enjoyed
reading it.

This work investigates the relationship between economic growth and
biodiversity in the United States. It leverages an extensive database
that collects an array of time-consistent species surveys at different
locations to build yearly biodiversity indices for eight taxa across 50
years. Using fixed-effects regressions, the authors relate the
biodiversity outcomes with state-level GDP measures in an unbalanced
data set. They find a robust negative correlation between economic
growth and biodiversity outcomes, with an elasticity of 1.5 to 3.5%.
Although varying in size, estimates are consistent across taxa,
production industries, biodiversity indices used, or alternative
observational units (e.g., counties, eco-regions). The paper further
delves into a causal identification of the impacts of economic growth on
biodiversity using exogenous variations in military spending in a
shift-share IV approach. The second part of the paper further explores
two potential mechanisms, pollution and land-use change, highlighting
their role in the decline of biodiversity across the United States.

The paper makes a highly valuable contribution to understanding the
trade-offs between economic growth and its impacts on biodiversity.
Furthermore, the authors spearhead a new spatially granular database on
biodiversity measures that has received little attention from
environmental and ecological economists. I am convinced that readers
will be eager to follow and use the BioTIME database to understand the
economic and political impacts on biodiversity.

Although I am fully convinced about the timeliness and importance of the
paper, I have some comments related to framing and the empirical
approach of the mechanism analysis. Nonetheless, many of the raised
points can be easily addressed. If the authors pursue these improvements
and others they receive elsewhere, I believe they will make a highly
valuable contribution to the environmental economics literature.

**Major Comments**

1\. The paper combines a multitude of empirical approaches and units of
analysis. Although each approach has its advantage, switching back and
forth between different approaches decreases the manuscript\'s
readability. Although it is undoubtedly a matter of writing style and a
question of the target journal, I believe that reordering some sections
could ease the reading experience and streamline some of the arguments.

a\. I suggest to order the arguments that are also linked to empirical
approaches as follows: A) Correlation between biodiversity and GDP using
OLS, B) Establish causality with IV; C) Robustness on measurements
biases using the IV approach (instead of OLS); D) analyzing
heterogeneities (e.g., by taxa, EKC, distributional, etc.) with the IV
approach (instead of OLS); D) Pollution channel analysis with
Wind-direction-IV E) Land-use channel analysis using OLS correlation:
Though I would put this to the appendix or skip it entirely (see
comments below). F) Environmental regulations channel analysis using
TWFE. Though I would leave out the fuzzy regulation-GDP-biodiversity
link G) Protected area channel analysis. However, I would replace it
with a panel on protected area creation and use a TWFE estimator
(instead of a heterogeneity analysis with interaction terms.

b\. Before delving into potential heterogeneous results in section 3.2,
I would address the potential biases. Section 2.3 (Title should be:
"Potential sources of *measurement* bias") deals with the potential
measurement biases, while only section 4.1 addresses the omitted
variable bias and reverse causality bias. I think it is best to address
all biases next to each other. I would first describe the empirical
strategy and then, directly after, the potential a) measurement biases
and b) the potential omitted variable and reverse causality biases
together.

c\. After addressing potential biases I would create two separate
chapters a) on heterogeneities (now section 3.2) and on potential
channels (now sections 4.2 and 4.3).

2\. After the main results, you choose to contrast two samples: All taxa
vs non-bird taxa. The comparison group is missing. One should present
results for either both groups, i.e., Bird taxa + non-bird taxa, or the
three samples, i.e., all, bird, and non-bird. Results are mostly better
for non-bird taxa, while results for the full sample are often
insignificant. This bears the question if results for birds only are
always insignificant or even point in a different direction.

3\. Results on sectoral GDP (Table 2) are highly biased and, therefore
not very informative. Regressing biodiversity on GDP is already subject
to selection bias (though I think the paper is making a good point and
presents a very valuable first analysis). Differentiating between
sectoral GDP growth and jointly using all indicators in one regression
must increase the problems of attribution, multicollinearity, reverse
causality, and omitted variable bias. You do recognize these issues when
discussing the positive estimate for agricultural GDP... I suggest
excluding this argument (analysis) from the paper or trying a different
empirical approach. Maybe it is possible to combine the IV strategy in
combination with pre-period sectoral shares?

4\. In the pollution channel analysis (section 4.2), I would like to see
a more detailed reasoning for the selection of contributing counties.
First, why are counties in a 300 km radius excluded? It would seem that
close pollution sources are the most important. Second, the LASSO
regression selects counties (see Figures 5a and 5b) that are thousands
of miles away. Could it be that those relations are a statistical
artifact and do not represent a true physical impact? I know that
pollution from massive forest fires can travel large distances (e.g.,
Indonesia, Canada), but maybe you can back up your argument with natural
science literature. On the other hand, far-away pollution sources might
not pose a problem in your analysis as the IV is weighted by the inverse
distance. Nonetheless, Figure 5 and your description is misleading at
first sight.

5\. The analysis of land-use policies (section 5.2) could be improved by
using a panel of protected areas. I am unfamiliar with the expansion of
protected areas in the United States. Still, if there is a significant
expansion of protected areas in the vicinity of the sampling locations,
that could be exploited in a quasi-experimental setting. You could use
the panel of new protected areas in a similar empirical framework as the
analysis on pollution attainment areas using TWFE.

## **Minor comments**

1\. I understand that many interdisciplinary journals prefer a graphical
depiction of the main results, though if you choose an economic journal,
I suggest showing results in Table format. I find it easier to read and
understand the empirical strategy and the number of fixed effects and
observations in a Table format.

a\. The main results table could present the results of Figure 3a
potentially using 3, 6 or 9 columns differentiating between all, bird,
and non-bird taxa. It is also the set-up you choose to carry on in the
text. Therefore, it might be more transparent to make the distinction
right away. Figure 3b could pose as additional information for the
appendix rather than a pre-step to show before summing everything up
into bird vs. non-bird species.

b\. OLS and IV estimates are easier to compare in Table format - Figure
4b does not easily convey how good the IV strategy is (first stage) and
how small or large the difference between the IV and OLS estimates is.
Table 3 is much more transparent but also mixes reduced form with IV
estimates. In general, I don't think it is not necessary to present a
complete graph with a single line-plot just to show one point estimate.

2\. I think the analysis of pollution regulations (section 5.1) can be
cut to the TWFE estimation only. The exercises with GDP and the repeated
comparison of overall vs. mechanism effects seems to massage the data a
bit too much.

3\. It might help to contrast the urbanization (section 4.3) and the
construction-sector GDP estimates (section 4.3) next to each other.

4\. Table 2 does not describe which FE are used.

5\. You are missing a dotted zero line in Figure 3d

6\. Figure A6 left has a wrong negative sign on the coefficient.

7\. On page 15, you write, "ηt denotes year fixed effects to capture
common shocks such as national recessions". Year fixed effecs also
capture common changes in federal environmental policies, regulations,
laws, financing of protected areas, overall enforcement budget, etc.

8\. Please provide a more straightforward argument why a state-level
analysis is the preferred spatial unit. Later on, you sometimes shift
the unit of analysis, which adds unnecessary to the complexity of the
manuscript. I would recommend to choose one unit of analysis for the
main text, as there are already many variations in the empirical
strategy.

> 9\. How is Table A.2 a panel regression if its outcome is constant
> over time (columns 2-6)?
>
> 10\. Sometimes the paper mixes the data description with the
> estimation strategy: E.g., on page 9, "As previously noted, in all
> regressions we include ... ". I would try to streamline the text for
> easier reading.

## Evaluator details {#survey-questions}

1.  How long have you been in this field?

> I started my Ph.D. in 2012. Thereby I am already 11 years in the
> field.

2.  How many proposals, papers, and projects have you evaluated/reviewed
    (for journals, grants, or other peer-review)?

I have reviewed 13 papers for 8 journals.
