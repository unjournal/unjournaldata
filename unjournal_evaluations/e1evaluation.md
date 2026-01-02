---
article:
  doi: 10.21428/d28e8e57.bfae2fbd/2387e2c6
  elocation-id: 7ap0zmbj
author:
- Anonymous
bibliography: /tmp/tmp-60pbtghIbg1dNg.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 30
  month: 10
  year: 2023
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: "Evaluation 1 of \"Money (Not) to Burn: Payments for Ecosystem
  Services to Reduce Crop Residue Burning\""
uri: "https://unjournal.pubpub.org/pub/7ap0zmbj"
---

# Summary measures

## **Overall assessment**

Answer: 90/100

90% CI: (75,95)

## **Quality scale rating**

"On a 'scale of journals', what 'quality of journal' should this be
published in?: Note: 0= lowest/none, 5= highest/best"

Answer: 5

90% CI: (2, 5)

[**See
here**](https://unjournal.pubpub.org/pub/jackevalsum/release/1 "null")
for a more detailed breakdown of the evaluators' ratings and
predictions.

# Written report

## **Summary**

This paper presents a randomized evaluation of a new intervention to
target air pollution: paying farmers in North India not to burn crop
stubble. Air pollution is a tremendous public health concern in India,
and stubble burning (in order to quickly clear the field for winter
planting) is one of the biggest contributors to PM pollution in North
India. Both bans on stubble burning and subsidizing alternatives have
failed to gain traction, and so this paper aims to test a new
intervention to see whether it can address the problem. Farmers were
promised a *payment for ecosystem services* (PES) contract in which they
would be paid if they could verify that they did not burn their crop
stubble before winter planting. There were two broad treatments:
*standard PES*, in which the payment was entirely conditional, and
*upfront PES*, in which farmers who agreed to the contract were paid
part of the contract value as an unconditional upfront payment. The
authors found that the upfront PES contract reduced stubble burning by
10 percentage points, whereas standard PES had no effect. They calculate
that upfront PES saves a life for \$3,000-\$4,400, which is much lower
than the mortality cost of crop burning and much cheaper than other
pollution abatement opportunities.

## **Assessment**

This paper identifies a politically feasible and cost-effective solution
to a major public health problem. Libraries could be filled with studies
showing negative effects of air pollution, but there are far fewer
studies that propose solutions that could actually be implemented in
developing countries today, and test them with an RCT. This aspect alone
makes the paper an amazing contribution to our knowledge.

Moreover, while this goes beyond the scope of the paper and into
speculative territory, the upfront PES contract they describe has a lot
of potential at scale. First, if it was implemented at scale and had a
history of reliable payments, it would increase trust among farmers that
they would actually be paid for not burning their stubble. Second,
having the carrot of PES payments for not burning stubble would make the
stick of punishing stubble burning more credible; it's impossible to
punish the 90% of farmers who burn their stubble, but if that percentage
was 78% or even lower, it would be more feasible. Finally, scaling this
intervention could increase learning about alternative crop residue
management (CRM) techniques and make farmers more likely to adopt them.
As a bonus, it does not require legal enforcement capacity and thus
could be arranged by a nonprofit as well as by the government.

Furthermore, the results are far from a black box---the authors have a
lot of data on farmer heterogeneity that can be used to get close to
understanding their results. Understanding how farmers respond to
regulations and incentives is important in many settings beyond stubble
burning, and the authors' data allows us to get closer to understanding
farmer decision making. Even specific to stubble burning, the authors
are able to focus on the difference between in-situ and ex-situ CRM
techniques and thus show that ex-situ CRM is the way to go for
policymakers.

In short, this paper cleanly identifies an attractive policy that solves
a big problem---nothing in the next section takes away from that.

## **Suggestions**

There are a few ways in which the paper could be improved:

1.  **The paper does not address a puzzle; why do experienced farmers
    have negative beliefs about alternative CRM?**

    1.  75% of study-enrolled farmers have tried non-burning CRM
        techniques (Table A.1), and they show negative beliefs about
        those techniques (Table 1), but the study finds no effect of the
        program on winter cropping time or yields. If alternative CRM
        has no negative effects, why do *experienced* farmers have
        negative beliefs about it?

    2.  It's possible that the intent-to-treat shown in Table A.8
        underestimates the negative effects on yield because of the
        large number of never-takers (since 78% of the upfront PES group
        also burned their stubble). One important check would be to use
        randomization into the upfront PES group as an instrument for
        using alternative CRM, and thus estimate the effect of
        alternative CRM on winter yields and delays. It's possible that
        this approach would find a significant negative effect of
        alternative CRM and thus validate farmers' negative beliefs
        about CRM.

    3.  Another possibility is that the farmers who complied with the
        treatment (in the IV sense, not in the sense that they followed
        the contract) selected into compliance because of idiosyncratic
        shocks to their kharif harvest time. Farmers who saw their
        kharif harvest come early would have a lower cost of doing
        alternative CRM (less risk of delays), and that could have
        induced them to comply with upfront PES. This should be
        measurable - did farmers who requested checks of their fields
        (and thus didn't burn) do so earlier than farmers who burned
        their stubble (according to either spot checks or machine
        learning)? This could be used to estimate a selection model
        similar to [Suri
        (2011)](https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA7749)
        to understand the importance of heterogeneous costs to farmers
        choosing whether to comply with upfront PES or not.

2.  **The paper could do more to identify the mechanism behind why
    upfront PES works when standard PES fails.**

    1.  One way that the authors could extract more information from the
        existing sample is to use the kappa-weighting procedure of
        [Abadie
        (2003)](https://economics.mit.edu/sites/default/files/publications/Semiparametric%20instrumental%20Variable.pdf)
        to compare the mean characteristics of compliers and
        never-takers. (Here, I mean compliers in the IV sense, not
        farmers who followed the contract.) In particular,
        kappa-weighting could be used to answer some questions that
        illustrate why upfront PES works:

        1.  Do compliers have less negative beliefs about alternative
            CRM than never-takers?

        2.  Are compliers more likely to report that cash constraints
            play a role in their CRM decisions than never-takers?

        3.  Are compliers more likely to trust that they will be repaid
            than never-takers?

    2.  Understanding the mechanism behind these effects is first-order,
        not just because they help us make sense of the results, but
        because they can improve targeting and cost-effectiveness of an
        upfront PES contract. Targeting the payments at farmers who are
        most likely to be marginal minimizes the payments made to
        farmers who will eventually burn their stubble anyway.

3.  **The cost-effectiveness calculations could include climate
    co-benefits from reduced stubble burning.**

    1.  [Venkatramanan et al
        (2021)](https://www.frontiersin.org/articles/10.3389/fenrg.2020.614212/full)
        estimate that stubble burning of rice, wheat and sugarcane
        across India caused 9.1 million tons of CO2-equivalent emissions
        (CO2e) in 2017, based on methane and nitrous oxide release.

    2.  With the authors' estimate that 8.8 million acres of farmland
        are burned each year, this means that burning one acre is
        responsible for 1.034 tons of CO2e.

    3.  Since upfront PES results in an acre unburned for \$34-\$51,
        this means that upfront PES averts a ton of CO2e for \$34-\$51,
        which is below nearly all estimates of social cost of carbon.

    4.  Thus, upfront PES has benefits that exceed costs even without
        considering air pollution. It is worth including these estimates
        as part of the cost-effectiveness calculation.

4.  **The paper does not account for machine learning prediction error
    in its inference.**

    1.  The main outcome of interest, crop burning, is mostly not
        measured directly but rather is the prediction of a machine
        learning model. While it is common practice to treat machine
        learning predictions as perfectly measured, it is not a good
        practice and can severely bias the results. Critically, this is
        *non-classical* measurement error. Although economists are used
        to thinking about classical measurement error in the dependent
        variable as being innocuous, prediction error in this case is
        non-classical in the sense explained below.

    2.  This particular kind of error causes problems for both point
        estimates and inference. The first issue is that it causes
        attenuation bias in the estimates: many plots are randomly
        misclassified, so the treatment will mechanically be less
        correlated with any particular classification. (See [these
        notes](https://econ.lse.ac.uk/staff/spischke/ec524/Merr_new.pdf "null"),
        page 11 for more details.) This would make the authors\'
        estimates conservative, which is not a problem for their main
        conclusion - though it is still desirable to fix, and would show
        their treatment to be even more cost-effective.

    3.  However, the second issue *is* a problem for their conclusions.
        The conventional standard errors they use are too small to
        capture the true uncertainty in the treatment effect estimates,
        because they fail to take into account prediction errors by the
        machine learning model. This could potentially cause them to
        over-reject the null of no treatment effect. (Although, the net
        effect of this and the attenuation bias above is ambiguous.)

    4.  As a simple intuition check, imagine that the machine learning
        model simply classified plots at random. Then the treatment
        effect estimate would be uncertain not just because of sampling
        randomness, but because of the randomness in which plots were
        classified as burned or non-burned (which obviously affects the
        estimate). However, the standard errors would not take into
        account the second type of randomness and would thus be too
        small. 

    5.  The model in this paper obviously does better than random
        chance, but there is nothing special about that example; as long
        as the model\'s accuracy is not 100%, there is uncertainty over
        which plots were classified accurately. The standard errors do
        not recognize this kind of uncertainty - they effectively assume
        that the model\'s accuracy is 100%, and thus artificially shrink
        variance in the treatment effect estimates.

    6.  This issue can be fixed in different ways. If the authors don\'t
        care about the attenuation bias (which cannot reverse their
        conclusions) and only want to fix the inference issues, the
        simplest approach is a bootstrap, using different subsamples of
        the ground truth burning data to train different models and
        using the distribution of treatment effects to construct
        standard errors. But my non-expert reading of the statistics
        literature is that the efficient approach is the one constructed
        by [Chakrabortty and Cai
        (2017)](https://arxiv.org/abs/1701.04889 "null"), which will
        improve both estimation and inference.

# Evaluator details

1.  How long have you been in this field?

Two years

2.  How many proposals, papers, and projects have you evaluated/reviewed
    (for journals, grants, or other peer-review)?

Zero

# Works Cited:

Abadie, Alberto. 2003. "Semiparametric Instrumental Variable Estimation
of Treatment Response Models." *Journal of Econometrics* 113(2):
231--63. [@abadie2003semiparametric]

Angelopoulos, Anastasios N. et al. 2023. "Prediction-Powered Inference."
<http://arxiv.org/abs/2301.09633> (October 30, 2023).
[@angelopoulos2023prediction]

Chakrabortty, Abhishek, and Tianxi Cai. 2018. "Efficient and Adaptive
Linear Regression in Semi-Supervised Settings." *The Annals of
Statistics* 46(4). <http://arxiv.org/abs/1701.04889> (October 30, 2023).
[@chakrabortty2018efficient]

Suri, Tavneet. 2011. "Selection and Comparative Advantage in Technology
Adoption." *Econometrica* 79(1): 159--209. [@suri2011selection]

Venkatramanan, V., Shachi Shah, Ashutosh Kumar Rai, and Ram Prasad.
2021. "Nexus Between Crop Residue Burning, Bioeconomy and Sustainable
Development Goals Over North-Western India." *Frontiers in Energy
Research* 8.
<https://www.frontiersin.org/articles/10.3389/fenrg.2020.614212>
(October 30, 2023). [@venkatramanan2021nexus]
