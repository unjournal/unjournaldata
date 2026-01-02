---
affiliation:
- id: 0
  organization: Lingnan University
article:
  doi: 10.21428/d28e8e57.bd540428
  elocation-id: banningwildlifeeval1liew
author:
- Jia Huan Liew
bibliography: /tmp/tmp-603zqZqLoPL9l2.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 24
  month: 05
  year: 2023
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 1 of "Banning wildlife trade can boost demand for
  unregulated threatened species" (by Jia Huan Liew)
uri: "https://unjournal.pubpub.org/pub/banningwildlifeeval1liew"
---

This is an evaluation of Kubo et al ([@temp_id_46591174058413976]).

# Summary measures 

**Overall assessment**

Answer: 75/100

Confidence (from 0 - 5): 5

**Quality scale rating**

"On a 'scale of journals', what 'quality of journal' should this be
published in?: Note: 0= lowest/none, 5= highest/best"

Answer: 3

Confidence (from 0 - 5): 5

See
[HERE](https://unjournal.pubpub.org/dash/pub/banning-wildlife-eval-summ/overview "null")
for a more detailed breakdown of the evaluators' ratings and
predictions.

# Written report

Kubo et al assessed the possible impacts of wildlife trade bans on
non-target species using an online auction dataset spanning 10-years.
The authors demonstrated spillover effects in the form of increased
trade volume involving closely related species. The spillover effects
differed between the three broad groups studied, leading the authors to
posit that spillover effects may differ as a function of demand for the
banned species, as well as the availability of legal alternatives in the
market. Overall, I thought that this is an interesting and topical paper
that provides important support for anecdotes of unintended negative
outcomes from trade bans. I was also intrigued by the authors'
application of synthetic difference-in-differences (SDID) which seemed a
potentially powerful method for assessing the broad effects of policy
decisions.

Despite my general appreciation of this work, I feel that the evidence
supporting the authors' overarching conclusion was not presented with
sufficient clarity. This is because the modelling approach is fairly
advanced, yet the details provided were too scant.

The most important component of this study, in my opinion, lies in the
authors' selection of "spillover" and "control" species, as I expect
this to be highly influential on SDID outcomes. For "spillover" species,
I recommend the authors better justify their selection by explaining,
from a buyer's point-of-view, why these would be realistic alternatives.
The authors provide strong justification for giant water bugs (i.e.,
same market name), but not for salamanders and freshwater fish.
"Spillover" species for the latter two were close-relatives, which could
be a reasonable choice if the authors cite evidence to establish the
logic that underlies a potential buyer's decision to choose
phylogenetically close alternatives in the event of a ban. As these are
likely to be kept as pets, perhaps other species traits (e.g.,
appearance, size) that may not necessarily be linked to phylogeny may be
more important? To clarify, I do not believe that the authors' approach
is wrong. I do, however, suggest the authors better explain their
selection process.

Relatedly, "control" units were defined as "trades in the same
categories as banned species, excluding potential spillover species"
(Page 12, Paragraph 2). This is too vague for readers to follow and
potentially replicate. I could not deduce what the term "categories"
refer to. The identities of top control units were detailed in Fig S2
and Fig S4, but the texts were in Japanese (Fig S2) or too small to read
(S4). From what I could tell, some of the control units were congeners
of the banned salamander species and selected "spillovers". I therefore
wondered about how phylogenetic relatedness of "spillover" species were
ranked and how the authors decided that spillover effects would not also
affect the trade of "control" species.

With my admittedly limited understanding of SDID, I am also wondering if
the issues regarding "spillover" and "control" species selection could
have been averted if the authors use an unrelated group of animals
(e.g., turtles) to parameterise their synthetic controls, assuming this
group was not subject to similar bans. This may also help overcome the
potential issue of any spillover effects in the currently selected
"control" units which could obfuscate the estimation of DiD values. If
the appeal of SDID was the allowance for differences in trend between
intervention and control groups before the ban, do control units need to
be close relatives of the spillover species?

I appreciate the novelty of applying SDID, but I am concerned that there
is insufficient context to ease comprehension if this work were to be
submitted to journals with a broader readership. I think the description
of Eq. 1 as a method to solving the "minimisation problem" epitomises my
concern. I could be in the minority, but "minimisation" is not a term I
encounter frequently in my reading. Therefore, I did not initially
understand why there was a "minimisation problem" that had to be solved,
much less understand how to solve it. I suggest the authors provide a
brief explanation about what SDID (or even DiD) achieves in simpler
terms (e.g., assess the effects of interventions by comparing observed
outcomes against predicted outcomes representing non-intervention).

I liked the figures presented in this paper. In particular, I appreciate
the clean aesthetics of the plots presented here. However, figures
depicting outcomes of SDID in the main text and the supplementary
section can be difficult to decipher without additional details about
the application of SDID (or even of DID and SC). Without prior
knowledge, the captions and text do not provide sufficient information
about what the readers should look out for in the plots on the left side
of Figures 3, S3, and S5. For instance, the caption mentions "arrows"
indicating estimated effects, but the arrows are difficult to see on the
plot. Moreover, I recommend the authors include additional information
about the vertical lines representing ban enforcement, as well as the
significance of trend lines representing post-ban averages and the SDID
synthetic control, respectively. This will make it easier to understand
what the "estimates" in plots on the right of Figures 3, S3, and S5
signify. Relatedly, the captions specify that plots on the right of
these figures represent "estimates concerning trade volumes of each
taxon". In my understanding, these should instead refer to the estimated
spillover effects of the ban? If my interpretation is correct, the
labelling of a 0 value for estimates (i.e., vertical broken line) as
"Trade (n)" is quite confusing. I recommend the use of more precise
descriptions in the plot and captions.

I appreciate the concise nature of the paper. The authors did a good job
of providing key information but I believe that there is some room for
improvement. First, some context about the volume or relative importance
of online auctions as a platform for trading in animals could help
readers better understand the significance and applicability of findings
to the wider wildlife trade. Second, the authors provide additional
information about the relevant policies in the methods section, but this
information may be better placed in earlier parts of the text to avert
confusion about focal species selection. Third, I believe that the
argumentation leading to the authors' conceptualisation of spillover
effects (Fig. 5) can be further developed. The authors argue that
spillover effects may be diluted when more alternatives are available in
the market, but they do not explain what "alternatives" mean in the
context of the wildlife (e.g., pet) trade. The text (page 6) assumes
that animals in the "freshwater taxon" were potential alternatives to
the golden venus chub, while animals within the "salamander taxon" were
potential alternatives to the Tokyo salamander. These assumptions imply
that potential buyers are unlikely to consider taxonomically distant
animals as alternatives to banned species, yet I am unaware of
supporting studies/papers. I recommend the authors provide additional
justification for this assumption, preferably by citing relevant
literature.

Finally, there were several instances of imprecise or unclear writing. I
list these below, along with some suggestions for the authors'
consideration:

> 1\) Page 2: "It activated the underground market" suggests that
> underground markets only came into existence when CITES regulations
> came into effect. Perhaps consider revising to "These regulations
> coincided with a growing underground market".
>
> 2\) Page 2: "Even a few empirical studies have focused on introducing
> trade ban policies on banned species" is a confusing sentence.
> Consider revising to "A small number of empirical studies focus on
> quantifying the effects of trade bans, but the focus was on species
> that were the targets of the ban".
>
> 3\) Page 7: Two sentences about exotic species trade and native
> species policies in developed countries were quite confusing to read.
> I recommend editing the sentences to "An increase in exotic species
> trade can increase overexploitation risk in source countries and lead
> to population declines unless appropriate management is implemented.
> Developing source countries may struggle to cope with the additional
> management needs as they often struggle to implement robust natural
> resource governance".
>
> 4\) Page 9: "evidence regarding cross-country spillovers" seems to be
> a very serious issue but no citations were provided to help readers
> learn more about it. I recommend citing the relevant sources.
>
> 5\) Page 9: "We suggest the development of a database comprising
> banned and non-banned species" is a vague statement that may cover all
> known species. I recommend the authors be more specific, perhaps by
> narrowing the statement down to species known to be in the trade.

In conclusion, I believe that this is a very promising study with an
important, policy-relevant message. However, the paper needs to be
revised for clarity. In particular, additional details about the study's
modelling approach will help improve reader comprehension and strengthen
the authors' argument about the significance of spillover effects from
trade bans.

# Evaluator details

1.  How long have you been in this field?

    -   13 years

2.  How many proposals and papers have you evaluated?

    -   \~60 as a peer-reviewer or editor
