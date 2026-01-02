---
affiliation:
- id: 0
  organization: UC Berkeley
article:
  elocation-id: e2fundraisingcharitablegivingreiley
author:
- David Reiley
bibliography: /tmp/tmp-601wg9pxAzBk2r.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: Evaluation 2 of "Does online fundraising increase charitable
  giving? A nationwide field experiment on Facebook"
uri: "https://unjournal.pubpub.org/pub/e2fundraisingcharitablegivingreiley"
---

# Abstract 

The experiment is a well-designed example of geographic randomization to
measure the treatment effects of an advertising campaign.\
\
The authors demonstrate a marginally significant ATE.  They also
demonstrate large, positive, significant spillover effects across
geographically close postal codes, indicating that their ATE is a lower
bound on the truth.  I would like to see more exploration of this
result, because it is a surprisingly large effect.\
\
I love that the authors measure the final outcome of actual donations
made, instead of some intermediate proxy, because I am never confident
that a proxy actually tells us what researchers want it to tell us about
final outcomes.   But I think the authors might be more careful to
present confidence intervals and point out how much statistical
uncertainty they have in their estimates.

# Summary Measures

We asked evaluators to give some overall assessments, in addition to
ratings across a range of criteria. *See the *[*evaluation summary
"metrics"*](https://unjournal.pubpub.org/pub/evalsumfundraisingcharitablegiving#metrics "null")*
for a more detailed breakdown of this. See these ratings in the context
of all Unjournal ratings, with some analysis, in our *[*data
presentation
here.*](https://unjournal.github.io/unjournaldata/chapters/evaluation_data_analysis.html#basic-presentation "null")[^1]*
*

+-------------------+-------------------+---+
|                   | **Rating**        | * |
|                   |                   | * |
|                   |                   | 9 |
|                   |                   | 0 |
|                   |                   | % |
|                   |                   | C |
|                   |                   | r |
|                   |                   | e |
|                   |                   | d |
|                   |                   | i |
|                   |                   | b |
|                   |                   | l |
|                   |                   | e |
|                   |                   | I |
|                   |                   | n |
|                   |                   | t |
|                   |                   | e |
|                   |                   | r |
|                   |                   | v |
|                   |                   | a |
|                   |                   | l |
|                   |                   | * |
|                   |                   | * |
+===================+===================+===+
| **Overall         | 90/100            | 8 |
| assessment **     |                   | 5 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 9 |
|                   |                   | 5 |
+-------------------+-------------------+---+
| **Journal rank    | 4.5/5             | 3 |
| tier, normative   |                   | . |
| rating**          |                   | 9 |
|                   |                   |   |
|                   |                   | - |
|                   |                   | 4 |
|                   |                   | . |
|                   |                   | 7 |
+-------------------+-------------------+---+

**Overall assessment **(See footnote[^2])

**Journal rank tier, normative rating (0-5): ** On a 'scale of
journals', what 'quality of journal' should this be published in?[^3]
*Note: 0= lowest/none, 5= highest/best. *

# Claim identification and assessment [^4]

## I. Identify the most important and impactful factual claim this research makes[^5] {#i-identify-the-most-important-and-impactful-factual-claim-this-research-makes}

To me, the most stunning result in the paper is the measurement of huge
geographic spillovers in a geo-randomized advertising experiment on
Facebook in Germany.  The primary research question was to ask the
average treatment effect for an ad campaign on donations for the charity
Save the Children.  The ATE was barely statistically significant, as I
would expect from my years of working in this area, because these
questions are hard to answer.  But the secondary question about
spillovers shows an indirect effect (the effect of treating neighboring
postal codes) that is ten times higher than the direct effect (the
effect of treating one's own postal code).  Though the randomization was
set up to answer the primary question, it also creates a lot of
randomness in the share of neighboring postal codes that were treated,
and the authors exploit that variation to ask the spillover question.  
Assuming it is true, this spillover effect is creating a large downward
bias on the estimated main treatment effect.

## II. To what extent do you \*believe\* the claim you stated above?[^6] {#ii-to-what-extent-do-you-believe-the-claim-you-stated-above}

I think the claim is probably true, but I worry that it may be
exaggerated by the choice of functional form.   I cannot find any
concrete reason I expect the claim to be false, but the spillover
effects seem implausibly huge to me.  I believe the geographic
randomization was likely done well, so I have very little doubt about
the measurement of the main average treatment effect (a simple
difference in means gives no room for specification searching), but the
spillover result relies on a number of arbitrary assumptions, such as
the distance over which spillovers can versus cannot occur, and the
functional form through which we measure these spillover effects.  

## III. Suggested robustness checks[^7] {#iii-suggested-robustness-checks}

I would like to know whether the huge result is robust to different
variations on the arbitrary assumptions chosen by the authors.
 Differences in the distance threshold.  Allowing the spillover effect
to vary continuously with distance, rather than being a step function
that is "on" if the neighboring postal code is within 30km and "off"
otherwise.  Modeling the spillover effect not just as proportional to
the share of treated neighboring postal codes, but as proportional to
the share of population that was treated in the neighboring postal
codes.

## IV. Important 'implication', policy, credibility[^8] {#iv-important-implication-policy-credibility}

If true, the spillover claim means that the Facebook ad campaign might
be much more effective than what was measured in the main average
treatment effect.   If this is a generally true phenomenon in digital
advertising, it means that folks are generally underestimating the
effects of advertising with geo-experiments, so ad campaigns might be a
lot more effective (3x, 5x, 10x) than has been typically measured in
advertising experiments.

# Written report

This paper [@n3jjuzq0yre] implements a geo-randomized experiment in
Facebook advertising to solicit donations to the charity Save the
Children. 8000 German zipcodes were randomized between treatment
(receiving an advertisement) and control. In addition, the treatment
group was randomized into four different subtreatments to explore the
value of two different types of video-ad creatives and two different
advertising-algorithm strategies.

## Contents

[**Comments on the Main Analysis (Table
2)**](#comments-on-the-main-analysis-table-2)

> [**Fishing for Statistical
> Significance**](#fishing-for-statistical-significance)
>
> [Transforming the outcome
> variable](#transforming-the-outcome-variable)
>
> [Length of measurement window](#length-of-measurement-window)
>
> [**Using Covariates, Especially Lagged Y, to Improve
> Precision**](#using-covariates-especially-lagged-y-to-improve-precision)

[**Spillover Effects from One Location to
Another**](#spillover-effects-from-one-location-to-another)

[**It's Hard to Measure Advertising Effectiveness
Precisely**](#its-hard-to-measure-advertising-effectiveness-precisely)

> [Harder Question #1: Different Advertising
> Strategies](#harder-question-1-different-advertising-strategies)
>
> [Harder Question #2: Impact on Competing
> Charities](#harder-question-2-impact-on-competing-charities)
>
> [Harder Question #3: Measuring
> Profitability](#harder-question-3-measuring-profitability)
>
> [Harder Question #4: Heterogeneous Treatment
> Effects](#harder-question-4-heterogeneous-treatment-effects)
>
> [How can we use HTEs?](#how-can-we-use-htes)

[**Robustness Checks**](#robustness-checks)

> [Randomization Inference](#randomization-inference)
>
> [Length of Measurement Window](#length-of-measurement-window-1)

[**Finding the Data Appendix**](#finding-the-data-appendix)

[**Final Thoughts**](#final-thoughts)

## Comments on the Main Analysis (Table 2)

I begin with the main treatment effects: how much more do individuals
donate when they are treated with advertising than when they are not?
Most of my comments here have to do with the choices made by the
authors, and what this tells me about the degrees of freedom that the
authors may have allowed themselves in their analysis.

### Fishing for Statistical Significance

I congratulate the authors for preregistering their experiment,
including a pre-analysis plan. I have never done this myself, because
during the period of time when pre-registrations started being done for
experiments, I was doing my experiments as a scientist employed by
for-profit companies (Yahoo!, Google, Pandora, SiriusXM). I found that
my employers did not necessarily want there to be a public record of the
experiments I was doing, so they were reluctant to have me put something
into an online database, even if it was supposed to be confidential
until a paper was published. Often I have been lucky enough to convince
my employers to allow me to publish scientifically interesting results,
and I have tried hard to maintain scientific integrity and not publish
articles that were biased in favor of my employer's interests. But I had
enough difficulty getting permission to publish a completed paper, so I
have never tried to fight the internal battle of getting permission to
publish a preregistration of an experiment.

What's great about preregistered pre-analysis plans is that we can often
fool ourselves by making different choices in favor of demonstrating
statistically significant effects. We transform the data by trimming out
outliers. We examine several different outcomes but only publish the
results for one of them. We try a variety of different econometric
specifications, but only publish the one that has the highest
t-statistic on the treatment dummy. Pre-analysis plans require us to
commit to a plan before the data have been collected, so that other
scholars can see that we did not allow ourselves so many degrees of
freedom, and our results are therefore more trustworthy - we don't need
to mentally adjust p-values for the fact that we expect the authors to
have done a bunch of fishing before committing a selective set of
results to paper.

I noticed in this paper that there were a number of deviations from the
pre-registered analysis plan. It's fine with me that researchers often
think of new ideas for analysis once they have started digging into the
data and getting to know it. Sometimes we don't know the right follow-up
question to ask until we have seen the initial results. But if authors
want to get the full benefit from having preregistered their analysis
plan, I think they should be more careful to specify where they have
stuck to the plan, and where they have deviated from it. I will give a a
couple of examples below.

#### Transforming the outcome variable

Footnote 19 argues why the authors chose to trim out (i.e., winsorize)
any location-days with gifts of over 1000 euros. I think this trimming
might not be a good idea. Trimming does reduce variance and give
additional statistical precision, but only if you think that larger
donations shouldn't matter that much to the charity. (In other words,
this decision gives up on the unbiasedness of their estimators in order
to reduce the variance of the estimate.) From footnote 19, I notice that
only 68 location-days were trimmed, out of what I estimate are about
640,000 total location-days in the dataset (12 weeks times 7 days per
week times nearly 8000 locations). And I note that trimming the data
like this was not described in the preregistered pre-analysis plan
\<<https://osf.io/5gphr>\>, so it is a degree of freedom that the
authors introduced to their analysis afterwards, in order to boost their
statistical significance. This violates the spirit of a registered
pre-analysis plan, in which one is supposed to estimate statistical
power in advance, and state exactly what one intends to do with the data
once the experiment has been conducted. If I were representing the
management of the charity, since large donations are the most important
ones to the organization, I'd personally rather see what the results
look like without trimming the data, even if those results have less
statistical significance.

Similarly, I didn't notice anything in the pre-analysis plan that
specified that donations would be normalized by the population of each
zip code. The pre-analysis plan just talked about the "sum of the
donations" in each zip code, without dividing by population in each
location. That's another degree of freedom the authors gave themselves
in the final analysis, in violation of the spirit of a pre-analysis
plan.

#### Length of measurement window

By contrast, another area with considerable degrees of freedom is the
number of days of outcome that the authors choose to study after the ad
campaign was turned off. Here, their pre-analysis plan was specific that
they would look at the period of the actual experiment (November 10-24)
and the post-period until the end of the year (November 24 to December
31), and in their analysis the authors did indeed look at precisely a
38-day period after the treatment ended. They could have decided to look
at January data as well, or to shorten their post-period to just two
weeks after the experiment, to see which period would give them the most
statistical significance, but they did not do this. Instead, they
reasoned in advance that it would be best to look at the remainder of
the year, and then they stuck exactly to this plan. This is exactly the
way a pre-analysis plan should work, helping readers feel more confident
of results because of a precommitment to an analysis strategy that would
deprive them of degrees of freedom that might overstate true statistical
significance.

Later, in Section 4.3.1, the authors do a robustness check to see how
the estimated treatment effects vary with the period of time the
researchers choose to examine, from including only the period of the
campaign to including up to 48 post-campaign days. The results are
displayed in Figure A5 of the
[Appendix](https://bibliothek.wzb.eu/pdf/2024/ii20-302r2_appendix.pdf).
We see, as in my 2015 NBER conference-volume paper with Randall Lewis
and Justin Rao [@n3dc641fq5y] (cited by the authors), that as we expand
the analysis window, we get slightly narrower confidence intervals, as
additional time tends to smooth out the variance in the outcome
variables. However, the treatment effect tends to drop right after the
advertising campaign ends. The treatment effects are usually highest
when the stimulus is still being applied, though there can be some
long-run persistent positive effects even after the ads have been turned
off. This is a particularly interesting case where the treatment effect
grows again over time. I agree with the authors that this phenomenon is
likely because donation revenues for most charities tend to increase
towards the very end of the calendar year. If the donation-solicitation
campaign has a persistent effect, we might expect these persistent
treatment effects to be highest at the very end of the year when
revenues are usually highest. This is why I think the authors made a
great choice to run their campaign in November and monitor donations all
the way to the end of the year. For windows with more than 39 days
post-treatment (i.e, after January 1), we see a drop in the estimated
treatment effect, as donation totals are usually lower in early January
than in late December. I congratulate the authors for making an
intelligent choice for the timing of this campaign and the choice of an
appropriate post-treatment window to examine.

I also like Section 4.3.2, a second robustness check which decomposes
the treatment effects into new versus repeat donors, and into one-time
versus recurring donations. It is interesting to observe that all four
coefficients are positive, though not all are statistically significant
at the 5% level.

### Using Covariates, Especially Lagged Y, to Improve Precision

I prefer to help the reader more with interpretation of table
coefficients than the authors have done in Table 1. If I understand
Table 1 correctly, it shows that before the experiment begins, the
treatment group contributed approximately 11 euros per million people
per day *less* than the control group, and approximately 0.07 donation
counts per million people per day *more* than the control group.
However, neither is as large as the estimated standard error of the
difference. It is also interesting to note that the added covariates
serve to decrease the standard error of the measured placebo-test
"treatment effect," as we would expect in a randomized experiment where
all covariates are independent of the assigned treatment, but they
decrease the standard errors only very slightly.

In Table 2, it is disappointing that the standard errors increase
slightly from column (1) to column (2) in the short-run effects. Adding
additional covariates cannot, in general, lower the precision of the
treatment effect, so I'm curious what happened here. Maybe it was just a
statistical fluke, but I find in my experience that such flukes are
pretty rare.

In Table 2, I notice that the covariates in the regression include
lagged dependent variable, population, share employed, share Catholic,
and the number of post codes per location. In the pre-analysis plan, the
covariates proposed were population size (which became a
dependent-variable denominator rather than a covariate), the share of
Protestants and Catholics, income, and the vote share of Germany's five
largest parties in the federal election in 2013. I'm not particularly
worried about this, as including covariates in a regression to measure
the treatment effect in a randomized experiment cannot change the
estimated treatment effect by much, and we can see that the covariates
end up not reducing the standard error very much either. I want to point
out that this is another example of a deviation from the pre-analysis
plan that gives the authors more degrees of freedom, but in this case I
don't think it presents any real problem.

It's interesting to note the important differences between the
short-term and the long-term revenue results in Table 2. The long-run
effect is a bit bigger than the short-run event, but the main reason the
long-term effect is much more statistically significant is that it has a
smaller standard error. This is almost certainly because including more
weeks of data per postal code causes the variance of Y to decrease. In
other words, smoothing the data over more weeks causes the variance
across locations to go down. But that's only for the revenue results.
For the results on number of donations, the treatment effect actually
goes down by about 30% when increasing from short run to long run, but
the standard error goes down by about 40%.

The authors consider a difference-in-difference estimator in the
Appendix, in order to make sure the small pre-treatment differences are
not affecting the estimated treatment effect. But this seems
unnecessary, because including the lagged dependent variable as a
control in Table 2 accomplishes almost exactly the same thing. In fact,
a diff-in-diff estimator turns out to be a special case of a regression
estimate with a treatment dummy and a lagged dependent variable, where
the coefficient on the lagged dependent variable is constrained to equal
1 (which we can see by adding the lagged dependent variable to both
sides of the diff-in-diff specification). So I prefer the estimate in
Table 2, because the more flexible form has the opportunity to better
explain the variance in Y, and thus should have smaller standard errors.
Indeed, when I consult the online appendix table A3, I find that the
standard errors are indeed noticeably smaller in Table 2 in the main
text. When I have the choice between two unbiased estimators, I always
prefer the one with lower variance.

## Spillover Effects from One Location to Another

Section 4.3.3 makes an ambitious foray into measuring spillovers. If
people receive ads while working in a treatment-group postal code but
then make donations while at home in a control-group postal code, the
mismeasurement would cause us to underestimate the ATE. (For intuition,
notice that in the limit of 100% mismeasurement, we would be guaranteed
to have a zero treatment effect, because actual treatment assignment
would be completely uncorrelated with the treatment group observed for
measured outcomes.) It is very interesting to see positive, and
statistically significant, measured effects for postal codes with a
large share of nearby postal codes also having been treated. This means
that the main ATEs in the paper are indeed a lower bound on the true
treatment effect.

I spent some time trying to figure out how to interpret the implications
of the spillover effects for the correct treatment effect of the ad
campaign. I am somewhat puzzled by the large size of the estimated
spillovers, and I don't think I really understand them to my
satisfaction. In Table 8, the direct geographic effect of treatment is
estimated to be 17.661 (not terribly different from the effect
originally estimated in Table 2), with an additional indirect effect of
228.5 times the share of neighbor postal codes who were treated. The
authors report that the sample average share of neighbor postal codes
treated is 66.8%. This is in itself surprising, as half the postal codes
were treated in the experiment. (I suppose the postal codes might be
clustered in such a way that the average postal code has more than half
its neighbors treated, but if so, I would love for the authors to
explain how this happened.)

> *Editors note: *Maja Adena clarifies that
>
> > The share of postal codes that received treatment was 66.6% or 2/3
> > and not 50%. In the paper we write: \"\...assigned each of the six
> > consecutive postal codes to one block. In any given block, we
> > randomly assigned the postal codes to one of the following
> > conditions: **two postal codes received no ads** (the control
> > group) **and four postal codes were allocated to the ad
> > condition** (the treatment group).

This suggests, then, that the average level of total spillover effect
observed in a given postal code (228.5\*0.668 = 152.6) is much higher
than the direct effect (17.6). The authors' total number of €170.3032,
in the last sentence of Section 4.3.3, comes from adding the direct
effect to the spillover effect. I find this surprisingly high, and it
makes me wonder whether there might be something else going on here that
we are not understanding correctly. For example, there might be some
kind of bad specification error in the way we are modeling the spillover
as a linear function of the share of the treated neighboring postal
codes, or the way we are defining "neighboring."

One additional idea I have to add here is that it might be useful,
instead of measuring merely the share of nearby postal codes that were
treated, maybe we could measure the share of nearby postal-code
populations that were treated. This is because I expect spillovers to be
larger if there are more people crossing over from one postal code to
another, so the estimated effects might be proportional to the size of
the treated population.

## It's Hard to Measure Advertising Effectiveness Precisely

The important paper by Lewis and Rao (2015 [@n0qizto6r09], cited by the
authors) demonstrates how difficult it can be to measure the impacts of
advertising even when they are highly profitable, and even when we have
a large randomized experiment, because treatment effects tend to be low
compared to overall variance. This problem becomes even greater when
researchers want to investigate subtler effects, such as the difference
in impact between two ad campaigns, or the impact of a campaign on
competitors, since we expect those treatment effects to be smaller than
the main treatment effect of "Is the advertising producing its intended
result at all?"

An even more vexing statistical-power problem arises when researchers
try to answer more subtle questions, such as the differences between one
ad creative and another, or between one targeting strategy and another.
When it's hard to measure the effects of advertising at all, it's even
harder to measure the difference between two strategies.

### Harder Question #1: Different Advertising Strategies

I appreciate that the authors are honest about their inability to
distinguish between the donation effectiveness of the two video
creatives in Table 5 Panel A. They do find higher point estimates for
the "empathy" video than for the "effectiveness" video, especially in
the short run, but the difference is not statistically significant. They
also find in Table 6 some statistically significant differences in the
short run between some upstream metrics: namely, clicks per video view,
and long views (at least 3 seconds of video) per video view. It is
somewhat common, in my experience, to be able to obtain statistically
significant differences in upstream metrics like ad clicks, but not to
be able to obtain statistical significance on final metrics like actual
donations. This is in part because upstream metrics don't always
translate into downstream metrics, and in part because downstream
metrics tend to have higher variance (relative to the treatment effect)
than upstream metrics. There are quite a few papers in the marketing
literature that report on upstream metrics like clicks or survey
outcomes, both because the data is easier to obtain and because it is
relatively less noisy than the final outcome the advertiser really cares
about.

The authors are similarly honest about their inability to distinguish
between the effectiveness of two different targeting strategies
(allowing the Facebook algorithm to try to minimize cost per ad
impression, versus fixing the budget per person in each postal code).
The point estimates in Table 5 Panel B show that the Facebook algorithm
gives a higher point estimate on donations, but it is not statistically
significantly different from the strategy using a fixed budget per
person in each postal code. In Table 6, the intermediate outcome of
clicks per view shows a significantly higher value under Facebook
allocation than under fixed budgeting, but the other intermediate
outcome (long views per view) shows a significantly significant
difference in the opposite direction. The authors summarize this by
saying "In this case, intermediate and comprehensive measures mostly
point in the same direction: They indicate a positive effect of granting
full freedom to the Facebook algorithm in a fundraising context." Given
that one of the tests (long views per view) gives a statistically
significant result in the wrong direction, I would personally tone down
this statement. I agree that if I had to pick one strategy based on this
experiment, based on the point estimates in Table 5, I would choose the
empathy video and the Facebook default targeting algorithm. But I
wouldn't feel terribly certain in my choice.

I congratulate the authors for being able to implement one of the
relatively few experiments measuring final outcomes rather than merely
some upstream, intermediate outcome. Finding statistically significant
difference between two different advertising strategies is an order of
magnitude more difficult than finding a significant effect of the ads on
the final outcome.

In Table 6 on the upstream, intermediate outcomes like clicks, I would
have preferred to see standard errors of the mean reported underneath
each of the means, so that I get a sense for the amount of variance,
beyond merely the number of asterisks reported for significance tests. I
would also suggest considering regression analysis rather than simple
difference-in-proportion tests, because controlling for covariates (such
as past donations) can often reduce standard errors. Some folks are
afraid to use OLS regression when the dependent variable is binary, like
clicks, but I think it is perfectly appropriate. It is, after all, the
natural generalization of a simple difference-in-proportions test to
control for covariates and thereby gain statistical precision, as a
difference-in-proportions test is numerically identical to regressing
the binary outcome on the binary treatment dummy. To those who believe
(erroneously) that one must never use OLS for a binary dependent
variable, either because they learned this as a fixed rule, or because
they fear the specification error that can result from having predicted
values less than zero or greater than one, I will say that in my decades
of running field experiments, I have never found a single predicted
value to lie outside the interval \[0,1\] when I regressed a binary
outcome on treatment dummies plus covariates.

However, having just made my rant about how scholars should be less
afraid to use OLS with binary outcomes in field experiments, I will also
say it's quite reasonable for the authors not to have bothered to do
this in Table 6. My reasoning is that the most useful covariate is
usually the past value of the dependent variable. But here we are
looking at variables that were undefined before the ad campaign started
(clicks per view, etc.), so there is no way to include the lagged
dependent variable. It's possible that the lagged value of donations per
person will help explain the variance in clicks per view, but I wouldn't
expect it to help very much.

### Harder Question #2: Impact on Competing Charities

In the analysis of effects on competing charities (Table 3), the authors
note that they found statistically significant pretreatment differences
in the competitive outcome. I went to Appendix Table A4 and noticed that
the t-statistics for these differences are close to 2. If we assume the
authors implemented a true randomization, a t-statistic of 2 means that
there was approximately a 2.5% chance of getting a pretreatment
difference at least that large. Unusual, but certainly not unheard of,
to get such a difference. That reassures me about the randomization
being valid - I would not have felt so sanguine if the t-statistic had
instead been 3.5. So the authors were unlucky that they happened to put
postal codes with larger-than-average competitor donation revenue into
the treatment group, and the smaller-than-average postal codes into the
control group.

To handle this difference, the authors appropriately choose to include
pretreatment Y as a covariate in their preferred specification
regressing Y on the treatment dummy. This is a great solution, because
if pretreatment Y is a good predictor of posttreatment Y in different
postal codes, then this regression corrects for the pretreatment
imbalance by predicting higher donations in the postal codes with high
pretreatment Y. It also provides a lower standard error for the
treatment effect, because successfully predicting some of the variance
in Y (using the pretreatment Y) increases the signal-to-noise ratio of
the estimate. Another way to think about this is that the bias we might
worry about from the pretreatment estimates is not so much a bias as a
kind of variance, at least from the pre-randomization point of view - we
just got unlucky in the randomization, and would give us a relatively
extreme estimate if we didn't correct for the pre-period difference
using lagged Y as a covariate.

The authors also consider a diff-in-diff estimator here. In column (2),
they regress the difference (post Y - pre Y) on a treatment dummy,
instead of regressing (post Y) on a treatment dummy and (pre Y) in
column (1). I'd like to note that I usually prefer the specification in
column (1), because it is a more flexible way to predict (post Y). If we
rearrange the DID regression specification from column (2) by adding
(pre Y) to both sides, we see that it is identical to the
lagged-dependent-variable regression in column (1) except that the
coefficient on the lagged dependent variable is constrained to equal
one. That is, the DID estimator assumes that for every 1-euro increase
in pre-period donations, the post-period donations should also increase
by exactly 1 euro. The lagged-dependent-variable regression instead
allows the covariate to have an estimated coefficient of, say, 0.7 or
1.2 (post Y varies not one-for-one with pre Y, but with some other
ratio). I'm surprised to see in Table 4 that for both outcome variables,
the diff-in-diff estimator produces smaller standard errors than the
lagged-dependent-variable estimator, because usually I would expect the
better predictor to produce smaller standard errors. This comparison
tells me that imposing the one-for-one restriction of DID in column (2)
happens in this case to produce more accurate predictions than the more
flexible specification in column (1), and therefore I prefer the DID
specification. But both are very similar: the difference in standard
errors is not large, and neither is the difference in the estimated
coefficient.

I applaud the authors for their efforts to measure crowding-out effects
on other charities. It required a lot of extra work to do this analysis.
Unfortunately, the results on this topic have low statistical power.
They find point estimates indicating that donations to competing
charities are lower in the treatment group to whom Save the Children was
advertised on Meta. These estimates are barely statistically
significant, only in the short run and not in the long run, at the 5%
significance level in one dataset and at the 10% significance level in
the other. I note that the result that achieved 5% significance was the
one that included trimming out of outlier donations (more than €1000 per
charity per postal code per day), and that trimming likely led to
improved significance, though as a marketing manager I do think I care a
lot about the effects on large donations, so I would have preferred not
to trim the data. I also note that there is nothing in the [pre-analysis
plan](https://osf.io/5gphr) about investigating the effects on competing
charities, so the authors likely engaged in some discretionary choices
(such as trimming the data, and using a diff-in-diff estimator) that
likely resulted in more statistical significance. This is not to say
that the authors have done anything duplicitous; it is just to emphasize
that while this is an important question, the results are really quite
weak statistically, though the paper plays them up as an important
result. The point estimates are large, but the confidence intervals are
very wide indeed.\
\
Given that it's very difficult to find enough statistical power to show
that an ad campaign has a statistically significant main effect (for the
advertised charity), it's not surprising to me that it would be even
harder to find statistically significant effects on competing charities.
Even if there were one-for-one crowding out of donations to all other
charities caused by incremental Save the Children donations, we only
have a subset of all other charities for which we can do measurement, so
the measured effects on competitors are almost guaranteed to be smaller
than the main treatment effect on Save the Children donations.

### Harder Question #3: Measuring Profitability

Section 4.3.4 considers profitability. As shown by Lewis and Rao (2015
[@n2wunsb8cu8]), it is generally hard enough to measure whether there is
any effect of an ad campaign at all, much less whether the effect is
high enough to offset the cost of the ads. In this case, the authors are
not able to measure a statistically significant effect above and beyond
the cost. The authors chose to use a 90% confidence interval of €47,700
± €42,800 for incremental revenue, but if we instead use a 95%
confidence interval, the estimated incremental revenue becomes €47,700 ±
€51,000. When we subtract off the cost of the ads of €33,700, we get a
direct-profit confidence interval of €14,000 ± €51,000, which is very
uncertain indeed. Translated into euros of revenue per euro spent on
ads, this becomes €1.45±€1.51.

The total revenue effect (direct effects plus future indirect effects
through repeat donations) might well be 1.75 times higher than the
direct effect measured by the experiment, as the authors assume. I tend
to think this multiplier of 1.75 is rather uncertain, as it has been
roughly calibrated from other data - I can imagine that its uncertainty
might be something like 1.75±0.5. But even if I assume that we know the
multiplier parameter exactly, we need to apply the multiplier both to
the point estimate and to the width of the confidence interval, so we
end up with 95% confidence interval of (€2.53 ± €2.65) raised per euro
spent on ads. We could also restate this as an estimated profit of
(€1.53 ± €2.65) per euro spent on ads, which shows us that we are
extremely uncertain about the profitability of the campaign even if we
feel confident in the multiplier parameter of 1.75.

Also, when measuring profitability, I feel pretty strongly that trimming
the data (removing observations above €1000 per postal code per day) is
a bad idea. It may increase statistical precision, but it means we are
measuring something different from actual profitability, as large
donations can be quite important for both revenues and profits.

Later, in the conclusion of the paper, the authors say, "Reassuringly,
the largely untargeted campaign was profitable for the fundraiser: €1
spent translated into an immediate return of €1.45 and is expected to
turn into €2.53 in the long run." But I'm not feeling as reassured as
the authors want me to be. While this is a valid interpretation of the
paper's main point estimate, I find it misleading because it fails to
remind the reader about the degree of uncertainty in the estimate. I
would prefer to see 95% confidence intervals instead: "€1 spent
translated into an immediate return of €1.45±€1.51, and is expected to
turn into €2.53 ± €2.65 in the long run." I agree that the point
estimate does indicate a profitable campaign; I just want to recognize
the amount of uncertainty in that estimate.

### Harder Question #4: Heterogeneous Treatment Effects

Section 4.3.5 considers heterogeneous treatment effects (HTE). I'll note
that I would have liked the authors to be explicit about their outcome
measure, since they had two preferred outcomes in Table 2, and I can't
find in the text or the table where they have defined this outcome. I
assume, given the magnitudes of the coefficients, that we must be
talking about donation revenues here instead of donation frequency.

Once again, HTE is a much more subtle question than the question of
whether the advertising has a positive ATE, so it's harder to answer. I
like the way the authors do above-versus-below-median splits on a number
of covariates, so that we have more than 3000 observations in both
"high" and "low" conditions. The most intriguingly large treatment
effects singled out by the authors happen with less-urban postal codes,
or those with high Facebook "estimated potential," low population size,
low Facebook reach, low share of German nationals, low share of
Protestants, low share of couples, and low share of single parents.

Unfortunately, the authors did not conduct F-tests to conclude which of
these HTEs were statistically significant (for example, are we really
confident that we get higher treatment effects in postal codes with a
lower share of German nationals?). Since we are comparing two disjoint
groups in each column, I can get a good idea of the likely result of
such an F-test, since the standard errors of the mean for each group are
around 11 euros per million inhabitants, and since we have equal-sized
groups, the standard error for the difference in means must be around 11
times the square root of 2, or about 15. Looking at the magnitudes of
the differences between high and low groups in each column, this tells
me that all of the "most intriguing" differences I listed above are
likely to be statistically significant, except that the share of couples
and the urban status look only just marginally significant.

Also, the coefficients with the biggest high-low differences all ended
up estimating positive treatment effects for one half of the data and
negative treatment effects for the other half, which helped the
difference become big enough for statistical significance. But it's hard
for me to imagine that negative treatment effects are genuine, rather
than mere noise, because I don't see a good theory for why Save the
Children ads would cause donations to decrease among half the
population. Since the authors have checked 13 different covariates for
heterogeneous treatment effects (and maybe more that they didn't report,
since they didn't specify HTE in their preregistered pre-analysis plan),
we also know we should want a higher threshold for statistical
significance than if just one variable had been checked, so I have some
skepticism about whether these HTEs are real. This is consistent with my
baseline belief that it is very hard to measure the effects of
advertising. I continue to believe that the results are intriguing,
though.

In a case like this, where we see an intriguing difference, like "Zip
codes with low share of single parents are the best places to run Save
the Children ads on Facebook," but we might be getting fooled by a fluke
in a case where we have low statistical power and we know we have gone
fishing over a lot of different population splits, I recommend a
follow-up experiment. If this effect is real, then it should hold up in
a second experiment. If it doesn't hold up, it was probably a fluke.
Intriguing but statistically weak results such as these should best be
treated as hypotheses: we did a lot of exploratory data analysis from
our first experiment, found a number of intriguing results, and now if
we want to feel confident, we run a second experiment to see whether
those results hold up (or whether they are disproven as flukes). I will
put statistical uncertainty aside for a moment in order to make my next
comment.

#### How can we use HTEs?

Now suppose all of these HTEs are really true. What is the best way to
make practical use of this information? Well, one thing we could do is
pick one of the thirteen HTEs and focus on it. "Estimated potential"
seems like a good one to consider, since Facebook thinks this is a good
measurement of the potential of an ad campaign, and the experiment
validated that notion. We could choose to advertise only to the top half
of zip codes on this score, and we might get a more profitable ad
campaign. In other work (including Lewis 2014 [@npzk32xb74p]; Johnson,
Lewis, and Reiley 2015 [@n816o6l27pp]) I have become convinced that
advertising often has approximately constant returns to frequency, at
least for the number of impressions per person that are typically used
in the industry. In other words, the tenth ad impression seen by a given
individual has approximately the same effectiveness as the first
impression they saw. That means taking the same budget and applying it
to only half of the postal codes might double the benefits in the most
advantageous postal codes, and provide additional profits relative to
spreading the ad spend uniformly across the whole population.

But instead of picking just one of the covariates to focus on, we could
also make use of recent developments in machine learning (ML) to combine
the various covariates for causal inference. (After all, as the authors
note, their 13 covariates are all correlated with each other.) An
experiment can never observe the treatment effect for a single
individual (or other single treatment unit, like a single postal code) -
instead, we get to observe the average treatment effect (ATE) across a
group of individuals. Shalit, Johansson, and Sontag (2016
[@ny0kh1nvb05]) proposed a technique to estimate "individual treatment
effects," and what they really mean by this is to use ML techniques to
estimate a surface of heterogeneous treatment effects (HTEs) across all
covariates of interest. The most important pitfall to watch out for with
this idea is underestimating the size of our confidence intervals via
"overfitting," a notion is closely related to the warnings I raised
above about testing a lot of different covariates for heterogeneous
treatment effects - the more we search, the more false positives we are
going to find in hypothesis tests. Athey and Wager (JASA, 2018
[@n8ygoomr6ek]) propose the valuable idea of splitting the experimental
data, so that only half the observations are being used to discover the
best-fitting functional form for the HTEs, and the other half of the
data are used to estimate the coefficients. The idea can be thought of
as an automated pre-analysis plan, with the first stage specifying the
plan, and the second stage implementing the estimation. (This second
stage is a form of cross validation, a technique developed in order to
combat the problem of overfitting/oversmoothing in statistics and
econometrics) . I have found that it can be hard to use these estimation
techniques in practice, because they can be computationally expensive on
large datasets. I had difficult memory-management problems when I first
tried to use these techniques nearly ten years ago, but the methods and
the software to implement these techniques are getting better.

I have two favorite examples of applications of these techniques to
estimate heterogeneous treatment effects and use them to improve policy
through effective personalization. The first is one of my own: Goli,
Reiley, and Zhang (Marketing Science, 2025 [@n26r6fjfrk8]) experiment
with advertising load on Pandora, finding that when the quantity of
advertising increases, listeners decrease their listening, but also
increase their willingness to pay for an ad-free Pandora subscription.
This latter effect has strong heterogeneities across listeners: for
example, listeners who live in zip codes with higher median income are
much more likely to react to an ad-load increase by purchasing an
ad-free subscription. Goli, Zhang, and I discover, using a
neural-network estimation technique, that Pandora could personalize the
number of ads per listener in a way that would increase subscription
profits by 7% without having any negative impact on advertising
revenues.

The second is Dube and Misra (JPE, 2023 [@nn78m5kleko]), who experiment
with prices to employers listing jobs on ZipRecruiter. The experiment
showed that they could increase the uniform price to increase profits by
55% Then they used a Bayesian Bootstrap estimator to estimate
heterogeneous treatment effects, and they estimated that their strategy
could realistically improve profits by an additional 19% (implementing
prices only within the scope of the experiment). Most importantly, their
paper does something I have long believed would be the best way to
evaluate an proposed optimal strategy obtained through empirical
economic analysis: they implement a second experiment to validate their
proposed optimal pricing strategy (see Section 4.5.1). A treatment
adopting the proposed optimal uniform-price strategy earns more revenue
than the default uniform-price strategy, as predicted by the analysis of
the first experiment: the point prediction was 55%, and the measured
empirical benefit was 68%. (The difference relative to the prediction
was not statistically significant, though the difference between
treatment and status-quo control is significant at p\<0.01). The
treatment adopting the proposed optimal personalized-pricing strategy
produced increased revenue of 84% relative to control, compared with the
point estimate of 86% from the first experiment's HTE analysis. (The
difference between prediction and second-experiment outcome is not
statistically significant, nor is the difference between predicted
optimal uniform pricing and predicted optimal personalized pricing. The
difference relative to control is, of course, also highly significant at
p\<0.01). This is a really terrific way to validate predictions made
through modeling. Since we can fool ourselves with overfitting if we're
not careful, and since consumer behavior might not be stable over time,
I think it is always valuable to validate predictions through an
experiment. I hope other researchers will emulate Dube and Misra (2023
[@ncda8ole1ru]) in order that the scientific community can have more
confidence in analysis (whether experimental or from structural
econometrics) that makes predictions about optimal policies.

## Robustness Checks

I find two of the authors' robustness checks worth commenting on:
randomization inference, and measurement window length. I will address
them here in turn.

### Randomization Inference

In Section 4.3.1, the authors implement randomization-inference tests to
examine the robustness of their main results from Table 2. I really like
randomization inference, so I want to describe the idea for those who do
not feel comfortable with it. For any randomized experiment, we can
imagine imposing the null hypothesis of a zero treatment effect on each
observation (this is also known as the "sharp" null hypothesis, since it
applies to each individual observation rather than just to the
population mean). Then, since this is a randomized experiment, we can do
a clever trick. Under the null hypothesis, we can randomly reassign each
observation either to treatment or control again, and recompute a new
"treatment effect" based on that new randomization. We can repeat this
thousands of times. Each time, we get a draw from the distribution of
possible treatment effects that we could obtain if the null hypothesis
were really true, and we can therefore plot this empirical distribution
of the average treatment effect (ATE) we could obtain from these
observations under the null hypothesis. Plots of these distributions are
shown in Figure A4 of the
[Appendix](https://bibliothek.wzb.eu/pdf/2024/ii20-302r2_appendix.pdf).
If the actual ATE is far out in the tails of the null-hypothesis
distribution we obtain from re-randomization, then we know that we have
obtained an ATE that is very unlikely to have arisen under the null
hypothesis, and we can say we have a statistically significant effect.
(The p-value comes from the area under the tail of the curve, where the
tail is defined to begin at the location of the actual ATE for the true
randomization.)

I generally think of randomization inference the way I think of
nonparametric statistical tests (Mann-Whitney, Wilcoxon) for differences
in outcomes. That is, I generally believe that with large samples (in
the thousands), we don't need to rely on nonparametric tests, because in
large samples the Central Limit Theorem generally tells us that we can
rely on the sample means to be normally distributed. With smaller
samples (say \<30 observations per treatment), or extraordinarily
fat-tailed distributions, we might not trust the Central Limit Theorem
to help us calculate confidence intervals, because we don't know what
will be the shape of the distribution of the sample mean. But the nice
thing about randomization inference is that we can always use it for
robustness in a randomized experiment (unlike in observational
research). Here the authors use it and, as expected, confirm their
original results that had relied on the Central Limit Theorem to assume
normality of the sample means.

### Length of Measurement Window

Another robustness check in Section 4.3.1 examines how the estimated
treatment effects vary with the period of time the researchers choose to
examine, from including only the period of the campaign to including up
to 48 post-campaign days. The results are displayed in Figure A5 of the
[Appendix](https://bibliothek.wzb.eu/pdf/2024/ii20-302r2_appendix.pdf).
We see, as in my 2015 paper with Randall Lewis and Justin Rao, that as
we expand the analysis window, we get slightly narrower confidence
intervals, as additional time tends to smooth out the variance in the
outcome variables. However, the treatment effect tends to drop right
after the advertising campaign ends. The treatment effects are usually
highest when the stimulus is still being applied, though there can be
some long-run persistent positive effects even after the ads have been
turned off. This is a particularly interesting case where the treatment
effect grows again over time. I agree with the authors that this
phenomenon is likely because donation revenues for most charities tend
to increase towards the very end of the calendar year. If the
donation-solicitation campaign has a persistent effect, we might expect
these persistent treatment effects to be highest at the very end of the
year when revenues are usually highest. This is why I think the authors
made a great choice to run their campaign in November and monitor
donations all the way to the end of the year. For windows with more than
39 days post-treatment (i.e, after January 1), we see a drop in the
estimated treatment effect, as donation totals are usually lower in
early January than in late December. I congratulate the authors for
making an intelligent choice for the timing of this campaign and the
choice of an appropriate post-treatment window to examine.

I also like Section 4.3.2, which decomposes the treatment effects into
new versus repeat donors, and into one-time versus recurring donations.
It is interesting to observe that all four coefficients are positive,
though not all are statistically significant at the 5% level.

## Finding the Data Appendix 

This paper refers the reader in a number of places to the online
[Appendix](https://bibliothek.wzb.eu/pdf/2024/ii20-302r2_appendix.pdf)
for such details as descriptive statistics on the other charities that
might be competing with Save the Children for donations. I had
difficulty finding the online Appendix on the *Management Science*
website.

> *Editor: *We moved the rest of this discussion to a footnote, as it
> was partially clarified by the authors.[^9]
>
> The link to the relevant content is is
> [here](https://pubsonline.informs.org/doi/suppl/10.1287/mnsc.2020.00596/suppl_file/mnsc.2020.00596.sm1.pdf "null"),

* *

## Final Thoughts

Overall, I think this is an admirable piece of research, and I learned
something valuable from reading this paper. The experiment is a
well-designed example of geographic randomization to measure the
treatment effects of an advertising campaign. The big advantage of a
geographic randomization is that it makes measuring outcomes feasible in
a world where online tracking is discouraged, so it becomes difficult to
know for sure, in an individual-level randomization, whether individual
donations came from the treatment group or the control group.[^10] The
disadvantage of a geographically randomized campaign is that if the ad
campaign does not reach a very large fraction of the population, the
campaign might explain too small of a fraction of the variance in
donations across geographic areas. In this case, measuring a
statistically significant treatment effect turns out to be just barely
possible (depending on whether one is satisfied with a 90% confidence
interval instead of a 95% one).\
\
I find it especially interesting that the authors are able to
demonstrate positive (and statistically significant) spillover effects
across geographically close postal codes, perhaps because users get
targeted with ads at their work location and later make donations at
their home location. Indeed, the results show spillovers primarily of
advertising in urban areas spilling over to adjacent rural areas. But
because the estimated spillover effects are so huge (the indirect effect
of neighboring areas being treated is ten times higher than the direct
treatment effect we're measuring), I worry that we may be
misunderstanding something. The authors have to make various assumptions
to estimate the spillover effects: which are the "neighboring postal
codes" that matter versus don't, and what is the functional form of the
way these neighbors impact the postal code of interest? We don't know
how good these assumptions are, so there might be substantial
specification error here. I would really like to see the authors go
deeper into this analysis and better understand what is happening with
the spillovers, because if the spillover effects really are huge, then
that means the main result presented in the paper could be badly
underestimating the true treatment effects.

I also find it interesting that the authors are able to demonstrate that
the point estimates of the ATE get larger rather than smaller when they
take into account more weeks of post-treatment data (through the end of
the calendar year). This tells us that advertising is probably not
merely accelerating donations forward in time (donations which would
have happened even without the advertising), but is actually increasing
total donations relative to the status quo.

I think the authors oversell some of their results, mainly by failing to
provide confidence intervals rather than point estimates in some of
their discussions. After eighteen years of running experiments with
digital advertising, including those described by Lewis and Rao (2015
[@ngteqee6iaa]) in their paper, I have learned that it is quite
challenging to obtain sufficient statistical power to be able to say
that even a profitable advertising campaign has any treatment effect at
all on final purchases. I love that the authors measure the final
outcome of actual donations made, instead of some intermediate proxy,
because I am never confident that a proxy actually tells us what
researchers want it to tell us about final outcomes. But I think the
authors might be more careful to present confidence intervals and point
out how much statistical uncertainty they have in their estimates. This
is particularly true for the harder questions they try to answer, which
suffer even more difficult statistical-power problems.\
\
I like that the authors went to the trouble of registering a
pre-analysis plan, something I personally have never done. But because
the authors deviated in a number of ways from their pre-analysis plan, I
think it's worth having some skepticism about the different degrees of
freedom they allowed themselves in the analysis. I don't mind that the
authors came up with additional analysis ideas after the experiment was
over - that is to be expected - but I would like them to point out which
analyses were contained in the plan and which ones were not. Because we
typically struggle with statistical power in advertising experiments,
there is a danger of type-I error from choices made in the analysis. I
would love to see authors point out in their text when they have stuck
to their pre-analysis plan, and when they have deviated from it. When
findings are only marginally significant and the authors had a number of
choices to make before presenting results, that makes the results more
untrustworthy than the reported p-values and confidence intervals would
suggest. For the more subtle results presented in the paper, if I were
running the charity and wanted to feel confident about the strategies
proposed as optimal for fundraising, I would want to repeat the
experiment and see whether the results still hold up (with analysis
specifications fixed as in the original analysis).

As physics Nobel laureate Richard Feynman said, when you want to
practice good science, "The first principle is that you must not fool
yourself---and you are the easiest person to fool." Many of my comments
are designed to help the community think about how we can do a better
job of practicing science, and fooling ourselves less.

## References

[@nnmowcfvc5p] Adena, Maja, and Anselm Hager. 2025. 'Does Online
Fundraising Increase Charitable Giving? A Nationwide Field Experiment on
Facebook'. *Management Science* 71 (4): 3216--31.
<https://doi.org/10.1287/mnsc.2020.00596>.

[@nynncyhq76u] Lewis, Randall A., and Justin M. Rao. 2014. 'The
Unfavorable Economics of Measuring the Returns to Advertising'. SSRN
Scholarly Paper No. 2367103. Social Science Research Network, September
18. <https://doi.org/10.2139/ssrn.2367103>.

[@n1b1wo36rc3] Lewis, Randall A., and David H. Reiley. 2014. 'Online Ads
and Offline Sales: Measuring the Effect of Retail Advertising via a
Controlled Experiment on Yahoo!' *Quantitative Marketing and Economics*
12 (3): 235--66. <https://doi.org/10.1007/s11129-014-9146-6>.

[@nqlidx7mp8x] Johnson, Garrett, Randall A. Lewis, and David Reiley.
2015. 'When Less Is More: Data and Power in Advertising Experiments'.
SSRN Scholarly Paper No. 2683621. Social Science Research Network,
December 29. <https://doi.org/10.2139/ssrn.2683621>.

[@nvhxeugr4nw] Johansson, Fredrik D., Uri Shalit, and David Sontag.
2018. 'Learning Representations for Counterfactual Inference'.
arXiv:1605.03661. Preprint, arXiv, June 6.
<https://doi.org/10.48550/arXiv.1605.03661>.

[@ne0o7zdupmy] Wager, Stefan, and Susan Athey. 2018. 'Estimation and
Inference of Heterogeneous Treatment Effects Using Random Forests'.
*Journal of the American Statistical Association*, July 3. world.
<https://www.tandfonline.com/doi/abs/10.1080/01621459.2017.1319839>.

[@nse72duuciy] Goli, Ali, David H. Reiley, and Hongkai Zhang. 2025.
'Personalizing Ad Load to Optimize Subscription and Ad Revenues: Product
Strategies Constructed from Experiments on Pandora'. *Marketing Science*
44 (2): 327--52. <https://doi.org/10.1287/mksc.2022.0357>.

[@n5tjqt9j35r] Dubé, Jean-Pierre, and Sanjog Misra. 2023. 'Personalized
Pricing and Consumer Welfare'. *Journal of Political Economy*, ahead of
print, January 1. Chicago, IL. <https://doi.org/10.1086/720793>.

# Evaluator details

1.   What is your research field or area of expertise, as relevant to
    this research?

    -   Field experiments on the effects of advertising campaigns

2.  How long have you been in your field of expertise?

    -   Eighteen years working on digital advertising, thirty years
        evangelizing for the use of field experiments in economics.

3.  How many proposals, papers, and projects have you evaluated/reviewed
    (for journals, grants, or other peer-review)?

    -   Probably around 200 over 30 years

[^1]: Note: if you are reading this before, or soon after this has been
    publicly released, the ratings from this paper may not yet have been
    incorporated into that data presentation.

[^2]: We asked them to rank this paper "heuristically" as a percentile
    "relative to all serious research in the same area that you have
    encountered in the last three years." We requested they "consider
    all aspects of quality, credibility, importance to knowledge
    production, and importance to practice.

[^3]: See ranking tiers discussed
    [here](https://globalimpact.gitbook.io/the-unjournal-project-and-communication-space/policies-projects-evaluation-workflow/evaluation/guidelines-for-evaluators#journal-ranking-tiers).

[^4]: This comes from the form. If the author didn't do this, please
    skip this section.

[^5]: The evaluator was given the following instructions: Identify the
    most important and impactful factual claim this research makes --
    e.g., a binary claim or a point estimate or prediction.

    Please state the authors' claim precisely and quantitatively.
    Identify the source of the claim (i.e., cite the paper), and briefly
    mention the evidence underlying this. We encourage you to explain
    why you believe this claim is important, either here, or in the text
    of your report.

[^6]: "Feel free to express this in terms of the probability of the
    claim being true or as a credible interval for the parameter being
    estimated."

[^7]: *We asked:*

    \[Optional\] What additional information, evidence, replication, or
    robustness check would make you substantially more (or less)
    confident in this claim?

    Feel free to refer to the main body of your evaluation here; you
    don\'t need to repeat yourself. Please specify how you would perform
    this robustness check (etc.) as precisely as you are willing. E.g.,
    if you suggest a particular estimation command in a statistical
    package, this could be very helpful for future robustness
    replication work.

[^8]: *We asked:* \[Optional\] Identify the important \*implication\* of
    the above claim for funding and policy choices? To what extent do
    you \*believe\* this implication? How should it inform policy
    choices? Note: this 'implication' could be suggested by the
    evaluation manager in some cases. As an example of an
    \'implication\' \... in a global health context, the \'main claim\'
    might suggest that a vitamin supplement intervention, if scaled up,
    would save lives at a \$XXXX per life saved.

[^9]: E2: I retrieved the Supplemental Materials from the *Management
    Science* website. Although I read a claim that the Appendix would be
    there, I found no Appendix but was only able to retrieve the data
    and code replication files as "supplementary materials." I could not
    find the Appendix anywhere. I did find the Appendix on the authors'
    WZB site, so I want to put a link
    [here](https://bibliothek.wzb.eu/pdf/2024/ii20-302r2_appendix.pdf)
    for readers' convenience. I hope that *Management Science* will
    correct this oversight, so that this document will be part of their
    public record in case the WZB website becomes defunct at some point.

    *Editor's note:* The authors clarified that the web appendix was
    made available among the supplementary material, requiring a "click
    on the PDF and not on the blue" --- the link is
    [here](https://pubsonline.informs.org/doi/suppl/10.1287/mnsc.2020.00596/suppl_file/mnsc.2020.00596.sm1.pdf).

[^10]: As the authors note in their footnote 10, a well-powered
    experiment randomized at the individual level needs to be careful to
    track individual ad exposure by using placebo ads or "ghost ad"
    logging of hypothetical exposures, otherwise the results could be
    plagued with what Lewis, Rao, and I first called "activity bias" in
    our [[2011 WWW conference
    paper]{.underline}](https://dl.acm.org/doi/abs/10.1145/1963405.1963431).
    The authors cite Johnson et al. (2017) on this phenomenon, but
    Lewis, Rao, and Reiley (2011) was where the term "activity bias" was
    first coined.
