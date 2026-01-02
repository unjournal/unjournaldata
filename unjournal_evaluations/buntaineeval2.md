---
article:
  doi: 10.21428/d28e8e57.4fa081a7
  elocation-id: buntaineeval2
author:
- Anonymous
bibliography: /tmp/tmp-60BH2PfWVq2OFJ.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 09
  month: 08
  year: 2023
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 2 of "Does the Squeaky Wheel Get More Grease? The
  Direct and Indirect Effects of Citizen Participation on Environmental
  Governance in China" (Buntaine et al)
uri: "https://unjournal.pubpub.org/pub/buntaineeval2"
---

# Summary Measures

**Overall Assessment**

Answer: 80

90% CI: (71, 86)

**Quality scale rating**

"On a 'scale of journals', what 'quality of journal' should this be
published in?: Note: 0= lowest/none, 5= highest/best"

Answer: 4.3

90% CI: (3.7, 4.8)

*See the evaluation summary for a more detailed breakdown of the
evaluators' ratings and predictions.*

# Written report

## Overview

This paper presents the results of a randomised control trial examining
the impact of citizens reporting violations of pollution standard (water
and air) by firms in China. Specifically, if a firm is allocated to a
treatment arm and goes on to violate emissions standards, the violation
is reported to the regulator by a citizen acting on behalf of the
experimenters. They broadly find that these reports lead to the
regulator intervening more often, firms polluting less, and these
effects being particularly strong when the citizen report is made public
through social media (T2 vs private reports, T1). Moreover, they are
able to begin to elucidate the mechanisms by which these effects are
bought about (various arms within T1 which vary who the report is sent
to), and show that (at least within prefecture) this is not a zero-sum
game (ie there is no evidence for substantial local leakage). Clearly,
issues regarding air and water pollution are incredibly important, and
this paper *may *offer a way for citizens to reduce the damage these
cause by increasing compliance. In the sense that this paper answers a
large and important question, with a well-thought through and
implemented large-scale RCT of a low-cost intervention it is a
potentially very important contribution.

While I think that this paper will publish very well even in its current
draft, there are points where I think clarification - and less bold
claims - are advisable in the writing and interpretation of the results.
Similarly, the econometric approach is broadly well implemented, but I
think recognition of the pitfalls (primarily regarding the SUTVA
assumption) might be necessary. As noted in the additional comments
regarding open science, it is a shame that the pre-registration included
only details regarding treatments and nothing on how the data were to be
analysed, but I recognise this obviously cannot be changed at this
point. I organise my comments by theme (econometrics, generalisability,
interpretation of results, ease of understanding) and within these
themes order from more to less significant suggested changes.

*\[Evaluation manager: I copy the treatment abbreviations and
descriptions from the original paper for clarification below, as the
evaluator refers to these in their response\] *

-   Control Group (C): "When the CEMS data indicated that the firm
    violated its emission standards, we did not intervene in any way.
    About 1/7 of the CEMS firms were assigned to this group."

-   Private Appeals Group (T1):  "\...  a citizen volunteer filed a
    private appeal against that violation that was not observable by the
    public. About 5/7 of the CEMS firms ..."

-   Public Appeals Group (T2): " ... wrote a post on Weibo  ... and "@"
    the official Weibo account of the corresponding local EPA. ... We
    assigned 1/7 ...."

-   Private Appeals to Regulator via Direct Message on Social Media
    Group (T1A): "\...  sent a private message to the corresponding
    local EPA's official Weibo account, notifying them about the
    pollution violation and requesting that they investigate ...."

-   Private Appeals to Regulator on Government Website Group (T1B):
    "\... filed a private appeal via the 12369 website to the
    corresponding local EPA ... 

-   Private Appeals to Regulator through Government Hotline Group (T1C):
    "\... called the 12369 hotline to privately appeal to the
    corresponding local EPA. In the phone call, she notified the local
    EPA ..." 

-   Private Appeals to Firm through Phone Call (T1D):  "... called the
    violating firm to privately appeal the violation. In the phone call,
    she notified the firm about its violation and requested that they
    check the issue"

## Econometric approach

All prefectures contain some treated firms, but the intensity of
treatment (70% or 95% of firms assigned to treatment) varies so that
they can assess the "general equilibrium" effect of the treatment on
non-treated firms in prefectures with a higher (95%) or lower (75%)
intensity of treatment. This is clearly a very neat experimental design.
However, the motivation for high/low intensity ("indirect effect")
clearly means that the SUTVA assumption across firms does not hold, such
that the difference in outcomes between treated firms and control firms
(those in the remaining 30/5%) captures the sum of the direct effect on
treated firms and the indirect effects on control firms. I therefore
find the comparisons within treatment arms (public vs private, the way
private treatments are implemented), and comparisons of high vs low
intensity prefectures more compelling. To better understand the impact
of this SUTVA violation, it would be nice to see a plot of how control
firm violations vary through time - ie does the onset of treatment lead
to changes in control firms' violations?

Relatedly, the claim that general equilibrium effects are estimated
needs caveating as just local general equilibrium effects are mediated
(at least as discussed in your paper) by the regulator's capacity
constraint. Of course, even including solely these local general
equilibrium effects is still rather novel. But, a key problem in
environmental pollution and policy (eg carbon markets) is the impact of
(global) leakage (policy reduces output but relatively inelastic demand
simply means that this shifts elsewhere). I don't think that your
estimates capture across prefecture leakage, and certainly wouldn't
include leakage beyond China's border. Data on firm-level output might
help mitigate this concern (ie if it shows supply actually is not
constrained), and perhaps the evidence regarding the firms being fully
operational is sufficient (but would need more discussion).

Much more minor comments that are easily addressed: 1) I think estimates
are in effect intent to treat - the ongoing violation reporting outside
of the experiment means control firms experience the "treatment" just
less intensely - and this could be explicitly recognised. I think you
could therefore consider using the treatment as an instrument for
intensity of treatment (receiving a report conditional on a violation)
in a 2SLS approach. 2) I think clustering of the standard errors in the
firm-level analyses should account for the possibility errors are
correlated within the citizen doing the reporting across
firms/prefectures (ie some citizens may \[randomly\] have more or less
impact across all the reports they send) 3) I think standard errors in
table 6  need to be clustered at the firm level to account for multiple
observations through time from different violations by the same firm.

## Generalisability/impact

On P1, you give evidence that lots of different countries have made it
possible for citizens to report violations, yet present little evidence
that citizens then actually do use this tool. You present evidence that
in China citizens do this later (P2) but understanding if your results
are relevant globally would be useful - ie do citizens outside of China
regularly engage in such violation reporting? I note that even if the
paper is only relevant to China, the potential impact/importance of the
paper is still very large. Similarly, given your evidence and the
relatively low cost of implementation, it brings into question why so
much cash is being left on the table, and I think this could be
discussed in the concluding remarks. Perhaps part of the reason for
limited wider take-up is simply how rare the hourly and near real-time
data China releases is. Alternatively, is it because reporting
violations is privately costly but publicly beneficial, similar to
punishment in PGG?

## Interpreting results

It seems to me that it is not possible to ascertain what the effect of
*citizen participation *is through this experiment. Rather, the effects
of the treatments compared with control conditions could be through some
salience-of-information channel, and there is good evidence that
information does matter in other environmental contexts (eg
[@temp_id_8704003764136694]). Indeed, in the pre-registration document
it reads as if there will be an information treatment separate from
citizen reports ("Firms will be assigned to complaint, information, or
control conditions"). This matters only for understanding what drives
your results, and therefore what range of interventions might have led
to similar outcomes. The impact of the Weibo likes could be 1) public
pressure and therefore unrest or 2) information contained within the
idea lots of people think this matters. On p27/28 you present evidence
which suggests social media isn't useful because of it involving more
people per se conditional upon the severity of the violation. It would
be nice to see in this observational data whether more non-treatment
reports tend to be made when the violation is worse (I assume they are),
in which case this would support the possibility that greater public
engagement (likes, number of appeals) normally contains some information
(even though in your treatment it obviously does not). Similarly, you
claim that your results show "social media is an especially effective
way to deliver public appeals" yet you have no comparison for delivering
public appeals with anything other than social media.

Building on the idea of identifying the channels through which effects
occur, my view is that you generally do a really good job of isolating
channels, but this work could be explained better. As well as being
better explained, I would have much appreciated you flagging that you
will deal with the potential concerns when you mention the main effects.
First, I was concerned about the potential for data manipulation, yet
the paragraph on p26/27 details a range of robust evidence that that is
not what is happening. You might also want to look at whether the data
from treated and non-treated firms follows similar leading-digit
distributions, applying Benford's Law as per [@temp_id_7031660687815904]
Climatic Change.\
\
Second, the public vs private effect could operate through several
channels: 

\(1\) firm knowledge;

\(2\) firms feeling consumer pressure; 

\(3\) public pressure on regulators; 

\(4\) speed through the system to the local EPA rather than through the
central report body; 

\(5\) novelty of social media reports; 

\(6\) the role of central government. \

\(1\) can be explored through comparison to the effect observed in T1D
and T1C\*T1D and would appear to not be driving the result (but see
comment in the understanding section RE common knowledge); (2) is dealt
with through T1C and the evidence regarding whether the business is a
final product producer; (4) seems unlikely given the comparator of
results under T1A; (6) is dealt with by the subset of T1A which receive
a threat of central government follow-up. Which leaves (3) and (5). The
former is what you argue to be driving the effect - supported by the
"likes" treatment, while I discuss the data needed to show if there is
extra "novelty" of social media in the next paragraph.

At the moment, it is unclear how much the treatment changes the
probability that a violation is reported by a citizen. In text, the
paper mentions \~300k reports during the treatment period but later
(P18) suggests just \~5.5k of those are actually applicable (identifying
a specific violation etc). Understanding how these relevant
non-treatment induced reports are split would be good: what number are
private vs public? Individual citizen or NGO made? The same individuals
making lots of complaints or many individuals infrequently? Finally, how
are these 5478 valid appeals distributed across the 5366 real violations
that occur during the treatment period - perhaps a histogram of the
number of violations by the number of non-treatment valid appeals that
they get would be useful.

You claim that the fact that effects persist (and if anything appears
stronger) in the medium-term (ie at the end of the 8-month treatment
period) suggests that if the treatments were implemented in the long
term the effect would remain. This seems a little challenging. One could
imagine it getting stronger if there are long-run adaptations they make,
or imagine it weaken if the recipients simply get used to experiencing a
high volume of appeals.

It would perhaps be good to discuss how your results fit in the wider
literature regarding the impact of mandatory disclosure laws to citizens
on firm behaviour (eg [@temp_id_7197310421461056] JEEM). Perhaps they
would also benefit from additional consideration of *how *a party might
reasonably increase the number of appeals - eg could making the
algorithm that you developed to identify the cases of violations be
useful? (which links into my previous comment RE discussing why so much
cash might be being left on the table).

## Ease of understanding

These comments are much more minor, in order in which they appear in the
paper, and I think in general personal taste issues:

-   When you first use the term "appeals" early in the paper (abstract,
    early intro) it is unclear what this means - I would define as
    "appeals in the forms of reports made to the regulator if a
    violation of an emission standard occurs".

-   MEE and MEP are confused in the first parts of the paper before
    Footnote 13 comes in and clarifies MEE replaced MEP

-   Unclear early on why there are multiple regulators - at that stage
    we don't know there is a central monitor and many local regulators

-   I would like to see a diagram of the different actors in this space
    and their roles (MEE/MEP recording and publishing data, operating
    the hotline; local EPAs beneath this policing firms; firms;
    citizens). Perhaps this diagram could also include the incentives
    they face (official and unofficial) - eg are the local EPA legally
    required to investigate every violation? And defined over what
    timescale (hourly or daily violations etc)

-   How you define daily violations given the data and standards seem to
    be at the hourly rate is not quite clear (I assume that it is if
    they had any violation in a 24 hour period)

-   Figure 1 - would be good to have an additional plot which is a
    histogram plot of counts of the number of stacks/firms by number of
    violations that they commit. Fig 1 horizontal axis labels could also
    be better formatted as "1st Jan 2018" etc rather than year end and
    YY/MM/DD

-   Figure 4 - I think this would be better done as a Sankey plot. Using
    the same bins for where firms start, then track where the individual
    firms are in the distribution at the end. (At present, it is unclear
    if all firms are reducing their emissions a bit, or if the violation
    firms are reducing their emissions loads and the other firms
    changing very little).

-   Common knowledge is mentioned, but it is not clear if you're using
    this in the precise definition (the firm knows, the regulator knows,
    and each know that the other party knows) or in a looser way (they
    each know, but are not specifically informed that the other party
    knows). If it is the former, please explain that each party was
    additionally informed that the other party knew (in T1C\*T1D) or if
    the latter please use a different term.
