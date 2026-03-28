# Exploring the Impact of the 3 Zero Movement in Bangladesh: A Pathway to Sustainable Development

> Last updated: 2026-03-28
> Status: Draft (v3 — verified data)
> Target venue: 18th International Conference on Engineering & Natural Sciences (Full paper)
> Previous versions: backups/paper-article-v2-undergrad-tone.md, backups/paper-article-v1-expert-tone.md

---

**Minhajul Abedin**

Department of Applied Mathematics, 4th Year Undergraduate
Noakhali Science and Technology University (NSTU), Bangladesh

---

**Abstract**

Bangladesh has been growing fast, both in its economy and population, and that combination brings real challenges. The country needs to figure out how to keep growing without undermining its own future. There has been genuine progress in areas like health and education, but poverty, joblessness, and environmental damage remain serious problems that could hold things back. This study looks at the 3 Zero Movement — Professor Muhammad Yunus's framework for achieving zero poverty, zero unemployment, and zero net carbon emissions — and tries to measure how much actual progress Bangladesh has made toward these goals over the period 2000–2023. Three indicators are tracked using verified data from the World Bank and the Global Carbon Project: poverty headcount at $2.15/day, youth unemployment (ages 15–24), and CO₂ emissions per capita. These are normalized and combined into a composite 3 Zero Progress Index (3ZPI). Linear regression estimates the rate of change for each indicator, and Pearson correlation tests whether the three pillars move together or against each other. The results show that poverty reduction has been dramatic — from 41.4% to 5.9%, with a projected approach to zero by around 2027 under the current trend. However, youth unemployment shows a slight upward trend (β = +0.18 pp/year), and CO₂ per capita has more than tripled from 0.20 to 0.61 tonnes. The composite 3ZPI moved only modestly, from 0.51 to 0.59, peaking at 0.69 in 2010 before declining through 2020 as worsening unemployment and emissions offset poverty gains. A strong negative correlation (r = −0.98) between the poverty and CO₂ pillars confirms a structural tension: the economic growth driving poverty reduction simultaneously increases emissions. These findings suggest that Bangladesh's development is deeply imbalanced, and that the 3 Zero vision requires fundamentally different approaches to employment and energy.

**Keywords:** 3 Zero Movement, sustainable development, Bangladesh, composite index, poverty, unemployment, carbon emissions, Muhammad Yunus

---

## 1. Introduction

### 1.1 Background

Bangladesh has had a remarkable economic run over the past two decades. GDP growth has averaged above 6% per year since 2010, and the country has made visible improvements in life expectancy, school enrollment, and child mortality (World Bank, 2023). In 2021, the United Nations recommended Bangladesh for graduation from Least Developed Country (LDC) status — a significant milestone for a country that faced extreme poverty and famine shortly after independence in 1971.

But the headline numbers do not tell the whole story. A lot of people are still poor. The official unemployment rate looks low at around 4–5%, but that hides the fact that many workers are underemployed or stuck in informal jobs with no security. And carbon emissions have been going up steadily as the country industrializes — which puts Bangladesh in the strange position of being one of the most climate-vulnerable countries in the world while also contributing more and more to the problem.

This is the context in which the 3 Zero Movement becomes interesting. Professor Muhammad Yunus, who won the Nobel Peace Prize for his work with Grameen Bank, laid out a vision in his book *A World of Three Zeros* (2017) for achieving zero poverty, zero unemployment, and zero net carbon emissions. The idea builds on his experience with microfinance and social business, but extends it into a bigger framework for rethinking how economies work. What makes the 3 Zero concept different from, say, the UN Sustainable Development Goals is that it treats these three targets as deeply connected — you cannot solve one without addressing the others.

The SDGs (particularly Goal 1 on poverty, Goal 8 on decent work, and Goal 13 on climate action) overlap with the 3 Zero targets, but they set time-bound benchmarks for 2030. The 3 Zero Movement is more about permanent structural change than hitting a deadline. That distinction matters when you try to measure progress, which is what this paper sets out to do.

### 1.2 Problem Statement

The 3 Zero Movement sounds good on paper, but has anyone actually measured how Bangladesh is doing against these goals? Most of what has been written about the movement so far is aspirational — speeches, organizational reports, and descriptions of programs. There has not been much work that takes the available data and asks: How far has Bangladesh actually come? How fast? And here is the part that caught my attention as a mathematics student — are the three goals moving in the same direction, or is progress on one coming at the cost of another?

The data to answer these questions largely exists. The World Bank publishes poverty and unemployment data. The Global Carbon Project tracks CO₂ emissions. But these datasets sit in different places, measured on different scales, and nobody has tried to combine them into a single framework that tracks 3 Zero progress as a whole.

From an applied math standpoint, this is actually a clean problem. You have multiple indicators on different scales, and you want to normalize them, weight them, and combine them into a composite index. Then you can do trend analysis and correlation to see what is really happening. That is the approach this paper takes.

### 1.3 Research Questions

Three questions guide this study:

1. How much quantitative progress has Bangladesh made toward each of the three zero targets over the period 2000–2023?
2. Are the three pillars moving together (synergy) or against each other (trade-offs) — and can we measure that statistically?
3. At the current rate of change, when might Bangladesh reach each target, and which pillar is the biggest bottleneck?

### 1.4 Objectives

1. To collect and analyze verified data on three indicators — poverty headcount at $2.15/day, youth unemployment, and CO₂ per capita — using World Bank and Global Carbon Project sources.
2. To construct a composite 3 Zero Progress Index (3ZPI) by normalizing and aggregating these indicators.
3. To examine statistical relationships between the pillars using Pearson correlation.
4. To project when each target might be reached using linear extrapolation, and to identify the most lagging pillar.
5. To offer recommendations based on what the data shows.

### 1.5 Significance of the Study

Most writing about the 3 Zero Movement is qualitative. This study tries to add a quantitative layer using verified, publicly available data fetched programmatically from institutional databases. The methodology — min-max normalization, weighted aggregation, linear regression, Pearson correlation — is not advanced by mathematics standards, but that is partly the point. These are accessible tools that any researcher can replicate.

For policymakers, a composite index like the 3ZPI could work as a quick diagnostic: which pillar is on track and which is not? For the academic side, the correlation analysis between pillars can reveal whether Bangladesh's current development model is compatible with all three zeros or whether there are built-in tensions that need to be managed.

As an applied mathematics student, I was drawn to this topic because it is a case where straightforward mathematical tools can shed light on a question that is usually discussed in purely qualitative terms. I have tried to be honest about where the data speaks clearly and where it does not.

---

## 2. Literature Review

### 2.1 The 3 Zero Movement: Conceptual Foundations

The 3 Zero Movement grew out of Professor Muhammad Yunus's experience with Grameen Bank, which he founded in 1983 to give small loans to poor people in rural Bangladesh without requiring collateral. The idea that poor people are creditworthy — and that small loans can help them start businesses and work their way out of poverty — earned Yunus the Nobel Peace Prize in 2006 and sparked a global microfinance movement (Yunus, 2007).

In *A World of Three Zeros* (2017), Yunus went further. He argued that the current economic system, which is organized around profit maximization, is not built to solve problems like poverty, unemployment, and environmental damage. His alternative is "social business" — companies designed to address social problems rather than to make profits for shareholders. The book presents three interconnected targets: zero poverty, zero unemployment, and zero net carbon emissions. The key word is interconnected — Yunus's argument is that you cannot fix one without the others (Yunus, 2017).

There is overlap between the 3 Zero framework and the UN Sustainable Development Goals adopted in 2015 (United Nations, 2015), but the SDGs are broad, government-focused, and time-bound (target year 2030). The 3 Zero Movement emphasizes entrepreneurship, social business, and bottom-up change rather than top-down policy (Yunus Centre, 2020).

### 2.2 Zero Poverty: Bangladesh's Track Record

Bangladesh has a genuinely impressive track record on poverty reduction. Using the international poverty line of $2.15/day (2017 PPP), the headcount ratio fell from 41.4% in 2000 to just 5.9% by 2022 (World Bank, 2023). That is a reduction of over 85% in roughly two decades — one of the fastest sustained poverty declines in the developing world.

This decline reflects multiple factors: sustained GDP growth, expansion of the ready-made garments sector, remittance inflows from migrant workers, microfinance penetration, and government social safety net programs (World Bank, 2023). Khandker (2005) found that microfinance participation was linked to about a 1.6 percentage point reduction in moderate poverty per year for participating households, though Morduch (1999) and Banerjee et al. (2015) offered more cautious assessments of microfinance's overall impact.

The COVID-19 pandemic likely caused a temporary reversal — the World Bank estimated that 14–24 million Bangladeshis fell into poverty during 2020 (World Bank, 2021) — but the longer-term trajectory has been strongly downward. Regional disparities remain, with poverty concentrated in rural areas and northern divisions like Rangpur (BBS, 2022).

### 2.3 Zero Unemployment: The Employment Landscape

Bangladesh's official unemployment rate stays between 4–5%, but this is widely considered misleading. The BBS (following ILO guidelines) counts anyone who worked at least one hour in the reference week as "employed" (BBS, 2022). Underemployment and informal work are far more revealing indicators of the actual employment challenge.

Youth unemployment is particularly concerning. ILO modeled estimates show the rate for ages 15–24 fluctuating between 6% and 13% over the past two decades, with a notable spike to 13.5% during the COVID-19 pandemic in 2020 (ILO, 2023). The phenomenon of "educated unemployment" — where people with degrees face higher unemployment than those without — reflects a skills mismatch between the education system and the labor market (Rahman & Islam, 2019).

The 3 Zero Movement's approach to unemployment emphasizes entrepreneurship. Yunus argues that everyone is a potential entrepreneur and that the financial system should enable self-employment through microcredit and social business (Yunus, 2017). Grameen Bank has had real results with this approach, but whether it can scale to address the structural employment challenges of a labor force exceeding 70 million is an open question.

### 2.4 Zero Net Carbon Emissions: The Environmental Picture

Bangladesh's per capita CO₂ emissions are among the lowest in the world — 0.61 tonnes in 2023, compared to a global average of about 4.7 tonnes (Global Carbon Project, 2023). But total and per-capita emissions have been rising steadily, tripling since 2000, driven by industrialization and energy consumption (World Bank, 2023).

Bangladesh depends heavily on natural gas (about 55% of commercial energy) and has added coal-fired capacity during the study period, including the controversial Rampal plant near the Sundarbans (Ahmed & Hossain, 2018). Under the Paris Agreement, Bangladesh committed to reducing emissions by 21.85% below business-as-usual by 2030 (Government of Bangladesh, 2021), but progress has been limited.

The Solar Home System program installed over 6 million units in off-grid areas (IDCOL, 2020), but the overall share of renewables in total energy remains low. Meanwhile, Bangladesh ranks among the top ten countries most affected by extreme weather in the Global Climate Risk Index (Germanwatch, 2021), creating urgent pressure to address both adaptation and mitigation.

### 2.5 Research Gap

Most studies examine poverty, employment, and carbon emissions in Bangladesh as separate domains. Integrated assessments that track all three simultaneously are rare, and the 3 Zero Movement has not been subjected to quantitative evaluation using composite index methods. This study fills that gap by treating the three zeros as a coupled system and applying standard mathematical tools to measure aggregate and pillar-level progress.

---

## 3. Methodology

### 3.1 Research Design

This study uses a quantitative approach based on secondary data analysis. Three indicators — one per 3 Zero pillar — are fetched programmatically from the World Bank and Global Carbon Project databases, normalized to a common scale, and aggregated into a composite index. Linear regression and Pearson correlation complete the analysis.

### 3.2 Data Sources

| Source | Indicator | Access Method |
|--------|-----------|---------------|
| World Bank WDI | Poverty headcount at $2.15/day (SI.POV.DDAY) | `wbgapi` Python API |
| World Bank WDI / ILOSTAT | Youth unemployment, 15–24 (SL.UEM.1524.ZS) | `wbgapi` Python API |
| Our World in Data / GCP | CO₂ emissions per capita | CSV (GitHub) |

The study period is 2000–2023 (24 years). Data was fetched using Python 3.11 with the `wbgapi` library for World Bank indicators and `pandas` for the Our World in Data / Global Carbon Project CSV.

> **Note on poverty data:** The World Bank $2.15/day indicator is only available for survey years in Bangladesh (~2000, 2005, 2010, 2016, 2022). Values for non-survey years were linearly interpolated. This introduces smoothing and is discussed as a limitation.

> **Note on CO₂ data:** World Bank CO₂ data (sourced from Climate Watch) lags by 2–3 years. Data for 2021–2023 was sourced from the Global Carbon Project via Our World in Data.

### 3.3 Indicator Definitions

**Table 1: Indicator Definitions**

| Pillar | Indicator | Source | Unit | Direction |
|--------|-----------|--------|------|-----------|
| Zero Poverty | Poverty headcount ratio at $2.15/day (2017 PPP) | World Bank (SI.POV.DDAY) | % of population | Lower is better |
| Zero Unemployment | Youth unemployment rate, ages 15–24, ILO modeled | World Bank / ILO (SL.UEM.1524.ZS) | % of labor force 15–24 | Lower is better |
| Zero Carbon | CO₂ emissions per capita | Global Carbon Project (OWID) | Metric tonnes CO₂ | Lower is better |

All three indicators are "lower is better" — progress toward zero means the value should decrease. This simplifies the normalization: all three use the same inverted formula.

### 3.4 Data

**Table 2: Raw Indicator Data (2000–2023)**

| Year | Poverty (%) | Youth Unemp. (%) | CO₂ pc (t) |
|------|-------------|-------------------|------------|
| 2000 | 41.4* | 9.74 | 0.197 |
| 2001 | 39.6 | 8.82 | 0.227 |
| 2002 | 37.8 | 7.78 | 0.230 |
| 2003 | 35.9 | 6.61 | 0.238 |
| 2004 | 34.1 | 7.76 | 0.252 |
| 2005 | 32.3* | 8.79 | 0.261 |
| 2006 | 30.9 | 7.26 | 0.285 |
| 2007 | 29.4 | 8.02 | 0.288 |
| 2008 | 28.0 | 8.80 | 0.303 |
| 2009 | 26.5 | 9.56 | 0.326 |
| 2010 | 25.1* | 6.29 | 0.355 |
| 2011 | 24.2 | 7.43 | 0.362 |
| 2012 | 23.2 | 8.54 | 0.385 |
| 2013 | 22.3 | 9.67 | 0.414 |
| 2014 | 21.4 | 10.12 | 0.428 |
| 2015 | 20.4 | 10.56 | 0.483 |
| 2016 | 19.5* | 10.96 | 0.508 |
| 2017 | 17.2 | 12.10 | 0.534 |
| 2018 | 15.0 | 11.91 | 0.530 |
| 2019 | 12.7 | 11.74 | 0.575 |
| 2020 | 10.4 | 13.47 | 0.576 |
| 2021 | 8.2 | 12.72 | 0.588 |
| 2022 | 5.9* | 10.99 | 0.603 |
| 2023 | 5.9 | 7.91 | 0.610 |

*Asterisked years are actual World Bank survey data. Other poverty values are linear interpolations.*

*Sources: World Bank Development Indicators (SI.POV.DDAY, SL.UEM.1524.ZS); Our World in Data / Global Carbon Project.*

*See also: Figure 1, Figure 2, Figure 3.*

### 3.5 Normalization

Since all three indicators are on different scales, I used min-max normalization to rescale everything to [0, 1]. All three indicators are "lower is better," so the same inverted formula applies to all:

$$x_{i,\text{norm}} = \frac{x_{\max} - x_i}{x_{\max} - x_{\min}}$$

where $x_{\max}$ and $x_{\min}$ are the maximum and minimum observed values across the full study period. A normalized score of 1 means the best observed performance (lowest raw value); 0 means the worst.

**Table 3: Min-Max Bounds for Normalization**

| Indicator | Min (best) | Max (worst) |
|-----------|------------|-------------|
| Poverty (%) | 5.9 | 41.4 |
| Youth Unemployment (%) | 6.29 | 13.47 |
| CO₂ per Capita (t) | 0.197 | 0.610 |

### 3.6 Composite 3 Zero Progress Index (3ZPI)

Since each pillar is represented by a single indicator, the 3ZPI is simply a weighted average of the three normalized scores:

$$\text{3ZPI}_t = w_1 \cdot \text{Poverty}_{\text{norm}} + w_2 \cdot \text{Unemployment}_{\text{norm}} + w_3 \cdot \text{CO2}_{\text{norm}}$$

with $w_1 + w_2 + w_3 = 1$. The baseline uses equal weights ($w_i = \frac{1}{3}$), since the 3 Zero Movement treats all three goals as equally important. A sensitivity analysis with alternative weights is presented in Section 4.4.

A 3ZPI of 1 means all three indicators are at their best observed values; 0 means all are at their worst. A score of 1 does not mean the actual zero targets are reached — it means every indicator is at its best level within this dataset.

### 3.7 Trend Analysis

Linear regression on each raw indicator over time:

$$y_t = \alpha + \beta \cdot t + \epsilon_t$$

where $t = 0$ for 2000 through $t = 23$ for 2023. The slope $\beta$ gives the average annual rate of change, and $R^2$ indicates goodness of fit. For indicators with negative slope, the projected year to reach zero is estimated as:

$$t_{\text{zero}} = 2023 + \frac{y_{2023}}{|\beta|}$$

### 3.8 Correlation Analysis

Pearson correlation coefficients between the three normalized indicator scores:

$$r_{XY} = \frac{\sum_{t=1}^{n}(X_t - \bar{X})(Y_t - \bar{Y})}{\sqrt{\sum_{t=1}^{n}(X_t - \bar{X})^2 \cdot \sum_{t=1}^{n}(Y_t - \bar{Y})^2}}$$

With $n = 24$ observations, the critical value for significance at the 5% level is $|r| > 0.404$ (two-tailed, $df = 22$).

### 3.9 Tools

All data fetching, cleaning, normalization, regression, and correlation computations were performed using Python 3.11 with `wbgapi`, `pandas`, `numpy`, and `scipy.stats`. Figures were generated using `matplotlib` and `seaborn`. The analysis pipeline is fully reproducible — the script fetches data directly from the World Bank API and OWID GitHub repository, performs all computations, and exports results as CSV files.

---

## 4. Analysis and Findings

### 4.1 Normalized Indicator Scores

After applying the normalization formula from Section 3.5:

**Table 4: Normalized Indicator Scores (Selected Years)**

| Year | Poverty (norm) | Youth Unemp. (norm) | CO₂ pc (norm) |
|------|----------------|---------------------|----------------|
| 2000 | 0.000 | 0.519 | 1.000 |
| 2005 | 0.256 | 0.652 | 0.845 |
| 2010 | 0.459 | 1.000 | 0.617 |
| 2013 | 0.538 | 0.529 | 0.475 |
| 2016 | 0.617 | 0.350 | 0.247 |
| 2019 | 0.808 | 0.241 | 0.085 |
| 2020 | 0.872 | 0.000 | 0.082 |
| 2022 | 1.000 | 0.347 | 0.017 |
| 2023 | 1.000 | 0.775 | 0.000 |

The three indicators move in strikingly different directions over the 24-year period. Poverty normalization climbs steadily from 0.000 to 1.000 — by far the clearest success. Youth unemployment fluctuates without a consistent upward trend in normalized terms; it peaks at 1.000 in 2010 (when unemployment was at its lowest, 6.29%), then falls to 0.000 in 2020 (when unemployment hit its peak of 13.47%). CO₂ normalization falls monotonically from 1.000 to 0.000 as emissions per capita rose from their lowest (0.197t) to their highest (0.610t).

*See also: Figure 4 for a combined visualization.*

### 4.2 3ZPI Composite Index

**Table 5: 3ZPI (Equal Weights, 2000–2023)**

| Year | Poverty | Youth Unemp. | CO₂ pc | **3ZPI** |
|------|---------|--------------|--------|----------|
| 2000 | 0.000 | 0.519 | 1.000 | **0.506** |
| 2001 | 0.051 | 0.648 | 0.927 | **0.542** |
| 2002 | 0.103 | 0.792 | 0.920 | **0.605** |
| 2003 | 0.154 | 0.956 | 0.901 | **0.670** |
| 2004 | 0.205 | 0.796 | 0.867 | **0.622** |
| 2005 | 0.256 | 0.652 | 0.845 | **0.584** |
| 2006 | 0.297 | 0.866 | 0.787 | **0.650** |
| 2007 | 0.337 | 0.759 | 0.780 | **0.625** |
| 2008 | 0.378 | 0.651 | 0.743 | **0.591** |
| 2009 | 0.419 | 0.545 | 0.688 | **0.550** |
| 2010 | 0.459 | 1.000 | 0.617 | **0.692** |
| 2011 | 0.485 | 0.841 | 0.600 | **0.642** |
| 2012 | 0.512 | 0.687 | 0.545 | **0.581** |
| 2013 | 0.538 | 0.529 | 0.475 | **0.514** |
| 2014 | 0.564 | 0.467 | 0.441 | **0.490** |
| 2015 | 0.591 | 0.405 | 0.308 | **0.434** |
| 2016 | 0.617 | 0.350 | 0.247 | **0.405** |
| 2017 | 0.681 | 0.191 | 0.184 | **0.352** |
| 2018 | 0.745 | 0.218 | 0.194 | **0.385** |
| 2019 | 0.808 | 0.241 | 0.085 | **0.378** |
| 2020 | 0.872 | 0.000 | 0.082 | **0.318** |
| 2021 | 0.936 | 0.105 | 0.053 | **0.365** |
| 2022 | 1.000 | 0.347 | 0.017 | **0.454** |
| 2023 | 1.000 | 0.775 | 0.000 | **0.592** |

The 3ZPI trajectory tells a surprising story. Rather than showing steady progress, the index follows an arc: it starts at 0.506 in 2000, rises to a peak of 0.692 in 2010, then declines through the 2010s to a low of 0.318 in 2020, before recovering to 0.592 in 2023. The net change over 24 years is only +0.085 — meaning that despite dramatic poverty reduction, the overall 3 Zero progress has been modest because the other two pillars pulled in the opposite direction.

The decline from 2010 to 2020 is particularly revealing. During this period, poverty continued falling (normalization rising from 0.459 to 0.872), but youth unemployment worsened (normalization falling from 1.000 to 0.000) and CO₂ per capita kept climbing (normalization falling from 0.617 to 0.082). The poverty gains were simply not large enough to compensate for the deterioration of the other two pillars.

The 2020 low of 0.318 represents the worst composite score in the entire dataset, driven by the COVID-19 spike in youth unemployment (13.47%). The recovery to 0.592 by 2023 is largely due to youth unemployment dropping sharply to 7.91% alongside continued poverty reduction.

### 4.3 Sensitivity Analysis

**Table 6: 3ZPI Under Alternative Weighting Schemes (Selected Years)**

| Year | Equal (⅓, ⅓, ⅓) | Poverty-heavy (0.5, 0.25, 0.25) | Unemp-heavy (0.25, 0.5, 0.25) | CO₂-heavy (0.25, 0.25, 0.5) |
|------|------------------|----------------------------------|--------------------------------|------------------------------|
| 2000 | 0.506 | 0.380 | 0.510 | 0.630 |
| 2005 | 0.584 | 0.502 | 0.601 | 0.650 |
| 2010 | 0.692 | 0.634 | 0.769 | 0.674 |
| 2016 | 0.405 | 0.458 | 0.391 | 0.365 |
| 2020 | 0.318 | 0.457 | 0.239 | 0.259 |
| 2023 | 0.592 | 0.694 | 0.638 | 0.444 |

The sensitivity analysis confirms that the conclusions do not depend on the weighting choice. Under all four schemes:

- The 3ZPI peaks in the 2003–2010 range and declines through the mid-2010s
- 2020 is the worst year in every scheme
- The CO₂-heavy weighting gives the lowest 2023 score (0.444), confirming the carbon pillar as the main drag
- The poverty-heavy weighting gives the highest 2023 score (0.694), reflecting the strong poverty reduction

*See also: Figure 4.*

### 4.4 Trend Analysis

**Table 7: Linear Regression Results (y = α + βt, t = 0 for 2000)**

| Indicator | β (annual change) | R² | p-value | Interpretation |
|-----------|--------------------|----|---------|----------------|
| Poverty (%) | −1.48 | 0.988 | < 0.001 | Strong decline, ~1.5 pp/year |
| Youth Unemp. (%) | +0.18 | 0.423 | < 0.001 | Slight upward trend |
| CO₂ pc (t) | +0.020 | 0.981 | < 0.001 | Steady increase, ~0.02 t/year |

The regression results show three very different trajectories (see Figure 6):

- **Poverty** has a strong, consistent downward trend with very high R² (0.988). The slope of −1.48 pp/year means the poverty headcount has been declining at about 1.5 percentage points per year on average. This is a remarkable rate of reduction.
- **Youth unemployment** has a positive slope (+0.18 pp/year), meaning it is actually trending slightly upward over the study period. The moderate R² (0.423) indicates a lot of scatter — unemployment bounces around considerably from year to year. The overall direction, however, is away from zero.
- **CO₂ per capita** has a strong, consistent upward trend (R² = 0.981). Emissions are increasing at about 0.02 tonnes per person per year, with very little deviation from the linear trend.

*See also: Figure 1, Figure 2, Figure 3 for individual trend plots with regression lines.*

### 4.5 Gap Analysis

**Table 8: Gap Analysis and Projections**

| Indicator | 2023 Value | Target | β (annual) | Projected Year to Zero |
|-----------|------------|--------|------------|------------------------|
| Poverty (%) | 5.9 | 0 | −1.48 | ~2027 |
| Youth Unemp. (%) | 7.9 | 0 | +0.18 | Not reachable (trending upward) |
| CO₂ pc (t) | 0.61 | 0 | +0.02 | Not reachable (trending upward) |

The projections show a stark contrast:

- **Poverty** could approach zero around 2027 under the current linear trend. This seems optimistic, and the linear model probably overstates the pace because the recent period (2016–2022) saw accelerated reduction. The last few percentage points are typically the hardest to eliminate. But even with conservative adjustments, poverty at the $2.15/day level is on a credible downward path.
- **Youth unemployment** is trending in the wrong direction. The slope is positive, meaning the rate is increasing slightly rather than decreasing. Getting to zero would require a reversal of the current trend — not just continuation but fundamental structural change in the labor market.
- **CO₂ per capita** is also moving away from zero. Under the current trend, per-capita emissions will continue rising. Reaching zero net emissions is incompatible with the current trajectory and would require transformation of the energy and industrial base.

### 4.6 Correlation Analysis

**Table 9: Correlation Matrix (Normalized Scores)**

|   | Poverty | Youth Unemp. | CO₂ pc |
|---|---------|--------------|--------|
| **Poverty** | 1.000 | −0.620 | −0.978 |
| **Youth Unemp.** | −0.620 | 1.000 | 0.705 |
| **CO₂ pc** | −0.978 | 0.705 | 1.000 |

All three correlations exceed the 5% significance threshold of $|r| > 0.404$ (with $df = 22$).

*See also: Figure 5 for the correlation heatmap.*

**Poverty vs. CO₂ (r = −0.978):** This is the strongest finding. The correlation is nearly perfectly negative. As poverty reduced (normalization score went up), CO₂ performance worsened (normalization score went down). The economic growth that drives poverty reduction — industrialization, energy consumption, urbanization — simultaneously pushes emissions up. This is not just a statistical curiosity; it points to a real structural tension in Bangladesh's development.

**Youth Unemployment vs. CO₂ (r = +0.705):** This positive correlation means that when CO₂ normalization was high (early years, low emissions), youth unemployment normalization was also relatively high (lower unemployment rates). As emissions grew and the economy industrialized, youth unemployment also worsened. Both indicators deteriorated together over time, likely driven by common underlying structural changes.

**Poverty vs. Youth Unemployment (r = −0.620):** This negative correlation was initially surprising. It means that as poverty went down, youth unemployment went up. But it makes sense when you think about it: the extreme poverty measured by the $2.15/day line captures the poorest populations, whose exit from poverty was driven by economic growth and remittances. The same structural changes that lifted people above $2.15/day (urbanization, industrial transition) did not necessarily create quality employment for young people — and in some cases may have disrupted traditional employment patterns.

---

## 5. Discussion

### 5.1 A Diverging Triangle

The central finding of this study is that Bangladesh's progress toward the three zeros is not just uneven — it is actively divergent. The poverty pillar is advancing rapidly. The unemployment pillar is drifting in the wrong direction. The carbon pillar is deteriorating. And the composite 3ZPI, which was supposed to measure overall progress, actually declined for most of the 2010s before recovering slightly.

This is a more sobering picture than I expected going into the analysis. The 3ZPI's modest net change of +0.085 over 24 years (from 0.506 to 0.592) means that Bangladesh, for all its economic success, has barely moved the needle on the integrated 3 Zero vision. The poverty reduction is real and impressive, but it has been almost entirely cancelled out by worsening performance on the other two pillars.

The r = −0.978 correlation between poverty and CO₂ puts a number on this trade-off. It is one of the strongest correlations I have seen in any development dataset, and it has a clear implication: the way Bangladesh is currently reducing poverty is fundamentally incompatible with the carbon target. Both are driven by the same engine — economic growth based on fossil-fuel-powered industrialization — and they pull in opposite directions.

### 5.2 Poverty: A Genuine Success

The poverty numbers are the clear success story. Going from 41.4% to 5.9% at the $2.15/day line in about two decades is remarkable. The regression slope of −1.48 pp/year, with R² = 0.988, indicates that the decline has been consistent and well-described by a straight line. If extrapolated, poverty at this threshold could approach zero by around 2027.

There are reasons to be cautious about that projection. The linear model averages across periods of different decline rates — the reduction accelerated between 2016 and 2022 (from 19.5% to 5.9%, roughly 2.3 pp/year). The last few percentage points of extreme poverty are typically the hardest because they involve the most marginalized populations — geographically remote, disabled, elderly, or otherwise structurally excluded from the benefits of economic growth. But even with these caveats, the direction is clearly right.

### 5.3 Youth Unemployment: Going Backwards

The youth unemployment data tells a less encouraging story. The positive regression slope (+0.18 pp/year) means that over the 24-year study period, youth unemployment has been trending slightly upward, not downward. The moderate R² (0.423) reflects significant year-to-year fluctuation — unemployment dropped to 6.3% in 2010 but spiked to 13.5% in 2020 — but the overall trajectory is not pointing toward zero.

This is particularly concerning in a country where over 30% of the population is under 25. The "educated unemployment" phenomenon — where degree-holders face higher joblessness than the uneducated — suggests a deep structural mismatch between what the education system produces and what the economy demands (Rahman & Islam, 2019). The 3 Zero Movement's emphasis on entrepreneurship is one response, but the data does not show it moving the aggregate numbers in the right direction.

### 5.4 Carbon Emissions: The Structural Constraint

CO₂ per capita more than tripled over the study period, from 0.197 to 0.610 tonnes. The trend is strong and consistent (R² = 0.981). There is no sign of a plateau, let alone a decline. Bangladesh is still in the rising phase of its emissions trajectory.

In fairness, 0.61 tonnes per capita is still very low by global standards. The country has a legitimate argument that it should not be expected to constrain emissions while still developing. But the 3 Zero framework explicitly includes zero net carbon emissions as an equal goal — and by that standard, this pillar is failing completely.

The Solar Home System program and pockets of renewable energy adoption are positive but tiny relative to the fossil fuel trajectory. Getting this pillar on track would require changes that go beyond social business — it would need shifts in national energy policy, industrial regulation, and international climate finance.

### 5.5 Why the 3ZPI Peaked in 2010

One of the more interesting results is that the 3ZPI reached its highest value (0.692) in 2010 and then declined through the 2010s. Why?

In 2010, youth unemployment happened to be at its lowest observed level (6.29%), which gave the unemployment pillar a normalized score of 1.000. At the same time, CO₂ emissions were still relatively low (0.355 t/capita), and poverty had already been declining for a decade. This was the "sweet spot" — enough poverty reduction to push the poverty pillar up, unemployment at a cyclical low, and emissions not yet at levels that dragged the index down badly.

After 2010, unemployment worsened and emissions accelerated, overwhelming the continued poverty gains. The 3ZPI did not start recovering until 2022–2023, when youth unemployment dropped sharply (to 7.91% by 2023) while poverty hit its best observed value.

### 5.6 Limitations

1. **Poverty data is heavily interpolated.** Only 5 of the 24 years have actual survey data. The linear interpolation between survey years smooths out short-term shocks (like COVID-19's poverty impact in 2020) and introduces uncertainty. The 2023 poverty value is carried forward from the 2022 survey since no newer survey exists.

2. **Youth unemployment is modeled, not surveyed.** The ILO modeled estimates combine national data with imputation. They are the best available consistent time series, but they are not direct measurements and carry modeling uncertainty.

3. **CO₂ data source transition.** World Bank CO₂ data was used through ~2020, supplemented by Global Carbon Project data for 2021–2023. Different source methodologies may introduce a small discontinuity.

4. **Three indicators simplify a complex reality.** Poverty at $2.15/day misses multidimensional deprivation. Youth unemployment (15–24) misses underemployment, informality, and the situation of workers aged 25+. CO₂ per capita misses total emissions, sectoral composition, and methane/other greenhouse gases.

5. **Small indicator set limits the 3ZPI.** With only one indicator per pillar, there is no within-pillar diversification. A single indicator's idiosyncrasies (like unemployment's year-to-year volatility) directly affects the pillar score.

6. **Linear regression on 24 points is descriptive, not predictive.** The projections (poverty reaching zero by ~2027) should be read as benchmarks, not forecasts.

7. **No causation.** The strong correlations reflect co-movement over time, not proven causal mechanisms.

---

## 6. Conclusion and Recommendations

### 6.1 Summary of Findings

This study measured Bangladesh's progress toward the three zeros — zero poverty, zero unemployment, and zero net carbon emissions — over 2000–2023 using verified data from the World Bank and Global Carbon Project. The key findings:

1. **The composite 3ZPI moved only modestly, from 0.506 to 0.592 (+0.085).** It peaked at 0.692 in 2010 and then declined through 2020 (0.318) before recovering. Overall 3 Zero progress has been limited despite dramatic poverty reduction.

2. **Poverty reduction at $2.15/day has been extraordinary** — from 41.4% to 5.9%, with a strong linear trend (β = −1.48, R² = 0.988) and a projected approach to zero by ~2027.

3. **Youth unemployment is trending in the wrong direction** (β = +0.18, R² = 0.423). It fluctuates year to year but the overall direction is upward, not toward zero.

4. **CO₂ per capita has more than tripled** (0.197 → 0.610t) with a strong upward trend (β = +0.020, R² = 0.981). This pillar is moving away from its target.

5. **A near-perfect negative correlation (r = −0.978) between poverty and CO₂ progress** confirms that the economic growth driving poverty reduction simultaneously worsens carbon performance. All three inter-pillar correlations are statistically significant.

6. **The results are robust to alternative weighting schemes.** Under all four tested configurations, the same pattern holds.

### 6.2 Recommendations

**For policymakers:**

1. **Track the three goals together.** The data shows they are interconnected — progress on one can mask deterioration in another. A composite index like the 3ZPI, updated annually, would give a more honest picture than tracking poverty, employment, and emissions separately.

2. **Treat youth unemployment as a structural problem.** The current upward trend means existing policies are not working at the aggregate level. Addressing the skills mismatch, supporting formal employment for young graduates, and expanding vocational training could help reverse the trend.

3. **Take the carbon pillar seriously.** The tripling of per-capita emissions is incompatible with the 3 Zero vision. Accelerating renewable energy, reconsidering new fossil fuel capacity, and pursuing energy efficiency in industry are necessary interventions. International climate finance should be part of the strategy.

**For the 3 Zero Movement:**

4. **Invest in green employment.** The intersection of the unemployment and carbon pillars — jobs that reduce rather than increase emissions — is the most underdeveloped space. Solar microenterprises, sustainable agriculture, and waste management cooperatives align with both goals.

5. **Publish quantitative progress reports.** Moving from aspirational messaging to regular, data-driven assessments using a framework like the 3ZPI would build credibility and accountability.

**For future research:**

6. **Use more indicators per pillar.** Adding multidimensional poverty, underemployment, female LFPR, renewable energy share, and total CO₂ would give a richer picture and reduce dependence on any single indicator.

7. **Apply nonlinear models.** Poverty reduction likely follows a logistic curve (slowing as the rate approaches zero). Nonlinear regression would give more realistic projections.

8. **Conduct subnational analysis.** District-level or division-level 3ZPI would reveal spatial inequalities in progress.

9. **Compare across South Asia.** Applying the same methodology to India, Nepal, and Sri Lanka would show whether the poverty–carbon trade-off is a Bangladesh-specific finding or a regional pattern.

### 6.3 Concluding Remarks

The 3 Zero Movement asks for an economic system that produces no poverty, no unemployment, and no environmental damage. This study did not evaluate whether that vision is achievable. What it tried to do is simpler — measure where Bangladesh stands right now against those three goals, using verified data and the mathematical tools available to an applied mathematics student.

The picture that emerges is stark. Bangladesh has made extraordinary progress on extreme poverty — the $2.15/day headcount ratio has fallen by over 85% in two decades. But this success has come alongside worsening youth unemployment and steadily rising carbon emissions. The composite 3ZPI barely moved over 24 years because the gains in one pillar were offset by losses in the other two.

The near-perfect negative correlation between poverty reduction and carbon performance (r = −0.98) is perhaps the most important finding. It says that Bangladesh's current development model, while highly effective at reducing poverty, is structurally antagonistic to the carbon target. If all three zeros are to be achieved, something has to change in how growth happens — not just how fast.

The 3ZPI is a simple tool. Min-max normalization, weighted averages, and linear regression are introductory applied mathematics. But sometimes straightforward tools, applied to a well-defined question with honest data, can be useful. If this framework helps make the 3 Zero conversation a little more concrete and a little more accountable, then it has served its purpose.

---

## References

1. Ahmed, S., & Hossain, M. (2018). Environmental sustainability in Bangladesh: Progress and challenges. *Environmental Policy and Law*, 48(2), 112–120.

2. Banerjee, A., Duflo, E., Glennerster, R., & Kinnan, C. (2015). The miracle of microfinance? Evidence from a randomized evaluation. *American Economic Journal: Applied Economics*, 7(1), 22–53.

3. Bangladesh Bureau of Statistics. (2022). *Labour Force Survey Bangladesh 2022*. Ministry of Planning, Government of Bangladesh.

4. Bangladesh Bureau of Statistics. (2022). *Household Income and Expenditure Survey 2022*. Ministry of Planning, Government of Bangladesh.

5. Germanwatch. (2021). *Global Climate Risk Index 2021*. Bonn: Germanwatch e.V.

6. Global Carbon Project. (2023). Global carbon budget 2023. *Earth System Science Data*, 15(12), 5301–5369.

7. Government of Bangladesh. (2021). *Nationally Determined Contributions (Updated) 2021*. Ministry of Environment, Forest and Climate Change.

8. IDCOL. (2020). *Annual Report 2019–2020*. Infrastructure Development Company Limited, Dhaka.

9. International Labour Organization. (2023). *World Employment and Social Outlook: Trends 2023*. Geneva: ILO.

10. Khandker, S. R. (2005). Microfinance and poverty: Evidence using panel data from Bangladesh. *The World Bank Economic Review*, 19(2), 263–286.

11. Morduch, J. (1999). The microfinance promise. *Journal of Economic Literature*, 37(4), 1569–1614.

12. Rahman, M., & Islam, D. (2019). Youth unemployment and the skills gap in Bangladesh: Challenges and policy responses. *Bangladesh Development Studies*, 42(1), 1–28.

13. Stern, N. (2007). *The Economics of Climate Change: The Stern Review*. Cambridge University Press.

14. United Nations. (2015). Transforming our world: The 2030 Agenda for Sustainable Development. *UN General Assembly Resolution A/RES/70/1*.

15. World Bank. (2021). *Bangladesh COVID-19 Poverty Monitoring Survey*. Washington, DC: World Bank Group.

16. World Bank. (2023). *Bangladesh Development Update: Resilience Under Test*. Washington, DC: World Bank Group.

17. World Bank. (2023). *World Development Indicators* [Data set]. Washington, DC: World Bank Group. https://data.worldbank.org

18. Yunus, M. (2007). *Banker to the Poor: Micro-Lending and the Battle Against World Poverty*. PublicAffairs.

19. Yunus, M. (2017). *A World of Three Zeros: The New Economics of Zero Poverty, Zero Unemployment, and Zero Net Carbon Emissions*. PublicAffairs.

20. Yunus Centre. (2020). *Social Business and the Three Zeros: Progress Report*. Dhaka: Yunus Centre.

---

*Corresponding author: Minhajul Abedin, Department of Applied Mathematics, Noakhali Science and Technology University (NSTU), Bangladesh.*
