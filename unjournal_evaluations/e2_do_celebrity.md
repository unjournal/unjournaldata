---
article:
  doi: 10.21428/d28e8e57.f5b7e124/6edcc86d
  elocation-id: 2sfao90j
author:
- Anirudh Tagat
bibliography: /tmp/tmp-60xySCqmjL1FWC.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 25
  month: 08
  year: 2023
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 2 of "Do Celebrity Endorsements Matter? A Twitter
  Experiment Promoting Vaccination In Indonesia"
uri: "https://unjournal.pubpub.org/pub/2sfao90j"
---

# Summary Measures

**Overall assessment**

Answer: 85

Confidence (from 0 - 5): 4

**Quality scale rating**

"On a 'scale of journals', what 'quality of journal' should this be
published in?: *Note: 0= lowest/none, 5= highest/best"*

Answer: 4

Confidence (from 0 - 5): 5

*See the evaluation summary for a more detailed breakdown of the
evaluators' ratings and predictions.*

# Written report

***Note from David Reinstein, Evaluation Manager: ***This evaluator
considered the May 2023 (MIT) working paper version titled "[Do
Celebrity Endorsements Matter: A Twitter Experiment Promoting
Vaccination In
Indonesia](https://economics.mit.edu/sites/default/files/2023-05/Indonesia_Twitter_Paper.pdf "null")"

**Brief explanation:**

1.  This paper is important for understanding how celebrities and in
    general, influencers could play a role in health communication in a
    developing country context (Indonesia). It provides a novel and
    carefully designed experiment where celebrities post messages on
    Twitter that are intended to boost immunization rates and awareness
    in the country.

2.  It is grounded in a rigorous theory drawing from network science as
    well as the economics of networks, and makes a clear contribution to
    newer applications of network theory in the realm of applied
    economics work.

3.  The empirical framework aims to cover various aspects of how the
    intervention that the authors implemented might operate, focusing in
    detail on potential mechanisms (as explained by their theoretical
    framework), as well as on two main questions: (a) what
    characteristics of a message have the most reach; and (b) whether
    seeing these messages has some downstream impact on knowledge and
    beliefs around immunization.

4.  The paper is well written and clearly a very rigorously conducted
    experiment that has tremendous value to those working in health
    policy and health communication. In terms of causal inference,
    however, there are a few concerns that the authors could take into
    account to strengthen the confidence in their results, especially
    those surrounding the impact of these messages on knowledge and
    beliefs ("offline sample").

**Summary:**

This paper looks at the impact of celebrity endorsements on Twitter
related to immunization in Indonesia. The authors recruited 46
celebrities and 1032 ordinary citizens to participate in their study,
and randomly assigned each of them to tweet a message around
immunization practice during the July 2015 to February 2016. This allows
authors to exploit randomized variation in the messages to study
important and relatively unexplored aspects of how messages are passed
on within large networks (especially networks formed on social media
platforms such as Twitter). They vary the timing of the tweet, who it is
originally composed by (an ordinary citizen or a celebrity), and whether
or not the tweet had a source attached. This type of randomization is
important because it allows one to disentangle the *endorsement* effect
from the *reach* effect, an important contribution of this paper. The
endorsement effect refers to the response to a celebrity directly
tweeting a particular message, whereas the reach effect refers to the
response when the celebrity simply re-tweets the message that was posted
by an ordinary citizen. This effect is important to disentangle using
careful randomization since doing so using observational
data/econometric methods is challenging. Given that the authors had an
opportunity to randomize, they are able to distinguish this. From a
methodological perspective, this is a significant value addition to
emerging work that uses social media data to study a range of issues
including polarization, misinformation, and message diffusion (the topic
of this paper).

The paper has some important findings:

-   Messages that come (originally) from celebrities are more likely to
    be engaged with (retweeted or liked), relative to those that come
    from ordinary citizens. This finding is important to understand how
    celebrities (and their endorsements) are central to maximizing the
    reach and engagement of public health messaging via social media.

-   The second finding is that including a source in the message (which
    the authors refer to in their design as the credible sourcing
    treatment) actually reduces the likelihood of engaging with a
    message. This is counterintuitive (as the authors admit), since
    adding an information source should ideally boost the likelihood of
    engagement, not reduce it. They do well to use their theoretical
    framework to explain that this might be on account of the lack or
    originality associated with a message that comes with a source. By
    introducing this variation randomly, the authors are better able to
    build on the value of celebrity endorsements, by also being able to
    study *what type* of message is likely to get the most reach and
    engagement when it comes to health communication in Indonesia.

-   Last, they find that being exposed to these messages increases
    vaccine-related knowledge, promotes accurate and scientific beliefs
    around immunisation, and has better recall (i.e., that participants
    are more likely to recall the associated hashtag). This last piece
    of evidence is actually the most critical to public health, since it
    suggests that such campaigns can have measurable real-world impacts,
    outside of the social media platform on which such interventions can
    be designed and implemented.

Here, I restrict my comments primarily to the causal inference aspects
of the paper, and potentially ruling out other explanations for the
results.

-   Overall, given the count outcomes data used, the Poisson regression
    model is a reasonable choice for estimation framework, and they also
    use a rigorous method to control for multiple hypothesis testing.
    However, they would do well to attempt to use existing methods that
    take into account a similar approach (e.g.,
    [@temp_id_2294109343475823]).

-   First, in modelling the user response to a tweet (whether it comes
    from a celebrity or another ordinary citizen), the authors
    acknowledge the potential endogeneity arising from how much the
    message has been retweeted or liked *at the time* that the user saw
    the message. It is of course challenging to do this, but using
    timestamps, there could potentially be a way to account for the
    immediately preceding reach or engagement that the tweet received as
    this could influence to a large extent whether a user chooses to
    like or retweet the message. They attempt an exercise similar to
    this in Table E.1 (in Appendix E of the 2023 working papers), but it
    proceeds with arbitrary linear thresholds (i.e., 5, 10, 15 tweets),
    whereas it should ideally enter as a continuous variable in this
    estimation.

-   It also could help link this work to other work in computer science
    and networks on how messages go viral ([@temp_id_365114411641386]),
    which suggests that tweet engagement is likely to be a function of
    emotions and may not always follow a clear chain as described in the
    paper. These may not be mutually exclusive per se, but I suspect
    that incorporating emotions in the model may be challenging as they
    can perhaps only be primed in the messages (e.g., an emotional
    appeal could be another treatment group that was randomly varied).

-   Second, tweet engagement is also strongly determined by the Twitter
    algorithm, which we have no clear idea of. This means that the fact
    that a user sees or engages with a tweet is not solely due to the
    fact that a certain number of people tweeted it, but also how the
    algorithm weights the importance of that tweet to audiences that may
    or may not have mutual network nodes with those sharing the content.
    The authors make a mention of how the feed works and also note
    changes in the algorithm in a period around their study (footnote
    10), but it remains unclear if the implemented randomization
    translates uniformly to all Twitter users in Indonesia. This brings
    me to the main issue with the suggestive evidence provided on
    impacts of this intervention on the "offline" sample using phone
    surveys. The authors acknowledge the limitations of this, but I
    think they need to also emphasize that these are mainly correlations
    and **cannot** trace any causality back to their interventions,
    which is an important limitation of this study, given that the
    offline data relies on self-report information related to knowledge
    and beliefs around vaccination.

-   One way to overcome this is to perhaps use secondary data (if
    available) on child immunization per capita correlated with the
    regions where the hashtag #AyoImmunisasi received the most
    engagement. This data may not be public, but given access to the
    API, it may be possible to correlate the two.

-   Translating online engagement to offline behaviour is without a
    doubt challenging, and a very ambitious ask for a project that
    already has quite a bit of novelty and rigor in terms of
    experimental design and inference. However, it helps to go beyond
    self-report data, and also correlate with whether such knowledge and
    beliefs might have changed owing to the large-scale social media
    campaign (for which panel data from users before and after the
    Twitter intervention would be needed).

Two other minor things to consider in terms of the validity of the
design:

1.  Can users (including celebrities) delete the tweet once it is sent
    out as part of their participation in the experiment? This would
    also affect the extent to which it has reach or engagement. If
    authors could report on whether this was possible (which I suspect
    it was, although recruited individuals may have had to agree to not
    delete the content after it was tweeted).

2.  Finally, in an older version of the paper (NBER working paper,
    2019), estimation of equation 3.3 was conditioned on a sample of
    individuals who followed at least 3 celebrities. It was not clear
    how this criteria was developed. I could not find this in the most
    recently updated version (2023).

Overall, this paper offers important and critical information on
effectiveness of public health messaging via social media. It also helps
to disentangle important aspects of reach vs. engagement in social
media, when those with power on these platforms send out messages, and
precisely the channel through which one might expect diffusion. The
offline sample results, although important from a public health outcomes
perspective, are correlational in nature, and can be ideally put down as
a supplementary part of the paper or bolstered with some secondary data
on immunizations before and after the intervention.

# Evaluator details

1.  How long have you been in this field?

    -   I am 2 years post-doc, and have been working in applied
        microeconomics in a developing country context (India) since
        2014, and have been working on health policy and communication
        (with a focus on behavioural science) since 2020.

2.  How many proposals and papers have you evaluated?

    -   For the Unjournal, I have been managing editor on one other
        evaluation, and have evaluated one other paper. As a peer
        reviewer, I have done about 25 papers, largely in the domain of
        health and applied economics. I am also currently Deputy Editor
        at South Asia Research, where I edit papers in economics.
