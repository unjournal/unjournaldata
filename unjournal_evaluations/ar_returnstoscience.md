---
affiliation:
- id: 0
  organization: Open Philanthropy
article:
  elocation-id: arreturnstoscience
author:
- Matt Clancy
bibliography: /tmp/tmp-594iNPBOPLEA4R.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 20
  month: 01
  year: 2025
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Authors' response to Unjournal evaluations of "The Returns to
  Science In the Presence of Technological Risks"
uri: "https://unjournal.pubpub.org/pub/arreturnstoscience"
---

*Evaluation manager:* I highlighted some content and headers using bold
font. Bracketed sections represent nontrivial copy-editing changes;
other such changes are noted.

# Preamble

Let me begin by thanking the three \[evaluators\] for their careful read
and thoughtful comments on [Clancy
(2023)](https://arxiv.org/abs/2312.14289), and to The Unjournal for
coordinating this \[evaluation\]. It's a great relief to \[get feedback
suggesting\] that my math and code don't have any serious mistakes, that
evaluators find the paper well argued, and that the main parameters
associated with forecasting biocatastrophes are reasonable choices, at
least, so far as these individual evaluations are concerned. Since the
evaluators were quite engaged, they had a lot of comments and critiques.
I won't be able to respond to all of these individually, but I'll try to
cover the biggest ones and the ones that I personally believe have the
most interesting implications for the paper's results. Note the views
expressed in this response are my own and do not necessarily reflect the
views of Open Philanthropy.

# Incremental vs. Large-Scale Effects

\[Evaluator\] #1 is generally positively disposed toward the paper but
cautions against extrapolating from the results to larger scale policy
changes. They note that "the paper does not have enough space to cover
other factors that are relevant... \[these\] should be considered before
an actor can have confidence when taking large scale actions in the
space." They also consider whether the results would hold up if we
envisioned a permanent pause to science, rather than a one-year pause.

I endorse this interpretation. I agree with the \[evaluator\] that the
scientific and technological ecosystem are a complex adaptive system
where the long-run effects of seemingly small changes are hard to
predict. Indeed, I think this is another reason for using an epistemic
discount rate.

I also believe that a permanent stop to science would have significantly
different effects than scaling up the effects of a one-year pause. As I
note in footnote 6, "I'm a bit of a science fundamentalist and believe
that if we completely and permanently shut down science, growth would
slow very dramatically in the long-run."

In general, the paper's motivation was to help philanthropists assess
whether work that has the effect of accelerating scientific progress is
no longer positive, when we take into account technological risks. A key
assumption of the paper is that the impact of philanthropists is likely
to be small relative to the overall size of the scientific ecosystem.
For example, given that science is a decentralized international
activity, I've assumed the option of stopping all science is a
non-starter. Instead, all we can do is affect the speed of science on
the margin.

# Domain Experts vs Superforecaster Estimates

A key issue in Clancy (2023) is the wide divergence between domain
expert and superforecaster estimates of risks from future technologies.
Throughout the majority of the paper, my approach is to present the
model using each set of estimates. However, in section 11, I give some
reasons for my personal preference for superforecaster estimates
relative to domain experts. In section 11.2 I give my subjective
assessment as a 3 in 4 chance that superforecasters assessment of the
risk is right. Evaluators #1 and #3 think this is too strong and express
more ambivalence over which group is correct. I don't think we disagree
dramatically here and I would emphasize that my views are not decisively
in favor of the superforecasters either.

Nonetheless, below I present some brief responses to their arguments
that people should give more weight to domain expert forecasts than I
do:

-   **Claim**: **Higher intersubjective accuracy**[^1][^2]** **is not
    validated as a good proxy for accuracy and could be confounded by
    effort and time spent in discussions (Evaluation #3, pg. 4)

    -   **Response**: I agree that we do not have good evidence on
        whether people who display high intersubjective accuracy also
        tend to be more accurate on their other forecasts, though it
        seems like a sensible thing to believe without evidence to the
        contrary. However, some [preliminary
        studies](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3954498)
        on intersubjective accuracy do find that it performs as well as
        conventional incentivized forecasting on resolvable questions.

-   **Claim**: An alternative theory of **correlated pessimism**[^3] is
    that some people have lumpy knowledge; they know a lot about some
    areas but not others. Rationally, they may choose to avoid
    excessively confident predictions (in this case, that existential
    risks are very small) about areas where they lack information.
    (Evaluation #3, pgs 4-5)

    -   **Response**: This may be true, but as discussed on page 35 of
        the [XPT
        report](https://forecastingresearch.org/ai-adversarial-collaboration),
        pessimism is also correlated on questions that are not obviously
        about low probability events, such as the number of future
        humans that will be born or the year that the human race will go
        extinct.

-   **Claim**: It is not very compelling that, in a different context,
    domain experts predicted a few too many bio events over a ten year
    period. (Evaluation #3, pg 5)

    -   **Response**: I agree; it is only a small data point in favor of
        superforecasters.

-   **Claim**: XPT participants were asked to consider a very wide range
    of challenging questions, and it is possible (or likely) that
    **domain experts gave more thought and attention to the areas they
    knew best and less attention to the areas they do not know well
    ***\[emphasis added\]*. Superforecasters, whose knowledge is not so
    unevenly distributed, would be more likely to spread their limited
    attention more evenly across questions. This means we should
    interpret domain expert answers on the area of their expertise as
    reflecting more effort, as well as more background knowledge, than
    superforecasters and accordingly rate them more highly. (Evaluation
    #1, pg 7)

    -   **Response**: Perhaps. But a [followup
        study](https://forecastingresearch.org/ai-adversarial-collaboration)
        by the Forecasting Research Institute on AI risk attitudes tried
        to evaluate whether deeper engagement on a narrower set of
        questions led participants to revise their opinions. The results
        were pretty comparable to the XPT study. This indicates to me
        that differential attention is not the driving force behind
        disagreement.

For these reasons, I continue to personally put more weight on the
superforecaster estimates. That said, because reasonable people can (and
in fact do!) disagree, I tried throughout the report to present results
that would be useful for people who think domain expert results are
preferable.

# Code and Calculations

\[Evaluator\] #1 had a close read of the code and calculations in Clancy
(2023) and pointed to a number of areas with minor mistakes, or where
the code could be written more clearly. I thank the evaluator for their
close attention and will work to revise the code in line with their
suggestions. Importantly, they do not find any results are substantively
impacted by these errors.

# Parameter Choices

In a quantitative exercise like this, the choice of parameters is just
as important as the modeling framework and calculations. Evaluator #2
was asked to carefully review the choices for key parameters in this
model. In this section, I discuss how different assumptions suggested by
this evaluator would affect the model's conclusions.

## *G*: Baseline Growth

Evaluator #2 suggests it would make more sense to set *G =* 2% per year,
since this is the historical rate of growth. In Clancy (2023), I settle
on a more conservative 1% per year, based on the idea that temporary
boosts to growth that push the long-run rate of income growth above the
long-run rate of technological progress might abate in the future. A 1%
rate is also close to Robert Gordon's 2015-2040 forecast. That said,
interest rate forecasts are more consistent with future rates of growth
closer to 2%.

If we set *G* = 0.02, then we can maintain the assumption that pausing
science reduces growth by 0.0025, by setting *g* = 0.0175. **This
results in a higher return to science, via the health-income effect**
(pausing science leads to a greater reduction in utility, because people
in the distant future who die prematurely would have enjoyed more
utility from income when income grows at 2% per year instead of 1% per
year). In the baseline model with no time of perils, I find the ROI of
science rises from 331x to 465x with *G* = 0.02 and *g* = 0.0175.

## *g*: Growth when science is paused

Evaluator #2 also suggests that *g* = 0 is a plausible choice for the
rate of growth when science is paused; namely, pausing science for one
year stops growth in technological progress for a year. For the reasons
stated in the report, I think a smaller effect on growth is more
reasonable, but I do think setting *g* = 0 is a plausible measure of
what would happen if science were stopped forever (as noted in footnote
6, also referenced above). If we set *G* = 0.01, and *g* = 0, and assume
no time of perils, then the social impact of science rises in the
baseline from 331x to 536x.

## *d*: Excess mortality in the time of perils

Evaluator #2 suggests modeling excess mortality with an assumed
distribution, whose parameters are tuned to match XPT forecasts, as this
would give a better way of forecasting the burden of disease for minor
outbreaks that kill less than 1% of the population (which were ignored
in this report). I think this is a good suggestion but estimating this
is beyond the scope of this response. I hope future work will explore
this approach.

## *p*: The epistemic discount rate

My main report uses an annual discount rate of 2%, meaning it assumes
there is a 2% chance each year that the world changes such that we
cannot forecast policy impacts past this horizon. Evaluator #2 notes:

> The author considers several alternative ways of deriving this
> discount rate. First he turns to probabilities \[that\] participants
> of the XPT tournament gave to the event of observing 15% annual
> economic growth within certain time horizons as a proxy for the
> arrival of transformative AI as well as participants' probabilities of
> a major catastrophe. This yields discount rates in the range
> 0.05-0.7%. He then dismisses these discount rates arguing that 'the
> XPT only asked for forecasts through 2100\[\...\], and it may be
> inappropriate to extrapolate their forecasts forward by thousands of
> years.' However, the 2% discount rate he ends up adopting is mainly
> driven by the 1.6% annual probability of transformative AI arriving
> derived from the Open Philanthropy Worldview contest which assembled
> participants' credences of AGI arriving *before 2043*. Hence it is
> subject to the same criticism.

Evaluator #2 is correct that by using the 2% discount rate I'm
implicitly extrapolating out for thousands of years a forecast designed
to be resolved in \~20 years. However, there's an asymmetry with respect
to the sensitivity of our model to assumptions about the distant future.
With a 2% annual discount rate, the value of a future state of the world
drops to 1% of its initial value after 228 years. In practice, events
occurring after that year have limited practical import on policy
assessment. If we drop this to a 0.7% annual discount rate, it takes 656
years before we discount the value of events down to 1% of their initial
value. And if we drop to a 0.05% discount rate, it takes more than 9,000
years before discounting drops the value of a year down to 1% of initial
value. In opting for the higher 2% discount rate, my thinking was that,
while relying on either the XPT or Open Philanthropy forecasts to set
the discount rate implicitly extrapolate the forecasts beyond their
intended frame, this shortcut has less severe consequences for the
model's results when the implied discount rate is higher.

As is implied by the above discussion, this model is very sensitive to
the choice of discount rate. This is because my model assumes science
takes 74 years to have an impact, and then has a small impact per year
in perpetuity (so long as we remain in the current epistemic regime)
that add up over time. The smaller the discount rate, the more value we
place on those benefits and the higher is the expected return of
science. **Below I show a sample of how the ROI of science changes as we
scale the discount rate up or down under alternative assumptions about
the time of perils.** \[In the model without existential risk.\]

***AR table 1***

+----------------+----------------+----------------+----------------+
| Discount Rate  | No Time of     | S              | Domain Experts |
|                | Perils         | uperforecaster |                |
+================+================+================+================+
| 1%             | 12,980x        | 12,769x        | 9,673x         |
+----------------+----------------+----------------+----------------+
| 1.5%           | 1,259x         | 1,243x         | 994x           |
+----------------+----------------+----------------+----------------+
| 2%             | 331x           | 326x           | 238x           |
+----------------+----------------+----------------+----------------+
| 2.5%           | 123x           | 120x           | 72x            |
+----------------+----------------+----------------+----------------+
| 5%             | 4x             | 3x             | -8x            |
+----------------+----------------+----------------+----------------+
| 10%            | 0x             | 0x             | -2x            |
+----------------+----------------+----------------+----------------+

**Note there is an asymmetry to these results.** If the discount rate is
low, the returns to science are positive and very large, but if the
discount rate is high, the returns to science do **not** become negative
and very large. Instead, **large discount rates imply returns to science
near zero** (they can be positive or negative). This is because a high
discount rate shrinks both the future benefits and the future costs
associated with science. While the benefits shrink more than the costs,
since both are shrinking, we converge to zero impact.

In other words, if we are very wrong about the correct discount rate
(for example, if our forecasts of transformative AI are way off), there
is a chance that we either substantially underrate how good science is,
or that we think it is important but actually it isn't a very big deal
one way or the other. **Fortunately, a discount rate mistake would not,
on its own, lead us to see science as good when it is in fact very**
**bad.**

## *d*~*x*~: Extinction Risk

Evaluator #2 notes that we should perhaps think of this risk as a lower
bound since it does not account for science-derived existential risks
outside biocatastrophes. I explore this topic in depth in the next
section.

Evaluator #3 suggests it would be useful to have more analysis of how
existential risk probabilities affect $\lambda$, the number of years of
current global utility that would make us indifferent between pausing
science or not. As a reminder, when we model extinction risk, we are
forced to take a stance on how valuable the world might be in the next
epistemic regime (the world that happens beyond our ability to forecast
policy impacts). This is because if we go extinct, we lose this value,
and so it must enter our cost-benefit calculations.

To put it mildly, it is challenging to estimate what this value might
be, since it describes a world we do not understand enough to forecast
policy impacts. In my paper, I assume it as some multiple of the annual
global utility of the world today. I then define the parameter $\lambda$
as a break-even parameter, where if we believe the next epistemic regime
will be worth more than $\lambda$ years of today's global utility, we
would prefer to pause science.

The equation that determines $\lambda$ is given by equation (6) of
Clancy (2023).

$$\frac{V_{SQ} - V_{PS}}{W}\frac{1 - p(1 - d_{x})}{d_{x}(1 - p)} = \lambda$$

(6)

When $d_{x}$ is very small, this can be approximated as
$\frac{V_{SQ} - V_{PS}}{W}\frac{1}{d_{x}}$. If $V_{SQ} - V_{PS}$ \[*the
net benefit or cost of a year of science in the current regime*\] does
not much change when we change $d_{x}$, then to a first approximation
$\lambda$ is simply proportional to $1/d_{x}$. If you double the
extinction risk, you halve $\lambda$.

This isn't quite right though, because in general, if you increase
$d_{x}$ then you are also likely to increase $d$ (the non-extinction
excess mortality rate), and an increase in $d$ will tend to reduce
$V_{SQ} - V_{PS}$. Indeed, in the main report, as we go from the
superforecasters to the domain experts, we increase extinction
probability by a factor of 143x, but reduce $\lambda$ by 192-199x
(depending on the model). So a rough rule of thumb to estimate $\lambda$
is to start at a known value of $\lambda$ and $d_{x}.$ To assess a
higher extinction risk decrease $\lambda$ by a slightly larger
proportion than you need to increase $d_{x}$ to arrive at your preferred
value. To assess a lower extinction risk, increase $\lambda$ by a
slightly lower proportion than you need to decrease $d_{x}$ to arrive at
your preferred value.

# Modeling AI Risk

A theme all three evaluators noted at various points was that this
analysis should be extended to include AI risk. I'll use this response
as an opportunity to discuss this issue in some detail.

To start, one of the major critiques of Clancy (2023) comes from
**Evaluator #3, who notes that the paper stacks the deck against
concluding in favor of a science slowdown by comparing *****all***** the
benefits of science to only a *****subset***** of the risks of science,
namely the risks emerging from biotechnology** (Evaluator #2 also makes
this comment). I think this is quite a good critique (and one I am
surprised in retrospect that I did not hear more forcefully earlier).

To begin, **let's establish that it is reasonable to focus on
biotechnology and AI, and leave out other technological risks**. To do
that, we can start by asking what are the major risks to human society
posed by science. A nice place to get a consensus short-list is question
9 of the XPT, which asked about total catastrophic risk. Looking at the
detailed question summary for catastrophic risk (p. 324), the report
notes:

"\...there was broad agreement about what the important factors were:

-   AI and nuclear weapons were generally seen as likely the biggest
    risks.

-   Pathogens, both natural and anthropogenic, were a somewhat more
    controversial third.

-   Consequences from climate change, especially war, famine, disease,
    and heat waves, were also considered.

-   Non-anthropogenic risks---in one team's formulation: "solar flares,
    coronal mass ejections, asteroid collisions, pandemics,
    supervolcanic eruptions" (team 344)---were often mentioned, but
    their risk (aside from pandemics) was generally considered low to
    negligible."

The main threats on this list that derive from technological progress
here are AI, nuclear weapons, anthropogenic pathogens, and consequences
from climate change. This is not an exhaustive list of the possible
harms that might derive from future technology (one could imagine
nanotechnology, antimatter weapons, directed asteroids, etc.), but it
appears to be a list of the factors that participants in the XPT thought
most compelling.

My view is that nuclear weapons and climate change (derived from fossil
fuels) are at this point, primarily sunk costs of technological
progress. Indeed, my own expectation is that scientific progress will on
net lower the risks associated with climate change. I don't have strong
views one way or the other for nuclear weapons. But as the evaluators
note, that leaves two big dangers: AI and engineered pathogens. *If* it
is appropriate to set AI aside, then I think the report does not
disproportionately stack the deck in favor of science by focusing
primarily on bio related risks from science.

My explanation for setting aside AI in the report is too brief and
restricted to a footnote(!): "One reason this report focuses
specifically on biocatastrophes rather than risks from advanced AI is
that the rate of progress in AI is currently driven by major labs that
operate outside the traditional academic ecosystem where science today
is largely performed. Fundamental advances in the life sciences, in
contrast, continue to be predominantly made in the academic ecosystem."

I think the evaluators (especially evaluator #3, who makes this argument
at length) are correct that the report should have spent more time on
this question. In this response, I'll present **three different ways of
thinking about \[how to consider AI risk in this modeling\]**.

1.  Assume science's impact on the arrival of transformative AI is small
    enough to ignore (this is the approach I used in the paper)

2.  Assume science affects the arrival of transformative AI, analogously
    to how it affects the timing of the time of perils, and use XPT
    forecasts to assess the net impact of transformative AI

3.  Assume science affects the arrival of transformative AI, but these
    effects occur in the next epistemic regime, and we cannot decide if
    the post-AI world is better or worse than the status quo in
    expectation

## Approach 1: Separate R&D Spheres

One way to interpret the role of AI in this model is that it matters a
great deal, but the trajectory of its development is unaffected by
science. This is essentially how I thought about AI while writing the
paper. I essentially imagined two separate spheres of technological
progress. One contained the AI labs and the associated AI innovation
ecosystem, the other sphere consisted of the major institutions that
practice fundamental science. I had assumed the causal path from science
to AI progress was small enough to be ignored, so that changes in the
sphere of non-AI science do not affect the pace of AI progress. Note the
model does not assume the reverse; progress in AI has substantial
effects on science. Indeed, progress in AI is one of the motivating
factors behind the time of perils, and the prospect of transformative AI
(including AI-driven extinction) is captured by the discount rate *p*.

The paper would be improved by more carefully articulating and defending
this position, which I'll try to do now.

To begin, I think it can be established reasonably well that, at least
today, most research directly related to the progress of AI is happening
in the private sector. For example, "In 2021, nondefense US government
agencies allocated US\$1.5 billion on AI. In that same year, the
European Commission planned to spend €1 billion (US\$1.2 billion). By
contrast, globally, industry spent more than US\$340 billion on AI in
2021, vastly outpacing public investment." ([Ahmed, Wahed, and Thompson
2021](https://www.science.org/stoken/author-tokens/ST-1055/full)). As
noted in the report too, all the advanced models are coming from
specialized labs, rather than the academic sector.

Additionally, during writing, I assumed that fundamental science's main
contributions to AI were in the past (for example, the discovery of
neural networks and other deep learning principles). Going forward, it
seemed quite plausible that further advances would be driven by ongoing
application of scaling laws, coupled with intense *applied* research
effort, to mostly be undertaken in the labs.

I apologize that, in some places, the report is unclear that **I am
interested exclusively in fundamental science and its long-run impact**.
For example, Evaluator #3 writes "the scoping of meta-science in section
1.0 does not limit itself to 'fundamental research': major 'applied' lab
progress could be complemented by (e.g.) 'DARPA-like agencies',
public-private partnerships, acquiring FROs, continued flows of
academia-trained CS PhDs, etc." While it is true that section 1.0 gives
several examples related to technological progress in general, the
primary purpose of the modeling effort is to assess interventions that
impact science specifically. I think this is most clearly articulated in
section 4, which frequently motivates the selection of various
parameters by drawing distinctions between science and overall R&D.

That all said, on reflection, I think evaluator #3 makes a good argument
that the assumption that any link between basic science and AI progress
is small enough to be ignored is perhaps overly strong. As Evaluator #3
notes, even if this describes the current state of AI research, a lot
can happen between now and 2100. Moreover, it is not a given that "scale
is all you need." Finally, since writing this report, I have become
aware of various bottlenecks to scaling that could plausibly benefit
from new scientific discoveries.

**While I continue to believe spillovers between basic science and
progress on frontier labs are likely to be small, I recognize not
everyone finds this compelling.** Accordingly, in the next two sections,
I suggest two approaches to using this model to think about the case
where science influences the arrival of transformative AI.

## Approach #2: AGI in the Current Epistemic Regime

A second approach is to treat AI as analogous to the time of biological
perils in Clancy (2023). In this section, I'll talk about the arrival of
AGI, rather than transformative AI, to underscore that we're talking
about a phenomena that fits inside the current epistemic regime (and so
isn't completely transformative). As with the advance of biotechnology,
I'll assume the onset of AGI is not *so* dissimilar to our own world
that we can't predict some policy impacts.

In Clancy (2023), I think of scientific advances as having positive
effects via their impact on income and life expectancy, and negative
effects via their impact on excess mortality risk. For advanced
biological capabilities, I used forecasts from the XPT to estimate the
associated excess mortality risk, but assumed advanced biological
capabilities wouldn't have positive income or health effects *beyond*
allowing historical improvement trend rates to persist. **For AGI
though, I will assume that increased risk is potentially accompanied by
increased economic growth.** This is because the impact of AGI on the
rate of scientific discovery and economic growth has been a topic of
much debate. My sense is that people who believe transformative AI would
be powerful enough to cause catastrophes or extinction often believe AI
is also likely (though not necessarily certain) to lead to significantly
faster economic growth. Indeed, in the XPT, both superforecasters and
domain experts think the probability of global GDP growth of +15% in a
single year is actually *more* likely than an AI catastrophe (much less
AI extinction).

If we set out to model this carefully from first principles, we would
probably assume that the arrival of something like AGI leads to a faster
rate of economic growth as well as a heightened excess mortality risk.
Such a modeling exercise is beyond the scope of this response though.
Instead, I'll tweak some parameters in my model in such a way to provide
some suggestive evidence on whether the XPT forecasts imply
incorporating AI risk into this model would revise the main conclusions
about whether the average returns to science are positive.

Let's start with income. We'll imagine that AGI leads to faster growth
in expectation, and that the onset of AGI depends on the advance of
science. That means if we pause science for one year, we now lose out on
some economic growth in two ways. First, as usual, pausing science leads
to a 0.25% drop in the growth rate for one year, because of the link
between conventional economic growth and science. But now we also lose
out on one year of accelerated growth that we would have gotten from
AGI. We can imperfectly capture this lost year of growth with the term
*G* - *g*, which enters in the "pure income effect" term of Table 3. If
we leave *G* at 0.01, we can set *g* to a level such that *G* - *g* is
equal to the lost growth from a one-year delay in the onset of AGI.

What should *G* - *g* be? There's not a good question from the XPT to
ground this answer, so this will just have to be illustrative. **I'll
assume AGI will add 0.5% to growth in expectation**, so that we go from
1% per year to 1.5%, and if we delay AGI by one year by pausing science,
we give up that 0.5% for one year, plus the usual 0.25%. Thus *G* - *g*
= 0.75% instead of the usual 0.25%.[^4] I will set aside potential
health gains from AGI, since as we'll see, these income effects alone
suffice to illustrate some of the dynamics.

Let's turn next to the excess mortality risk posed by AGI. As Evaluator
#3 points out, \[as well as asking about pandemic risks,\] the XPT
\[also\] asks about the probability of ... \[an AI catastrophe\]\...by
2100, as well as an AI extinction event by 2100. I pull out that data
below, and calculate an "AI multiplier" by dividing the probability of a
given engineered pathogen risk by its corresponding AI risk. As we can
see, superforecasters see the AI extinction probability as 38x higher
than the bio extinction probability.

+---------------+-----------------+-------------+---------+----------+
|               |                 | *           | **AI**  | **AI     |
|               |                 | *Engineered |         | mult     |
|               |                 | Pathogen**  |         | iplier** |
+===============+=================+=============+=========+==========+
| **            | S               | 0.85%       | 2.13%   | 251%     |
| Catastrophe** | uperforecasters |             |         |          |
+---------------+-----------------+-------------+---------+----------+
|               | Domain Experts  | 4%          | 12%     | 300%     |
+---------------+-----------------+-------------+---------+----------+
| *             | S               | 0.01%       | 0.38%   | 3800%    |
| *Extinction** | uperforecasters |             |         |          |
+---------------+-----------------+-------------+---------+----------+
|               | Domain Experts  | 1%          | 3%      | 300%     |
+---------------+-----------------+-------------+---------+----------+

Median community probabilities of catastrophes and extinction events by
2100, drawn from tables 2 and 3 of the XPT report.

Next, I reproduce table A3.8 from Clancy (2023). This table gives the
estimated probability of engineered pandemics that kill various
proportions of the population.

+-------------------+-------------+----------+---------+---------+---------+--------------+
| Pandemic Event    |             | 0-1%     | 1-10%   | 10-100% | 100%    | Expected     |
|                   |             |          |         |         |         | Annual       |
|                   |             |          |         |         |         | Mortality    |
+===================+=============+==========+=========+=========+=========+==============+
|                   | Mortality   | 0        | 2%      | 20%     | 100%    |              |
|                   | Rate        |          |         |         |         |              |
+-------------------+-------------+----------+---------+---------+---------+--------------+
| Superforecasters  | Baseline    | 99.96%   | 0.03%   | 0.0064% | 0.0000% | 0.0020%      |
| Annual            |             |          |         |         |         |              |
| Probabilities     |             |          |         |         |         |              |
+-------------------+-------------+----------+---------+---------+---------+--------------+
|                   | Time of     | 99.92%   | 0.07%   | 0.0128% | 0.0002% | 0.0041%      |
|                   | Perils      |          |         |         |         |              |
+-------------------+-------------+----------+---------+---------+---------+--------------+
|                   | Change      | 0.0021%  |         |         |         |              |
+-------------------+-------------+----------+---------+---------+---------+--------------+
| Domain Experts    | Baseline    | 99.82%   | 0.16%   | 0.0216% | 0.0000% | 0.0075%      |
| Annual            |             |          |         |         |         |              |
| Probabilities     |             |          |         |         |         |              |
+-------------------+-------------+----------+---------+---------+---------+--------------+
|                   | Time of     | 99.42%   | 0.49%   | 0.0669% | 0.0228% | 0.0460%      |
|                   | Perils      |          |         |         |         |              |
+-------------------+-------------+----------+---------+---------+---------+--------------+
|                   | Change      | 0.0385%  |         |         |         |              |
+-------------------+-------------+----------+---------+---------+---------+--------------+

Engineered pathogen mortality probabilities

As a bounding exercise, I will create analogous tables for AI risk.
Since this is a bounding exercise, I'll assume the **baseline**
probabilities of AI-driven mortality are equal to zero; that is, current
levels of AI pose zero risk. Since I will assume there are risks from AI
during the time of perils, this assumption maximizes the increase in
risk during the time of perils. To estimate mortality risks from AI
during the time of perils, I will take the various probabilities of
engineered pathogen events and scale them up by the AI multiplier given
above. For example, I'll scale up the superforecaster forecasts for 2%
and 20% mortality events by 251% (the AI multiplier associated with
catastrophes) and the forecast of 100% mortality by 3800% (the AI
multiplier associated with extinction). The analogous estimates for
domain experts are scaled up by 300%. The following table results.

+---------+---------+---------+---------+---------+---------+---------+
| AI      |         | 0-1%    | 1-10%   | 10-100% | 100%    | E       |
| Event   |         |         |         |         |         | xpected |
|         |         |         |         |         |         | Annual  |
|         |         |         |         |         |         | Mo      |
|         |         |         |         |         |         | rtality |
+=========+=========+=========+=========+=========+=========+=========+
|         | Mo      | 0       | 2%      | 20%     | 100%    |         |
|         | rtality |         |         |         |         |         |
|         | Rate    |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| Su      | B       | 100.00% | 0.00%   | 0.00%   | 0.00%   | 0.0000% |
| perfore | aseline |         |         |         |         |         |
| casters |         |         |         |         |         |         |
| Annual  |         |         |         |         |         |         |
| Probab  |         |         |         |         |         |         |
| ilities |         |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         | Time of | 99.79%  | 0.17%   | 0.0320% | 0.0064% | 0.0161% |
|         | Perils  |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         | Change  | 0.0161% |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| Domain  | B       | 99.82%  | 0.00%   | 0.0000% | 0.0000% | 0.0000% |
| Experts | aseline |         |         |         |         |         |
| Annual  |         |         |         |         |         |         |
| Probab  |         |         |         |         |         |         |
| ilities |         |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         | Time of | 98.26%  | 1.47%   | 0.2006% | 0.0684% | 0.1379% |
|         | Perils  |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         | Change  | 0.1379% |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+

\[As\] a bounding exercise, we'll assume risks from AI and
biocatastrophes are additive. (Since it seems likely that forecasters
expect AI to sometimes bring about catastrophe *\[via\]* its impact on
an engineered pathogen, adding the risks together should *overstate* the
\[implied risk\].) ...) This implies an upper bound on the excess
mortality risk, assuming either AI risk or engineered pathogen is
0.0021% + 0.0161% = 0.0183% for superforecasters or 0.0385% + 0.1379% =
0.1764% for domain experts.

We can then run my model, setting *g* = 0.25% (so that *G - g =* 0.75%)
and *d* = 0.0183% or 0.1764%. The results are in the following table:

+------------------------+---------------+-------------+--------------+
| Excess Mortality       | Model         | Total       | Break-even   |
|                        |               | Impact      | AGI growth   |
|                        |               |             | rate boost   |
+========================+===============+=============+==============+
| Superforecaster (*d* = | Baseline      | +419x       | \-           |
| 0.0183%)               |               |             |              |
+------------------------+---------------+-------------+--------------+
|                        | Realistic     | +140x       | \-           |
|                        | Health        |             |              |
+------------------------+---------------+-------------+--------------+
| Domain expert (*d* =   | Baseline      | +64x        | 0.2%         |
| 0.1764%)               |               |             |              |
+------------------------+---------------+-------------+--------------+
|                        | Realistic     | +54         | 0.15%        |
|                        | Health        |             |              |
+------------------------+---------------+-------------+--------------+

Possible ROI of science in the presence of AI + bio risks

To sum up \[when we add AI to the model\]:

-   **The implied returns to science are +140x to +419x if we assume
    excess mortality risks derived from superforecaster forecasts of AI
    and bio risks and that delaying AGI by one year results in a loss of
    0.5% annual growth.** The dispersion in estimated impacts depends on
    which model from Clancy (2023) of health we use.

-   Note that if we assume there is *no* expected income boost from AGI,
    then superforecaster estimates of AI+bio risks are about 50% of the
    bio alone risks from Clancy (2023). Thus, the analysis of domain
    expert risks in Clancy (2023) is a rough guide to the consequences
    of including superforecaster beliefs about AI risk, without any
    offsetting benefits.

-   The implied returns to science are +54x to +64x if we assume excess
    mortality risks derived from domain expert forecasts of AI and bio
    risks and that delaying AGI by one year results in a loss of 0.5%
    annual growth. The dispersion in estimated impacts depends on which
    model from Clancy (2023) of health we use.

-   Note that if we assume there is *no* expected income boost from AGI,
    then domain expert estimates of excess mortality risk ***exceed***
    the break-even values computed in Clancy (2023). In other words, if
    we think AGI does not add any benefits above the historical
    baseline, and increases risks as implied by domain expert forecasts,
    and that science leads to AGI, then we would prefer pausing science
    for one year to the status quo.

-   The choice of a one-year delay to AGI leading to a 0.5% income loss
    is not well grounded, so in the final column, I compute the level of
    lost growth I would need to assume to be indifferent between pausing
    and continuing science. **In general, if the domain experts are
    broadly correct in their assessment of AI and bio risks, then we
    would only want to continue science if we thought getting AGI sooner
    by one year would lead to roughly 0.15-0.2% more growth**.

There is a lot to critique about this too-short exercise, even if it
builds on a much longer exercise. It is a bit kludgey and hackey. It
neglects positive potential health effects of AGI and the positive
health-income effects from their interaction. It also assumes the
baseline for AI risk is 0, even though XPT participants do see some
risks before 2030, which has the effect of magnifying the relative
increase in risk during the time of perils. And income effects are
modeled inappropriately, though I hope the approach is at least
suggestive of magnitudes in play. And lastly, **this simple exercise
hasn't grappled with extinction issues**, as in section 8.0 of Clancy
(2023).

But I think this exercise is **suggestive that dramatically higher
forecasts of risk from AI, relative to biocatastrophe, do not
necessarily imply that we should be pessimistic about the impact of
science**. This is either because, in the case of superforecasters,
their estimated risks from biocatastrophe are so small that even much
larger risks (*in proportional terms*) do not offset the historic gains
from science. **Among domain experts, this is because risks from AGI are
also paired with a greater expectation of large benefits from AGI** (25%
probability of +15% growth, for example).

## Approach #3: Deep Uncertainty about AGI

While approach #2 does not "flip the sign" of my main results, it does
change their magnitudes a lot in some cases. Moreover, it is notable
that attempting to model AI risk does lead to much larger estimates of
both the costs and benefits of science. Moreover, I suspect it is likely
that many readers will disagree with how I modeled AGI in the preceding
section. A seeming natural impulse, in response to all this, is to
recommend that we devote a lot more energy to trying to forecast the
impact of AI. A natural impulse is to assume we should get this right,
because it is the most important thing to get right.

However, estimating the likely impact of transformative AI is a
contentious and controversial topic where reasoned debate has proven
largely ineffective to shift opinions ([XPT
2023](https://static1.squarespace.com/static/635693acf15a3e2a14a56a4a/t/64f0a7838ccbf43b6b5ee40c/1693493128111/XPT.pdf),
[XPT
2024](https://static1.squarespace.com/static/635693acf15a3e2a14a56a4a/t/65ef1ee52e64b52f145ebb49/1710169832137/AIcollaboration.pdf),
and personal experience!). This is despite significant effort and public
debate on the topic. For that reason, in this section, I present a third
approach for thinking about transformative AI when we believe science
accelerates its arrival but we are deeply unsure about whether that is
desirable.

Let us suppose we hold the following beliefs:

-   Scientific progress will accelerate the arrival of transformative AI

    Transformative AI will truly be transformative; we cannot predict
    how policy actions will affect the post AI world.

-   We expect the post AI world to be radically different, but we don't
    know if it will be radically better, worse, or something else, and
    accordingly would **neither** definitely prefer that we accelerate
    the arrival of AI or delay it.

We can reflect this bundle of beliefs in our model. We'll start with
equation (1) in Clancy (2023), which lays out the basic framework for
doing policy analysis.

$V_{0} = \left\{ p^{t}n(t)u(t) + (1 - p^{t})\widehat{n}(t)\widehat{u}(t) \right\}$

As noted in Clancy (2023):

-   The term $p^{t}$ corresponds to the probability we are still in the
    current epistemic range in period *t*. If so the utility obtained is
    proportional to:

    -   $u(t)$, which is the utility obtained in period *t* in the
        current epistemic regime.

    -   $n(t)$ is the number of people alive in period *t*.

-   The term $(1 - p^{t})\widehat{n}(t)\widehat{u}(t)$ corresponds to
    the utility we expect to obtain in the event we have exited the
    current epistemic regime. This happens with probability $1 - p^{t}$,
    in which case we use $\widehat{n}(t)$ and $\widehat{u}(t)$ to
    compute the number of people we expect to be alive and their
    utility.

Let us assume "entering the next epistemic regime" happens only if and
when transformative AI arrives, and there is some policy we could take
that has no impact on the world except that it would accelerate or delay
the arrival of transformative AI. We can model this as a change in the
annual probability *p*. Let's have this alternative policy be
represented by:

$V_{1} = \left\{ {\underline{p}}^{t}n(t)u(t) + (1 - {\underline{p}}^{t})\widehat{n}(t)\widehat{u}(t) \right\}$

This is the same as the previous equation, except I have replaced $p$
with $\underline{p}$. If this is a policy that accelerates the arrival
of transformative AI, then $\bar{p} < p$. If it slows it, then
$\bar{p} > p$.

If we would not definitely prefer to accelerate or slow AI, that can be
modeled by us behaving as if we believed $V_{0} = V_{1}$. If this is
true for $\bar{p} < p$ and for $\bar{p} > p$ then this is only true if
$p$ and $\bar{p}$ drop out of the equation when $V_{0} = V_{1}$. It can
be shown this implies we believe
$\widehat{n}(t)\widehat{u}(t) = n(t)u(t)$.[^5]

Note, this is not to say that the next epistemic period actually *is*
the same as the status quo. Instead, it is an assertion that we think
*in expectation* that it is not better or worse, possibly because large
potential upsides (explosive economic growth?) are balanced by large
potential downsides (extinction?).

The intuition is simple. If we think the post AI world is better (in
expectation) than the status quo, then we should want to accelerate
towards it. If we think it is worse, then we should delay it. And if we
think it is neither better or worse in expectation, then we should be
indifferent to calls to accelerate or delay the arrival of AGI. So if we
are indifferent to the arrival time of AI, then it means we believe the
status quo and the post AGI world are equally desirable in expected
utility terms. Importantly, I interpret "indifferent" here as meaning
"too unsure to decide in favor of a policy of acceleration or
deceleration" rather than being *uninterested* in the question of what
will happen!

If this is true, then we can use the model to evaluate a policy change
that has the incidental impact of changing the arrival of AI. Let the
status quo be described by the first equation in this section. Now let
us consider an alternative policy that changes consumption, population,
and the arrival time of the new epistemic regime. One example of such a
policy is a policy to pause science for one year. This policy can be
written as:

$V_{2} = \left\{ {\bar{p}}^{t}\bar{n}(t)\bar{u}(t) + (1 - {\bar{p}}^{t})\widehat{n}(t)\widehat{u}(t) \right\}$

Note that we have replaced $n(t)u(t)$ by $\bar{n}(t)\bar{u}(t)$ to
reflect the fact that population and utility are different under this
alternative policy.

The change in utility from this policy is given by:

$V_{0} - V_{2} = \left\{ p^{t}n(t)u(t) + (1 - p^{t})\widehat{n}(t)\widehat{u}(t) \right\} - \left\{ {\bar{p}}^{t}\bar{n}(t)\bar{u}(t) + (1 - {\underline{p}}^{t})\widehat{n}(t)\widehat{u}(t) \right\}$

Now, let us substitute $\widehat{n}(t)\widehat{u}(t) = n(t)u(t)$ to
reflect our uncertainty \[implying indifference\] about whether the new
epistemic regime is more or less desirable than the status quo

$V_{0} - V_{2} = \left\{ p^{t}n(t)u(t) + (1 - p^{t})n(t)u(t) \right\} - \left\{ {\bar{p}}^{t}\bar{n}(t)\bar{u}(t) + (1 - {\bar{p}}^{t})n(t)u(t) \right\}$

We can rewrite this as follows, gathering like terms related to the new
epistemic regime:

$V_{0} - V_{2} = p^{t}n(t)u(t) - {\bar{p}}^{t}\bar{n}(t)\bar{u}(t) + \left\{ (1 - p^{t}) - (1 - {\bar{p}}^{t}) \right\} n(t)u(t)$

Simplifying, we obtain:

$V_{0} - V_{2} = p^{t}n(t)u(t) - {\bar{p}}^{t}\bar{n}(t)\bar{u}(t) + ({\bar{p}}^{t} - p^{t})n(t)u(t)$

Finally, this can be rewritten as:

$V_{0} - V_{2} = {\bar{p}}^{t}(n(t)u(t) - \bar{n}(t)\bar{u}(t))$

Note that we now have just a single discount rate again, except now that
rate is $\bar{p}$ rather than $p$. The above equation can be interpreted
as evaluating the consequences of a policy *entirely in the current
epistemic regime*, but using the discount rate $\bar{p}$ instead of $p$,
to reflect the fact that the policy changes $p$ as well as utility and
population.[^6]

If we wanted to apply this method to the report in Clancy (2023), it
would imply we should use the same model, but with a different discount
rate. In my model, I assumed an annual probability of transformative AI
of 1.6%, which implies the transformative AI will be reached by 1/1.6% =
62.5 years in expectation. If pausing science delays the expected
arrival by one year, then we need to change the discount rate to 1.575%
(since 1/1.575% = 63.5). This would imply using a discount rate of
1.975% instead of 2%, setting $p = 0.98025$. Using this discount rate
changes the impact of science by about 6%.

## Summary: AI Risk

To reiterate, I think the reviews are correct to point out that the
paper does not adequately justify its decision to set AI risk aside, and
I've tried to rectify that a bit in this response. I first argue that AI
and bio collectively account for the majority of forecast risks to
humanity that can be attributed to science. I then lay out three
approaches for thinking about AI.

First, if AI advances are mostly driven by applied research in the
current paradigm, then one option is to ignore the impact of science on
AI. This is the approach taken in approach #1 and in Clancy (2023). I
think this approach makes the most sense if one expects the current AI
scaling paradigm to persist, but also agree it is possible for someone
to believe that is true and that science still affects the arrival of
AGI.

Second, if one believes science does accelerate the arrival of AGI,
there are two approaches you can take. One approach is to try and work
out the various costs and benefits of AGI and explicitly build these
into the model. This is the route I go in approach #2. Note that if one
wants to go this route, it's important to specify potential benefits
from AGI, since these are expected to be large. Another option, not
explored in this note, is to go part-way between approaches #1 and #2,
by assuming science only gets part of the credit for accelerating AGI,
analogously to how we gave science only part of the credit for
accelerating health and income gains in Clancy (2023). If you go this
route, it will tend to move the results more closely towards the results
in Clancy (2023), which completely set AI risk aside.

Finally, the other approach you can take if you believe science does
accelerate the arrival of AGI, but think trying to anticipate the impact
of AGI is fruitless, is presented by approach #3. This approach requires
a strong commitment to a kind of cluelessness about AI; an inability to
decide whether it would be good to bring it forward or push it back in
time. Even so, this position might be a useful one for policy analysis,
if we believe the debate about the post-AI world is stuck and will
likely remain so. In approach #3, I show that if there is a certain kind
of ambivalence about what a post-AGI world will look like, then we can
model policies that affect its arrival using the approach in Clancy
(2023), but with a slightly modified discount rate. Again, it is
possible to go slightly in between approaches #1 and #3, if one believes
the impact of science on AI is small; in this case, that would lead one
to modify the discount rate by a smaller amount.

[^1]: Manager's note: Superforecasters were better at this

[^2]: Manager's note: we added the bold emphasis here. All bold emphasis
    below was added by us, it was not in the authors' response as
    written.

[^3]: Manager's note: From the paper "A second reason I prefer the
    superforecaster estimates is that there is extensive cross-domain
    correlation related to general pessimism and optimism among groups
    in ways that imply biases. ... even for categories that seem likely
    to be uncorrelated. ... I think it is \[\...\] likely that domain
    experts are too pessimistic... \[a pessimistic individual\] would be
    disproportionately likely to seek to learn more about catastrophic
    risk, and hence become a domain expert. "

[^4]: For comparison, [[Amodei
    (2024)]{.underline}](https://darioamodei.com/machines-of-loving-grace)
    argues powerful AI could lead to 10x faster scientific and
    technological progress. For a discussion of the merits of this view,
    see [[this
    debate]{.underline}](https://asteriskmag.com/issues/03/the-great-inflection-a-debate-about-ai-and-explosive-growth)
    between Clancy and Besiroglu. On the more skeptical side, Tyler
    Cowen [[argues
    AI]{.underline}](https://www.bloomberg.com/opinion/articles/2023-08-16/ai-won-t-supercharge-the-us-economy?utm_content=view&cmpid%3D=socialflow-twitter-view&utm_campaign=socialflow-organic&utm_source=twitter&utm_medium=social&sref=htOHjx5Y)
    will increase US annual growth rates by 0.25 to 0.5 percentage
    points. I've taken the higher side of Cowen's estimate for this
    illustrative example.

[^5]: To see why, set the two equations equal to each other, group like
    terms, and simplify.

[^6]: Manager's note: Here we assumed that radical uncertainty implies
    indifference between the current payoffs and the payoffs under TAI.
    Thus we simply compare the flow of payoffs under the status quo to
    those under an alternative policy such as 'pausing science for one
    year'. We use the discount rate
    [[$\overset{ˉ}{p}$]{.katex-mathml}[[[]{.strut
    style="height:0.7622em;vertical-align:-0.1944em;"}[[[[[[]{.pstrut
    style="height:3em;"}[p]{.mord
    .mathnormal}]{style="top:-3em;"}[[]{.pstrut
    style="height:3em;"}[[ˉ]{.mord}]{.accent-body
    style="left:-0.1667em;"}]{style="top:-3em;"}]{.vlist
    style="height:0.5678em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
    style="height:0.1944em;"}]{.vlist-r}]{.vlist-t .vlist-t2}]{.mord
    .accent}]{.base}]{.katex-html aria-hidden="true"}]{.katex} : under
    this new policy we transition to TAI with probability
    [[$\overset{ˉ}{p}$]{.katex-mathml}[[[]{.strut
    style="height:0.7622em;vertical-align:-0.1944em;"}[[[[[[]{.pstrut
    style="height:3em;"}[p]{.mord
    .mathnormal}]{style="top:-3em;"}[[]{.pstrut
    style="height:3em;"}[[ˉ]{.mord}]{.accent-body
    style="left:-0.1667em;"}]{style="top:-3em;"}]{.vlist
    style="height:0.5678em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
    style="height:0.1944em;"}]{.vlist-r}]{.vlist-t .vlist-t2}]{.mord
    .accent}]{.base}]{.katex-html aria-hidden="true"}]{.katex} in each
    period, after which the payoffs are the TAI payoffs which equal the
    current payoffs anyways.
