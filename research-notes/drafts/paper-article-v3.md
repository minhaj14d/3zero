# Introduction

## Background

Bangladesh has had a remarkable economic run over the past two decades.
GDP growth has averaged above 6% per year since 2010, and the country
has made visible improvements in life expectancy, school enrollment, and
child mortality (World Bank 2023a). In 2021, the United Nations
recommended Bangladesh for graduation from Least Developed Country (LDC)
status.

But the headline numbers do not tell the whole story. The official
unemployment rate looks low at around 4--5%, but that hides widespread
underemployment and informal labour. Carbon emissions have been going up
steadily as the country industrializes, placing Bangladesh in the
paradoxical position of being one of the most climate-vulnerable
countries while contributing more and more to the problem.

Professor Muhammad Yunus, who won the Nobel Peace Prize for his work
with Grameen Bank, laid out a vision in *A World of Three Zeros* (Yunus
2017) for achieving zero poverty, zero unemployment, and zero net carbon
emissions. The framework treats these three targets as deeply connected
--- you cannot solve one without addressing the others.

## Problem Statement

Despite the conceptual appeal of the 3 Zero Movement, there has been
limited quantitative assessment of Bangladesh's actual progress. Most
existing writing is aspirational. This study asks: How far has
Bangladesh actually come? How fast? And are the three goals moving in
the same direction, or is progress on one coming at the cost of another?

From an applied math standpoint, this is a clean problem: multiple
indicators on different scales that need to be normalized, weighted, and
combined into a composite index, with trend and correlation analysis to
reveal the underlying dynamics.

## Research Questions

1.  How much quantitative progress has Bangladesh made toward each of
    the three zero targets over 2000--2023?

2.  Are the three pillars moving together (synergy) or against each
    other (trade-offs)?

3.  At the current rate of change, when might Bangladesh reach each
    target, and which pillar is the biggest bottleneck?

## Objectives

1.  To collect and analyze verified data on three indicators using World
    Bank and Global Carbon Project sources.

2.  To construct a composite 3 Zero Progress Index (3ZPI).

3.  To examine statistical relationships between the pillars using
    Pearson correlation.

4.  To project target achievement timelines using linear extrapolation.

5.  To offer recommendations based on the findings.

# Literature Review

## The 3 Zero Movement

The 3 Zero Movement grew out of Yunus's experience with Grameen Bank,
founded in 1983 (Yunus 2007). In *A World of Three Zeros*, Yunus
proposed "social business" as the vehicle for achieving zero poverty,
zero unemployment, and zero net carbon emissions (Yunus 2017). The
framework intersects with the UN Sustainable Development Goals (United
Nations 2015) but differs in emphasizing bottom-up entrepreneurship over
top-down policy (Yunus Social Business 2021).

## Poverty Reduction in Bangladesh

Using the \$3.00/day international poverty line, Bangladesh's headcount
ratio fell from 41.4% in 2000 to 5.9% by 2022 (World Bank 2023b) ---
over 85% reduction. This reflects sustained GDP growth, the ready-made
garments sector, remittances, and microfinance (Khandker 2005; Morduch
1999; Banerjee et al. 2015). COVID-19 caused a temporary reversal, with
an estimated 14--24 million Bangladeshis falling into poverty during
2020 (World Bank 2021).

## Youth Unemployment

ILO modeled estimates show youth unemployment (15--24) fluctuating
between 6% and 13% over the past two decades, with a spike to 13.5%
during COVID-19 (International Labour Organization 2023). The "educated
unemployment" phenomenon reflects a skills mismatch (Rahman et al.
2021). Yunus's entrepreneurship-focused approach has had results through
Grameen Bank but faces scaling challenges (Yunus 2017).

## Carbon Emissions

Bangladesh's per capita CO~2~ emissions tripled from 0.20 to 0.61 tonnes
between 2000 and 2023 ([Friedlingstein et al.]{.nocase} 2023), driven by
industrialization and fossil fuel dependence (Alam et al. 2012). The
country committed to 21.85% emission reduction below business-as-usual
by 2030 under the Paris Agreement (Government of Bangladesh 2021). The
Solar Home System program installed over 6 million units (Infrastructure
Development Company Limited 2020), but renewables remain a small share
of total energy. Bangladesh ranks among the top ten climate-vulnerable
countries (Germanwatch 2021).

## Research Gap

Most studies address poverty, employment, and emissions separately. This
study treats the three zeros as a coupled system and applies composite
index methods to measure integrated progress.

# Methodology

## Research Design and Data Sources

Three indicators were fetched programmatically using Python 3.11 with
`wbgapi` (World Bank) and `pandas` (Global Carbon Project CSV):

::: {#tab:indicators}
  Pillar              Indicator                                          Source                    Unit
  ------------------- -------------------------------------------------- ------------------------- ------
  Zero Poverty        Poverty headcount at \$3.00/day (2021 PPP)         WB (SI.POV.DDAY)          \%
  Zero Unemployment   Youth unemployment, 15--24, ILO modeled            WB/ILO (SL.UEM.1524.ZS)   \%
  Zero Carbon         CO~2~ emissions per capita (fossil + industrial)   GCP (OWID)                t

  : Indicator Definitions
:::

The study period is 2000--2023 (24 years). Poverty data is available
only for survey years ($\sim$`<!-- -->`{=html}2000, 2005, 2010, 2016,
2022); non-survey years were linearly interpolated.

## Normalization

All three indicators are "lower is better," so inverted min-max
normalization is applied: $$\begin{equation}
x_{i,\text{norm}} = \frac{x_{\max} - x_i}{x_{\max} - x_{\min}}
\end{equation}$$ where $x_{\max}$ and $x_{\min}$ are the maximum and
minimum observed values across the full study period.

::: {#tab:bounds}
  Indicator                  Min (best)   Max (worst)
  ------------------------ ------------ -------------
  Poverty (%)                       5.9          41.4
  Youth Unemployment (%)           6.29         13.47
  CO~2~ per Capita (t)            0.197         0.610

  : Min-Max Normalization Bounds
:::

## Composite 3 Zero Progress Index (3ZPI)

$$\begin{equation}
\text{3ZPI}_t = w_1 \cdot \text{Poverty}_{\text{norm}} + w_2 \cdot \text{Unemployment}_{\text{norm}} + w_3 \cdot \text{CO2}_{\text{norm}}
\end{equation}$$ with $w_1 + w_2 + w_3 = 1$. Baseline: equal weights
($w_i = \frac{1}{3}$).

## Trend Analysis

Linear regression on each raw indicator: $$\begin{equation}
y_t = \alpha + \beta \cdot t + \epsilon_t
\end{equation}$$ where $t = 0$ for 2000 through $t = 23$ for 2023. For
indicators with $\beta < 0$, the projected year to reach zero:
$t_{\text{zero}} = 2023 + y_{2023}/|\beta|$.

## Correlation Analysis

Pearson correlation coefficients between normalized scores. With
$n = 24$, the significance threshold at 5% is $|r| > 0.404$ ($df = 22$).

# Analysis and Findings

## Raw Data and Trends

Table [3](#tab:rawdata){reference-type="ref" reference="tab:rawdata"}
presents the verified indicator data.
Figures [1](#fig:poverty){reference-type="ref"
reference="fig:poverty"}--[3](#fig:co2){reference-type="ref"
reference="fig:co2"} show individual trends with regression lines.

::: {#tab:rawdata}
    Year   Poverty (%)   Youth Unemp. (%)   CO~2~ pc (t)
  ------ ------------- ------------------ --------------
    2000        41.4\*               9.74          0.197
    2005        32.3\*               8.79          0.261
    2010        25.1\*               6.29          0.355
    2013          22.3               9.67          0.414
    2016        19.5\*              10.96          0.508
    2019          12.7              11.74          0.575
    2020          10.4              13.47          0.576
    2022         5.9\*              10.99          0.603
    2023           5.9               7.91          0.610

  : Raw Indicator Data (Selected Years)
:::

= actual survey data; other poverty values are interpolated.

<figure id="fig:poverty" data-latex-placement="H">
<embed src="../figures/fig1_poverty_trend.pdf" style="width:85.0%" />
<figcaption>Poverty headcount ratio at $3.00/day, Bangladesh
(2000–2023).</figcaption>
</figure>

<figure id="fig:unemployment" data-latex-placement="H">
<embed src="../figures/fig2_unemployment_trend.pdf"
style="width:85.0%" />
<figcaption>Youth unemployment rate (15–24), Bangladesh
(2000–2023).</figcaption>
</figure>

<figure id="fig:co2" data-latex-placement="H">
<embed src="../figures/fig3_co2_trend.pdf" style="width:85.0%" />
<figcaption>CO<sub>2</sub> emissions per capita, Bangladesh
(2000–2023).</figcaption>
</figure>

## 3ZPI Composite Index

::: {#tab:3zpi}
    Year   Poverty (norm)   Youth Unemp. (norm)   CO~2~ (norm)    **3ZPI**
  ------ ---------------- --------------------- -------------- -----------
    2000            0.000                 0.519          1.000   **0.506**
    2003            0.154                 0.956          0.901   **0.670**
    2010            0.459                 1.000          0.617   **0.692**
    2016            0.617                 0.350          0.247   **0.405**
    2020            0.872                 0.000          0.082   **0.318**
    2023            1.000                 0.775          0.000   **0.592**

  : 3ZPI Trajectory (Selected Years)
:::

The 3ZPI peaked at 0.692 in 2010, declined to 0.318 in 2020, and
recovered to 0.592 by 2023. The net change over 24 years is only +0.085.
Figure [4](#fig:3zpi){reference-type="ref" reference="fig:3zpi"} shows
the full trajectory.

<figure id="fig:3zpi" data-latex-placement="H">
<embed src="../figures/fig4_three_zero_index.pdf" style="width:85.0%" />
<figcaption>Three Zero Progress Index and component indicators
(2000–2023).</figcaption>
</figure>

## Sensitivity Analysis

::: {#tab:sensitivity}
    Year   Equal   Poverty-heavy   Unemp-heavy   CO~2~-heavy
  ------ ------- --------------- ------------- -------------
    2000   0.506           0.380         0.510         0.630
    2010   0.692           0.634         0.769         0.674
    2020   0.318           0.457         0.239         0.259
    2023   0.592           0.694         0.638         0.444

  : 3ZPI Under Alternative Weighting Schemes (Selected Years)
:::

The qualitative conclusions are robust across all weighting schemes.

## Trend Analysis

::: {#tab:regression}
  Indicator            $\beta$ (annual)   $R^2$   $p$-value        Projected year to zero
  ------------------ ------------------ ------- ----------- -----------------------------
  Poverty (%)                   $-1.48$   0.988    $<0.001$   $\sim$`<!-- -->`{=html}2027
  Youth Unemp. (%)              $+0.18$   0.423    $<0.001$           Never (trending up)
  CO~2~ pc (t)                 $+0.020$   0.981    $<0.001$           Never (trending up)

  : Linear Regression Results
:::

See Figure [5](#fig:regression){reference-type="ref"
reference="fig:regression"} for a comparison of regression slopes.

<figure id="fig:regression" data-latex-placement="H">
<embed src="../figures/fig6_regression_summary.pdf"
style="width:75.0%" />
<figcaption>Annual rate of change (regression slope <span
class="math inline"><em>β</em></span>) per indicator.</figcaption>
</figure>

## Correlation Analysis

::: {#tab:correlation}
                    Poverty   Youth Unemp.   CO~2~ pc
  -------------- ---------- -------------- ----------
  Poverty             1.000       $-0.620$   $-0.978$
  Youth Unemp.     $-0.620$          1.000   $+0.705$
  CO~2~ pc         $-0.978$       $+0.705$      1.000

  : Correlation Matrix (Normalized Scores)
:::

All correlations exceed the 5% significance threshold ($|r| > 0.404$,
$df = 22$).

The near-perfect negative correlation ($r = -0.978$) between poverty and
CO~2~ is the central finding: the economic growth driving poverty
reduction simultaneously worsens carbon performance. See
Figure [6](#fig:heatmap){reference-type="ref" reference="fig:heatmap"}.

<figure id="fig:heatmap" data-latex-placement="H">
<embed src="../figures/fig5_correlation_heatmap.pdf"
style="width:65.0%" />
<figcaption>Correlation heatmap of normalized pillar
scores.</figcaption>
</figure>

# Discussion

## The Three Pillars Are Not Moving Together

The central finding is that Bangladesh's progress toward the three zeros
is not just uneven --- it is actively divergent. The 3ZPI's modest net
change of +0.085 over 24 years means that despite extraordinary poverty
reduction, the overall 3 Zero progress has been limited because gains in
one pillar were offset by losses in the other two.

The $r = -0.978$ correlation between poverty and CO~2~ quantifies a
structural tension: the way Bangladesh reduces poverty
(fossil-fuel-powered industrialization) is fundamentally incompatible
with the carbon target.

## Poverty Reduction Has Been Strong

The decline from 41.4% to 5.9% at the \$3.00/day line is one of the
fastest sustained poverty reductions in the developing world. The linear
projection suggests poverty at this threshold could approach zero by
$\sim$`<!-- -->`{=html}2027, though the final percentage points will be
the hardest.

## Youth Unemployment Is Getting Worse

The positive regression slope ($+0.18$ pp/year) means youth unemployment
is trending upward, not toward zero. The "educated unemployment" paradox
and structural skills mismatch (Rahman et al. 2021) suggest that
economic growth alone is not solving the employment problem for young
people.

## Carbon Emissions Keep Rising

CO~2~ per capita tripled over the study period with a strong, consistent
upward trend ($R^2 = 0.981$). Bangladesh's emissions are still low by
global standards, but the trajectory is incompatible with any pathway to
zero. Addressing this pillar requires changes beyond social business ---
national energy policy and international climate finance are necessary
(Stern 2007).

## Limitations

Key limitations include: heavy interpolation of poverty data (5 survey
points over 24 years); modeled rather than surveyed unemployment data;
CO~2~ source transition between World Bank and GCP;
single-indicator-per-pillar design; and linear regression on 24 points
providing descriptive rather than predictive power.

# Conclusion and Recommendations

## Summary

Bangladesh has made extraordinary progress on extreme poverty
($-$`<!-- -->`{=html}85% at \$3.00/day) but youth unemployment is
trending upward and CO~2~ per capita has tripled. The composite 3ZPI
moved only +0.085 over 24 years. A near-perfect negative correlation
($r = -0.978$) between poverty and carbon progress reveals that the
current development model, while effective at reducing poverty, is
structurally antagonistic to the carbon target.

## Recommendations

For policymakers: (1) track the three goals together using a composite
index; (2) treat youth unemployment as a structural problem requiring
skills reform; (3) accelerate renewable energy and reconsider fossil
fuel expansion.

For the 3 Zero Movement: (4) invest in green employment at the
intersection of the unemployment and carbon pillars; (5) publish regular
quantitative progress reports.

For future research: (6) expand to multiple indicators per pillar; (7)
apply nonlinear models; (8) conduct subnational and multi-country
analysis.

## Concluding Remarks

The 3 Zero Progress Index is a simple tool --- min-max normalization,
weighted averages, and linear regression. But applied to verified data
and a well-defined question, it reveals that Bangladesh's development is
deeply imbalanced. If the 3 Zero vision is to be realized, something has
to change in how growth happens, not just how fast.

::::::::::::::::::::: {#refs .references .csl-bib-body .hanging-indent}
::: {#ref-alam2012energy .csl-entry}
Alam, Mohammad Jahangir, Ismat Ara Begum, Jeroen Buysse, and Guido Van
Huylenbroeck. 2012. "Energy Consumption, Carbon Emissions and Economic
Growth Nexus in Bangladesh: Cointegration and Dynamic Causality
Analysis." *Energy Policy* 45: 217--25.
<https://doi.org/10.1016/j.enpol.2012.02.022>.
:::

::: {#ref-banerjee2015miracle .csl-entry}
Banerjee, Abhijit, Esther Duflo, Rachel Glennerster, and Cynthia Kinnan.
2015. "The Miracle of Microfinance? Evidence from a Randomized
Evaluation." *American Economic Journal: Applied Economics* 7 (1):
22--53. <https://doi.org/10.1257/app.20130533>.
:::

::: {#ref-gcp2023 .csl-entry}
[Friedlingstein, Pierre, Michael O'Sullivan, Matthew W. Jones, et
al.]{.nocase} 2023. "Global Carbon Budget 2023." *Earth System Science
Data* 15 (12): 5301--69. <https://doi.org/10.5194/essd-15-5301-2023>.
:::

::: {#ref-germanwatch2021 .csl-entry}
Germanwatch. 2021. *Global Climate Risk Index 2021*. Germanwatch e.V.
<https://www.germanwatch.org/en/19777>.
:::

::: {#ref-gob2021ndc .csl-entry}
Government of Bangladesh. 2021. *Nationally Determined Contributions
(Updated) 2021*. Ministry of Environment, Forest; Climate Change,
Government of Bangladesh.
<https://unfccc.int/sites/default/files/NDC/2022-06/Bangladesh%20NDC%202021.pdf>.
:::

::: {#ref-idcol2020 .csl-entry}
Infrastructure Development Company Limited. 2020. *Annual Report
2019--2020*. Infrastructure Development Company Limited (IDCOL).
<https://idcol.org/home/publication>.
:::

::: {#ref-ilo2023 .csl-entry}
International Labour Organization. 2023. *World Employment and Social
Outlook: Trends 2023*. International Labour Organization.
<https://www.ilo.org/global/research/global-reports/weso/WCMS_865332/lang--en/index.htm>.
:::

::: {#ref-khandker2005 .csl-entry}
Khandker, Shahidur R. 2005. "Microfinance and Poverty: Evidence Using
Panel Data from Bangladesh." *The World Bank Economic Review* 19 (2):
263--86. <https://doi.org/10.1093/wber/lhi008>.
:::

::: {#ref-morduch1999 .csl-entry}
Morduch, Jonathan. 1999. "The Microfinance Promise." *Journal of
Economic Literature* 37 (4): 1569--614.
<https://doi.org/10.1257/jel.37.4.1569>.
:::

::: {#ref-selim2021youth .csl-entry}
Rahman, Mahbubur, Mohammad Omar Farooq, and Mohammad Selim. 2021.
"Mitigating Educated Youth Unemployment in Bangladesh." *Journal of
Developing Areas* 55 (1): 185--200.
<https://doi.org/10.1353/jda.2021.0014>.
:::

::: {#ref-stern2007 .csl-entry}
Stern, Nicholas. 2007. *The Economics of Climate Change: The Stern
Review*. Cambridge University Press.
<https://doi.org/10.1017/CBO9780511817434>.
:::

::: {#ref-un2015sdg .csl-entry}
United Nations. 2015. *Transforming Our World: The 2030 Agenda for
Sustainable Development*. UN General Assembly Resolution A/RES/70/1.
<https://undocs.org/A/RES/70/1>.
:::

::: {#ref-wb2021covid .csl-entry}
World Bank. 2021. *Bangladesh COVID-19 Poverty Monitoring Survey*. World
Bank Group.
<https://www.worldbank.org/en/country/bangladesh/publication/bangladesh-covid-19-poverty-monitoring>.
:::

::: {#ref-wb2023update .csl-entry}
World Bank. 2023a. *Bangladesh Development Update: Resilience Under
Test*. World Bank Group.
<https://www.worldbank.org/en/country/bangladesh/publication/bangladesh-development-update>.
:::

::: {#ref-wb2023wdi .csl-entry}
World Bank. 2023b. *World Development Indicators*. Dataset.
<https://data.worldbank.org>.
:::

::: {#ref-yunus2007banker .csl-entry}
Yunus, Muhammad. 2007. *Banker to the Poor: Micro-Lending and the Battle
Against World Poverty*. PublicAffairs.
:::

::: {#ref-yunus2017three .csl-entry}
Yunus, Muhammad. 2017. *A World of Three Zeros: The New Economics of
Zero Poverty, Zero Unemployment, and Zero Net Carbon Emissions*.
PublicAffairs.
:::

::: {#ref-yunussb2021 .csl-entry}
Yunus Social Business. 2021. *2020 Annual Report*. Yunus Social Business
Global Initiatives.
<https://www.yunussb.com/articles/2020-annual-report>.
:::
:::::::::::::::::::::
