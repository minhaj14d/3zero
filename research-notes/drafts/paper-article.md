# Exploring the Impact of the 3 Zero Movement in Bangladesh: A Pathway to Sustainable Development

> Last updated: 2026-03-28
> Status: Draft (v2 — tone revision)
> Target venue: 18th International Conference on Engineering & Natural Sciences (Full paper)
> Previous version backup: backups/paper-article-v1-expert-tone.md

---

**Minhajul Abedin**

Department of Applied Mathematics, 4th Year Undergraduate

---

**Abstract**

Bangladesh has been growing fast, both in its economy and population, and that combination brings real challenges. The country needs to figure out how to keep growing without undermining its own future. There has been genuine progress in areas like health and education, but poverty, joblessness, and environmental damage remain serious problems that could hold things back. This study looks at the 3 Zero Movement — Professor Muhammad Yunus's framework for achieving zero poverty, zero unemployment, and zero net carbon emissions — and tries to measure how much actual progress Bangladesh has made toward these goals over the period 2013–2023. Rather than relying only on qualitative assessments, this paper takes a quantitative approach: eight indicators across the three pillars are collected from sources like the World Bank, the Bangladesh Bureau of Statistics, the ILO, and the Global Carbon Project. These indicators are normalized and combined into a composite 3 Zero Progress Index (3ZPI). Linear regression is used to estimate how fast each indicator is changing, and Pearson correlation analysis is used to check whether the three pillars move together or pull against each other. The results show that poverty reduction has been the strongest area of progress (pillar score rising from 0.00 to 1.00), employment has improved but took a big hit during COVID-19 (0.51 to 0.92), and the carbon emissions pillar has actually gotten worse (0.67 to 0.33), with total emissions growing by about 54%. The overall 3ZPI went from 0.39 to 0.75, but a strong negative correlation (r = −0.94) between poverty and carbon progress suggests a real tension: the same economic activity that lifts people out of poverty also drives up emissions. These findings point to a structural imbalance in how Bangladesh is developing, and suggest that without targeted action on clean energy and greener forms of employment, the carbon pillar will keep dragging down overall progress.

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

The data to answer these questions largely exists. The World Bank publishes poverty and emissions data. The Bangladesh Bureau of Statistics runs labour force surveys and household income surveys. The Global Carbon Project tracks CO₂. But these datasets sit in different places, measured on different scales, and nobody has tried to combine them into a single framework that tracks 3 Zero progress as a whole.

From an applied math standpoint, this is actually a pretty clean problem. You have multiple indicators on different scales, and you want to normalize them, weight them, and combine them into a composite index. Then you can do trend analysis and correlation to see what is really happening. That is the approach this paper takes.

### 1.3 Research Questions

Three questions guide this study:

1. How much quantitative progress has Bangladesh made toward each of the three zero targets over the decade 2013–2023?
2. Are the three pillars moving together (synergy) or against each other (trade-offs) — and can we measure that statistically?
3. At the current rate of change, when might Bangladesh reach each target, and which pillar is the biggest bottleneck?

### 1.4 Objectives

1. To collect and analyze data on eight indicators across the three pillars using publicly available secondary sources.
2. To construct a composite 3 Zero Progress Index (3ZPI) by normalizing and aggregating these indicators.
3. To examine statistical relationships between the pillars using Pearson correlation.
4. To project when each target might be reached using linear extrapolation, and to identify the most lagging pillar.
5. To offer some recommendations based on what the data shows.

### 1.5 Significance of the Study

Most writing about the 3 Zero Movement is qualitative. This study tries to add a quantitative layer. The methodology — min-max normalization, weighted aggregation, linear regression, Pearson correlation — is not advanced by mathematics standards, but that is partly the point. These are accessible tools that any researcher can replicate, and they have not been applied to this particular problem before.

For policymakers, a composite index like the 3ZPI could work as a quick diagnostic: which pillar is on track and which is not? For the academic side, the correlation analysis between pillars is potentially the most useful contribution, since it can reveal whether Bangladesh's current development model is compatible with all three zeros or whether there are built-in tensions that need to be managed.

As an applied mathematics student, I was drawn to this topic because it is a case where straightforward mathematical tools can shed light on a question that is usually discussed in purely qualitative terms. The math is not the hard part here — the hard part is interpreting what the numbers mean for real policy. I have tried to be honest about where the data speaks clearly and where it does not.

---

## 2. Literature Review

### 2.1 The 3 Zero Movement: Conceptual Foundations

The 3 Zero Movement grew out of Professor Muhammad Yunus's experience with Grameen Bank, which he founded in 1983 to give small loans to poor people in rural Bangladesh without requiring collateral. The idea that poor people are creditworthy — and that small loans can help them start businesses and work their way out of poverty — earned Yunus the Nobel Peace Prize in 2006 and sparked a global microfinance movement (Yunus, 2007).

In *A World of Three Zeros* (2017), Yunus went further. He argued that the current economic system, which is organized around profit maximization, is not built to solve problems like poverty, unemployment, and environmental damage. His alternative is "social business" — companies designed to address social problems rather than to make profits for shareholders. The book presents three interconnected targets: zero poverty, zero unemployment, and zero net carbon emissions. The key word is interconnected — Yunus's argument is that you cannot fix one without the others. Poverty will not stay eliminated if employment is precarious, and neither goal is sustainable if the environment is being degraded (Yunus, 2017).

There is overlap between the 3 Zero framework and the UN Sustainable Development Goals adopted in 2015 (United Nations, 2015), but they are not the same thing. The SDGs are broad, government-focused, and time-bound (target year 2030). The 3 Zero Movement is more specific in its philosophy — it emphasizes entrepreneurship, social business, and bottom-up change rather than top-down policy (Yunus Centre, 2020).

### 2.2 Zero Poverty: What the Literature Says About Bangladesh

Bangladesh has a genuinely impressive track record on poverty reduction. The national poverty headcount ratio went from about 48.9% in 2000 down to 24.3% by 2016, based on the Household Income and Expenditure Survey by the Bangladesh Bureau of Statistics (BBS, 2017). The 2022 HIES brought this down further to roughly 18.7%, though comparing across surveys is tricky because the methodology changes over time.

Microfinance has been one contributor to this decline. Khandker (2005) found, using panel data from Bangladesh, that microfinance participation was linked to about a 1.6 percentage point reduction in moderate poverty per year for participating households. But the evidence is not one-sided — Morduch (1999) pointed out that many studies on microfinance suffer from selection bias, and that the real impact may be more modest than the headline numbers suggest. More recently, Banerjee et al. (2015) found that microfinance helps with consumption smoothing and small investments but is less effective at permanently lifting people out of poverty.

The Multidimensional Poverty Index (MPI), developed by Alkire and Foster (2011), gives a broader picture by tracking deprivations across health, education, and living standards — not just income. Bangladesh's MPI has improved consistently: the proportion of multidimensionally poor people fell from about 41.7% in 2014 to around 24.6% by 2019 (UNDP & OPHI, 2020).

The COVID-19 pandemic set things back. The World Bank estimated that between 14 and 24 million Bangladeshis were pushed into poverty during 2020 because of lost income, closed businesses, and reduced remittances (World Bank, 2021). There was partial recovery afterwards, but the episode showed how fragile poverty gains can be without strong safety nets.

One persistent issue is the rural-urban gap. Poverty remains much higher in rural areas and in divisions like Rangpur and Mymensingh, while Dhaka and Chittagong have done better thanks to industrial employment (BBS, 2022).

### 2.3 Zero Unemployment: The Employment Situation

Bangladesh's official unemployment rate stays between 4% and 5%, which sounds low but is misleading. The BBS (following ILO guidelines) counts anyone who worked at least one hour in the reference week as "employed." Under that definition, someone doing a few hours of irregular work with no contract counts the same as someone with a full-time job (BBS, 2022).

Underemployment is a more telling number. The 2022 Labour Force Survey found that about 6.4% of the labour force was working fewer than 40 hours per week despite wanting more work. When you add in people whose earnings fall below subsistence levels, the real picture of inadequate employment is much worse than 4%.

Youth unemployment stands out as a problem. Among people aged 15–29, unemployment runs at 10–12%, two to three times the national average (ILO, 2023). There is also a paradox of "educated unemployment" — people with secondary or university degrees actually face higher unemployment than those with less education, because the skills the education system produces do not match what employers need (Rahman & Islam, 2019).

Women's labour force participation has been going up, rising from about 33.5% in 2013 to 42.0% by 2023 (BBS, 2022). The ready-made garments (RMG) sector, which employs around 4 million workers (mostly women), has been a big driver of this (Kabeer & Mahmud, 2004). But the quality of these jobs — wages, working conditions, safety — remains a serious concern.

The 3 Zero Movement's take on unemployment is distinctive. Instead of conventional job-creation policies, Yunus argues that everyone is a potential entrepreneur and that the financial system should enable self-employment through microcredit and social business (Yunus, 2017). Grameen Bank has had real results with this approach, but whether it can scale to cover a labour force of over 70 million people is an open question.

### 2.4 Zero Net Carbon Emissions: The Environmental Picture

Bangladesh's carbon situation is full of contradictions. Per capita emissions are among the lowest in the world — about 0.57 tonnes of CO₂ per person in 2023, compared to a global average of around 4.7 tonnes (Global Carbon Project, 2023). But total emissions have been climbing fast, from roughly 65 million tonnes (Mt) in 2013 to nearly 100 Mt by 2023, a 54% increase driven by population growth, industrialization, and more energy use (World Bank, 2023).

The energy sector accounts for over 60% of CO₂ emissions. Bangladesh still depends heavily on natural gas (about 55% of commercial energy), and several new coal-fired power plants came online during the study period. The Rampal plant near the Sundarbans drew a lot of criticism internationally (Ahmed & Hossain, 2018). Industrial emissions come largely from brick kilns — there are thousands of them across the country — plus cement and steel production.

Under the Paris Agreement, Bangladesh committed to reducing greenhouse gas emissions by 21.85% below business-as-usual by 2030, with 6.73% unconditional and the rest depending on international support (Government of Bangladesh, 2021). But so far, progress toward these targets has been limited.

There is a bright spot in renewable energy. The Solar Home System program, backed by IDCOL, installed over 6 million solar units in off-grid rural areas, which is one of the biggest programs of its kind anywhere (IDCOL, 2020). However, the overall share of renewables in total energy is still only about 4.5% as of 2023 — nowhere near enough for any realistic path to zero emissions.

What makes this especially urgent for Bangladesh is vulnerability. The Global Climate Risk Index consistently ranks Bangladesh in the top ten countries most affected by extreme weather (Germanwatch, 2021). Cyclones, floods, sea-level rise, and riverbank erosion affect millions of people. The country bears a disproportionate share of climate costs relative to its contribution to the problem.

### 2.5 The Gap This Study Addresses

Reading through the literature, a couple of things stood out. First, most studies look at poverty, employment, and carbon emissions separately. Integrated studies that assess all three together are rare. Second, while there is plenty of writing about the 3 Zero Movement as a concept, I could not find any study that attempts to measure progress toward the three zeros quantitatively using a composite index.

This paper tries to fill both of those gaps. It treats the three zeros as parts of a single system and uses mathematical tools — normalization, weighted indexing, regression, and correlation — to track how they are moving. The methods are standard applied mathematics, and the whole thing is designed to be reproducible by anyone with access to the same public datasets.

---

## 3. Methodology

### 3.1 Research Design

This study uses a mixed-methods approach, but the emphasis is on the quantitative side. The main analytical work involves secondary data analysis using publicly available datasets. A qualitative review of policy documents is included to help explain the trends that show up in the data, but the numbers are the core of the paper.

The quantitative analysis has four stages: (i) data collection and indicator definition; (ii) normalization and composite index construction; (iii) trend analysis using linear regression; and (iv) inter-pillar correlation analysis.

### 3.2 Data Sources

The data comes from the following sources:

- **Poverty indicators:** World Bank Development Indicators; BBS Household Income and Expenditure Survey (HIES) 2016 and 2022; UNDP/OPHI Multidimensional Poverty Index reports.
- **Employment indicators:** BBS Labour Force Survey (multiple rounds); ILO ILOSTAT database; Bangladesh Bank annual reports on microcredit disbursement.
- **Carbon emissions indicators:** World Bank CO₂ emissions data (sourced from CDIAC and Global Carbon Project); IRENA statistics; Bangladesh Power Development Board annual reports.
- **Policy documents:** Government of Bangladesh 8th Five Year Plan (2020–2025); Bangladesh Climate Change Strategy and Action Plan (BCCSAP); Nationally Determined Contributions under the Paris Agreement; Yunus Centre publications.

The study covers 2013 to 2023. For indicators where annual data was not available (especially poverty and MPI, which come from surveys done every few years), values were linearly interpolated between survey years. This is a limitation I discuss later.

### 3.3 Indicator Selection

I selected eight indicators across the three pillars, based on three criteria: relevance to the zero target, availability of data for the full study period, and consistency of measurement.

**Table 1: Indicator Definitions**

| Pillar | Indicator | Description | Source | Unit | Direction |
|--------|-----------|-------------|--------|------|-----------|
| P1 | Poverty Headcount Ratio | Population below national poverty line | BBS/World Bank | % | Lower is better |
| P2 | MPI Value | Multidimensional Poverty Index | UNDP/OPHI | Index (0–1) | Lower is better |
| U1 | Unemployment Rate | % of labour force unemployed | BBS/ILO | % | Lower is better |
| U2 | Youth Unemployment Rate | Unemployment among ages 15–29 | BBS/ILO | % | Lower is better |
| U3 | Female LFPR | Female labour force participation rate | BBS | % | Higher is better |
| C1 | Total CO₂ Emissions | Annual carbon dioxide emissions | World Bank/GCP | Mt CO₂ | Lower is better |
| C2 | CO₂ per Capita | Per-person annual emissions | World Bank | t CO₂ | Lower is better |
| C3 | Renewable Energy Share | Renewables as % of total primary energy | IRENA/Govt. | % | Higher is better |

The "Direction" column matters for normalization. Some indicators are better when they go down (poverty, unemployment, emissions), and some are better when they go up (female LFPR, renewable share).

### 3.4 Data

**Table 2: Raw Indicator Data (2013–2023)**

| Year | P1 (%) | P2 | U1 (%) | U2 (%) | U3 (%) | C1 (Mt) | C2 (t) | C3 (%) |
|------|--------|------|--------|--------|--------|---------|--------|--------|
| 2013 | 26.4 | 0.196 | 4.3 | 11.2 | 33.5 | 64.8 | 0.42 | 2.8 |
| 2014 | 25.6 | 0.183 | 4.4 | 11.4 | 34.1 | 68.2 | 0.43 | 2.9 |
| 2015 | 24.8 | 0.170 | 4.2 | 10.9 | 35.6 | 72.5 | 0.45 | 3.0 |
| 2016 | 24.3 | 0.157 | 4.2 | 10.6 | 36.3 | 76.1 | 0.47 | 3.1 |
| 2017 | 23.2 | 0.143 | 4.4 | 10.8 | 37.2 | 79.8 | 0.48 | 3.3 |
| 2018 | 21.8 | 0.132 | 4.3 | 10.5 | 38.4 | 84.0 | 0.50 | 3.5 |
| 2019 | 20.5 | 0.119 | 4.2 | 10.2 | 39.1 | 88.2 | 0.52 | 3.7 |
| 2020 | 22.0 | 0.126 | 5.3 | 12.8 | 36.8 | 82.6 | 0.49 | 3.9 |
| 2021 | 21.2 | 0.118 | 4.8 | 12.1 | 38.0 | 90.5 | 0.53 | 4.1 |
| 2022 | 18.7 | 0.104 | 4.5 | 11.5 | 40.6 | 95.3 | 0.55 | 4.3 |
| 2023 | 17.8 | 0.095 | 4.2 | 10.8 | 42.0 | 99.8 | 0.57 | 4.5 |

*Sources: World Bank Development Indicators; BBS HIES (2016, 2022); BBS Labour Force Survey; UNDP/OPHI MPI; Global Carbon Project; IRENA.*
*Note: Poverty and MPI values for non-survey years are linear interpolations.*

### 3.5 Normalization

Since the indicators are measured on completely different scales (percentages, index values, megatonnes), they need to be brought to a common range before they can be compared or combined. I used min-max normalization to rescale everything to [0, 1], where 1 means the best observed performance and 0 means the worst.

For indicators where lower is better (P1, P2, U1, U2, C1, C2), I used the inverted formula:

$$x_{i,\text{norm}} = \frac{x_{\max} - x_i}{x_{\max} - x_{\min}}$$

For indicators where higher is better (U3, C3), the standard formula:

$$x_{i,\text{norm}} = \frac{x_i - x_{\min}}{x_{\max} - x_{\min}}$$

Here $x_{\max}$ and $x_{\min}$ are the maximum and minimum values observed across the full 2013–2023 period. This means the normalization is relative — it shows how each year compares to the best and worst years in the dataset, not against some absolute benchmark.

**Table 3: Min-Max Bounds for Normalization**

| Indicator | Min | Max |
|-----------|------|------|
| P1 — Poverty (%) | 17.8 | 26.4 |
| P2 — MPI | 0.095 | 0.196 |
| U1 — Unemployment (%) | 4.2 | 5.3 |
| U2 — Youth Unemp. (%) | 10.2 | 12.8 |
| U3 — Female LFPR (%) | 33.5 | 42.0 |
| C1 — CO₂ Total (Mt) | 64.8 | 99.8 |
| C2 — CO₂ per Capita (t) | 0.42 | 0.57 |
| C3 — Renewable Share (%) | 2.8 | 4.5 |

### 3.6 Composite 3 Zero Progress Index (3ZPI)

Building the index involves two steps. First, the pillar-level scores are computed by averaging the normalized indicators within each pillar:

$$P = \frac{1}{n_P} \sum_{j=1}^{n_P} x_{P_j,\text{norm}}, \quad U = \frac{1}{n_U} \sum_{j=1}^{n_U} x_{U_j,\text{norm}}, \quad C = \frac{1}{n_C} \sum_{j=1}^{n_C} x_{C_j,\text{norm}}$$

where $n_P = 2$, $n_U = 3$, and $n_C = 3$.

Then the overall 3ZPI is a weighted sum of the three pillar scores:

$$\text{3ZPI}_t = w_P \cdot P_t + w_U \cdot U_t + w_C \cdot C_t$$

with $w_P + w_U + w_C = 1$. For the baseline, I used equal weights ($w_P = w_U = w_C = \frac{1}{3}$), since the 3 Zero Movement treats all three goals as equally important. I also ran a sensitivity analysis with different weights to check whether the conclusions change (Section 4.4).

A 3ZPI of 1 would mean every indicator has reached its best observed value; a score of 0 would mean everything is at its worst observed value. It is worth noting that a score of 1 does not mean the actual zero targets have been reached — just that every indicator is at its best level within this particular dataset.

### 3.7 Trend Analysis

To get a sense of how fast things are changing, I ran a simple linear regression on each raw indicator over time:

$$y_t = \alpha + \beta \cdot t + \epsilon_t$$

where $t = 0$ for 2013 through $t = 10$ for 2023. The slope $\beta$ tells us the average annual rate of change, and $R^2$ tells us how well a straight line fits the data.

For indicators where the target is zero, I estimated how long it would take to get there at the current rate:

$$t_{\text{zero}} = 2023 + \frac{y_{2023}}{|\beta|}$$

This is a rough projection — it assumes the current linear trend just continues indefinitely, which is obviously a simplification. But it gives a useful baseline for comparison.

### 3.8 Correlation Analysis

To check whether the pillars move together or against each other, I computed Pearson correlation coefficients between the annual pillar scores:

$$r_{XY} = \frac{\sum_{t=1}^{n}(X_t - \bar{X})(Y_t - \bar{Y})}{\sqrt{\sum_{t=1}^{n}(X_t - \bar{X})^2 \cdot \sum_{t=1}^{n}(Y_t - \bar{Y})^2}}$$

With $n = 11$ observations, the critical value for statistical significance at the 5% level is about $|r| > 0.602$ (two-tailed, $df = 9$). A positive correlation would suggest synergy (pillars improving together), and a negative correlation would suggest a trade-off (one gets better while the other gets worse).

### 3.9 Tools

All calculations were done in Python 3.11 using pandas, NumPy, and scipy.stats. Plots were made with matplotlib and seaborn.

---

## 4. Analysis and Findings

### 4.1 Normalized Indicator Scores

After applying the normalization formulas from Section 3.5, here are the results:

**Table 4: Normalized Indicator Scores (2013–2023)**

| Year | P1 | P2 | U1 | U2 | U3 | C1 | C2 | C3 |
|------|------|------|------|------|------|------|------|------|
| 2013 | 0.000 | 0.000 | 0.909 | 0.615 | 0.000 | 1.000 | 1.000 | 0.000 |
| 2014 | 0.093 | 0.129 | 0.818 | 0.538 | 0.071 | 0.903 | 0.933 | 0.059 |
| 2015 | 0.186 | 0.257 | 1.000 | 0.731 | 0.247 | 0.780 | 0.800 | 0.118 |
| 2016 | 0.244 | 0.386 | 1.000 | 0.846 | 0.329 | 0.677 | 0.667 | 0.176 |
| 2017 | 0.372 | 0.525 | 0.818 | 0.769 | 0.435 | 0.571 | 0.600 | 0.294 |
| 2018 | 0.535 | 0.634 | 0.909 | 0.885 | 0.576 | 0.451 | 0.467 | 0.412 |
| 2019 | 0.686 | 0.762 | 1.000 | 1.000 | 0.659 | 0.331 | 0.333 | 0.529 |
| 2020 | 0.512 | 0.693 | 0.000 | 0.000 | 0.388 | 0.491 | 0.533 | 0.647 |
| 2021 | 0.605 | 0.772 | 0.455 | 0.269 | 0.529 | 0.266 | 0.267 | 0.765 |
| 2022 | 0.895 | 0.911 | 0.727 | 0.500 | 0.835 | 0.129 | 0.133 | 0.882 |
| 2023 | 1.000 | 1.000 | 1.000 | 0.769 | 1.000 | 0.000 | 0.000 | 1.000 |

A few things jump out right away. The poverty indicators (P1, P2) climb steadily from 0 to 1 — that is the clearest positive trend in the dataset. The employment indicators (U1, U2, U3) were improving until 2020 hit and everything crashed, then gradually recovered. The carbon indicators tell a split story: C1 and C2 (actual emission levels) drop from 1.000 toward 0.000 as emissions grew, while C3 (renewable energy share) goes the other way, from 0.000 to 1.000. The problem is that the renewable gains are not nearly enough to offset the emission increases.

### 4.2 Pillar-Level Scores

Averaging the normalized indicators within each pillar gives the following:

**Table 5: Pillar Scores and 3ZPI (2013–2023)**

| Year | Poverty (P) | Unemployment (U) | Carbon (C) | **3ZPI** |
|------|-------------|-------------------|------------|----------|
| 2013 | 0.000 | 0.508 | 0.667 | **0.392** |
| 2014 | 0.111 | 0.476 | 0.632 | **0.406** |
| 2015 | 0.222 | 0.659 | 0.566 | **0.482** |
| 2016 | 0.315 | 0.725 | 0.507 | **0.516** |
| 2017 | 0.449 | 0.674 | 0.488 | **0.537** |
| 2018 | 0.585 | 0.790 | 0.443 | **0.606** |
| 2019 | 0.724 | 0.886 | 0.398 | **0.669** |
| 2020 | 0.603 | 0.129 | 0.557 | **0.430** |
| 2021 | 0.689 | 0.418 | 0.433 | **0.513** |
| 2022 | 0.903 | 0.687 | 0.381 | **0.657** |
| 2023 | 1.000 | 0.923 | 0.333 | **0.752** |

The three pillars tell very different stories:

**Poverty (P):** This is the clear winner. The score goes from 0.000 to 1.000 over the decade — meaning that by 2023, both poverty indicators had reached their best values in the dataset. The poverty headcount dropped 8.6 percentage points and the MPI roughly halved. Even the COVID-19 dip in 2020 (down to 0.603) was relatively mild compared to the employment pillar, and it bounced back quickly.

**Unemployment (U):** This pillar was doing well before the pandemic, reaching 0.886 in 2019. Then COVID-19 hit and it crashed to 0.129 in 2020 — the most dramatic single-year drop in the entire dataset. Unemployment spiked, and female labour force participation fell back. Recovery was slow — it took until 2023 to get back to 0.923. The volatility here says something about how vulnerable Bangladesh's employment base is to external shocks.

**Carbon (C):** This is the problem pillar. It is the only one that got worse over the decade, falling from 0.667 to 0.333. Renewable energy adoption improved (C3 went from 0.000 to 1.000 in normalized terms), but that was overwhelmed by the steady increase in actual emissions (C1 and C2 both ended at 0.000). The carbon pillar is moving in the opposite direction from the other two.

### 4.3 3ZPI Trajectory

Overall, the composite 3ZPI went from 0.392 in 2013 to 0.752 in 2023, which is a 92% increase from the starting value. But the path was not smooth:

- **2013–2019:** Steady climb from 0.392 to 0.669, driven mainly by poverty reduction and improving employment.
- **2020:** Sharp fall to 0.430 because of COVID-19 — roughly five years of progress wiped out in one year.
- **2021–2023:** Recovery and then acceleration to a new high of 0.752.

One thing worth noting about 2020: the three pillars responded very differently to the pandemic. Poverty dipped moderately (0.724 → 0.603). Employment collapsed (0.886 → 0.129). And carbon actually improved temporarily (0.398 → 0.557), because reduced economic activity meant lower emissions. That last point is telling — the carbon improvement was a side-effect of economic pain, not a real structural shift. As soon as the economy recovered, emissions went right back up.

### 4.4 Sensitivity Analysis: Alternative Weighting Schemes

Equal weights seem reasonable since the 3 Zero Movement treats all three goals as equally important, but I wanted to check whether the results depend heavily on that choice. So I ran the index with three alternative weighting schemes:

- **Poverty-heavy:** $w_P = 0.50$, $w_U = 0.25$, $w_C = 0.25$
- **Employment-heavy:** $w_P = 0.25$, $w_U = 0.50$, $w_C = 0.25$
- **Carbon-heavy:** $w_P = 0.25$, $w_U = 0.25$, $w_C = 0.50$

**Table 6: 3ZPI Under Alternative Weighting Schemes (Selected Years)**

| Year | Equal (⅓, ⅓, ⅓) | Poverty-heavy | Employment-heavy | Carbon-heavy |
|------|------------------|---------------|------------------|--------------|
| 2013 | 0.392 | 0.294 | 0.421 | 0.461 |
| 2016 | 0.516 | 0.465 | 0.571 | 0.511 |
| 2019 | 0.669 | 0.683 | 0.765 | 0.561 |
| 2020 | 0.430 | 0.473 | 0.236 | 0.557 |
| 2023 | 0.752 | 0.814 | 0.795 | 0.648 |

The main takeaway: the conclusions do not change much with different weights. The carbon-heavy weighting gives the lowest 2023 score (0.648), confirming that the carbon pillar drags things down no matter how you weight it. The poverty-heavy weighting gives the highest score (0.814), reflecting how strong that pillar is. The employment-heavy weighting shows the deepest COVID crash (0.236 in 2020). But in all four cases, the same basic pattern holds: poverty is doing well, employment is volatile but recovering, and carbon is the weak link.

### 4.5 Trend Analysis: Linear Regression Results

Here are the regression results for each raw indicator:

**Table 7: Linear Regression Results (y = α + βt, t = 0 for 2013)**

| Indicator | β (annual change) | R² | What it means |
|-----------|--------------------|----|---------------|
| P1 — Poverty (%) | −0.76 | 0.92 | Poverty dropping ~0.76 pp/year |
| P2 — MPI | −0.0094 | 0.97 | MPI declining steadily |
| U1 — Unemployment (%) | −0.003 | 0.001 | Basically flat — no real trend |
| U2 — Youth Unemp. (%) | −0.005 | 0.001 | Also flat |
| U3 — Female LFPR (%) | +0.72 | 0.85 | Going up ~0.72 pp/year |
| C1 — CO₂ Total (Mt) | +3.24 | 0.95 | Emissions rising ~3.2 Mt/year |
| C2 — CO₂ per Capita (t) | +0.014 | 0.96 | Per-capita emissions rising too |
| C3 — Renewable Share (%) | +0.17 | 0.99 | Renewables growing, but slowly |

The poverty indicators have strong downward trends with high $R^2$, meaning the decline has been consistent and well-described by a straight line. Unemployment shows essentially no linear trend at all — $R^2$ is near zero — because the COVID-19 disruption threw off any pattern that might have existed. Female LFPR is the bright spot in the employment pillar, with a solid upward trend. Carbon indicators have strong upward trends (meaning emissions are reliably increasing every year), and renewable energy growth, while consistent, is very slow at just 0.17 percentage points per year.

### 4.6 Gap Analysis and Projections

Using the regression slopes, I estimated when each target might be reached if current trends just continue:

**Table 8: Gap Analysis and Linear Extrapolation**

| Indicator | 2023 Value | Target | β (annual) | Projected Year to Target |
|-----------|------------|--------|------------|--------------------------|
| P1 — Poverty (%) | 17.8 | 0 | −0.76 | ~2047 |
| P2 — MPI | 0.095 | 0 | −0.0094 | ~2033 |
| U1 — Unemployment (%) | 4.2 | 0 | ~0 | Not reachable at current rate |
| U2 — Youth Unemp. (%) | 10.8 | 0 | ~0 | Not reachable at current rate |
| C1 — CO₂ Total (Mt) | 99.8 | 0 | +3.24 | Going the wrong way |
| C2 — CO₂ per Capita (t) | 0.57 | 0 | +0.014 | Going the wrong way |

These projections should be taken as rough indicators, not forecasts. But they do highlight how differently the three pillars are positioned:

- **Poverty** is on a plausible downward path. The MPI could approach zero around 2033 and the headcount ratio around 2047, assuming the current pace holds. That is slow, but at least the direction is right.
- **Unemployment** is stuck. The headline rate is low but not changing in any meaningful way. Getting to "zero unemployment" in any real sense would require a fundamentally different kind of labour market — one that addresses underemployment, informality, and skills mismatch.
- **Carbon** is going the wrong way. Emissions are not just failing to decline; they are actively increasing every year. Under the current trend, they will keep rising. This is the farthest any pillar is from its target.

### 4.7 Inter-Pillar Correlation Analysis

This is probably the most interesting part of the analysis. Here is the correlation matrix between the three pillar scores:

**Table 9: Correlation Matrix of Pillar Scores**

|   | Poverty (P) | Unemployment (U) | Carbon (C) |
|---|-------------|-------------------|------------|
| **Poverty (P)** | 1.000 | 0.329 | −0.939 |
| **Unemployment (U)** | 0.329 | 1.000 | −0.595 |
| **Carbon (C)** | −0.939 | −0.595 | 1.000 |

**Poverty vs. Carbon (r = −0.939):** This is the big finding. The correlation is almost perfectly negative, which means that the years in which Bangladesh made the most progress on poverty were the same years in which carbon performance got worse. That is not a coincidence — the economic growth that pulls people out of poverty (more factories, more energy consumption, more urbanization) is also what drives emissions up. This result is statistically significant (well above the $|r| > 0.602$ threshold at 5% with $df = 9$), and it points to a real structural tension in Bangladesh's development model.

**Unemployment vs. Carbon (r = −0.595):** There is a moderate negative relationship between employment progress and carbon performance. When jobs improve (usually through industrial growth), emissions tend to worsen. This correlation is close to but does not quite hit the 5% significance threshold, partly because COVID-19 created a year where employment crashed but carbon temporarily improved, which adds noise.

**Poverty vs. Unemployment (r = 0.329):** This one surprised me. I expected a stronger positive correlation — intuitively, better employment should mean less poverty. But the relationship is weak. Looking at the data, I think there are a few reasons. A lot of employment in Bangladesh is informal and low-paid, so having a job does not necessarily mean escaping poverty. Poverty reduction has also been driven by factors other than domestic jobs — like remittances from workers abroad and government safety nets. And COVID-19 created a year (2020) where employment collapsed but poverty only rose modestly, which dilutes the correlation.

---

## 5. Discussion

### 5.1 An Imbalanced Picture

The main thing the data shows is that Bangladesh's progress toward the three zeros is lopsided. Poverty reduction is going well. Employment is improving but unstable. And carbon emissions are getting worse.

This kind of imbalance is probably not unique to Bangladesh. It is likely a feature of many developing countries that are trying to grow their way out of poverty. Economic growth based on manufacturing and energy-intensive industry creates jobs and raises incomes, but it also pushes emissions up. The question is whether this trade-off is unavoidable, or whether there are alternative ways to develop that do not have the same carbon cost.

The r = −0.94 correlation between the poverty and carbon pillars puts a number on this trade-off. It is a strong result, and it has a clear practical implication: if Bangladesh keeps reducing poverty the same way it has been — through industrialization and fossil-fuel-powered growth — the carbon pillar will keep getting worse. The 3 Zero Movement's argument that the three goals are interconnected is supported by the data, but the connection is currently adversarial rather than cooperative.

### 5.2 Poverty: Good Progress, Real Limits

The poverty numbers are genuinely encouraging. Going from 26.4% to 17.8% on the headcount ratio, and roughly halving the MPI, in a single decade is a real achievement. This reflects a combination of steady economic growth, the RMG sector providing employment, remittances from Bangladeshi workers abroad, microfinance programs, and government social safety nets (World Bank, 2023; BBS, 2022).

But there are limits. The regression slope of −0.76 pp/year implies it would take until about 2047 to reach zero poverty — which would miss the SDG deadline by 17 years. And that assumes the trend stays linear, which it probably will not; the last few percentage points of poverty are typically the hardest to reach because they involve the most marginalized and hardest-to-serve populations. The COVID-19 setback also showed that without stronger social protection, gains can be reversed quickly.

There are also geographic gaps. Poverty is still much worse in rural areas and in northern divisions like Rangpur, compared to the industrial centers of Dhaka and Chittagong. Getting to zero would require closing these spatial gaps, which is a harder problem than reducing the national average.

### 5.3 Employment: The Numbers Deceive

The employment pillar is tricky to assess because the headline unemployment rate of about 4.2% does not really capture the problem. The regression found essentially no trend ($\beta \approx 0$, $R^2 \approx 0$), which means the labour market is not undergoing any structural improvement — at least not the kind that shows up in unemployment statistics.

The real issues are underemployment, informality, and what might be called "working poverty" — having a job but still not earning enough to live decently. The 3 Zero Movement's vision of zero unemployment presumably means something more than the BBS definition of employment (one hour of work per week). It means everyone having meaningful, productive work. Bangladesh is a long way from that.

The female LFPR trend is one genuinely positive thing. Going from 33.5% to 42.0% over a decade, with a solid regression fit ($R^2 = 0.85$), shows that women are entering the workforce in larger numbers. If this continues, it could reach about 50% by the early 2030s. But whether these jobs are good jobs — well-paid, safe, with some security — is a separate question that the data used here cannot answer.

The COVID-19 crash (employment pillar going from 0.886 to 0.129 in one year) was the sharpest single movement in the dataset. It suggests that the 3 Zero framework should think not just about progress but about resilience — the ability to hold onto gains when a shock hits.

### 5.4 Carbon: The Bottleneck

The carbon pillar is where the news is worst. Emissions went up 54% over the decade. The trend is strongly positive and very consistent ($R^2 = 0.95$). There is no sign of the trajectory bending downward. Under linear extrapolation, emissions will just keep rising — which is obviously incompatible with any version of "zero net carbon emissions."

Bangladesh is in a tough position here. Its per-capita emissions are low — about 0.57 tonnes, compared to a global average of 4.7 tonnes — so there is a legitimate fairness argument that the country should not be expected to cut emissions while it is still developing. But the aggregate numbers are rising fast, and the country itself is among the most vulnerable to climate change. The costs of inaction fall disproportionately on Bangladesh.

Renewable energy is growing, but at 0.17 percentage points per year, it is far too slow to make a dent. The Solar Home System program has been a success in off-grid areas, but grid-scale renewable deployment has lagged behind.

If the 3 Zero Movement is serious about the carbon target, this pillar needs a fundamentally different approach. The social business model could play a role — solar microenterprises, sustainable agriculture cooperatives, waste-to-energy projects — but these are still small-scale relative to the size of the problem. What would really move the needle is a shift in energy and industrial policy: less coal, more grid-scale renewables, energy efficiency standards. That is more of a government-level change than a social-business-level change.

### 5.5 What COVID-19 Revealed

The pandemic year of 2020 worked almost like a natural experiment for the 3 Zero framework. Economic activity dropped, and the three pillars responded differently:

- Poverty went up modestly (pillar score dropped from 0.724 to 0.603).
- Employment collapsed (0.886 → 0.129).
- Carbon temporarily improved (0.398 → 0.557), since less economic activity meant fewer emissions.

By 2023, the 3ZPI had exceeded its pre-pandemic peak (0.752 vs. 0.669). But the recovery was driven by poverty and employment bouncing back — the carbon pillar continued getting worse as economic activity (and emissions) resumed. The brief carbon improvement was not a structural change; it was just a recession effect that reversed as soon as growth returned.

### 5.6 Limitations

I want to be upfront about the limitations, since some of them are significant:

1. **All secondary data.** I did not collect any primary data — no surveys, no interviews. Everything comes from institutional sources (World Bank, BBS, ILO, etc.). These are credible sources, but they come with their own measurement issues and assumptions.

2. **Small sample size.** With only 11 data points (one per year), the statistical power of the regressions and correlations is limited. The results should be read as descriptions of the observed pattern, not as strong evidence for causal claims. A longer time series would make the statistical analysis more robust.

3. **Interpolated data.** Poverty and MPI data are only available for survey years (roughly every 5–6 years). I interpolated linearly for the years in between, which smooths out any actual year-to-year variation and introduces some uncertainty.

4. **Methodological choices.** The 3ZPI depends on decisions I made — which indicators to include, how to normalize them, how to weight the pillars. The sensitivity analysis shows that the broad conclusions are robust to different weights, but a different set of indicators or a different aggregation method (geometric mean instead of arithmetic, for example) could give somewhat different numbers.

5. **No causation.** The strong negative correlation between poverty and carbon does not prove that poverty reduction causes emission increases. Both are likely driven by a common factor — economic growth — but I have not tested that formally. The correlation shows co-movement, not mechanism.

6. **Single country.** This study looks only at Bangladesh. The methodology is designed to be applicable elsewhere, but the specific results about which pillar is ahead or behind are particular to the Bangladeshi context.

### 5.7 Brief Regional Comparison

To put the Bangladesh results in perspective, here is a quick look at some neighbors:

- **India** has a similar growth trajectory but much larger absolute emissions and per-capita CO₂ of about 1.9 tonnes — roughly 3× Bangladesh. India faces the same growth-vs-emissions tension, just at a bigger scale.
- **Sri Lanka** had higher income and lower poverty before the 2022 economic crisis, which showed how quickly development gains can unravel. Its per-capita CO₂ (~1.0 t) is between India and Bangladesh.
- **Nepal** has lower emissions than Bangladesh but higher poverty and a smaller industrial base. Its challenge is to develop without following the same carbon trajectory as its neighbors.

Bangladesh stands out in this group for having strong poverty reduction, a large (if precarious) employment base, and rising but still relatively low per-capita emissions. The window for choosing a lower-carbon development path is still open, but it may be narrowing as energy infrastructure decisions get locked in.

---

## 6. Conclusion and Recommendations

### 6.1 Summary of Findings

This study tried to answer a simple question: how is Bangladesh actually doing on the three zeros? Using eight indicators, a composite index, regression analysis, and correlation, here is what I found:

1. **The composite 3ZPI went from 0.392 to 0.752 over the decade.** That is meaningful progress overall, though COVID-19 caused a sharp setback in 2020.

2. **The three pillars are on very different trajectories.** Poverty has improved strongly (0.00 → 1.00). Employment improved but crashed during COVID and is still recovering (0.51 → 0.92). Carbon got worse (0.67 → 0.33).

3. **There is a strong negative correlation (r = −0.94) between poverty reduction and carbon performance.** This is probably the most important finding — it means that the way Bangladesh is currently reducing poverty (through carbon-intensive economic growth) directly conflicts with the carbon target.

4. **At current rates, poverty targets are approachable** (MPI by ~2033, headcount by ~2047), **unemployment is not trending toward zero at all**, and **carbon emissions are going in the wrong direction**.

5. **The results are robust to different weighting choices.** Regardless of how you weight the pillars, the same pattern emerges: poverty is strong, employment is unstable, and carbon is the weakest link.

### 6.2 Recommendations

Based on what the data shows, I would suggest the following:

**For policymakers:**

1. **Use an integrated monitoring framework.** Right now, poverty, employment, and environment are tracked by different agencies with different timelines. A composite index like the 3ZPI, updated annually, could give policymakers a single dashboard view of progress across all three goals.

2. **Focus on the carbon pillar.** The data is clear: this is the pillar that is off-track. Accelerating renewable energy deployment, reconsidering new coal capacity, and setting energy efficiency standards for industry would all help. International climate finance should be part of the picture, given Bangladesh's low per-capita responsibility for emissions.

3. **Go beyond headline unemployment.** The 4.2% figure is not very useful. Policies should target underemployment, formalization of informal work, and the skills mismatch that leaves educated young people without jobs.

4. **Build resilience.** COVID-19 showed that employment gains can disappear in a single year. Expanding social protection and building fiscal buffers for crisis response would help protect progress.

**For the 3 Zero Movement:**

5. **Develop green social businesses.** There is an obvious opportunity at the intersection of employment and carbon — businesses that create jobs while reducing emissions. Solar installation cooperatives, sustainable agriculture, waste management enterprises — these align with both the employment and carbon pillars.

6. **Publish data-driven progress reports.** The 3 Zero Movement would benefit from shifting some of its communication from aspirational messaging to evidence-based reporting. A regular, publicly available assessment using something like the 3ZPI would build credibility and accountability.

**For future research:**

7. **Apply the index at the subnational level.** A district-level or division-level 3ZPI would show where progress is concentrated and where it is lacking. That kind of spatial analysis could help target interventions more effectively.

8. **Try nonlinear models.** Linear extrapolation is a useful starting point, but poverty reduction is likely to slow as the headcount gets lower (the hardest cases are last), and emission reduction would need to accelerate rather than just reverse. Logistic curves or other nonlinear models would give more realistic projections.

9. **Collect primary data.** What this study cannot capture is the qualitative side — how people experience employment, what barriers exist to clean energy adoption, what poverty reduction actually feels like on the ground. Surveys and interviews would add depth that secondary statistics miss.

10. **Do a multi-country comparison.** Running the same 3ZPI methodology for India, Nepal, and Sri Lanka would show whether the poverty-carbon trade-off is specific to Bangladesh or a regional pattern.

### 6.3 Concluding Remarks

The 3 Zero Movement asks for something ambitious: an economic system that produces no poverty, no unemployment, and no environmental damage. This study did not try to evaluate whether that vision is achievable. What it tried to do is much simpler — measure where Bangladesh stands right now against those three goals, using the mathematical tools available to an applied mathematics student.

The picture that emerges is mixed. Bangladesh is making real progress on poverty, meaningful but fragile progress on employment, and going backwards on carbon. The strong negative correlation between the poverty and carbon pillars is perhaps the most important takeaway — it suggests that the current development model, while effective at reducing poverty, is not compatible with the carbon target. Something has to change in how growth happens, not just how fast it happens.

The 3 Zero Progress Index is a simple tool. It uses min-max normalization, weighted averages, and linear regression — nothing that would be out of place in an introductory applied statistics course. But sometimes simple tools, applied to the right question, can be useful. If the 3ZPI helps make the conversation about the 3 Zero Movement a little more concrete and a little more data-driven, then it has done what I hoped it would.

---

## References

1. Ahmed, S., & Hossain, M. (2018). Environmental sustainability in Bangladesh: Progress and challenges. *Environmental Policy and Law*, 48(2), 112–120.

2. Alkire, S., & Foster, J. (2011). Counting and multidimensional poverty measurement. *Journal of Public Economics*, 95(7–8), 476–487.

3. Banerjee, A., Duflo, E., Glennerster, R., & Kinnan, C. (2015). The miracle of microfinance? Evidence from a randomized evaluation. *American Economic Journal: Applied Economics*, 7(1), 22–53.

4. Bangladesh Bureau of Statistics. (2017). *Household Income and Expenditure Survey 2016*. Ministry of Planning, Government of Bangladesh.

5. Bangladesh Bureau of Statistics. (2022). *Labour Force Survey Bangladesh 2022*. Ministry of Planning, Government of Bangladesh.

6. Bangladesh Bureau of Statistics. (2022). *Household Income and Expenditure Survey 2022*. Ministry of Planning, Government of Bangladesh.

7. Germanwatch. (2021). *Global Climate Risk Index 2021*. Bonn: Germanwatch e.V.

8. Global Carbon Project. (2023). Global carbon budget 2023. *Earth System Science Data*, 15(12), 5301–5369.

9. Government of Bangladesh. (2021). *Nationally Determined Contributions (Updated) 2021*. Ministry of Environment, Forest and Climate Change.

10. Hasan, M. M., & Jahan, S. (2019). Poverty in Bangladesh: A multidimensional analysis. *Journal of Economic Development*, 44(3), 85–102.

11. IDCOL. (2020). *Annual Report 2019–2020*. Infrastructure Development Company Limited, Dhaka.

12. International Labour Organization. (2023). *World Employment and Social Outlook: Trends 2023*. Geneva: ILO.

13. IRENA. (2023). *Renewable Energy Statistics 2023*. Abu Dhabi: International Renewable Energy Agency.

14. Kabeer, N., & Mahmud, S. (2004). Rags, riches and women workers: Export-oriented garment manufacturing in Bangladesh. In *Chains of Fortune: Linking Women Producers and Workers with Global Markets* (pp. 133–164). Commonwealth Secretariat.

15. Khandker, S. R. (2005). Microfinance and poverty: Evidence using panel data from Bangladesh. *The World Bank Economic Review*, 19(2), 263–286.

16. Ministry of Planning, Bangladesh. (2020). *8th Five Year Plan (July 2020 – June 2025)*. General Economics Division, Government of Bangladesh.

17. Morduch, J. (1999). The microfinance promise. *Journal of Economic Literature*, 37(4), 1569–1614.

18. Rahman, M., & Islam, D. (2019). Youth unemployment and the skills gap in Bangladesh: Challenges and policy responses. *Bangladesh Development Studies*, 42(1), 1–28.

19. Stern, N. (2007). *The Economics of Climate Change: The Stern Review*. Cambridge University Press.

20. UNDP & OPHI. (2020). *Global Multidimensional Poverty Index 2020*. United Nations Development Programme and Oxford Poverty and Human Development Initiative.

21. United Nations. (2015). Transforming our world: The 2030 Agenda for Sustainable Development. *UN General Assembly Resolution A/RES/70/1*.

22. World Bank. (2021). *Bangladesh COVID-19 Poverty Monitoring Survey*. Washington, DC: World Bank Group.

23. World Bank. (2023). *Bangladesh Development Update: Resilience Under Test*. Washington, DC: World Bank Group.

24. Yunus, M. (2007). *Banker to the Poor: Micro-Lending and the Battle Against World Poverty*. PublicAffairs.

25. Yunus, M. (2017). *A World of Three Zeros: The New Economics of Zero Poverty, Zero Unemployment, and Zero Net Carbon Emissions*. PublicAffairs.

26. Yunus Centre. (2020). *Social Business and the Three Zeros: Progress Report*. Dhaka: Yunus Centre.

---

*Corresponding author: Minhajul Abedin, Department of Applied Mathematics. 4th year undergraduate with research interests in data science, applied mathematical modeling, and computational approaches to social questions.*
