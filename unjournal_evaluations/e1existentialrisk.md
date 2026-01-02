---
affiliation:
- id: 0
  organization: Chapman University's Argyros School of Business and
    Economics
article:
  elocation-id: e1existentialrisk
author:
- Seth G. Benzell
bibliography: /tmp/tmp-44EyrbN0kiItLa.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 01
  month: 08
  year: 2024
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 1 of "Existential Risk and Growth"
uri: "https://unjournal.pubpub.org/pub/e1existentialrisk"
---

# Abstract 

Authors find: (1) existential risk follows an inverted-u shape in both
technology level and over time, (2) technological accelerations reduce
cumulative existential danger. \
These findings are novel and important, implying a "time of perils"
after which safety is (asymptotically) assured. \
Two critiques: (1) the representative agent of the model is neither a
normative goal nor a positive prediction, making implications nebulous.
(2) omission of savings from the model eliminates a potential mechanism
for intertemporal consumption smoothing, which may impact demand for
safety.

# Summary Measures

We asked evaluators to give some overall assessments, in addition to
ratings across a range of criteria. *See the *[*evaluation summary
"metrics"*](https://unjournal.pubpub.org/pub/evalsumexistentialrisk#metrics "null")*
for a more detailed breakdown of this. See these ratings in the context
of all Unjournal ratings, with some analysis, in our *[*data
presentation
here.*](https://unjournal.github.io/unjournaldata/chapters/evaluation_data_analysis.html#basic-presentation "null")[^1]*
*

+-------------------+---------+---------------------+
|                   | **R     | **90% Credible      |
|                   | ating** | Interval**          |
+===================+=========+=====================+
| **Overall         | 95/100  | 80 - 99             |
| assessment **     |         |                     |
+-------------------+---------+---------------------+
| **Journal rank    | 4.5/5   | 4.2 - 5.0           |
| tier, normative   |         |                     |
| rating**          |         |                     |
+-------------------+---------+---------------------+

**Overall assessment: **We asked evaluators to rank this paper
"heuristically" as a percentile "relative to all serious research in the
same area that you have encountered in the last three years." We
requested they "consider all aspects of quality, credibility, importance
to knowledge production, and importance to practice."

**Journal rank tier, normative rating (0-5): **"On a 'scale of
journals', what 'quality of journal' should this be published in? (See
ranking tiers discussed
[here](https://globalimpact.gitbook.io/the-unjournal-project-and-communication-space/policies-projects-evaluation-workflow/evaluation/guidelines-for-evaluators#journal-ranking-tiers "null"))"
*Note: 0= lowest/none, 5= highest/best".*

*See
*[*here*](https://globalimpact.gitbook.io/the-unjournal-project-and-communication-space/policies-projects-evaluation-workflow/evaluation/guidelines-for-evaluators#metrics-overall-assessment-categories "null")*
for the full evaluator guidelines, including further explanation of the
requested ratings.*

# Written report

## Executive Summary:

Authors find: (1) existential risk follows an inverted-u shape in both
technology level and over time (2), technological accelerations reduce
cumulative existential danger. These findings are novel and important,
implying a "time of perils" after which safety is (asymptotically)
assured. Two critiques: (1) the representative agent of the model is
neither a normative goal nor a positive prediction, making implications
nebulous (2) omission of savings from the model eliminates an alternate
mechanism for intertemporal consumption smoothing

## Full Review

Determining whether and when anthropocentric existential risks will
actually bite is a difficult question for several reasons. One reason is
the difficulty in estimating the 'existential risk damage function'.
Another is human agency - depending on our incentives we might
consciously work to reduce risk and increase safety.

This paper is focused on the second question. It investigates the
dynamics of economic growth existential risk, assuming simple but
plausible analytic forms for output, existential danger, and
representative agent utility. It highlights that, under the assumption
that risk aversion is strong: (1) existential risk follows an inverted-u
shape in both technology level and over time (2), technological
accelerations reduce cumulative existential danger.

I found the paper well written and generally easy to follow. I
especially appreciated the way that section 2 previewed the main results
in a mathematically accessible way. The paper anticipated my desire to
think about a less risk averse planner in section 3.3.4, and a humble
discussion of parameter selection in appendix A1. I will say I found
section 4 somewhat extraneous \-- although I appreciated the intuitive
result that if dot(A) directly and immediately increases danger, with
consumption benefits lagging, that dot(A) increases can be dangerous.

I do have some critiques of some aspects of the model and its
discussion, but overall I find it to make an important contribution to
our understanding of the relationship between economic growth and
existential risk.

## Why do we care about this particular representative agent? Distinguishing the normative and positive content of the model.

From the perspective of any potential optimizing representative agent,
an increase in A is always a good thing for welfare (by beta \> alpha).
The key words being "from the perspective of". The paper's implicit
normative framing is: An existential catastrophe would be exceedingly
bad and we should prefer decision rules that don't produce it. In other
words, the paper doesn't take the goals of the representative agent as
necessarily normative.

On the other hand, the paper only weakly argues that the representative
agent is anything like a positive model of how AI risk decisions will be
made in the real world. While the argument that the wealth induced by AI
will decrease the marginal propensity of consumption and induce
substitution into safety is a generally robust one, the details of
"who's marginal propensity to consume"[^2] is left open \-- is this the
MPC of the median voter in the US? Of the President? Of the average
person globally? The same question holds for the discount rate, which is
also heterogenous. Similarly, "Race" dynamics are likely to be important
between leading labs and countries (Aschenbrenner, 2024)[@ni3q9uatop1],
which would also be hard to model with a single representative agent.
This disconnect between the representative agent and the real world is
worse than the one in Jones (2016), which has a similar model, but is
concerned with individual mortality.

I think the paper could do a better job explaining why these particular
growth/risk paths are interesting if they are neither a positive
prediction nor a normative imperative. I think the authors would say
that the representative agent represents a sort of "idealized
international institution" that a sane hegemon would plausibly sign up
the world for (perhaps in the wake of a successful "The Project"
(Aschenbrenner, 2024)[@nazrd7gp695]).

Whether or not that's the case, in follow-up work it might be useful to
evaluate or contextualize the social planner analyzed according to other
explicit social welfare functions that might be normatively endorsed.
For example:

-   A "hard" utilitarian might choose a gamma with perfect substitution
    between consumption across periods -- so no decreasing marginal
    product of consumption \-- and a discount rate equal to the
    unpreventable existential risk rate

    -   This agent would view the representative agent as much too
        conservative and risk averse

-   An agent who is only trying to minimize existential risk, perhaps
    conditional on some minimum consumption level

    -   This agent would view the representative agent as much too
        incautious

## Is Leaving Capital Out of the Model Harmless?

A second question I have about the modeling is how harmless the
assumption of ignoring capital accumulation is. I have one concern and
one comment related to this.

The concern is that some of the results may be driven by the fact that
"decreasing safety" is the only way to increase immediate consumption in
the model. In real life, we also have the choice of reducing the saving
rate. This additional mechanism might weaken the papers' findings: a
shock to dot(A) increases future wealth in a way that only incentivizes
more safety in the current model. In a more general model with savings,
an increase in dot(A) could instead lead to dissaving in the short term
to smooth consumption between periods, and less of an increase in safety
spending. (I could also see it pushing in the opposite direction, making
future existence more valuable because of the ability to intertemporally
substitute with savings).

A more minor point is that the capital-labor distinction is one of the
major ways that heterogeneity in preferences complicates the
representative agent framework. The advance of AI is likely to increase
the share of income paid to capital and reduce the share paid to labor,
as well as redistributing income between types of workers. Likely, those
who own capital may have lower risk tolerances than those who provide
labor (they are both richer, and may also be more patient in general \--
although a lifetime savings model would suggest, alternatively, that the
richest agents might be on the verge of retirement and relatively
impatient). This is just one mechanism by which technology may itself
shape the preferences of a representative agent, but I think an
important one (Benzell et al 2023)[@n0ymjnv0tps].

## Minor Comments:

The authors argue that historical anthropocentric existential safety
expenditure has been near 0. I question this. If I view my enemy as
completely alien to my values, wouldn't military spending count? One
historical theory I have in mind is that the Habsburg Empire
intentionally slowed economic growth and increased military spending to
avoid a socialist revolution. An even older example could be the
prophecies of Jeremiah and similar prophets who connected contemporary
decadence and evil (the high consumption of the ruling class?) to a
coming disaster, and recommended shifting resources to ameliorating
religious rituals.

While this paper draws on Jones (2016)[@nn599e311l4] it does so much
less than the previous draft, and does a much better job highlighting
innovations vs. replicating that paper. Relative to Jones
(2024)[@nh9df4d3ikj] this paper is less precise in distinguishing the
effects of degrees of risk aversion, but has richer dynamics. My
critiques mostly apply to Jones (2024)[@n0pteywxdx2] as well.

## References

[@nytprzb5q1n]Aschenbrenner, Leopold. 2024. *Situational Awareness: The
Decade Ahead*. Retrieved from <https://situational-awareness.ai/>

[@n15lkk6g6ly]Benzell, S. G., Kotlikoff, L. J., LaGarda, G., & Sachs, J.
D. 2023. "Robots Are Us: Some Economics of Human Replacement", Working
paper.

[@nvo9f59fm6e]Jones, Charles I., "Life and Growth," Journal of Political
Economy, 2016, 124 (2), 539--578

[@nnqbny38qvj]Jones, Charles I., The A.I. Dilemma: Growth Versus
Existential Risk," 2024. Working paper.

# Evaluator details

1.  How long have you been in this field?

    -   8 years

2.  How many proposals and papers have you evaluated?

    -   4

[^1]: Note: if you are reading this before, or soon after this has been
    publicly released, the ratings from this paper may not yet have been
    incorporated into that data presentation.

[^2]: A small complementary point is that the parameterization of gamma
    less than 1 makes sense at an individual level, but is much too risk
    averse from a social welfare perspective. It is contrary to the
    ordinary intuition that two happy flourishing people is roughly
    twice as good as one happy flourishing person \-- i.e. aggregate
    utility is linear in individual utility. I understand this argument
    starts to go in a repugnant conclusion direction, and the authors
    are assuming a fixed exogenous population growth rate, but it's an
    illustration of how gamma as an individual behavior parameter might
    be different than gamma as a social welfare function parameter.
