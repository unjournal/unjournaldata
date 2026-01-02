---
affiliation:
- id: 0
  organization: Global Priorities Institute
article:
  elocation-id: authorresponseexistentialrisk
author:
- Philip Trammell
- Leopold Aschenbrenner
bibliography: /tmp/tmp-60u8k436j94pBF.json
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
title: Authors' response to Unjournal evaluations of "Existential Risk
  and Growth"
uri: "https://unjournal.pubpub.org/pub/authorresponseexistentialrisk"
---

Thank you to both evaluators for your comments! We will do our best to
incorporate many of the suggestions into any future revisions. A few
responses are below.

# Seth Benzell 

> The representative agent of the model is neither a normative goal nor
> a positive prediction, making implications nebulous.

I agree; perhaps this should be further emphasized. The paper
essentially finds that X (a tech acceleration) lowers Y (existential
risk) given conditions C (which include \[in some sense\] optimal
policy). Since I certainly find it plausible that C does not hold, the
only concrete implication is that one might do well to assume that X
lowers Y until one has identified how exactly, say, policy failures have
overturned this relationship. But it is a step further removed from a
directly applicable result than would be ideal.

> Omission of savings from the model eliminates a potential mechanism
> for intertemporal consumption smoothing, which may impact demand for
> safety.

Yes, this is an interesting possibility I have thought about a bit but
might be worth looking into further. Given that technology is, on most
accounts, the only driver of long-run growth, I expect that introducing
capital to the model would not much affect the impact of long-term
accelerations. But I expect it would worsen the risk implications of
short-term accelerations to the extent that risk must be mitigated by
specialized capital that must be accumulated in advance (since then an
unexpected jump in technology is all the more costly to mitigate), and
would improve the risk implications of short-term accelerations to the
extent that risk mitigation can be mitigated by general-purpose capital
(since then an unexpected jump in technology can be mitigated by capital
spend-downs that modestly reduce consumption in the future, instead of
sudden large consumption cuts).

> The authors argue that historical \[anthropogenic\][^1] existential
> safety expenditure has been near 0... If I view my enemy as completely
> alien to my values, wouldn't military spending count? An even older
> example could be the... prophets who connected contemporary
> decadence... to a coming disaster, and recommended shifting resources
> to ameliorating religious rituals.

i\. We make the claim that anthropogenic... existential safety
expenditure has risen over time in the context of pointing out that, if
one believes existential risk has risen over time, one must attribute it
to \[a\] rise in the baseline hazard rate rather than to a decline in
safety expenditures. Unless one believes that military and religious
expenditures in the distant past are in fact the reason why
anthropogenic existential risk was unlikely in the distant past, I
believe the argument stands. Perhaps instead of using the term "safety
expenditures", it would be more helpful to refer to expenditures that
seem today in fact to have lowered risk in the past (though this has its
own complications).

ii\. If one does believe that safety expenditures in the relevant sense
have fallen, to the extent that the baseline hazard rate posed by
today's technology is lower than that posed by the technology of the
past (and any risk-increase can be attributed to the fall in safety
expenditures), the headline results are only strengthened, as noted in a
reply to Dr. Bournakis below.

# Ioannis Bournakis

> I think there is a misleading point in not modeling any benefit
> function along with the hazard function. Without considering both
> benefits and potential risks of technology within the same framework,
> it is impossible to identify whether technology induces existential
> catastrophes for society.... Technological advancements have
> contributed to environmental degradation, yet... we can create
> technologies that are more environmentally friendly.

i\. I fully agree that technological advances may lower the hazard rate.
I believe we allow for this in Section 2 and in Appendix A.3 (which
generalizes Section 3): there is only a hazard function 𝛿(A), but 𝛿 may
be locally or indeed globally decreasing in A.

ii\. The exception is Section 3, where for simplicity we focus on a
particular 𝛿(A) that is increasing in A. The result of that section is
that, even here, speeding growth in A lowers 𝛿 after a risk-mitigating
policy response, so I do not see how allowing A to lower 𝛿 directly
would add anything.

> Have the authors considered the case where 𝐴 induces a constant
> hazard, regardless of how quickly the increase occurs?

Yes. The case where each technology level A is associated with a
constant hazard rate, regardless of how quickly the technology
developed, is the case we consider throughout Sections 2 and 3. It is
only in Section 4 that we consider the case that the speed of
technological progress affects the hazard rate. Alternatively, if you
are referring to the possibility that the development of technology A
induces a fixed amount of risk (not a constant hazard rate per unit of
time we linger at technology state A), that is covered by the model of
Section 4 with 𝜁 = 1, as discussed at the end of Section 4.2.

> Does this statement describe the case where the risks posed by two
> events occurring simultaneously are associated with certainty, while
> the sequence of events might induce uncertainty, as we do not know the
> exact intensity of the risk? "One valid criticism of this functional
> form is that it overemphasises a channel through which the risks posed
> by a series of technological developments can be cheaper to mitigate
> if they occur at once than if they occur in sequence."

No. This statement is about the fact that in the model of Section 4, a
given amount of safety spending this year cuts the risk in (say) half
this year, so if you cram in a lot of technological developments this
year instead of spreading it out over the years, you lower the risks
posed by all of them with the single expenditure.

[^1]: The original evaluation read "anthropocentric". Whe suspect this
    was a typo.
