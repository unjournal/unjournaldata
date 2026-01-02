---
article:
  doi: 10.21428/d28e8e57.072621d7/97c1c625
  elocation-id: e1pharmpricing
author:
- Evaluator 1
bibliography: /tmp/tmp-43Ob51T9DMbGka.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 30
  month: 06
  year: 2025
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 1 of "Pharmaceutical Pricing and R&D as a Global
  Public Good"
uri: "https://unjournal.pubpub.org/pub/e1pharmpricing"
---

# Abstract 

This paper provides a comprehensive analysis of pharmaceutical research
and development (R&D) as a global public good, highlighting the
contributions made by various countries. It successfully gathers
valuable data and employs innovative methods to calculate marginal
costs. However, the empirical approach could be improved by addressing
omitted variable bias and incorporating general equilibrium effects.
Furthermore, the conceptual framework could be broadened to include
dynamic factors and supply-side considerations.

# Summary Measures

We asked evaluators to give some overall assessments, in addition to
ratings across a range of criteria. *See the *[*evaluation summary
"metrics"*](https://unjournal.pubpub.org/pub/evalsumpharmpricing#metrics "null")*
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
| **Overall         | 51/100            | 3 |
| assessment **     |                   | 5 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 6 |
|                   |                   | 5 |
+-------------------+-------------------+---+
| **Journal rank    | 2.0/5             | 1 |
| tier, normative   |                   | . |
| rating**          |                   | 0 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 3 |
|                   |                   | . |
|                   |                   | 0 |
+-------------------+-------------------+---+

**Overall assessment **(See footnote[^2])

**Journal rank tier, normative rating (0-5): ** On a 'scale of
journals', what 'quality of journal' should this be published in?[^3]
*Note: 0= lowest/none, 5= highest/best. *

# Claim identification and assessment 

## I. Identify the most important and impactful factual claim this research makes[^4] {#i-identify-the-most-important-and-impactful-factual-claim-this-research-makes}

"For these reasons, US officials could raise these issues at
international negotiations and advocate for higher prices than presently
set in high-income ROW 35 countries. A multi-country agreement in this
direction would represent a serious effort to support improved world
health."

## II. To what extent do you \*believe\* the claim you stated above?[^5] {#ii-to-what-extent-do-you-believe-the-claim-you-stated-above}

The paper's recommendation to push for higher prices in the rest of the
world is not fully supported from an economic or econometric standpoint.
The empirical analysis is based on a simple linear estimation that fails
to consider potential endogeneity or general equilibrium effects. Since
prices result from market equilibrium, a general equilibrium approach is
necessary to conduct a counterfactual analysis on how changing
contributions across countries would impact prices. Without modeling the
complete market structure, the framework cannot accurately predict how
price increases in the rest of the world would influence global
innovation, access, or welfare.

# Written report

This paper examines the economic factors that drive spending on branded
pharmaceutical products in the United States compared to other OECD
countries, leading to pricing differences across nations.

The authors apply the theory of global public goods to pharmaceutical
research and development (R&D), suggesting that innovative medicines
provide benefits to all countries, and that funding for such innovation
is a shared global responsibility. The paper challenges the idea that
the rest of the world (ROW) completely free-rides on U.S. pharmaceutical
R&D efforts. While recognizing that contributions from ROW are lower
than those from the U.S., the authors find a positive correlation
between a country's GDP and its contributions to R&D.

Moreover, the study highlights that the current independent
contributions from various countries likely result in suboptimal global
R&D investment. The authors suggest that coordinated international
efforts could better align contributions with the global benefits
derived from pharmaceutical innovations, potentially leading to more
efficient and equitable outcomes.

The paper's main contribution to the literature lies in its conceptual
framework. While the authors note that other studies have explored drug
prices through a similar lens, they could more clearly articulate their
unique contribution in relation to previous work.

## Main Comments

1\. **Empirical estimates**. The primary regression analyzed in the
paper is overly simplistic and may be subject to omitted variable bias.
There could be other factors correlated with GDP that are not included
in the model. Therefore, results derived from this model should be
interpreted with caution as the estimated effect of GDP may be
overstated or misattributed. Here are some other important determinants
that may also be relevant:

-   **Healthcare System Structure**: The distinction between private and
    public healthcare systems could significantly impact pharmaceutical
    R&D contributions. For example, countries with predominantly private
    healthcare systems (such as the U.S.) may have different incentives
    and funding structures compared to those with extensive public
    healthcare programs. Including an indicator for public vs. private
    healthcare financing or using an index measuring healthcare system
    characteristics could provide deeper insights.\

-   **Government's Valuation of Health:** A proxy for government
    involvement in healthcare could offer a more informative perspective
    than just out-of-pocket health expenditures. The authors could
    consider incorporating government health expenditures as a
    percentage of GDP or the proportion of healthcare funds allocated to
    preventive care. These measures would better capture the extent to
    which government's value of health influences pharmaceutical
    contributions.\

-   **Regional and Institutional Controls**: OECD countries vary widely
    in terms of regulatory environments, economic structures, and
    healthcare policies. Instead of relying solely on country dummies
    for nations with larger pharmaceutical markets, the authors could
    consider introducing regional fixed effects or clustering countries
    based on relevant institutional criteria. Grouping by continent,
    level of economic development, or healthcare policy regime could
    help account for systematic differences across countries.\

-   **Scale Adjustments** **(Population or GDP per Capita)**: The
    current specification may combine the overall economic size with the
    per capita ability to contribute. The authors should consider
    including population as a control or, alternatively, replacing GDP
    with GDP per capita to determine whether contributions are more
    closely tied to absolute economic output or to individual wealth
    levels. A comparison of the results under both specifications would
    strengthen the paper's conclusions. Additionally, consider the
    possibility of reverse causality. While GDP likely influences
    contributions, it's also possible that higher contributions support
    the pharmaceutical industry, boosting GDP over the long term.\

2\. **Conceptual Framework**. The authors present a conceptual framework
where pharmaceutical innovation is treated as a public good, becoming
non-excludable only after patent expiration. While this is a useful
static framework, there are several aspects that could be explored
further:

-   **Temporary Excludability and Patent Length**: The authors explain
    that information about drugs is considered a public good when it is
    non-rival and non-excludable. The nonexcludable aspect only comes
    into play after a patent expires, which is why the authors discuss
    the concept of temporary excludability. It would be helpful to
    provide some statistics on patent duration.\

-   **Dynamic Considerations**: Since the framework is static, it does
    not explicitly model how contributions evolve across the excludable
    and non-excludable phases. A dynamic model could help illustrate how
    temporary excludability shapes countries' incentives to contribute
    to innovation. For example, do wealthier countries drive innovation
    by purchasing patented drugs while lower-income countries wait for
    generics? Discussing how this period affects firms' incentives to
    invest in R&D-----and how different countries internalize these
    incentives-----would add depth to the framework.

```{=html}
<!-- -->
```
-   **One-Sided Market Assumption**: The current framework focuses on
    the demand side, with country contributions driving innovation.
    However, pharmaceutical pricing and R&D incentives are also shaped
    by supply-side factors, such as production costs, regulatory
    barriers, and firm strategies. Incorporating general equilibrium
    effects or discussing how firm-side incentives interact with
    demand-driven contributions could make the framework more complete.

The paper's recommendation to push for higher prices in the rest of the
world is not fully supported from an economic or econometric standpoint.
The empirical analysis is based on a simple linear estimation that fails
to consider potential endogeneity or general equilibrium effects. Since
prices result from market equilibrium, a general equilibrium approach is
necessary to conduct a counterfactual analysis on how changing
contributions across countries would impact prices. Without modeling the
complete market structure, the framework cannot accurately predict how
price increases in the rest of the world would influence global
innovation, access, or welfare.

## Other comments

1.  The authors note that Turkey, Greece, and Estonia have negative
    contributions. While mathematically possible---given the formula
    used---this raises a question about the real-world plausibility of
    negative contributions. It would be useful for the authors to
    provide a concrete example or further discussion that explains how
    negative contributions might manifest in practice. This would help
    clarify the conceptual implications and improve the understanding of
    how countries with negative contributions might appear in the
    context of the model.\

2.  If the goal is to present this as an economics paper, as it is an
    NBER working paper, I recommend structuring it to align more closely
    with the conventions of the field. Specifically, Sections II and III
    provide valuable background information and could be consolidated.
    Sections IV through VII appear to form the core conceptual framework
    and can be grouped accordingly. Sections IX and A (which may be a
    subsection, though it's unclear) contribute to the data section by
    detailing the construction of key variables, while Section III
    presents descriptive statistics. Section X serves as the main
    empirical analysis and follows a more conventional structure.

# Evaluator details

1.  How long have you been in your field of expertise?

    -   6 years

2.  How many proposals, papers, and projects have you evaluated/reviewed
    (for journals, grants, or other peer-review)?

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
