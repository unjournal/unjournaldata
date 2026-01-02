---
article:
  doi: 10.21428/d28e8e57.4c60aac3/cdf00ea1
  elocation-id: eval2allfed
author:
- Anca Hanea
bibliography: /tmp/tmp-606UqEflhh22Dw.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 12
  month: 05
  year: 2023
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: "Evaluation 2: \"Long term cost-effectiveness of resilient foods
  for global catastrophes compared to artificial general intelligence\""
uri: "https://unjournal.pubpub.org/pub/eval2allfed"
---

This is an evaluation of Denkenberger et al [@temp_id_2588658881117145].

## Summary Measures

### Overall Assessment

Answer: 80

90% CI: (60,90)

### Quality Scale Rating

"On a 'scale of journals', what 'quality of journal' should this be
published in?: Note: 0= lowest/none, 5= highest/best"

Answer: 4

90% CI: (3, 5)

See [HERE](https://unjournal.pubpub.org/pub/y2a1lbzv/ "null") for a more
detailed breakdown of the evaluators' ratings and predictions.

## Written Report

I really enjoyed reading this paper and I did learn a lot as well, so
thank you for putting it together. It is a very clearly presented, very
dense piece of research. My area of expertise however is risk and
decision analysis under uncertainty. I am a probabilistic modeller with
loads of experience in structured expert judgement used to quantify
uncertainty when data are sparse or lacking. My evaluation will
therefore not cover the application area as such, as I have no
experience with catastrophic or existential risk. I assume the cited
literature is appropriate and not a non-representative sample, but I did
not spend time verifying this assumption.

At a first read, both the title and the abstract left me wondering if
the present analysis compares cost-effectiveness (of resilient foods)
with safety (of AGI), which would've been a strange comparison to make.
However, after reading the very clear (and dense) Introduction, things
became very clear. The only minor comment I have about the Introduction
is that it sounds more ambitious than what the results provide with
respect to the second objective.

The Methods section is well organised and documented, but once in a
while it lacks clarity and it uses terminology that may or may not be
appropriate. Here's a list of things Ii found a bit confusing:

-   Terminology 

    -   the first sentence mentioned "parameters" without the context of
        what these parameters may be (sometimes random variables are
        called parameters, some other times the parameters of a
        distribution are referred to as parameters, etc)  

    -   The probability distribution of the "expected cost
        effectiveness". Is "expected" in this context meant in a
        probabilistic sense, i.e., the expectation of the random
        variable "cost effectiveness"?

    -   The submodels for food and AGI are said to be "independent"; is
        this meant in a probabilistic way? Are there no hidden/not
        modelled variables that influence both?

    -   The "expert" model was quite confusing for me, maybe because
        "Sandberg" and the reference number after "Sandberg" don't
        match, or maybe because I was expecting a survey vs. expert
        judgement quantification of uncertainty. As I said (structured)
        expert judgement is one of my interests ([@nrp8vwuk60g]).

    -   In the caption of fig 2, "index nodes" and "variable nodes" are
        introduced. Index nodes are later described, but I don\'t think
        I understood what was meant by "variable" nodes. Aren't all
        probabilistic nodes variable?

-   Underlying assumptions/definitions

    -   Throughout the methods section I missed a table with a list of
        all variables, how where they measured, on what sort of scale,
        or using what formula, where were they quantified from (data,
        surveys, literature +reference, and if taken from other studies,
        what were the limitations of those studies)

    -   Some of the parameters of the, say, Beta distributions are
        mentioned but not justified

    -   The structure of the models is not discussed. How did you decide
        that this is a robust structure (no sensitivity to structure
        performed as far as I understood)

    -   What is meant  by "the data from surveys was used directly
        instead of constructing continuous distributions"?

    -   The arcs in Fig 1 are unclear, some of them seem misplaced,
        while others seem to be missing. This can be a misunderstanding
        from my part, so maybe more text about Fig.1 would help.

    -   It is unclear if the compiled data sets are compatible. I think
        the quantification of the model should be documented better or
        in a more compact way.

The Results section is very clear and neatly presented and I did enjoy
the discussion on the several types of uncertainty.

It is great that the models are available upon request, but it would be
even better if they would be public so the computational reproducibility
could be evaluated as well. 

Some of the references are missing links in the text, and at least one
does not link to the desired bibitem.\
