---
abstract: |
  This is an evaluation of "Does the Squeaky Wheel Get More Grease? The
  Direct and Indirect Effects of Citizen Participation on Environmental
  Governance in China\", involving an RCT investigating the effects of
  citizen participation through social media on environmental policy
  enforcement. The evaluation praises the RCT as ambitious and
  well-execute. It highlights the sophistication of the experimental
  design and the importance of the findings for both academic and policy
  circles. However, it also critiques the handling of over-time dynamics
  and the panel data specifications used in the analysis, suggesting
  alternative methodologies for clearer interpretation. The evaluation
  considers the external validity of the findings, discussing the
  potential impact and limitations of applying the Weibo intervention in
  different contexts. It underscores the importance of policymakers\'
  utility calculus and the institutional framework in determining the
  intervention\'s effectiveness. It concludes by acknowledging the
  study\'s contribution to understanding the role of social media in
  influencing government behavior towards environmental concerns, while
  also cautioning about generalizing the findings. *(This abstract was
  not written by Robert Kubinec). *
affiliation:
- id: 0
  organization: NYU Abu Dhabi
article:
  doi: 10.21428/d28e8e57.22756671
  elocation-id: buntaineeval1revised
author:
- Robert Kubinec
bibliography: /tmp/tmp-46t3H505sRmUbi.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 11
  month: 08
  year: 2023
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 1 of "Does the Squeaky Wheel Get More Grease? The
  Direct and Indirect Effects of Citizen Participation on Environmental
  Governance in China" (prize-winning evaluation)
uri: "https://unjournal.pubpub.org/pub/buntaineeval1revised"
---

# Summary measures

**Overall assessment**

Answer: 90

90% CI: (85, 95)[^1]

**Quality scale rating**

"On a 'scale of journals', what 'quality of journal' should this be
published in?: Note: 0= lowest/none, 5= highest/best"

Answer: 4.8

90% CI: (4.5, 5.0) [^2]

*See the evaluation summary for a more detailed breakdown of the
evaluators' ratings and predictions.*

# Written report

## Introduction

This review of [@Buntaine2022DOES] is at the request of the organization
\[*The\]* *Unjournal* and as such emphasizes certain issues that might
not be as of great import in a standard review. In particular, I will
examine the policy relevance and impact of this research, which means
that I will dwell on issues of external validity to a greater extent
than I might otherwise.

On the whole, I found this RCT to be both ambitious and remarkably
well-executed; as such the academic and policy communities both stand to
learn significant new information about how social media, pollution
monitoring, companies, and local bureaucracies interact. The research
design is also clear and clean; we know what was randomized and the
outcome measures are appropriate and relatively error-free. Even apart
from the substantive findings, I believe this paper should be a part of
curricula that teach RCTs as it raises the bar for the sophistication of
experiments.

At the same time, increasing complexity can also lead to more complex
analyses. My main fault with the paper is that the over-time dynamics of
the experiment are not appropriately handled, which can make it
difficult to interpret the effects of the treatment. There is
substantial work on over-time variation in cross-sectional data that the
authors could draw on to give us a better understanding of the dynamics
of the companies under study.

In terms of broader relevance, I believe that the study's Weibo
intervention points to the role that boosted posts could affect
government behavior. In some sense, this paper is the inverse of the
growing literature on state-backed misinformation on social media: if
nefarious actors can influence the social media discourse and
consequently what social media users believe ([@Tucker2017From]), it is
quite possible that altruistic organizations could influence what
governments believe based on social media, leading to consequent changes
in policy.

While this is a remarkable finding and one worth considering as a new
tool for policy engagement, an important caveat is that the findings of
this RCT depend on the policymaker's utility calculus. In the context in
China, policymakers had precommitted to learn from citizen complaints
and they also believed that the legitimacy of the state depended on
responding to environmental concerns. When policymakers do not share
these goals, the policy intervention could either have no effect or
possibly backfire on those who make the appeals. I discuss these issues
in greater length after examining the study.

# Research Design

As I mentioned above, I find the experiment to be remarkably
well-designed. It uses a sophisticated multiple-arm approach with
overlapping treatments, permitting them to maximize the different
treatment nuances and consequently increase learning in the experiment.
They also spent a significant amount of time to increase the validity of
the treatment by analyzing pollution data from the CEMS system. This
effort and attention to detail helps us know that the complaints being
filed are based on actual violations rather than just raising awareness
as such.

While the experiment was well-designed, [the
pre-registration](https://www.socialscienceregistry.org/trials/5601) was
quite limited. We have a rough though generally accurate description of
the experimental procedures and we are told that they intend to do the
survey with more than 25,000 firms across 7 treatment arms. Their
enrolled sample just missed this target at 24,620 firms. In general,
24,000 is still such a large number that I am not particularly concerned
about power or sub-group analyses. However, that is not to say that all
analyses will be well-powered, [as Tom Cuningham noted about the recent
Facebook
mega-experiment](https://tecunningham.github.io/posts/2023-07-27-meta-2020-elections-experiments.html).
Compared to most experiments, though, this one will probably estimate
most estimands with minimal noise and sampling error.

The limitations in the pre-registration, though, do affect how much we
can learn from the experiment. We do not know what if any priors the
authors' had about effect sizes, and we lack a good understanding of the
power of the design. It is a complicated design, so the power curve
would require simulation, which may be non-trivial. There are [R
packages that offer help with this
task](https://cran.r-project.org/web/packages/DeclareDesign/index.html).
This lack of confirmed priors mean we have to be careful when we
generalize beyond this study as we run the risk of confirmation bias;
i.e., seeing these results as firmly established rather than at least
partly exploratory. We can over-estimate the certainty of
finished/published results while under-estimating the uncertainty of
applying these interventions outside of their original context.

# Estimation

My main criticism of the article's methodology is the panel data
specifications that were employed. It appeared that the authors followed
a long-standing tradition in econometrics to include substantial numbers
of fixed effects as a way of "conservatively" estimating treatment
effects. However, the authors' specification, so far as I can tell,
boils down to a two-way fixed effects specification that has been
repeatedly criticized by authors in recent years ([@Imai2021Matching],
[@Goodman2018Difference], [@Chaisemartin2022Two],
[@Kropko2020Interpretation]). As an author of one of these studies, I
may be biased against this particular specification, but I think at
minimum the authors should consider implementing simpler and easier to
interpret estimates.

The issue of course is that, unlike canonical experiments in which the
treatment is assigned cross-sectionally and a single observation of the
outcome is obtained, the authors have companies observed daily for a
significant period of time. This means we have, theoretically, one
counterfactual outcome for each firm and each day. Which comparison on
which day is most relevant? This "repeated measures" issue is, in my
opinion, an artifact of the potential outcomes framework which
encourages people to think of discrete counterfactuals ($Y(1)$ and
$Y(0)$).

In this situation, expressing the research design as a causal graph is
quite helpful. At its simplest level, the causal graph of the experiment
can be expressed as the following:

$$
T \rightarrow M \rightarrow Y
$$

{#eq-dag1}

In this case, the treatment is randomly assigned and causes a mediator
$M$, which subsequently causes the outcome $Y$. $M$ in this experiment
could be many different things, including the actions of the regulators
to the appeals and the reaction of the firms to the investigations. The
treatment does not directly affect either the behavior of firms or air
quality directly but rather through specific causal pathways.

The authors do an admirable job in the experiment trying to ascertain
what these pathways are in part by randomizing different kinds of
treatments that should cause different values in $M$, such as by
informing governments publicly vs. privately. However, my point here is
that it is entirely possible to estimate the effect of $T$ on $Y$
without including any measures of $M$. Because $M$ is caused by $T$, it
is post-treatment and so the effect of $M$ is subsumed in any analysis
of the conditional probability $Pr(Y|T)$.

In the context of this experiment, we are fairly certain that these
mediated effects are the most relevant; it would not seem plausible that
the treatment would have much of a direct effect on $Y$ apart from the
mechanisms:

$$
T \rightarrow Y
$$

In other words, we would not think that monitoring CEMS data would have
any effect without being able to get policymakers to pay attention. As
such, we do not need to be as concerned about separating the direct from
the indirect effects.

For these reasons, I think the authors should perform a simple pooled
analysis as a baseline specification--i.e., compare post-treatment
observations for treatment to control without any fixed effects, or if
including fixed effects, include firm fixed effects only (to isolate the
within-firm effect) or fixed effects for the districts within which
randomization was conducted (for the between-firm effect). These naive
models will combine the direct and indirect effects of $T$ on $Y$ but
are also quite simple to interpret, and therefore provide a helpful
baseline before considering indirect pathways.

To understand the time dynamics better (i.e. what is involved in
$T \rightarrow M$, I think the authors should consider models of time.
On the semi-parametric side, we can look at splines and kernel density
estimators ([@Kenny2022Analysis]), and also the so-called
quasi-experimental methods like multi-period difference-in-difference
([@Callaway2020Difference]). The exogeneity of the randomization would
make assumptions such as parallel trends more credible
([@Rambachan2019honest]), and would allow the authors to better
decompose the post-treatment variation in the outcome.

Including the fixed effects as such, that is, without a clear causal
model, risks inducing post-treatment bias ([@Montgomery2018How]). Each
of the day $\times$ firm fixed effects could represent some part of $M$
that occurred post-treatment, and as such should be considered
post-treatment variables. The authors' RCT power may be affected by this
in hard-to-predict ways. In general, this post-treatment bias may
unnecessarily attenuate the treatment effects, and there are plenty of
results in the paper that are surprisingly noisy given the massive size
of the sample. Without other and simpler specifications being reported,
though, it is difficult for me to say whether this might be the case.

I would also encourage the authors to consider the growing literature on
sequential ignorability, especially as expressed using causal diagrams
([@Xu2023Causal]). There may be many possible estimators or comparisons,
but being clear about which particular comparisons are employed would
help make it clear exactly what the average treatment effect is.

# External Validity

These concerns aside, I do think that the experimental analysis as
written produces some clear findings, especially that social media posts
seem to generate more of a reaction from government officials and
consequently firms in terms of their behavior. It is important to note
as well that the experiment "failed" to affect some outcomes, such as
firm-level outcomes in terms of pollution when the appeals were made
privately (see row 1 in Table 3). Furthermore, while the treatment
lowers violations, its impact on aggregate pollution is less clear
(table 7), possibly because firms can meet air quality standards but
still pollute substantially. As such, we learn not only that Weibo is a
uniquely important mechanism for affecting government preferences in
China, but also that other channels by which the government could learn
apparently important information about polluters can have a very limited
effect at least in terms of pollution outcomes.

The Weibo treatment has clear policy impact. In fact, if it can be
implemented in China, which is notorious for controlling the information
environment, it should be even easier to implement in the many countries
that have much less control over social media. The impact of the policy
is also high relative to the cost: boosting social media posts does not
require enormous investments in capital. Highlighting complaints to
policymakers that are observable to other citizens would appear to be a
rewarding strategy that advocacy NGOs could use on behalf of important
issues like climate change, immigration and anti-corruption.

At the same time, there are important limitations to the external
validity which are not fully acknowledged in the present draft. Crucial
to this strategy succeeding is the utility function of the policymaker.
As the authors note, China is exceptional in its commitment to citizen
concerns concerning pollution, especially for an authoritarian state
which presumably does not face the same accountability pressures of
regular popular elections ([@Slater2012Ordering]). The Chinese Communist
Party, at least under the leadership of Hu Jintao, believed that the
legitimacy of the state rested on mitigating pollution harms, especially
those which resonated with the broader population. They imposed these
goals on local bureaucrats by designing institutions like the local EPAs
that have to fine and regulate local firms in order to survive and gain
promotion.

Importantly, the field experiment does not have any control over this
utility function. If we were to implement the Weibo treatment in an
institutional framework that did not prioritize pollution harms, we
would not necessarily observe such large treatment effects. Furthermore,
in authoritarian regimes that do not share China's commitment to
responding to citizen concerns, social media activism could well invite
repression and censorship rather than policy change ([@Pan2020How]). I
agree with the authors' assessment that their treatment was ethical in
China, but that analysis depended on China's particular legislation that
privileged and protected this kind of citizen speech. Any application of
the treatment to another state would have to do the same kind of
in-depth analysis to understand whether it would be effective *and*
whether it would expose ordinary people to harm or retaliation.

Second, the kind of general equilibrium analysis that the experiment
engages in is limited to displacement effects among firms. While the
experiment was appropriately designed to test this effect, I did not
find it to be the kind of general equilibrium analysis we should be most
concerned about with this treatment. A priori, I did not think it very
likely that local firms would increase pollution after observing
punishments aimed at other firms. It is possible, but depends on other
firms making a series of judgments about local bureaucrats being
overwhelmed by enforcement actions that I thought are unlikely to be as
great as the Bayesian updating that they could be the next target.

Instead, the equilibrium analysis we need is how companies would respond
after realizing that an external actor is selectively boosting social
media posts. It would seem that local companies and bureaucrats would
not have known that there was a campaign to send more enforcement
actions; were this knowledge to become known, firms might lobby
bureaucrats to ignore these requests because their external nature makes
them illegitimate ([@Buchanan1980Rent]). If bureaucrats are aimed at
appeasing public opinion, then they might become less responsive if they
see these appeals as being artificially generated by an interest group.
In summary, in general equilibrium the policy may not remain effective
over the long term due to counter-lobbying of companies and their
business associations.

Despite these concerns, I remain bullish on the applicability of this
intervention to broader contexts. The effectiveness of the treatment
will likely diminish once companies respond to the change in the policy
environment, but this kind of mitigation is almost a truism given what
we expect rational actors to do when facing serious costs to their
business. The treatment's cost-effectiveness strongly implies that it is
would be a valuable tool for policy change and enforcement. I would end
though with the caution that the implementer must have a good sense of
the risks of the strategy for those who post appeals on social media and
whether they might face repression or censorship as a result.

[^1]: The evaluator also noted "High" confidence.

[^2]: The evaluator also noted "High" confidence.
