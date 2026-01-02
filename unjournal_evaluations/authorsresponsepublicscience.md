---
affiliation:
- id: 0
  organization: Duke University, Fuqua School of Business
- id: 1
  organization: Duke University
- id: 2
  organization: Tel-Aviv University
article:
  doi: 10.21428/d28e8e57.53029336
  elocation-id: authorsresponsepublicscience
author:
- Ashish Arora
- Sharon Belenzon
- Larisa Cioaca
- Lia Sheer
- Hansen Zhang
bibliography: /tmp/tmp-59HhaLAXmbgD4z.json
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
title: Authors' response to Unjournal evaluations of "The Effect of
  Public Science on Corporate R&D"
uri: "https://unjournal.pubpub.org/pub/authorsresponsepublicscience"
---

# Response to Evaluations Requested by The Unjournal

Ashish Arora, Sharon Belenzon, Larisa Cioaca, Lia Sheer, and Hansen
Zhang\
June 16, 2025

## Introduction

We are grateful for the opportunity to receive constructive feedback
through *The Unjournal*'s transparent evaluation process. We fully
support *The Unjournal*'s mission to make rigorous research more
impactful (and impactful research more rigorous). We appreciate the
platform's commitment to open science and timely public evaluations.

The work we present in "The Effect of Public Science on Corporate R&D"
speaks directly to the goals of *The Unjournal*. The paper examines how
three components of publicly funded science--- knowledge, human capital,
and invention---affect corporate innovation. Using rich administrative
data and a research design that exploits firm-specific exposure to
politically driven changes in federal R&D budgets, we identify the
causal impact of public science on business R&D. We find that scientific
knowledge produced by universities affects corporate R&D when embodied
in inventions or in PhD scientists. University-trained human capital
fosters firm innovation, but inventions from universities tend to
substitute for internal corporate R&D, possibly reflecting increased
downstream competition. Importantly, abstract scientific advances *per
se* elicit little or no corporate response from our panel of large,
publicly traded corporations. These findings challenge the view that
public science uniformly fuels business R&D through knowledge spillovers
and suggest more nuanced mechanisms.

We appreciate the evaluators' thoughtful and constructive feedback. In
the spirit of *The Unjournal*'s mission to advance empirical rigor and
policy relevance, we respond to each evaluation in turn.

We note that the version that was evaluated---NBER Working Paper 31899
(November 2023)--- reflects an earlier stage of the project. Since then,
the paper has been substantially revised in response to comments from
three anonymous journal reviewers and an editorial team. Nonetheless, we
address all substantive points raised (offset text) ... to ensure a
complete and transparent dialogue. Our responses follow...

## Evaluator 1: Anonymous

***\[Identification strategy, shift-share design, endogenous shares
issue\] ***[^1]*** ***

> The identification strategy relies on a shift-share design, where the
> shifts are based on U.S. congressional subcommittee spending on public
> science and the shares are based on firm exposure to specific
> subcommittee's shocks (based on firms' exposure to expenditures from
> specific government agencies and the subcommittees responsible for
> those agencies' funding). To address potential exclusion restriction
> violations, the paper does not use raw changes in subcommittee
> appropriations as its primary shock variable, but instead uses the
> changes in appropriations predicted by those subcommittees' party
> shares. This report identifies two key issues in the identification
> strategy.
>
> First, the paper's shift-share design likely yields biased results due
> to the endogeneity of the shares. The primary IV models shown in the
> paper instrument firms' exposure to public science using a series of
> shift-share formulas that, generally speaking, instrument a firm's
> exposure to public innovation with a sum of the products of (1) the
> share of a firms' exposure to a specific class of innovation (e.g.,
> publication subfields, patent subclassifications, etc) and (2) the
> predicted R&D expenditures from all federal agencies for that
> innovation class. (1) is likely endogenous; the paper indeed finds a
> positive correlation between firm R&D stock and agency R&D funding. Of
> course, this is only one source of endogeneity, and many more may
> exist. This is a general gripe with shift-share designs; much is
> discussed about how exogenous the shocks are but little attention is
> paid to whether the shares are endogenous, which they often are.

We thank the evaluator for raising an important issue about shift-share
identification. Recent literature has emphasized the need to consider
not just the exogeneity of the shift but also the potential endogeneity
of the exposure shares. However, the evaluator's concern overstates the
problem in our setting and overlooks the specific design features that
mitigate this risk.

First, our exposure shares are lagged and pre-determined, based on a
firm's publishing (or patenting) patterns across scientific subfields
(or technology classes) in prior five-year cohorts. These shares reflect
past activity, not future behavior or outcomes, and are fixed before the
realization of the shifts (i.e., predicted agency R&D budgets). As such,
they are unlikely to respond to contemporaneous shocks to firm
innovation or to expectations about future agency funding.

Second, the evaluator notes a positive correlation between firm R&D
stock and agency R&D funding, which we report and explicitly control for
in all specifications. Our identification does not rely on the
assumption that exposure shares are uncorrelated with firm size or R&D
intensity. Rather, we rely on the assumption that, conditional on firm
fixed effects, controls (like lagged R&D stock), and year fixed effects,
the predicted variation in public science stemming from shifts in
congressional composition is exogenous. Importantly, our preferred
instruments rely on exogenous variation in agency budgets induced by the
political composition of congressional subcommittees---a source of
variation plausibly unrelated to technology shocks facing individual
firms.

Third, shift-share designs are not invalidated by share endogeneity per
se, as long as the identifying variation comes from the shifts (i.e.,
predicted agency R&D budgets), and the shares are not systematically
correlated with unobserved shocks to outcomes after conditioning on
controls and fixed effects. The shares are used to project firm-specific
relevance, and in our case, they are based on historical specialization
patterns in publications and patents, relatively inertial dimensions of
firm activity.

Fourth, any remaining bias from endogenous shares would likely attenuate
the estimates rather than generate the clear, opposing signs we document
for public invention and human capital. The evaluator's critique does
not explain *how* endogenous exposure shares could systematically
produce such patterns, especially given the directionally opposite
effects we find.

In summary, while the general concern about share endogeneity in
shift-share designs is well taken, we believe our approach---anchored in
lagged specialization patterns, rich firm-level controls, and exogenous
political variation in the shifts---mitigates the most serious risks.
That said, we are actively developing an additional identification
strategy inspired by the geography of invention literature.
Specifically, we aim to measure firm exposure to shocks in public
science based on the proximity between corporate headquarters and
research universities. We plan to include this analysis in the next
version of the paper.

***\[Colliders\]***

> The paper attempts to address the endogeneity of shares by controlling
> for lagged firm-level R&D stock, but this exposes the paper to a third
> identification issue: the main specifications all control for
> colliders. An often-overlooked issue in control specifications is
> whether the controls are themselves outcomes of the main exposures of
> interest (in this case, public science). Cinelli, Forney, & Pearl
> (2024) show that if a covariate is (1) influenced by an exposure of
> interest and (2) shares a common unobserved confounder with the
> outcome, then controlling for the covariate will bias the estimated
> relationship between the outcome and the exposure of interest. To
> illustrate, consider the 'birth weight paradox' (Hernández-Díaz,
> Schisterman, & Hernán 2006). Though maternal smoking is associated
> with higher infant mortality and more incidence of low birth weight,
> when controlling for birth weight, maternal smoking appears to
> decrease infant mortality. This is not because maternal smoking
> actually decreases infant mortality, but rather because newborns who
> are low birth weight because of maternal smoking likely exhibit lower
> mortality rates than newborns who are low birth weight because of
> other health complications. Applying this concept to the paper's
> specifications, firm exposure to public science may not decrease firm
> innovation; rather, it may be the case that firms with more R&D stock
> due to public science innovate less than firms who have more R&D stock
> due to the inherent innovative nature of their activities."
>
> These issues together place the entire identification strategy in a
> bind. Firms with innovation profiles similar to those invested into by
> public agencies likely have different levels of R&D investment for
> reasons unrelated to public science, but controlling for these levels
> of R&D investment yields bad control problems because private R&D
> investment is inherently influenced by public science. The clear
> endogeneity issues with the shift-share design do not seem like they
> can be controlled away with observable covariates."

We appreciate the evaluator's engagement with recent methodological
literature, particularly the concern raised about conditioning on
potential colliders. However, in our context, this concern is not
material. Our results are robust across models with and without the R&D
stock control, as well as under alternative estimation methods (e.g.,
Poisson IV and inverse hyperbolic sine transforms).

As shown in Table 1, excluding lagged *R&D stock* as a control in the
Patents, Publications, and AMWS scientists equations (and lagged *Sales*
as a control in the R&D expenditures equation) does not qualitatively
change our core findings. Across all outcomes---patents, publications,
AMWS scientists, and R&D expenditures---lagged human capital (PhDs)
remains a strong, positive, and statistically significant predictor in
both OLS and 2SLS models.

By contrast, lagged public invention stock (university patents) shows no
significant effect in OLS, but becomes negative and significant in 2SLS
for patents, publications, and R&D spending, similar to the results when
we included lagged R&D stock as a control. This pattern is consistent
with potential endogeneity in the OLS estimates and supports the paper's
main finding of a negative effect of public invention on firm innovation
for our sample of large, publicly traded firms.

The coefficient on lagged public knowledge stock (university
publications) is positive (though small in magnitude) and significant in
OLS, but the effect is largely insignificant in 2SLS models, suggesting
its apparent influence may be overstated when endogeneity is not
addressed. This pattern suggests that our findings are not an artifact
of conditioning on a potential collider.

**Table 1: Robustness Check -- Excluding the Firm Size Control**

+--------------------------+-------------+-------------+------------------+------------------+--------------+--------------+--------------+--------------+
| **Dependent variable:**  | **(1)       | **(2)       | **(3)            | **(4)            | **(5)        | **(6)        | **(7)        | **(8)        |
|                          | ln(1+       | ln(1+       | ln(1+            | ln(1+            | ln(1+AMWS    | ln(1+AMWS    | ln(\$1+R&D   | ln(\$1+R&D   |
|                          | Patents)ₜ** | Patents)ₜ** | Publications)ₜ** | Publications)ₜ** | sc           | sc           | expe         | expe         |
|                          |             |             |                  |                  | ientists)ₜ** | ientists)ₜ** | nditures)ₜ** | nditures)ₜ** |
+==========================+=============+=============+==================+==================+==============+==============+==============+==============+
| **Model**                | OLS         | 2SLS        | OLS              | 2SLS             | OLS          | 2SLS         | OLS          | 2SLS         |
+--------------------------+-------------+-------------+------------------+------------------+--------------+--------------+--------------+--------------+
| ln(1+Public invention    | -0.004      | -           | -0.002 (0.004)   | -0.066\*\*\*     | 0.001        | -0.011       | 0.001        | -0.198\*\*   |
| stock)~ₜ₋₁~              | (0.005)     | 0.119\*\*\* |                  | (0.021)          | (0.003)      | (0.014)      | (0.003)      | (0.114)      |
|                          |             | (0.031)     |                  |                  |              |              |              |              |
+--------------------------+-------------+-------------+------------------+------------------+--------------+--------------+--------------+--------------+
| ln(1+Human capital)~ₜ₋₁~ | 0.046\*\*\* | 0.344\*\*\* | 0.016\*\*\*      | 0.143\*\*\*      | 0.009\*\*\*  | 0.048\*\*\*  | 0.009\*\*\*  | 0.245\*\*\*  |
|                          | (0.004)     | (0.033)     | (0.003)          | (0.021)          | (0.002)      | (0.013)      | (0.002)      | (0.082)      |
+--------------------------+-------------+-------------+------------------+------------------+--------------+--------------+--------------+--------------+
| ln(1+Public knowledge    | 0.015\*\*\* | 0.037\*\*\* | 0.011\*\*\*      | 0.003 (0.010)    | 0.002\*      | 0.018\*\*\*  | 0.002\*      | 0.019        |
| stock)~ₜ₋₁~              | (0.003)     | (0.013)     | (0.002)          |                  | (0.001)      | (0.006)      | (0.001)      | (0.033)      |
+--------------------------+-------------+-------------+------------------+------------------+--------------+--------------+--------------+--------------+
| **Year FE**              | Yes         | Yes         | Yes              | Yes              | Yes          | Yes          | Yes          | Yes          |
+--------------------------+-------------+-------------+------------------+------------------+--------------+--------------+--------------+--------------+
| **Firm FE**              | Yes         | Yes         | Yes              | Yes              | Yes          | Yes          | Yes          | Yes          |
+--------------------------+-------------+-------------+------------------+------------------+--------------+--------------+--------------+--------------+
| **Mean DV**              | 28.30       | 28.30       | 15.72            | 15.72            | 4.80         | 4.80         | 142.18       | 142.33       |
+--------------------------+-------------+-------------+------------------+------------------+--------------+--------------+--------------+--------------+
| **Weak id.               | ---         | 109.38      | ---              | 109.38           | ---          | 109.38       | ---          | 82.14        |
| (Kleibergen--Paap)**     |             |             |                  |                  |              |              |              |              |
+--------------------------+-------------+-------------+------------------+------------------+--------------+--------------+--------------+--------------+
| **Firms**                | 3,372       | 3,372       | 3,372            | 3,372            | 3,372        | 3,372        | 3,372        | 3,167        |
+--------------------------+-------------+-------------+------------------+------------------+--------------+--------------+--------------+--------------+
| **Observations**         | 41,698      | 41,698      | 41,698           | 41,698           | 41,698       | 41,698       | 41,698       | 36,672       |
+--------------------------+-------------+-------------+------------------+------------------+--------------+--------------+--------------+--------------+
| **Adjusted R²**          | 0.85        | 0.01        | 0.87             | 0.00             | 0.93         | 0.00         | 0.93         | -0.01        |
+--------------------------+-------------+-------------+------------------+------------------+--------------+--------------+--------------+--------------+

***Notes****:* This table presents the main estimation results after
excluding the firm size control: lagged R&D stock in Columns 1-3 and
lagged Sales in Column 4. Standard errors (in parentheses) are robust to
arbitrary heteroskedasticity and allow for serial correlation through
clustering by firms. \* p \< 0.10; \*\* p \< 0.05; \*\*\* p \< 0.01.

**\[Statement of results, implications\]**

> With public science funding under threat both in the United States and
> globally, the paper's findings could mislead policymakers on the
> importance of public science for the private sector given the
> credibility issues with the empirical design. The paper's findings
> effectively imply that the research function of universities is, if
> anything, negative for the private sector. Given that the only
> positive relationship between university research activity and firm
> outcomes is found in the graduation of new PhDs, the policy
> implications of this paper taken at face value would imply that
> universities should prioritize training PhDs while simultaneously
> cutting back on university invention. Given that universities conduct
> the bulk of all basic scientific research, such a reorientation of
> university priorities should not arise without more credible evidence.

Our results do not show that university research harms the private
sector; they highlight nuanced differences in *how* various university
outputs relate to firm outcomes in the case of large, publicly traded
firms. The suggestion that universities should prioritize PhD training
over invention is a policy judgment that goes well beyond what our data
support. Specifically, it is plausible that university inventions are
the basis for entrepreneurial startups. We do not analyze the innovation
activity of such startups. Instead, our findings highlight the nuanced
role of different university outputs, including PhD training, in
supporting large-firm innovation.

## Evaluator 2: Ioannis Bournakis

"*From "Research Quality (Additional Comments)"*

> The paper develops a systematic framework for analysing how public
> science capital affects corporate R&D, leveraging rich firm level data
> and extensive robustness checks to support credible causal inference.
> My main question is whether this instrumental variables strategy
> offers clear advantages over a difference-in-differences design.
>
> The paper investigates how three components of public
> science---abstract knowledge (publications), human capital (PhD
> scientists), and public inventions (university patents)---affect
> corporate R&D, distinguishing upstream (research) from downstream
> (invention) activities within a simple profit-maximization framework
> that posits public knowledge and human capital lower the marginal cost
> of internal invention while public inventions may either serve as
> inputs or compete with firm generated inventions. Drawing on a novel
> firm-level panel of U.S. publicly traded, R&D-performing firms
> (1980--2015) linked to Compustat, PatentsView, Dimensions grant
> acknowledgments, ProQuest dissertations, and the AMWS directory, the
> authors measure firm-relevant public science via exposure-weighted
> stocks of non-corporate publications, dissertation-patent textual
> similarity, and university patents. To address endogeneity, they
> construct Bartik-style instruments based on exogenous shifts in
> federal agency R&D budgets---predicted by the partisan composition of
> House and Senate appropriations subcommittees---interacted with
> firm-specific exposure shares. They find that "pure" public knowledge
> (journal publications) has little to no effect on corporate patents,
> publications, or hiring of top scientists, indicating limited
> non-rival spillovers; by contrast, a one-standarddeviation increase in
> relevant PhD dissertations boosts firm patents by 53%, publications by
> 22%, and AMWS scientist employment by 9%, while a similar rise in
> university patents reduces firm patents by 51%, publications by 33%,
> AMWS hiring by 8%, and lowers profits---evidence that public
> inventions largely substitute for and compete with corporate R&D.
> Technology-frontier firms benefit more from human capital and less
> from public inventions, whereas follower firms---especially in the
> life sciences---are more responsive to public inventions and
> knowledge. These results challenge the notion of public science as a
> pure public good, highlighting that only excludable, rivalrous outputs
> (people and patents) drive private innovation, and they underscore the
> need to consider the competitive effects of university
> commercialization. My report applauds the papers rigorous causal
> strategy and rich data integration while suggesting robustness
> checks---such as a differencein-differences design---and
> clarifications on model specifications (e.g., inclusion of level
> dummies in interaction regressions, treatment of firm versus time
> subscripts, and the potential role of an international knowledge
> frontier)---refinements that could further enhance \[and strengthen\]
> insights into the relationship between public investment and corporate
> innovation.

We are sincerely grateful for Dr. Bournakis's clear and thoughtful
summary of the paper, as well as for his generous and constructive
suggestions for improvement. The interpretation of our framework and
findings is both accurate and nuanced, and we appreciate the effort to
situate the results within broader questions about the nature of public
science and its competitive effects.

We are particularly encouraged by Dr. Bournakis's recognition of the
paper's empirical strategy and data integration, and we welcome the
specific suggestions regarding robustness checks and model
clarifications. These are helpful and well taken. We have addressed each
of these points in detail below and believe that incorporating them will
improve the clarity and rigor of the paper.

***1. Claims, Strength, and Characterization of Evidence***

> The paper clearly states its primary research question: How do
> different aspects of public science influence corporate innovation
> activities? The approach is grounded in a thorough theoretical
> framework and supported by strong empirical evidence. The empirical
> strategy addresses potential endogeneity bias between corporate
> innovation activities and public knowledge, primarily by leveraging
> political shifts affecting agency R&D budgets. Although tackling
> (unobserved) endogeneity bias is an extremely challenging task in
> economics research, the authors' attempt demonstrates a level of
> credibility that likely outweighs the potential limitations of the
> chosen approach. Providing results that establish causal inference
> adds significant value to the paper and strengthens the robustness of
> its empirical findings.

We thank Dr. Bournakis for his generous and encouraging comments. We
especially appreciate the recognition of both the theoretical grounding
and the empirical strategy. Addressing endogeneity in this context is
indeed challenging, and we're grateful that Dr. Bournakis found our
identification approach---leveraging political variation in agency R&D
budgets---credible and well motivated. We agree that establishing causal
inference in this setting adds important value, and we've worked
carefully to ensure the analysis is transparent and robust throughout.

***2. Methods: Justification, Reasonableness, Validity, Robustness***

> The paper applies an instrumental variables (IV) estimation to
> identify the causal impacts of public science on corporate innovation.
> Specifically, it uses a Bartik-style shift-share IV, where the
> "shifts" are changes in federal agency R&D budgets, expected to
> represent exogenous shocks driven mainly by the political composition
> of Congress. The "shares" are firm-specific exposures based on past
> patenting activity, publications, or dissertation overlaps. The
> validity of this instrument depends on the assumption that political
> shifts in R&D funding are exogenous to firm-specific innovation
> shocks. Admittedly, this is a reasonable assumption within this
> context, although the presence of weak identification might persist,
> particularly for large firms, especially considering spatial
> dimensions that may be interrelated with the determination of the
> federal budget. The authors are aware of this concern and address it
> by controlling for potential firm size effects through the inclusion
> of lagged R&D stock or annual sales in all relevant specifications.
> This is convincing and sufficient to argue that the presented results
> are not significantly biased, especially given the inherent challenges
> of identifying causal relationships in models of this kind.

We appreciate Dr. Bournakis's close attention to our identification
strategy. As he notes, the core assumption behind our Bartik-style
shift-share instruments---that political shifts in federal R&D budgets
are exogenous to firm-specific shocks---is reasonable but not immune to
challenge, particularly in the presence of large firms with geographic
or political salience. We appreciate his point about potential spatial
correlations and agree that this is an important dimension to consider.

To address this concern, we include lagged firm-level *R&D stock* or
*Sales* in all specifications to account for differences in baseline
size and investment capacity. However, as Evaluator 1 rightly notes,
such controls *may* introduce their own bias. To test robustness, we
therefore re-estimate our models excluding these controls (as reported
in Table 1 above).

Table 2 presents another approach: 2SLS results after dropping either
the largest firms in our sample (Columns 1, 3, 5, and 7) or those with
above-median exposure to federal agencies (Columns 2, 4, 6, and 8). The
estimates remain qualitatively similar. While no empirical design is
without limitations, we believe these checks strengthen the case that
our results are not driven by endogenous selection into agency budget
trends.

**Table 2: Robustness Check: Excluding Large and High Agency Exposure
Firms**

+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+
| **Dependent variable:**      | **(1)          | **(2)         | **(3)            | **(4)            | **(5)         | **(6)        | **(7)         | **(8)         |
|                              | ln             | ln(           | ln(1+            | ln(1+            | ln(1+AMWS     | ln(1+AMWS    | ln(\$1+R&D    | ln(\$1+R&D    |
|                              | (1+Patents)ₜ** | 1+Patents)ₜ** | Publications)ₜ** | Publications)ₜ** | s             | sc           | exp           | exp           |
|                              |                |               |                  |                  | cientists)ₜ** | ientists)ₜ** | enditures)ₜ** | enditures)ₜ** |
+==============================+================+===============+==================+==================+===============+==============+===============+===============+
| **Exposure group**           | Small          | Low exposure  | Small            | Low exposure     | Small         | Low exposure | Small         | Low exposure  |
+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+
| **ln(1+Public invention      | -0.182\*\*\*   | -0.114\*\*\*  | -0.107\*\*\*     | -0.107\*\*\*     | 0.004 (0.009) | -0.002       | -0.259\*\*    | -0.194\*      |
| stock)ₜ₋₁**                  | (0.025)        | (0.029)       | (0.022)          | (0.024)          |               | (0.013)      | (0.117)       | (0.105)       |
+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+
| **ln(1+Human capital)ₜ₋₁**   | 0.086\*\*\*    | 0.260\*\*\*   | 0.046\*\*        | 0.103\*\*\*      | -0.003        | 0.047\*\*    | 0.124 (0.105) | 0.203 (0.126) |
|                              | (0.028)        | (0.044)       | (0.021)          | (0.028)          | (0.010)       | (0.018)      |               |               |
+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+
| **ln(1+Public knowledge      | -0.007 (0.018) | 0.017 (0.016) | -0.074\*\*\*     | -0.007 (0.013)   | 0.006 (0.011) | 0.016\*\*    | -0.010        | 0.074\*       |
| stock)ₜ₋₁**                  |                |               | (0.018)          |                  |               | (0.007)      | (0.051)       | (0.043)       |
+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+
| **ln(\$1+R&D stock)ₜ₋₁**     | 0.115\*\*\*    | 0.165\*\*\*   | 0.056\*\*\*      | 0.137\*\*\*      | 0.006 (0.009) | 0.022        | ---           | ---           |
|                              | (0.019)        | (0.021)       | (0.016)          | (0.022)          |               | (0.014)      |               |               |
+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+
| **ln(\$1+Sales)ₜ₋₁**         | ---            | ---           | ---              | ---              | ---           | ---          | 0.117\*\*\*   | 0.180\*\*\*   |
|                              |                |               |                  |                  |               |              | (0.020)       | (0.029)       |
+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+
| **Year FE**                  | Yes            | Yes           | Yes              | Yes              | Yes           | Yes          | Yes           | Yes           |
+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+
| **Firm FE**                  | Yes            | Yes           | Yes              | Yes              | Yes           | Yes          | Yes           | Yes           |
+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+
| **Mean DV**                  | 3.79           | 19.36         | 1.80             | 13.07            | 0.82          | 4.27         | 13.36         | 115.01        |
+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+
| **Weak id.                   | 48.83          | 84.62         | 48.83            | 84.62            | 2.34          | 8.52         | 47.78         | 72.19         |
| (Kleibergen--Paap)**         |                |               |                  |                  |               |              |               |               |
+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+
| **Firms**                    | 2,250          | 2,341         | 2,250            | 2,341            | 2,341         | 2,341        | 2,038         | 2,128         |
+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+
| **Observations**             | 20,409         | 21,728        | 20,409           | 21,728           | 20,409        | 21,728       | 17,358        | 18,574        |
+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+
| **Adjusted R²**              | 0.11           | 0.03          | 0.23             | 0.01             | 0.01          | 0.00         | 0.32          | 0.02          |
+------------------------------+----------------+---------------+------------------+------------------+---------------+--------------+---------------+---------------+

***Notes****:* This table presents the main estimation results (2SLS) in
two different subsamples. Columns 1, 3, 5, and 7 use a subsample of
firms with below-median annual sales (compared to other firms in the
same 4-digit SIC industry over the sample period of 1985-2015). Columns
2, 4, 6, and 8 use a subsample of firms with below-median agency
exposure shares (compared to other firms in the same 4-digit SIC
industry over the sample period of 1985-2015). Standard errors (in
parentheses) are robust to arbitrary heteroskedasticity and allow for
serial correlation through clustering by firms. \* p \< 0.10; \*\* p \<
0.05; \*\*\* p \< 0.01.

***\[Difference in differences (suggested approach)\]***[^2]

> Nonetheless, I would like to suggest that the authors consider whether
> a difference-in-differences (DiD) approach could also be used to
> address the endogeneity bias between public knowledge and inhouse
> innovation efforts. I do not claim that a DiD approach would
> necessarily outperform the strategy they have already employed, but it
> could serve as an additional robustness check. For example, one could
> identify a subset of firms more exposed to changes in public science
> funding (e.g., firms active in fields funded by certain agencies) and
> another subset less exposed, and then compare their innovation
> outcomes before and after the shocks, assuming the timing of R&D
> budget changes is exogenous. From the top of my head, one could think
> of firms heavily linked to NASA subfields versus those linked to the
> Department of Agriculture. This could be an interesting extension if
> the firm panel allows for such an analysis.
>
> *In any case, the current identification strategy has strong merits
> and mitigates endogeneity concerns in a reasonable and convincing
> manner.*

We thank Dr. Bournakis for this thoughtful suggestion. A
difference-in-differences (DiD) design exploiting variation in agency
exposure---such as comparing firms linked to NASA versus those tied to
the Department of Agriculture---could indeed provide a useful robustness
check. We are currently exploring this possibility.

That said, our empirical goal is not to estimate the effect of agency
R&D budgets on firm innovation directly, but rather to isolate the
causal impact of changes in each of the three components of public
science: *publications, PhD training, and university patents*. Because
these components are jointly shaped by budget shifts---yet differ in
timing, diffusion, and impact---finding a single exogenous event that
moves all three in parallel and with sufficient intensity is
challenging. We are continuing to investigate whether a DiD design can
be adapted to meet these criteria and appreciate Dr. Bournakis's
suggestion as a productive direction for future work.

***3. Overall Assessment: Contribution to Knowledge and Practice***

> This paper presents a significant and well-executed empirical study
> examining how public science, in its various dimensions, affects
> corporate research and development (R&D). The authors distinguish
> between three key components of public science: abstract knowledge
> (e.g., scientific publications), human capital (e.g., PhD scientists),
> and public inventions (e.g., university patents). Their findings that
> corporate R&D is driven more by embodied knowledge in human capital
> and inventions than by abstract knowledge itself offers important
> insights for science policy and innovation management.
>
> The study contributes to our understanding of how knowledge transfer
> mechanisms operate in practice and challenges conventional wisdom that
> treats public science primarily as a non-rival, purely
> spillover-driven input to private innovation. By leveraging firm-level
> exposure to exogenous shifts in federal R&D budgets tied to political
> subcommittee composition, the paper advances causal inference in this
> domain. Its nuanced implications---for example, the crowding-out
> effect of public invention on corporate R&D---are particularly
> relevant in an era of increasing university-industry partnerships and
> policy attention to innovation ecosystems.

We are grateful to Dr. Bournakis for his generous and clear summary of
the paper's core contributions. His interpretation aligns closely with
our goals: to unpack the distinct roles of abstract knowledge, human
capital, and public invention in shaping firm-level innovation activity,
and to challenge the simplifying assumption that public science
uniformly operates as a non-rival input. We especially appreciate his
recognition of the paper's effort to advance causal inference in a
domain where endogeneity is notoriously difficult to address, as well as
his engagement with the policy relevance of our findings. His comments
are both encouraging and motivating as we continue refining the work.

***4. Logic and Communication***

> The goals and questions of the paper are clearly articulated: the
> authors seek to disentangle the distinct effects of public knowledge,
> human capital, and public inventions on corporate innovation
> activities. Key concepts are well defined, and the framework guiding
> the empirical analysis is transparent and logically developed.
>
> Nonetheless, I have some specific queries that I would like to raise.

> **\[4.1\]** In Equation 3.1, is the variable r a stock variable
> (representing cumulative knowledge) or just a flow variable? I am
> aware that later in the paper, the authors treat public knowledge as a
> stock variable using the perpetual inventory method, but in the
> theoretical setup, this is not made explicit. It might be useful for
> the authors to clarify this point clearly from the very beginning.

We thank Dr. Bournakis for flagging this ambiguity. In the theoretical
framework (Section 3.1), *r* represents a flow of internal research
investment by the firm, while *u* denotes a stock of relevant public
knowledge. This distinction mirrors the empirical implementation: we
measure *r* using annual flows such as corporate publications and the
employment of AMWS scientists, while *u* is constructed as a stock of
non-corporate publications using a perpetual inventory method. We will
revise the text in Section 3.1 and rename the stock variables to make
this distinction explicit from the outset.

> **\[4.2\]** Additionally, regarding the function phi in the profit
> maximization problem: could it be subject to constant returns to scale
> (CRS) instead of diminishing returns to scale (DRS)? The authors
> implicitly assume that the productivity of investment falls with
> respect to both human capital and public knowledge. This is my
> understanding based on the setup of the model in Section 3.1, unless I
> am missing something. While this is a conventional assumption, would
> it not also be possible to allow for CRS or even increasing returns to
> scale (IRS) if the use of new knowledge capital (either internal or
> external to the firm) generates spillovers that lead to new ideas at a
> constant or increasing rate? In other words, is there any role for
> unintended spillovers in the model that could counteract the
> diminishing returns assumption? This is just a question and may not be
> crucial for the modelling approach, but it could be worth considering
> or clarifying.

We appreciate Dr. Bournakis raising this point. As he correctly notes,
our baseline model assumes diminishing returns to internal and external
knowledge inputs, consistent with standard formulations of R&D
production functions in the endogenous growth literature. This choice
captures capacity constraints and congestion effects common in
firm-level innovation. That said, the possibility of constant or
increasing returns---particularly through knowledge spillovers---is
theoretically plausible and indeed underpins many macro-level models of
idea generation. Our empirical design allows for such nonlinearities
somewhat indirectly: by examining how firms respond differently to
public science depending on their absorptive capacity and technological
position, we partly capture variation in marginal returns. We will
clarify this modeling choice in the revised Section 3.1 and explicitly
note the possibility of alternative returns-to-scale assumptions as an
avenue for future work.

> **\[4.3\]** Furthermore, I was wondering whether the authors included
> the level dummy for high ability in the regressions of Table 10, since
> they are using the interaction term between public investment and
> human capital. Isn't it the case that these regressions should also
> include the dummy variable itself?

We thank Dr. Bournakis for this helpful observation. Conceptually, we
agree that including the main effect of the high-ability dummy alongside
its interactions with public invention and human capital is important
for interpretation. However, because the high-ability dummy varies
little within firms over time, we lack sufficient within-firm variation
to estimate its level effect precisely in specifications with firm fixed
effects. We will clarify this limitation in the revised manuscript to
avoid any confusion.

> **\[4.4\]** Regarding this point, do we need to report the overall
> effects of the variables of interest (public investment and human
> capital) in Tables 10 and 11 etc, given that they are interacted with
> industry fixed effects, especially in Table 11? Also, why does the
> dependent variable in Tables 10, 11, and 12 include only the time
> subscript but not the firm subscript? Are we missing something here?

We thank Dr. Bournakis for these thoughtful questions. The overall
effects of the variables of interest shown in Table 11 correspond to the
baseline industry category (Other), which is why they are reported
separately despite the interactions with industry fixed effects.

Regarding the dependent variable notation, all regressions in Tables
3--11 are firm-year panel models. We omit the firm subscript in the
dependent variable notation purely for simplicity and readability, while
including the time subscript explicitly to highlight the lag structure
between dependent and independent variables. We will clarify this
notation in the revised manuscript to prevent confusion.

> **\[4.5\]** In Section 3.2.4, the authors distinguish between leaders
> and followers. While the paper specifically focuses on the U.S., I
> would like to raise a question about whether there could also be a
> role for a global frontier instead of just a national frontier, as
> well as the potential impact of international public knowledge
> capital. The authors have deliberately excluded non-U.S. PhDs from the
> empirical analysis. This choice merits further justification. Is this
> decision conceptually meaningful? Is the influence of international
> public knowledge capital on U.S. corporations truly negligible?
> Admittedly, U.S. firms are typically positioned at the international
> technological frontier, but there might be sectors where the U.S. lags
> behind other countries. Have the authors considered these
> possibilities?
>
> Overall, the central point of the paper---that there is a potential
> trade-off between public invention as a competitor versus as an
> input---is carefully and convincingly developed.

We appreciate Dr. Bournakis's important point. Our focus on the U.S.
technological frontier reflects both data constraints and the paper's
conceptual framing around domestic public science and firm innovation.
We excluded non-U.S. PhDs primarily because of data limitations and to
maintain a clear interpretation of exposure to U.S.-based public
knowledge capital, which is directly linked to federal R&D budget
shifts.

We acknowledge that international public knowledge and global frontiers
could matter, especially in certain sectors where U.S. firms may not
lead. However, incorporating these factors poses significant empirical
challenges, including measuring firm-specific international exposures
and disentangling their causal effects from domestic influences. This is
an important avenue for future research, and we will highlight this
limitation in the revised manuscript.

> **5. Replicability, Reproducibility, and Data Integrity**
>
> The paper demonstrates strong adherence to reproducibility standards.
> The dataset---DISCERN--- is publicly available through Zenodo, and the
> variable construction is extensively documented in appendices. The use
> of machine learning (SPECTER) for textual similarity analysis between
> patents and PhD dissertations is clearly explained and appropriately
> validated.
>
> The authors also conduct multiple robustness checks and use
> alternative operationalizations of their key variables (e.g.,
> alternative definitions of public invention using SPECTER-based
> similarity). Data integrity appears solid, with comprehensive coverage
> of firm-level R&D activity over a long time span (1986-2015) and
> linkage across several high-quality data sources, including Compustat,
> PatentsView, Dimensions, and ProQuest. I recommend that the authors
> enhance reproducibility by releasing anonymized intermediate datasets
> and code snippets for key transformations, and by archiving their
> data-processing scripts (e.g., on GitHub). This would enable other
> scholars to leverage the same data pipeline for related research in
> innovation, human capital, and public knowledge.

We appreciate Dr. Bournakis for his thoughtful comments and for
recognizing our efforts to ensure transparency, reproducibility, and
data integrity. We are especially pleased that the documentation of
variable construction and the validation of the SPECTER-based similarity
approach were found to be clear and appropriate.

We share Dr. Bournakis's commitment to open science. If the paper is
accepted for publication, we plan to provide the full replication code
for reported analyses, along with detailed guidelines for data cleaning
and preprocessing. These materials will complement the publicly
available DISCERN dataset and enable other researchers to build on the
data pipeline for related work in innovation, human capital, and public
knowledge.

***6. Relevance to Global Priorities and Usefulness for Practitioners***

> This paper offers valuable insights for both policymakers and
> practitioners concerned with the real-world impacts of public
> investment in science. The finding of this research that public
> inventions may substitute for internal R&D---especially among follower
> firms---has practical implications for how universities license
> technologies and for how governments design innovation policies.
>
> The focus on firm heterogeneity, such as differences between
> technology frontier and follower firms, adds depth and policy
> relevance. Quantitative estimates (e.g., a one standard deviation
> increase in relevant public invention reduces firm patents by 51%)
> provide actionable metrics for prioritization. By highlighting that
> only embodied knowledge (in people or patents) translates into
> corporate R&D investment, the study guides more effective knowledge
> transfer strategies."
>
> In sum, this paper represents a rigorous, transparent, and
> policy-relevant contribution to the field of corporate R&D investment
> and public knowledge capital. It challenges the commonly used
> assumption that there are spillovers from public investment in
> knowledge, systematically exploring the hypothesis of whether there is
> complementarity or substitutability between public investment and
> in-house innovation activity. This approach provides a more refined
> understanding of how public investment in research shapes
> private-sector innovation, which remains among the most important
> sources of economic growth.

We thank Dr. Bournakis for his generous and thoughtful assessment. We
are especially encouraged by his recognition of the paper's potential to
inform science and innovation policy, particularly with respect to
university licensing practices and the design of public R&D programs.

We agree that distinguishing between technology frontier and follower
firms, and measuring differential responses to public science, is
essential for understanding how public investment shapes private
innovation. We also appreciate Dr. Bournakis's point that the paper
challenges conventional assumptions about non-rival spillovers from
public knowledge. By showing that only embodied and excludable forms of
public science---such as people and patents---affect the behavior of
large, publicly listed firms, the study aims to contribute to a more
realistic foundation for policy design. In particular, our results
suggest that policy may be more effective if it focuses not only on what
the U.S. government funds, but also on how university scientists are
incentivized when producing knowledge, training PhDs, and generating
inventions.

In conclusion, we thank the two evaluators and *The Unjournal* editorial
team for their thoughtful and helpful engagement with our work.

Sincerely,

Ashish Arora, Sharon Belenzon, Larisa Cioaca, Lia Sheer, and Hansen
Zhang

[^1]: Unjournal manager: bracketed headings added

[^2]: Unjournal Manager: Added bracketed headers\
