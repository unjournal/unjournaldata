---
affiliation:
- id: 0
  organization: Toulouse School of Economics
article:
  doi: 10.21428/d28e8e57.2fff95a6/2abe3074
  elocation-id: e2technologicalrisks
author:
- Yassin Alaya
bibliography: /tmp/tmp-462EFyWGGU8NGk.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 01
  month: 07
  year: 2024
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 2 of "The Returns To Science In The Presence Of
  Technological Risks", Applied Stream
uri: "https://unjournal.pubpub.org/pub/e2technologicalrisks"
---

# Summary assessment

*Evaluation manager's note: *The ratings used below come from our
general 'academic stream' template and
[guiidelines](https://globalimpact.gitbook.io/the-unjournal-project-and-communication-space/policies-projects-evaluation-workflow/evaluation/guidelines-for-evaluators "null").
We are evaluating this work as part of our applied/policy stream;
however, we failed to communicate this carefully to the evaluator.

This evaluator was specifically asked to "critically assess the modeling
choices re discounting, economic parameters, etc."

+---------------------------------+---+---+
| **Criterion (see note above)**  | * | * |
|                                 | * | * |
|                                 | P | C |
|                                 | e | I |
|                                 | r | * |
|                                 | c | * |
|                                 | e |   |
|                                 | n |   |
|                                 | t |   |
|                                 | i |   |
|                                 | l |   |
|                                 | e |   |
|                                 | r |   |
|                                 | a |   |
|                                 | n |   |
|                                 | k |   |
|                                 | i |   |
|                                 | n |   |
|                                 | g |   |
|                                 | * |   |
|                                 | * |   |
+=================================+===+===+
| Advancing our knowledge and     | 6 | 3 |
| practice                        | 5 | 0 |
|                                 |   | - |
|                                 |   | 1 |
|                                 |   | 0 |
|                                 |   | 0 |
+---------------------------------+---+---+
| Justification, reasonableness,  | 6 | 4 |
| validity, robustness            | 0 | 5 |
|                                 |   | - |
|                                 |   | 7 |
|                                 |   | 5 |
+---------------------------------+---+---+
| Logic and communication         | 5 | 3 |
|                                 | 0 | 0 |
|                                 |   | - |
|                                 |   | 7 |
|                                 |   | 0 |
+---------------------------------+---+---+
| Open, collaborative, replicable | 6 | 3 |
| science                         | 0 | 5 |
|                                 |   | - |
|                                 |   | 8 |
|                                 |   | 5 |
+---------------------------------+---+---+
| Real-world relevance            | 7 | 5 |
|                                 | 0 | 0 |
|                                 |   | - |
|                                 |   | 9 |
|                                 |   | 0 |
+---------------------------------+---+---+
| Relevance to global priorities  | 9 | 8 |
|                                 | 0 | 0 |
|                                 |   | - |
|                                 |   | 1 |
|                                 |   | 0 |
|                                 |   | 0 |
+---------------------------------+---+---+
|                                 | * |   |
|                                 | * |   |
|                                 | J |   |
|                                 | o |   |
|                                 | u |   |
|                                 | r |   |
|                                 | n |   |
|                                 | a |   |
|                                 | l |   |
|                                 | t |   |
|                                 | i |   |
|                                 | e |   |
|                                 | r |   |
|                                 | * |   |
|                                 | * |   |
|                                 | [ |   |
|                                 | ^ |   |
|                                 | 1 |   |
|                                 | ] |   |
+---------------------------------+---+---+
| What journal ranking tier       | 4 | 3 |
| should this work be published   | . | - |
| in?                             | 5 | 5 |
+---------------------------------+---+---+
| What journal ranking tier will  | 2 | 0 |
| this work be published in?      |   | - |
|                                 |   | 4 |
+---------------------------------+---+---+

# Paper summary[^2]

'The Returns To Science In The Presence Of Technological Risks' by Matt
Clancy considers whether the benefits of science outweigh its risks by
modelling the welfare effects of globally pausing science for one year.
The benefits considered are increases in per capita income and a
decreasing mortality rate. The risks are advances in biotechnology which
might enable malicious actors to create dangerous pathogens. These risks
are modelled as an increased rate of mortality due to more frequent,
more severe pandemics and as a risk of extinction due to a pandemic
killing the entire human population.

In a model without extinction risk, the benefits of science strongly
outweigh the risks. It thus seems that the qualitative result\[s\] when
ignoring the possibility of science increasing extinction risk are not
sensitive to parameter choices. When extinction risk is accounted for,
the conclusions depend on how valuable one reckons the possible future
of humanity (which would be lost due to extinction) to be.

In this evaluation I focus on the choice of model parameters. To
introduce the parameters, I briefly summarise the report's model.
Welfare effects are computed based on the following infinite period
model:

$$V= \sum_{t=0}^\infty p^t n_t u(y_t)$$

Here, $y_t$ is per capita income in year $t$, $u(y_t)$ is the utility
experienced by an individual alive in a year in which per capita income
is $y_t$ and $n_t$ is the population size in year $t$. $p$ is a discount
factor (see discussion below). $y_t$ grows at rate $G$ each year. If
science is paused now, the income growth temporarily drops to $g$ in $T$
years before growing again at $G$ afterwards. Population size $n_t$
grows at a constant rate $s$ until in $t_1$ years, the \"time of
perils\" commences and population growth is reduced to $s-d$, where $d$
represents excess mortality due to the perils of biotechnology. When
science is paused for one year, this time of perils commences one year
later than it otherwise would have. \[...\] the constancy of the
population growth rate at $s$ (or $s-d$ during the time of perils) is
based on the assumption that the birth rate and the mortality \[rate\]
move in lockstep. However, pausing science for one year temporarily
slows the decline of the mortality rate attributable to scientific
progress after $T$ years without affecting the birth rate. The result is
a permanent decline in the net population growth rate to $\bar s$.

The returns to science in this baseline model are large and positive and
remain large when science's effect on health are modeled more
realistically in section 6. In section 8, a version of the model with
extinction risk is considered, where there is an annual extinction risk
of $d_x$ applying during the time of perils. Section 9 considers an
extension where science reduces both $d$ and $d_x$.

# General comments[^3]

While it is unsurprising that the version of the model without
extinction risk stipulates large returns to science that are almost
unaffected by the time of perils (see the results of the modified model
in section 6), an important contribution of the report is to establish a
threshold \[that\] the value of the future of humanity must exceed to
warrant pausing science when science contributes to extinction risk
(section 8). An important result is also the threshold \[that\] the
annual reduction in extinction risk due to science has to exceed in
order for the net impact of science (after accounting for the fact that
science also \[may\] bring about the time of perils) to be positive.

Overall, the methodology of the paper is transparent and well explained.
The author appropriately balanced tractability with realistic modelling.
The author considers a number of extensions to his baseline model that
address particular considerations. However some considerations are left
out of the model, e.g. animal welfare (the current value of humanity
might be negative because of factory farming) and how utility depends on
the total population size (in the current model, the flow value is
proportional to the population size). There may be minor flaws in
arguing for certain parameter choices (see my comments on parameter
choices below).

# Comments on parameter choices

The author carefully justifies his choice of parameters, making
reference to the academic literature as well as to forecasts of
superforecasters and experts who participated in the Existential Risk
Persuasion Tournament (XPT). For some parameters (in particular $p$) it
might be worthwhile to conduct robustness checks with alternative
values, at least in the model which includes extinction risk. In the
following, I summarise how the author chooses each parameter and offer
some commentary.

+-----+-------------------------------------------------------------+-------------------------------------------------+---+
| **  |                                                             |                                                 |   |
| Tab |                                                             |                                                 |   |
| le: |                                                             |                                                 |   |
| Par |                                                             |                                                 |   |
| ame |                                                             |                                                 |   |
| ter |                                                             |                                                 |   |
| c   |                                                             |                                                 |   |
| hoi |                                                             |                                                 |   |
| ces |                                                             |                                                 |   |
| and |                                                             |                                                 |   |
| c   |                                                             |                                                 |   |
| omm |                                                             |                                                 |   |
| ent |                                                             |                                                 |   |
| s** |                                                             |                                                 |   |
+=====+=============================================================+=================================================+===+
| La  | Value                                                       | Author's reasoning                              | C |
| bel |                                                             |                                                 | o |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
+-----+-------------------------------------------------------------+-------------------------------------------------+---+
| $G$ | $1\%$                                                       | The author first reasons with reference to the  | I |
|     |                                                             | economic literature that the past growth trend  | f |
|     |                                                             | of $2\%$ was in part due to temporary factors   | t |
|     |                                                             | and only $1\%$ was due to scientific progress.  | h |
|     |                                                             | He thus chooses $G=1\%$ but then states: 'An    | e |
|     |                                                             | additional $1\%$ likely will come from other    | a |
|     |                                                             | factors, but since this growth is baked in, we  | u |
|     |                                                             | can usually ignore it when comparing            | t |
|     |                                                             | counterfactual policies'                        | h |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | 2 |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | % |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | 2 |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | % |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | ? |
|     |                                                             |                                                 | T |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | T |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | 1 |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | % |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | ' |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | k |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | ' |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | 1 |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | % |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | . |
+-----+-------------------------------------------------------------+-------------------------------------------------+---+
| $g$ | $0.75\%$                                                    | This number is obtained \[...\] based on the    | T |
|     |                                                             | number of patents that directly or indirectly   | h |
|     |                                                             | rely on science and how important science       | e |
|     |                                                             | plausibly is for a patent's contribution to     | a |
|     |                                                             | economic growth.                                | r |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | I |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | [ |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | ] |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | x |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | - |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | ? |
|     |                                                             |                                                 | I |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | = |
|     |                                                             |                                                 | 0 |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | . |
+-----+-------------------------------------------------------------+-------------------------------------------------+---+
| $d$ | $0.0021\%$ and $0.0385\%$                                   | The author infers annual probabilities of       | T |
|     |                                                             | pandemics in different bins of severity from    | h |
|     |                                                             | superforecasters' and domain experts'           | e |
|     |                                                             | subjective probabilities of such pandemics      | a |
|     |                                                             | occurring over different time horizons and      | u |
|     |                                                             | combines these probabilities with guesses of    | t |
|     |                                                             | mortality rates for each bin. (E.g. he assumes  | h |
|     |                                                             | that pandemics killing $1-10\%$ of the          | o |
|     |                                                             | population kill $2\%$ on average.)              | r |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | k |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | 0 |
|     |                                                             |                                                 | - |
|     |                                                             |                                                 | 1 |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | % |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | 0 |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | H |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | , |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | k |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | ( |
|     |                                                             |                                                 | E |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | C |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | k |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | 1 |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | % |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | ) |
|     |                                                             |                                                 | I |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | , |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | z |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | , |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | ' |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | x |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | ' |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | , |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | , |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | x |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | . |
+-----+-------------------------------------------------------------+-------------------------------------------------+---+
| $p$ | $0.98$                                                      | This discount factor is not intended to         | I |
|     |                                                             | discount the utility of future generations      | a |
|     |                                                             | relative to today's utility. Instead, it aims   | g |
|     |                                                             | to account for the chance that general          | r |
|     |                                                             | conditions change so fundamentally that our     | e |
|     |                                                             | expectation of the impact of pausing science on | e |
|     |                                                             | flow utility becomes $0$. This change in        | w |
|     |                                                             | 'epistemic regime' is brought about by factors  | i |
|     |                                                             | unrelated to whether science is paused or not.  | t |
|     |                                                             | The author computes this probability as the sum | h |
|     |                                                             | of an annual probability of transformative AI   | t |
|     |                                                             | ($1.6\%$), a major economic break ($0.3\%$),    | h |
|     |                                                             | and extinction risk from causes other than AI   | e |
|     |                                                             | ($0.08$), yielding a discount rate of           | a |
|     |                                                             | $\approx 2 \%$.                                 | u |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | ' |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | T |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | F |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | , |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | [ |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | ] |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | X |
|     |                                                             |                                                 | P |
|     |                                                             |                                                 | T |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | 1 |
|     |                                                             |                                                 | 5 |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | % |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | z |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | x |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | A |
|     |                                                             |                                                 | I |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | ' |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | j |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | T |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | 0 |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | 0 |
|     |                                                             |                                                 | 5 |
|     |                                                             |                                                 | - |
|     |                                                             |                                                 | 0 |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | 7 |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | % |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | H |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | ' |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | X |
|     |                                                             |                                                 | P |
|     |                                                             |                                                 | T |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | k |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | 2 |
|     |                                                             |                                                 | 1 |
|     |                                                             |                                                 | 0 |
|     |                                                             |                                                 | 0 |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | [ |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | ] |
|     |                                                             |                                                 | , |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | x |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | ' |
|     |                                                             |                                                 | H |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | , |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | 2 |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | % |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | 1 |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | 6 |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | % |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | A |
|     |                                                             |                                                 | I |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | O |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | P |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | W |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | ' |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | A |
|     |                                                             |                                                 | G |
|     |                                                             |                                                 | I |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | * |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | 2 |
|     |                                                             |                                                 | 0 |
|     |                                                             |                                                 | 4 |
|     |                                                             |                                                 | 3 |
|     |                                                             |                                                 | * |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | H |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | j |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 |   |
|     |                                                             |                                                 | B |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | , |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | x |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | x |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | k |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | ( |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | ) |
|     |                                                             |                                                 | , |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | x |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | k |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | A |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | X |
|     |                                                             |                                                 | P |
|     |                                                             |                                                 | T |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | ' |
|     |                                                             |                                                 | j |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | [ |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | \ |
|     |                                                             |                                                 | ] |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | x |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | k |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | k |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | x |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | k |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | 8 |
|     |                                                             |                                                 | . |
|     |                                                             |                                                 | I |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | k |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | v |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | $ |
|     |                                                             |                                                 | . |
+-----+-------------------------------------------------------------+-------------------------------------------------+---+
| $d  | $0.00016\%$ and $0.02286\%$                                 | Inferred from XPT participants' beliefs about   | T |
| _x$ |                                                             | the probability of extinction through a         | h |
|     |                                                             | pandemic.                                       | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | p |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | g |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | w |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | d |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | f |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | y |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | b |
|     |                                                             |                                                 | u |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | o |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | x |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | l |
|     |                                                             |                                                 | r |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | k |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | h |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | t |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | i |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | n |
|     |                                                             |                                                 | c |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | m |
|     |                                                             |                                                 | a |
|     |                                                             |                                                 | k |
|     |                                                             |                                                 | e |
|     |                                                             |                                                 | s |
|     |                                                             |                                                 | . |
+-----+-------------------------------------------------------------+-------------------------------------------------+---+
| $T$ | $74$                                                        | see paper                                       |   |
+-----+-------------------------------------------------------------+-------------------------------------------------+---+
| $s$ | $0.6\%$                                                     | see paper                                       |   |
+-----+-------------------------------------------------------------+-------------------------------------------------+---+
| $\  | $0.5967\%$                                                  | see paper                                       |   |
| bar |                                                             |                                                 |   |
|  s$ |                                                             |                                                 |   |
+-----+-------------------------------------------------------------+-------------------------------------------------+---+
| $t  | $17-18$ years                                               | see paper                                       |   |
| _1$ |                                                             |                                                 |   |
+-----+-------------------------------------------------------------+-------------------------------------------------+---+

[^1]: M

[^2]: Manager's note: We make some small typographic edits below. Where
    these are not trivial, we spell them out in square brackets. We also
    added some additional paragraph spacing and formatting changes, not
    noted.

[^3]: Manager's note: We make some small typographic edits below,
    spelling these out in square brackets.
