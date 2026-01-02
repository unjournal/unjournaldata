---
article:
  doi: 10.21428/d28e8e57.8530472e
  elocation-id: evaltan
author:
- Joel Tan
bibliography: /tmp/tmp-60UPSvLYqE6clv.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 20
  month: 03
  year: 2023
journal:
  publisher-name: The Unjournal
  title: The Unjournal
link-citations: true
title: "Evaluation 3 of \"Advance Market Commitments: Insights from
  Theory and Experience\" by Joel Tan"
uri: "https://unjournal.pubpub.org/pub/evaltan"
---

## Summary Measures

### Overall Assessment

Answer: 79

90% CI: (59,94)

### Quality Scale Rating

"On a 'scale of journals', what 'quality of journal' should this be
published in?: Note: 0= lowest/none, 5= highest/best"

Answer: 5

Confidence: High

See [here](https://unjournal.pubpub.org/pub/amcmetrics/release/6 "null")
for a more detailed breakdown of the evaluators' ratings and
predictions.

## Written report

[Link to spreadsheet
calculations](https://docs.google.com/spreadsheets/d/1ccKrVshCocfKoFrTL5KAwAIps6IS_R__qhIb9sEhL7o/edit#gid=1533599707)

# Summary of Kremer, Levin & Snyder\'s Primary Findings

[Kremer, Levin & Snyder
(KLS)](https://cpb-us-e1.wpmucdn.com/sites.dartmouth.edu/dist/5/2287/files/2021/02/w26775.pdf)
find that the pneumococcal vaccine (PCV) advanced market commitment
(AMC) probably resulted in around 700,000 lives saved that would
otherwise have been lost.

# Counterfactual increase in coverage due to pneumococcal vaccine advanced market commitment

To estimate the counterfactual impact of the PCV AMC, KLS compare the
actual impact of the PCV AMC rollout to the rotavirus (RV) non-AMC
rollout. This choice of comparator does make sense; as KLS
write[s](https://unjournal.pubpub.org/pub/amcmetrics/release/6 "null"):
\"*We selected rotavirus from the six global vaccine initiatives
proceeding around that time for the following reasons. Three of them
(IPV, second dose of measles, birth dose of hepatitis) involved
early-vintage rather than new vaccines. The yellow-fever vaccine was not
rolled out in many high-income countries, leaving no good base rate for
coverage speed comparison. We conjecture the results would be stronger
using HPV, the remaining candidate apart from rotavirus, for comparison,
but any slow rollout of HPV vaccine in GAVI countries could be
attributed to its administration to older children, slowing coverage
expansion.*\"

That said, there is a reasonable worry over whether the results are
robust to a different comparator class of vaccines when estimating the
counterfactual impact of the pneumococcal vaccine (PCV) advanced market
commitment (AMC). To check this point, I ran a [rough quantitative
analysis of my
own](https://docs.google.com/spreadsheets/d/1ccKrVshCocfKoFrTL5KAwAIps6IS_R__qhIb9sEhL7o/edit?usp=share_link).
I use vaccination data from the following sources:

-   For RCV and RV vaccination, I use the International Vaccine Access
    Center & John Hopkins Bloomberg School of Public Health\'s
    [View-Hub](https://view-hub.org/map/) database (last access,
    2023-02-02), which draws on WUENIC estimates. WUENIC estimates are
    official WHO/UNICEF estimates of national immunization coverage,
    created by drawing on country-reported data as well as published and
    grey literature, even while correcting for potential biases

-   For human papillomavirus vaccine (HPV) vaccination, I pull from
    [UNICEF](https://data.unicef.org/resources/dataset/immunization/)
    (last access, 2023-02-02.

-   For yellow fever (YF) vaccination, I rely on Shearer et al's
    ([@temp_id_9006136122172754]) estimate of global yellow fever
    vaccination coverage (last access, 2023-02-03).

The disparate datasets are not ideal, but no single source I found while
undertaking this quick review provides comprehensive data on all
vaccines of relevance. Calculations were done in the linked Google
sheet, last edited 2023-02-05.

Using this data, I first look at the proportion of PCV coverage with the
AMC (across GAVI countries, for the first 12 years from introduction)
relative to full coverage. This was calculated by taking a
population-weighted average of coverage rates per country-year across
all 54 current GAVI countries across 12 years (from introduction in 2010
up to 2021). Based on the aforementioned data and this specific
methodology, overall coverage for GAVI countries across this time period
was 49%.

Second, I look at three different comparator classes: (a) rotavirus
vaccine (RV) coverage, (b) human papillomavirus vaccine (HPV) coverage,
as well as yellow fever (YF) vaccine coverage (similarly looking across
GAVI countries across for the first 12 years from introduction or
equivalent). [^1] [^2] These three classes were used as the vaccines in
question are either newer vaccines with a more recent introduction date
(RV & HPV), or else an older vaccine where there appears to be a
discrete recent push for vaccination by GAVI (YF) -- allowing for us to
perhaps observe the counterfactual world in which PVC was rolled out
without an AMC but with standard GAVI support. In each case, I look at
the proportion of the comparator vaccine\'s coverage across GAVI
countries for the first 12 years. And again, this is calculated by
taking a population-weighted average of coverage rates per country-year
across all 54 current GAVI countries across 12 years (n.b. RV: from
introduction in 2006 up to 2017, for comparability; for HPV, from
introduction in 2010 up to 2021; and for YF, from GAVI making a
[concerted
effort](https://www.gavi.org/types-support/vaccine-support/yellow-fever)
on YF in 2001 up to 2012, for comparability).

I find that KLS\'s results should be fairly robust, insofar as the
coverage rates for alternative comparator vaccines are in fact lower
than the mainline RV comparator KLS chose: coverage was 12% for RV, 2%
for HPV, and 9% for YF.

Going further, I estimate the probable proportion of PCV coverage across
GAVI countries across 12 years from introduction without the AMC, by
creating a weighted average of the 3 comparator classes. In doing this,
I firstly penalize dissimilarity in target demographics (n.b. PCV and RV
are both targeted for \<1 year olds, while HPV is for older individuals
and the YF vaccine is for 9 months+ individuals) -- this matters insofar
as the former two vaccines will more likely be deployed as part of
post-birth immunization schedules. Secondly, I penalize data limitations
(e.g. the uncertain YF extrapolations). Weights are assigned
subjectively and fairly aggressively, with each penalty leading to a
comparator class being weighed a magnitude less than it otherwise would
have. In all, the weighted average is 11% -- which is my best-guess
estimate of PCV coverage in the absence of the AMC.

Putting this together, the counterfactual impact of the PCV AMC as a
proportion of total disease burden avertable by vaccinations in the
relevant time period is around 38% relative to total coverage.
Importantly, this estimate here would not differ by much (\~2%) even if
we only used RV as the comparator to estimate the non-AMC counterfactual
-- which suggests that KLS\'s results are robust to comparator class.
That said, I would caution against using these results for direct
comparisons to KLS\'s findings -- this analysis is very rough, and given
the different datasets/methodologies, I would be wary of utilizing these
results for anything except a sense-check for the matter of comparator
class robustness.

There is a further caveat to note -- the datasets used see a
considerable amount of missing data; in such cases, I made the
methodological choice to treat missing data for country-years as 0%
coverage. The idea is that (a) any country lacking the state capacity to
report is unlikely to be doling out vaccines; and (b) such GAVI
countries by definition have GAVI support, and GAVI does publish its
data (which then feeds into the WUENIC estimates) -- so unless GAVI were
failing to report vaccinations (unlikely), it seems reasonable to think
that unreported country-years do in fact suffer 0% coverage.

# Robustness of headline DALY estimates

In any case, there are other issues that may affect the accuracy of the
final estimates of DALYs averted:

1.  The estimate relies on Tasslimi et al\'s
    ([@temp_id_08548500640418166]) calculations of DALYs averted per PCV
    shot -- and this in turn relies on O\'Brien et al\'s
    ([@temp_id_42056087938362485]) estimate of the global burden of
    disease caused by streptococcus pneumoniae. However, DALYs lost per
    capita to pneumococcus were declining in poor countries year-on-year
    for two decades even before the AMC, possibly due -- at least in
    part -- to economic growth bringing improvements in
    sanitation/nutrition/access to healthcare. Hence, projections on
    future DALYs averted based on past disease burden data may overstate
    the benefit. Theoretically, a way to account for this would be to
    re-run KLS\'s analysis but discounting each year\'s DALY per dose
    estimate using the rate at which pneumococcus DALY burden per capita
    was experiencing a secular decline in the two decades before the
    introduction of the vaccine.

2.  On the other hand, KLS do not model the speeding up of the
    development of existing vaccines -- hypothetically, the credible
    commitment provided by the AMC will have a dynamic effect not just
    on new entrants (to enter) but also on existing pharmaceuticals with
    nearly-licensed vaccines (to speed up their activities). The idea
    here is that with guaranteed profits on the horizon, existing
    pharmaceuticals will be willing to expand more resources and make
    greater efforts at bringing the nearly-licensed vaccine to market
    faster than they would otherwise have, thus bringing forward the
    date of introduction relative to a counterfactual world where the
    AMC was not made. Notably, the PCV-13 vaccine was licensed in
    [2010](https://www.cdc.gov/vaccines/pubs/pinkbook/pneumo.html),
    while the AMC was made in 2009 -- it is theoretically conceivable
    that licensure would have been later absent the AMC. That said, this
    is speculative, and hard to test besides -- no obvious way presents
    itself to me at this juncture, and more research on this point would
    be both valuable and interesting.

My sense is that effect 1 would outweigh effect 2, such that the true
effect of the PCV AMC is lower than currently estimated, but it is hard
to say by how much, if at all.

# Conclusion

Overall, relative to the null hypothesis (i.e. the AMC did nothing), I
would (a) have extremely high confidence that the AMC made a difference
and saved a significant number of lives; and (b) only moderate
confidence that at least 700,000 lives were saved, per KLS\'s original
estimate.

## Evaluator details

**How long have you been in this field?**

1 year for cause prioritization, 5 years for broader economic research
and analysis

**How many proposals and papers have you evaluated?**

Zero in an academic context

[^1]: In each case, I take the sum of proportional coverage per
    country-year, and divide by total number of countries (56) as well
    as total number of years (12, which means introduction year 2010 to
    2021 for PCV, introduction year 2006 to 2017 for RV, introduction
    year 2010 to 2021 for HPV, and 2001-2012 for YF on the premise that
    GAVI made a concerted effort on expanding YF vaccine from 2001
    onwards), to get average coverage across GAVI countries in that time
    period.

[^2]: Note that there were significant data limitations with respect to
    the YF calculations. Only 2000 and 2010 vaccination rates were
    available from the
    [[source]{.underline}](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(17)30419X/)
    I found; both WHO and the International Vaccine Access Center/John
    Hopkins View-Hub project were not forthcoming on comprehensive YF
    vaccination rates. To get around this, I assume a linear
    increase/decrease from 2000 to 2010 and then to 2012, thus
    extrapolating the vaccination rates for other years.
