---
affiliation:
- id: 0
  organization: London School of Economics
article:
  elocation-id: e2welfareclimatechange
author:
- Frank Venmans
bibliography: /tmp/tmp-59IENIB5aehJKf.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 23
  month: 05
  year: 2025
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 2 of "A Welfare Analysis of Policies Impacting Climate
  Change"
uri: "https://unjournal.pubpub.org/pub/e2welfareclimatechange"
---

# Abstract 

Under which policy does a dollar of subsidy create the largest impact on
welfare? Similarly, under which environmental tax does a dollar \[of
tax\] collected create the lowest impact on welfare? The paper answers
these questions by developing the Marginal Value of Public Funds (MVPF).
This allows \[one\] to rank government policies according to their
welfare impacts while respecting a given government budget.  \
\
The authors convincingly claim that their measure of the MVPF allows for
a better ranking of public policies compared to standard measures of
cost per tonne, be it the Resource cost per tonne, Government cost per
tonne or Social cost per tonne. This is because the MVPF includes the
role of inframarginal transfers which are \[an\] important part of
policies, often of larger magnitude than the externalities that the
policies correct for.\
\
The strong point of the paper is to make the different components of the
impacts of a policy additive and easy to distinguish. The paper builds
on a very large body of literature, and builds on causal inference
\[work published in\] the 18 most relevant economics journals (general
interest journals and environmental economics journals).\
\
The paper has also a novel way of estimating the social value of
learning-by-doing, in a way that requires very \[few\] parameters. This
makes it very policy-relevant. Overall, the paper does an extremely good
job in giving an overview of all the effects of environmental policies
over the last decades.

# Summary Measures

We asked evaluators to give some overall assessments, in addition to
ratings across a range of criteria. *See the *[*evaluation summary
"metrics"*](https://unjournal.pubpub.org/pub/evalsumwelfareclimatechange#metrics "null")*
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
| assessment **     |                   | 5 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 9 |
|                   |                   | 4 |
+-------------------+-------------------+---+
| **Journal rank    | 4.9/5             | 4 |
| tier, normative   |                   | . |
| rating**          |                   | 7 |
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

# Written report[^4]

> Under which policy does a dollar of subsidy create the largest impact
> on welfare? Similarly, under \[which\] environmental tax does a dollar
> collected \[...\] create the lowest impact on welfare? The paper
> answers these questions by developing the Marginal Value of Public
> Funds (MVPF). This allows \[one\] to rank government policies
> according to their welfare impacts while respecting a given government
> budget.
>
> The authors convincingly claim that their measure of the MVPF allows
> for a better ranking of public policies compared to standard measures
> of cost per tonne, be it the Resource cost per tonne, Government cost
> per tonne or Social cost per tonne. This is because the MVPF includes
> the role of inframarginal transfers which are important part of
> policies, often of larger magnitude than the externalities that the
> policies correct for.
>
> The strong point of the paper is to make the different components of
> the impacts of a policy additive and easy to distinguish. The paper
> builds on a very large body of literature, and builds on causal
> inference from the 18 most relevant economics journals (general
> interest journals and environmental economics journals).
>
> The paper has also a novel way of estimating the social value of
> learning by doing, in a way that requires very \[few\] parameters.
> This makes it very policy-relevant. Overall, the paper does an
> extremely good job in giving an overview of all the effects of
> environmental policies over the last decades.

Having done many environmental assessments myself, the results look very
robust and reasonable. I have three minor remarks or reflections on the
study.

### **1. Discuss more in detail the role of the shadow price of the government's budget constraint.**[^5] {#discuss-more-in-detail-the-role-of-the-shadow-price-of-the-governments-budget-constraint}

The authors set up the problem \[...\] as the solution for a government
which maximizes welfare W (the sum of utility over all individuals,
possibly weighted by some justice measure) subject to a budget
constraint. Hence it would be useful to explicitly write the Lagrangian
of the government in the paper, which is

$$L=W + \lambda B$$

with $ \lambda $ the shadow price of the government's budget constraint
and B the difference between income and expenditures of the government
(or equivalently a cap on government bonds).

Assuming for simplicity a single representative agent with marginal
utility $u'$, the marginal welfare effect of a policy which is
continuous in a policy measure p is

$$dL/dp=WTP*u' + \lambda \frac{dB}{dp}$$

(Secondary remark: in the paper, the $\lambda$ denotes the marginal
utility of the individual, which is different from $ \lambda $ here.)

Note that at optimum, the above derivative is zero and the MVPF is
$\lambda/u'$, but we are not at optimum, because the MVPF would be
identical among all policies.

The above equation is the essential equation to test if a policy is
welfare improving or not. It requires \[knowledge of\] the shadow price
of the public funds, $ \lambda $. Yet it is not handy to rank policies,
because some policies use up more funds than others. That is why the
ratio of the cost over the benefits is the focus of the MVPF.

If the policy is a tax, the tax is welfare improving if the ratio of the
cost ($WTP * u'$ ) over the tax gains ( $\lambda \frac{dB}{dp}$) is
below 1. If there is the possibility to raise lump sum taxes, \[then\]
$u'=\lambda$ and the MVPF\<1 is a sufficient condition for a welfare
increasing tax. However, in reality most taxes (or at least the marginal
least advantageous tax) comes with a deadweight loss, so $\lambda>u'$.
This should be discussed better in the paper. The paper does not write
the government Lagrangian, that would be helpful for the reader and to
discuss the role of $\lambda$. In other words, the MVPF is in essence a
cost benefit ratio, where the numerator is the cost of the tax and the
denominator is the benefit, but the shadow prices of these costs and
benefits should be discussed. Similarly for a subsidy the MVPF is the
ratio of the benefit of the subsidy over the cost of the subsidy, where
the shadow prices of both deserve more attention.

For example, consider a Pigouvian tax. The cost benefit ratio is (using
equation 25)

$$\frac{(-1+ \epsilon V/p) u'}{(1+ \epsilon \tau/p) \lambda}$$

Where $\epsilon$ is the elasticity of demand (negative), V is the
externality (negative), p is the price of the fuel and tau is the tax.
Equation 25 shows that for the Pigouvian tax, the welfare cost is
reduced by the reduction in pollution. However, the same reduction in
pollution will also reduce the tax income. As by the definition of a
Pigouvian tax, the tax $\tau$ equals the externality V, the SVPF is
unaltered. However for the cost-benefit ratio that is only the case for
$\lambda=u'$.

The text states that a Pigouvian tax has a MVPF equal to one. The
intuition is that at the optimal level of environmental taxation, there
is no gain from further taxing the pollution, so marginally increasing
the tax is similar to a lump sum tax (no deadweight loss nor welfare
gain) and the MRVT equals 1. That is true if lump sum taxing is possible
so that $u'=\lambda$. However, if lump sum taxing is not possible and
all other taxes have a deadweight loss, we have $\lambda>u'$ and the
Pigouvian tax -even at the optimal level- becomes attractive (MVPF\<1)
because it is the only tax that has no deadweight loss.

### 2. \[CES assumption, learning by doing gains\]

The authors make a very useful and robust contribution in valuing the
learning by doing gains. I think the assumption of a constant elasticity
of substitution requires more attention. Under constant elasticity, the
demand goes to infinity as the price reaches zero. In reality demand
follows an S-shape (for example a logistic shape). For example, once PV
\[photovoltaic\] and wind become cheaper than coal, they may reach 90%
of electricity production, but they will not become infinite, the total
electricity consumption will merely double. This overestimates the
learning by doing estimates. I think the learning by doing estimates are
relatively large for three other reasons, 1) a 2% discount rate is
acceptable but relatively low, 2) the authors ignore exogenous time
trend\[s\] in costs and assume that cost reductions are not the effect
of reduced fixed costs (the authors fully acknowledge this) and 3) the
climate policy is considered to be suboptimal and exogenous. I'll
develop the last point now.\

### 3. \[Climate policy, dynamic effects\] 

An extra solar panel today will make all solar panels in the future
marginally cheaper. The present value of that cost reduction is captured
in the dynamic price effect. However, this will also increase the use of
PV in the future. This does not increase the price advantage for
individual consumers due to the envelope theorem (if consumers optimize,
the marginal benefits equal marginal costs of an extra panel, so
chang\[ing\] the quantity does not affect the consumer surplus). This is
acknowledged by the authors. However, the present value of the
externalities of these extra solar panels are the Dynamic price effect.
Yet the envelope theorem also applies to the externalities in the case
climate policies are optimized. In other words, the installation of the
PV panel does increase the future quantity of PV's, but if climate
policy is optimal, marginal abatement costs equal the social cost of
carbon and therefore changing the quantity of abatement does not result
in welfare gains at the margin. However, when climate policy is below
optimal (which is the case), the dynamic price effect is positive. It is
a bit unclear how the externality V in equation 24 is defined. The
authors only talk about the externality and I assume they use the SCC,
where I would be inclined to use the SCC net of the MAC, as the net
externality.

### **Minor remark\[s\]**

The definition of $t^\ast$ in equation 23 is confusing, because it is
not really time zero (that is, the time of the subsidy, say 2025),
whereas in the boundary of the integral in equation 22 it is time zero.

I was impressed how large the transfers are compared to the
environmental externalities, especially for subsidies. (\$30,000 subsidy
for an extra electric car on the road). That makes the question of the
marginal utility of the winners and losers quite important. Although the
MVPF is designed to exclude this effect, it is worth giving it more
attention in the discussion.

# Evaluator details

1.  How long have you been in this field?

    -   10 years

2.  How many proposals and papers have you evaluated?

    -   50

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

[^4]: Manager: the quoted part of this section repeats the abstract.

[^5]: Headers added by managers/editors
