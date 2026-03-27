# Exploring the Impact of the 3 Zero Movement in Bangladesh: A Pathway to Sustainable Development

> Last updated: 2026-03-28
> Status: Draft
> Target venue: 18th International Conference on Engineering & Natural Sciences (Full paper)

---

**Minhajul Abedin**

Department of Applied Mathematics, 4th Year Undergraduate

---

**Abstract**

Bangladesh has sustained an average GDP growth rate exceeding 6% over the past decade, yet persistent poverty, inadequate employment conditions, and rising carbon emissions continue to undermine its long-term development prospects. The 3 Zero Movement, rooted in Nobel Peace Laureate Professor Muhammad Yunus's vision of achieving zero poverty, zero unemployment, and zero net carbon emissions, offers a unified framework for addressing these interlinked challenges. This study evaluates Bangladesh's progress toward the three zero targets over the period 2013–2023 using a quantitative approach grounded in secondary data from the World Bank, the Bangladesh Bureau of Statistics, the International Labour Organization, and the Global Carbon Project. Eight indicators spanning the three pillars are normalized and aggregated into a composite 3 Zero Progress Index (3ZPI) to measure overall advancement. Linear regression is applied to each indicator to estimate rates of change and project target achievement timelines, while Pearson correlation analysis examines interdependencies among the pillars. The results indicate that Bangladesh has achieved its strongest progress in poverty reduction (pillar score rising from 0.00 to 1.00 over the study period), followed by employment (0.51 to 0.92), while the carbon emissions pillar has deteriorated (0.67 to 0.33) as total emissions grew by approximately 54%. The composite 3ZPI increased from 0.39 in 2013 to 0.75 in 2023, with a notable disruption in 2020 due to COVID-19. A strong negative correlation (r = −0.94) between the poverty and carbon pillars highlights a fundamental tension: the economic processes driving poverty reduction simultaneously increase emissions. These findings suggest that Bangladesh's development pathway remains structurally imbalanced, and that targeted interventions in clean energy and green employment are necessary to bring the carbon pillar into alignment with the other two. The study contributes a replicable quantitative methodology for tracking 3 Zero progress that can be extended to other developing economies.

**Keywords:** 3 Zero Movement, sustainable development, Bangladesh, composite index, poverty, unemployment, carbon emissions, Muhammad Yunus

---

## 1. Introduction

### 1.1 Background

Bangladesh occupies an unusual position in the global development landscape. Over the past two decades, the country has registered some of the most consistent GDP growth rates in South Asia, averaging above 6% annually between 2010 and 2023, while also recording meaningful improvements in life expectancy, primary school enrollment, and infant mortality (World Bank, 2023). Its graduation from Least Developed Country (LDC) status, recommended by the United Nations Committee for Development Policy in 2021, was widely regarded as a milestone for a nation that was once described as a "basket case" in the aftermath of its 1971 independence war.

Yet this growth story is incomplete. The poverty headcount ratio, while declining, still leaves tens of millions below the national poverty line. Official unemployment figures remain deceptively low — hovering around 4–5% — but mask widespread underemployment and informal labor arrangements that offer little security or upward mobility. At the same time, industrialization and energy consumption have pushed total carbon dioxide emissions upward by more than 50% in the last decade, placing Bangladesh in the paradoxical position of being both one of the countries most vulnerable to climate change and a growing contributor to the problem.

It is against this background that the 3 Zero Movement acquires its relevance. Articulated by Nobel Peace Laureate Professor Muhammad Yunus in his book *A World of Three Zeros* (2017), the framework calls for a restructuring of economic systems to achieve three interconnected goals: zero poverty, zero unemployment, and zero net carbon emissions. The vision draws on Yunus's decades of experience with Grameen Bank and social business, extending the microfinance philosophy into a broader agenda for systemic change. Unlike narrowly defined policy targets, the 3 Zero framework insists that these three goals must be pursued together — that addressing poverty without tackling emissions, or creating jobs without ensuring their sustainability, leads to incomplete and fragile development outcomes.

The framework aligns closely with several of the United Nations Sustainable Development Goals (SDGs), particularly Goal 1 (No Poverty), Goal 8 (Decent Work and Economic Growth), and Goal 13 (Climate Action). However, while the SDGs set global targets with 2030 deadlines, the 3 Zero Movement frames its objectives as permanent structural transformations rather than time-bound benchmarks. This distinction matters for how progress is measured and assessed.

### 1.2 Problem Statement

Despite the conceptual appeal of the 3 Zero Movement, there has been limited quantitative assessment of Bangladesh's actual progress toward these goals. Much of the existing discourse around the framework remains aspirational — policy speeches, organizational mission statements, and programmatic descriptions. What is missing is a rigorous, data-driven evaluation that asks straightforward questions: How much progress has actually been made? At what rate? And are the three pillars advancing in harmony, or is progress in one area coming at the expense of another?

This gap is particularly significant for a country like Bangladesh, where development data is increasingly available but underutilized for integrated multi-pillar analysis. Poverty statistics, employment surveys, and emissions inventories are published by separate agencies with different methodologies and timelines. No standardized instrument currently exists to aggregate these indicators into a single measure of 3 Zero progress.

From an applied mathematics perspective, this represents a well-defined problem: given a set of heterogeneous indicators measured on different scales, how can they be normalized, weighted, and combined into a composite index that meaningfully tracks progress toward a stated goal? And what statistical relationships exist among the component variables that might reveal trade-offs or synergies?

### 1.3 Research Questions

This study is guided by three questions:

1. What is the quantitative trajectory of Bangladesh's progress toward each of the three zero targets over the decade 2013–2023?
2. What statistical relationships (correlations) exist among the three pillars — do improvements in one area tend to accompany or hinder progress in the others?
3. At current rates of change, when might Bangladesh plausibly reach each of the three zero targets, and which pillar represents the most critical bottleneck?

### 1.4 Objectives

The objectives of this study are:

1. To quantify Bangladesh's decade-long progress on eight indicators spanning the three pillars of the 3 Zero Movement, using publicly available secondary data.
2. To construct a composite 3 Zero Progress Index (3ZPI) that aggregates normalized indicator scores into a single trackable measure.
3. To analyze inter-pillar statistical relationships through Pearson correlation coefficients and identify potential synergies and trade-offs.
4. To estimate projected target achievement timelines through linear extrapolation and identify the most lagging pillar.
5. To derive policy-relevant recommendations grounded in the quantitative findings.

### 1.5 Significance of the Study

This study makes several contributions. First, it introduces a quantitative framework — the 3 Zero Progress Index — to a discourse that has been predominantly qualitative. For policymakers and development practitioners, a composite index provides a quick diagnostic of overall progress and reveals which dimension demands the most urgent attention. Second, the methodology is deliberately simple and replicable: min-max normalization, weighted aggregation, and linear regression are techniques accessible to any researcher with basic statistical training. This means the framework can be adapted and applied to other countries or subnational regions without specialized software or advanced modeling expertise. Third, the correlation analysis between pillars offers insight into the structural dynamics of Bangladesh's development — whether its growth model is compatible with all three zeros, or whether inherent trade-offs need to be managed through deliberate policy design.

For an applied mathematics audience, the study demonstrates how standard mathematical tools — index construction, linear models, and correlation — can be directed at questions that are often left to qualitative policy analysis. The intent is not to replace qualitative research but to complement it with a layer of quantitative rigor.

---

## 2. Literature Review

### 2.1 The 3 Zero Movement: Conceptual Foundations

The intellectual roots of the 3 Zero Movement lie in Professor Muhammad Yunus's work with Grameen Bank, founded in 1983 to provide microcredit to the rural poor in Bangladesh without requiring collateral. The success of the Grameen model — which demonstrated that the poor are creditworthy and that small loans can catalyze self-employment — earned Yunus the Nobel Peace Prize in 2006 and generated a global microfinance movement (Yunus, 2007).

In *A World of Three Zeros* (2017), Yunus extended this philosophy beyond microfinance. He argued that the existing economic system, built around profit maximization, is structurally incapable of solving poverty, unemployment, and environmental degradation. Instead, he proposed "social business" — enterprises designed to solve social problems rather than generate shareholder profit — as the primary vehicle for achieving the three zeros. The book lays out a vision in which these three goals are not merely desirable outcomes but achievable structural features of a redesigned economy.

The framework deliberately links goals that are often treated separately in policy discourse. The argument is that poverty cannot be eliminated without creating meaningful employment, and that neither goal is sustainable if the environmental basis of the economy is degraded. This systems perspective distinguishes the 3 Zero framework from siloed approaches that target poverty or emissions in isolation (Yunus, 2017).

The 3 Zero Movement intersects with the United Nations Sustainable Development Goals but differs in important respects. The SDGs, adopted in 2015, comprise 17 goals with 169 targets to be achieved by 2030 (United Nations, 2015). They are country-agnostic and emphasize government-led interventions. The 3 Zero framework is more philosophically specific — it centers entrepreneurship, social business, and bottom-up economic redesign rather than top-down policy targets (Yunus Centre, 2020).

### 2.2 Zero Poverty: Progress and Challenges in Bangladesh

Bangladesh's record on poverty reduction has been widely recognized. The national poverty headcount ratio declined from approximately 48.9% in 2000 to 24.3% in 2016, according to the Household Income and Expenditure Survey (HIES) conducted by the Bangladesh Bureau of Statistics (BBS, 2017). By the time of the 2022 HIES, this figure had further declined to an estimated 18.7%, though methodological changes between surveys complicate direct comparison.

Microfinance has been credited as a significant contributor to this trend. Khandker (2005), using panel data from Bangladesh, found that microfinance participation was associated with a reduction in moderate poverty by about 1.6 percentage points per year for participating households. Morduch (1999), however, offered a more cautious assessment, noting that the evidence for microfinance's poverty impact is mixed and that selection bias affects many studies. More recent evaluations have suggested that microfinance is effective at smoothing consumption and enabling small-scale investment, but less effective at lifting households out of poverty permanently (Banerjee et al., 2015).

Beyond income measures, the Multidimensional Poverty Index (MPI) developed by Alkire and Foster (2011) captures deprivations across health, education, and living standards. Bangladesh's MPI has shown consistent improvement: the headcount of multidimensionally poor individuals fell from approximately 41.7% in 2014 to around 24.6% by 2019 (UNDP & OPHI, 2020). This suggests that improvements extend beyond income to include access to healthcare, schooling, and basic services.

The COVID-19 pandemic disrupted this trajectory. The World Bank estimated that between 14 and 24 million Bangladeshis fell into poverty during 2020 due to income loss, business closures, and remittance declines (World Bank, 2021). While partial recovery occurred in subsequent years, the pandemic demonstrated the fragility of poverty gains in the absence of robust social protection systems.

Rural-urban disparities remain a persistent challenge. Poverty is disproportionately concentrated in rural areas and in specific divisions such as Rangpur and Mymensingh, while Dhaka and Chittagong have seen faster reductions tied to industrial employment (BBS, 2022). Addressing these spatial inequalities is a key requirement for reaching zero poverty.

### 2.3 Zero Unemployment: Employment Landscape in Bangladesh

Bangladesh's official unemployment rate has remained low — typically reported between 4% and 5% — but this figure is widely regarded as misleading. The definition used by the Bangladesh Bureau of Statistics (consistent with ILO guidelines) classifies anyone who worked at least one hour in the reference week as employed. Under this definition, large segments of the population engaged in sporadic, low-productivity informal work are counted as employed (BBS, 2022).

Underemployment provides a more revealing picture. The Labour Force Survey 2022 reported that time-related underemployment — defined as working fewer than 40 hours per week while being available and willing to work more — affected approximately 6.4% of the labour force. Combined with inadequate employment (workers whose earnings fall below subsistence thresholds), the effective unemployment and underemployment rate is substantially higher than the headline figure suggests.

Youth unemployment is a particular concern. Among the 15–29 age cohort, unemployment rates have consistently been two to three times the national average, reaching approximately 10–12% in recent surveys (ILO, 2023). The phenomenon of "educated unemployment" — where individuals with secondary or tertiary education face higher unemployment than those with less schooling — reflects a mismatch between the skills produced by the education system and those demanded by the labor market (Rahman & Islam, 2019).

Women's labour force participation has increased over the past decade, rising from approximately 33.5% in 2013 to 42.0% by 2023 (BBS, 2022). The ready-made garments (RMG) sector, which employs roughly 4 million workers (predominantly women), has been a primary driver of this increase (Kabeer & Mahmud, 2004). However, working conditions, wage levels, and job security in the sector remain contentious issues.

The 3 Zero Movement's approach to unemployment differs from conventional employment policy. Rather than focusing on job creation through industrial policy or public sector expansion, Yunus's framework emphasizes entrepreneurship. The argument is that every person is a potential entrepreneur, and that the financial system should be restructured to enable self-employment through microcredit and social business support (Yunus, 2017). While this philosophy has produced measurable results through Grameen Bank and its affiliates, scaling it to address the employment needs of a labor force exceeding 70 million remains an open question.

### 2.4 Zero Net Carbon Emissions: Environmental Realities

Bangladesh's carbon emissions profile presents a paradox. In per capita terms, Bangladesh is among the lowest emitters in the world — approximately 0.57 tonnes of CO₂ per person in 2023, compared to a global average of about 4.7 tonnes (Global Carbon Project, 2023). Yet in aggregate, the country's total emissions have been rising steadily, driven by population growth, industrialization, and increasing energy consumption. Total CO₂ emissions grew from approximately 65 million tonnes (Mt) in 2013 to nearly 100 Mt by 2023, an increase of roughly 54% (World Bank, 2023).

The energy sector is the dominant source of emissions, accounting for over 60% of total CO₂. Bangladesh remains heavily dependent on natural gas, which provides approximately 55% of commercial energy supply. Coal-fired power plants, several of which came online during the study period, have added to the emissions trajectory. The Rampal coal plant near the Sundarbans mangrove forest drew particular international attention and criticism (Ahmed & Hossain, 2018).

Industrial emissions are driven largely by the brick-making sector, which operates thousands of kilns across the country, and the cement and steel industries. The RMG sector, while not a major direct emitter, contributes indirectly through its energy consumption and logistics footprint.

Bangladesh has made commitments under the Paris Agreement through its Nationally Determined Contributions (NDCs), pledging to reduce greenhouse gas emissions by 21.85% below business-as-usual by 2030, with 6.73% unconditionally and the remainder conditional on international support (Government of Bangladesh, 2021). However, progress toward these targets has been slow, and enforcement mechanisms remain limited.

On the positive side, Bangladesh has been a relative success story in decentralized renewable energy. The Solar Home System (SHS) program, supported by the Infrastructure Development Company Limited (IDCOL), installed over 6 million solar home systems in off-grid rural areas, making it one of the largest off-grid solar programs globally (IDCOL, 2020). Nonetheless, the share of renewables in total primary energy remains low — approximately 4.5% by 2023 — far below what would be required for a meaningful pathway to zero net emissions.

The vulnerability dimension adds urgency. Bangladesh consistently ranks among the top ten countries most affected by extreme weather events in the Global Climate Risk Index (Germanwatch, 2021). Sea-level rise, cyclones, flooding, and riverbank erosion threaten millions of livelihoods, creating a situation where the country disproportionately bears the costs of a problem it has contributed relatively little to creating.

### 2.5 Research Gap

The literature on Bangladesh's development is extensive, but most studies address poverty, employment, and environmental sustainability as separate domains. Integrated assessments that evaluate progress across all three areas simultaneously are rare. Furthermore, while the 3 Zero Movement has generated considerable advocacy literature and organizational activity, it has not been subjected to systematic quantitative evaluation using composite index methods.

This study addresses both gaps: it treats the three zeros as a coupled system and applies a mathematical indexing approach to measure aggregate and pillar-level progress. The analytical tools — normalization, weighted aggregation, regression, and correlation — are standard in applied mathematics and readily reproducible, making the methodology accessible for extension and replication.

---

## 3. Methodology

### 3.1 Research Design

This study employs a mixed-methods approach with a quantitative emphasis. The primary analytical component consists of secondary data analysis using publicly available national and international datasets. A qualitative policy review complements the quantitative findings by providing context on the institutional and programmatic factors behind observed trends.

The quantitative analysis proceeds in four stages: (i) data collection and indicator definition; (ii) normalization and composite index construction; (iii) trend analysis using linear regression; and (iv) inter-pillar correlation analysis. Each stage is described in detail below.

### 3.2 Data Sources

Data for this study were drawn from the following sources:

- **Poverty indicators:** World Bank Development Indicators database; Bangladesh Bureau of Statistics Household Income and Expenditure Survey (HIES) 2016 and 2022; UNDP/OPHI Multidimensional Poverty Index reports.
- **Employment indicators:** BBS Labour Force Survey (multiple rounds); International Labour Organization (ILO) ILOSTAT database; Bangladesh Bank annual reports on microcredit disbursement.
- **Carbon emissions indicators:** World Bank CO₂ emissions dataset (sourced from CDIAC and Global Carbon Project); International Renewable Energy Agency (IRENA) statistics; Bangladesh Power Development Board annual reports.
- **Policy documents:** Government of Bangladesh 8th Five Year Plan (2020–2025); Bangladesh Climate Change Strategy and Action Plan (BCCSAP); Nationally Determined Contributions (NDC) submissions under the Paris Agreement; Yunus Centre publications.

The study period covers the decade from 2013 to 2023. Where annual data were unavailable (particularly for poverty and MPI, which are surveyed intermittently), values were interpolated linearly between survey years, and this is noted as a limitation.

### 3.3 Indicator Selection

Eight indicators were selected across the three pillars, chosen for their relevance to the respective zero targets, data availability over the study period, and consistency of measurement methodology:

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

The "Direction" column indicates whether a higher or lower value represents progress toward the corresponding zero target. This distinction is critical for the normalization procedure described below.

### 3.4 Data

The following table presents the raw data used in this study. Values for survey-gap years were linearly interpolated from adjacent survey data points. All figures have been rounded for presentation.

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

To enable cross-indicator comparison and aggregation, all indicators are normalized to a common [0, 1] scale using min-max normalization over the study period. A normalized score of 1 represents the best observed performance (maximum progress toward zero), and 0 represents the worst.

For indicators where a lower value indicates better performance toward the zero target (P1, P2, U1, U2, C1, C2), the inverted normalization formula is applied:

$$x_{i,\text{norm}} = \frac{x_{\max} - x_i}{x_{\max} - x_{\min}}$$

For indicators where a higher value indicates better performance (U3, C3), the standard formula is used:

$$x_{i,\text{norm}} = \frac{x_i - x_{\min}}{x_{\max} - x_{\min}}$$

Here, $x_{\max}$ and $x_{\min}$ refer to the maximum and minimum observed values of each indicator across the entire study period (2013–2023). This approach ensures that the normalization reflects relative progress within the observed range rather than against an absolute or theoretical benchmark.

**Table 3: Min-Max Bounds for Normalization**

| Indicator | Min (best for inverted; worst for standard) | Max (worst for inverted; best for standard) |
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

The composite index is constructed in two stages. First, pillar-level scores are computed by averaging the normalized indicators within each pillar:

$$P = \frac{1}{n_P} \sum_{j=1}^{n_P} x_{P_j,\text{norm}}, \quad U = \frac{1}{n_U} \sum_{j=1}^{n_U} x_{U_j,\text{norm}}, \quad C = \frac{1}{n_C} \sum_{j=1}^{n_C} x_{C_j,\text{norm}}$$

where $n_P = 2$, $n_U = 3$, and $n_C = 3$ are the number of indicators in each pillar.

Second, the overall 3ZPI is computed as a weighted sum of pillar scores:

$$\text{3ZPI}_t = w_P \cdot P_t + w_U \cdot U_t + w_C \cdot C_t$$

where $w_P + w_U + w_C = 1$. The baseline specification uses equal weights ($w_P = w_U = w_C = \frac{1}{3}$), reflecting the 3 Zero Movement's principle that all three goals are equally important. A sensitivity analysis using alternative weighting schemes is presented in Section 4.4.

The 3ZPI ranges from 0 (no progress on any pillar) to 1 (all three zero targets effectively achieved within the observed data range). It should be noted that a 3ZPI of 1 does not mean the zero targets have been reached in absolute terms — it means that every indicator has reached its best observed level within the study period.

### 3.7 Trend Analysis

Linear regression is applied to each raw indicator as a function of time to estimate the average annual rate of change:

$$y_t = \alpha + \beta \cdot t + \epsilon_t$$

where $y_t$ is the indicator value in year $t$ (coded as $t = 0$ for 2013 through $t = 10$ for 2023), $\alpha$ is the intercept, $\beta$ is the slope (annual rate of change), and $\epsilon_t$ is the error term. The coefficient $\beta$ and its associated $R^2$ value are reported for each indicator.

For indicators where the target is zero (poverty rate, unemployment, emissions), the projected year of reaching zero under the current linear trend is estimated by:

$$t_{\text{zero}} = 2023 + \frac{y_{2023}}{|\beta|}$$

This extrapolation assumes a continuation of the observed linear trend and is presented as a rough benchmark rather than a forecast.

### 3.8 Correlation Analysis

Pearson correlation coefficients are computed between the annual pillar scores (P, U, C) to examine inter-pillar relationships:

$$r_{XY} = \frac{\sum_{t=1}^{n}(X_t - \bar{X})(Y_t - \bar{Y})}{\sqrt{\sum_{t=1}^{n}(X_t - \bar{X})^2 \cdot \sum_{t=1}^{n}(Y_t - \bar{Y})^2}}$$

where $n = 11$ (the number of annual observations). The correlation coefficient $r$ ranges from −1 (perfect negative relationship) to +1 (perfect positive relationship). With $n = 11$, the critical value for statistical significance at the 5% level is approximately $|r| > 0.602$ (two-tailed test, $df = 9$).

Positive correlations between pillars would indicate synergy — progress in one area tends to accompany progress in another. Negative correlations would indicate trade-offs — gains in one pillar tend to coincide with setbacks in another.

### 3.9 Tools

Data processing, normalization, regression, and correlation computations were performed using Python 3.11 with the pandas, NumPy, and scipy.stats libraries. Visualizations were prepared using matplotlib and seaborn. The document was prepared in Markdown with LaTeX mathematical typesetting.

---

## 4. Analysis and Findings

### 4.1 Normalized Indicator Scores

Applying the normalization procedure described in Section 3.5, the following normalized scores were obtained:

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

Several patterns are immediately visible. The poverty indicators (P1, P2) show a consistent upward trajectory, reaching their maximum normalized values by 2023. The employment indicators (U1, U2, U3) show general improvement but with a severe disruption in 2020. The carbon indicators reveal a divergence: C1 and C2 (emission levels) decline monotonically from their best values in 2013 as emissions grew, while C3 (renewable share) improves steadily.

### 4.2 Pillar-Level Scores

Pillar scores are computed by averaging the normalized indicators within each pillar.

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

The results reveal a clear asymmetry across pillars:

**Poverty pillar (P):** This pillar shows the strongest and most consistent improvement, rising from 0.000 in 2013 to 1.000 in 2023. Even the COVID-19 dip in 2020 (to 0.603) was relatively contained compared to the employment pillar, and the subsequent recovery was swift. The poverty headcount ratio declined by 8.6 percentage points over the decade, and the MPI roughly halved.

**Unemployment pillar (U):** The employment pillar demonstrates strong pre-pandemic progress, peaking at 0.886 in 2019. The COVID-19 shock was devastating — the pillar score collapsed to 0.129 in 2020 as unemployment surged and female labour force participation dropped. Recovery was gradual, reaching 0.923 by 2023. The volatility of this pillar highlights the vulnerability of Bangladesh's employment structure to external shocks.

**Carbon pillar (C):** This is the only pillar showing net deterioration over the decade, declining from 0.667 in 2013 to 0.333 in 2023. While renewable energy adoption improved (C3 rose from 0.000 to 1.000 in normalized terms), this was overwhelmed by the worsening of emission indicators (C1 and C2 both fell to 0.000). The carbon pillar moves in the opposite direction from the other two, creating a structural imbalance in overall 3 Zero progress.

### 4.3 3ZPI Trajectory

The composite 3ZPI increased from 0.392 in 2013 to 0.752 in 2023, representing a net improvement of 0.360 points (92% increase from the base value). However, the trajectory was not smooth:

- **2013–2019:** Steady upward trend from 0.392 to 0.669, driven primarily by poverty reduction and employment gains.
- **2020:** Sharp drop to 0.430 due to COVID-19, representing a loss of approximately five years of progress.
- **2021–2023:** Recovery and acceleration, reaching a new high of 0.752 by 2023.

The 2020 disruption is notable because it affected the pillars asymmetrically. The poverty pillar dipped modestly (from 0.724 to 0.603), the carbon pillar actually improved temporarily (from 0.398 to 0.557, as reduced economic activity lowered emissions), but the employment pillar collapsed (from 0.886 to 0.129). This pattern illustrates how the composite index can mask pillar-level dynamics when interpreted in isolation.

### 4.4 Sensitivity Analysis: Alternative Weighting Schemes

To test the robustness of the 3ZPI results, three alternative weighting schemes were applied alongside the equal-weight baseline:

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

The key finding from the sensitivity analysis is that the carbon-heavy weighting produces the lowest 2023 score (0.648 vs. 0.752 under equal weights) and shows the flattest overall trajectory. This confirms that the carbon pillar is the primary drag on aggregate progress, regardless of weighting scheme. The poverty-heavy weighting produces the highest 2023 score (0.814), reflecting the strong performance of the poverty pillar. The employment-heavy weighting shows the deepest COVID-19 trough (0.236 in 2020), highlighting the sensitivity of this pillar to economic shocks.

The qualitative conclusions are robust across all four weighting schemes: poverty progress is strong, employment progress is volatile but recovering, and carbon performance is the weakest and worsening dimension.

### 4.5 Trend Analysis: Linear Regression Results

Linear regression was applied to each raw indicator over the 11-year period.

**Table 7: Linear Regression Results (y = α + βt, t = 0 for 2013)**

| Indicator | β (annual change) | R² | Interpretation |
|-----------|--------------------|----|----------------|
| P1 — Poverty (%) | −0.76 | 0.92 | Declining ~0.76 pp/year |
| P2 — MPI | −0.0094 | 0.97 | Consistent decline |
| U1 — Unemployment (%) | −0.003 | 0.001 | Effectively flat (no trend) |
| U2 — Youth Unemp. (%) | −0.005 | 0.001 | Effectively flat |
| U3 — Female LFPR (%) | +0.72 | 0.85 | Increasing ~0.72 pp/year |
| C1 — CO₂ Total (Mt) | +3.24 | 0.95 | Rising ~3.2 Mt/year |
| C2 — CO₂ per Capita (t) | +0.014 | 0.96 | Rising ~0.014 t/year |
| C3 — Renewable Share (%) | +0.17 | 0.99 | Slowly increasing |

The regression results confirm the pillar-level findings:

- **Poverty indicators** have strong negative trends with high $R^2$ values, indicating sustained and consistent decline. The poverty headcount is decreasing at approximately 0.76 percentage points per year.
- **Unemployment indicators** show essentially no linear trend ($R^2 \approx 0$), reflecting the disruption of COVID-19 that broke any pre-existing pattern. Female LFPR, however, shows a strong positive trend (+0.72 pp/year, $R^2 = 0.85$).
- **Carbon indicators** show strong positive trends (increasing emissions) with very high $R^2$ values. Total CO₂ is increasing at 3.24 Mt per year, and per-capita emissions at 0.014 tonnes per year. Renewable energy share is increasing, but at only 0.17 percentage points per year — a pace that is insufficient to offset emission growth.

### 4.6 Gap Analysis and Projections

Using the linear trend coefficients, projected years for reaching the zero target were estimated where applicable:

**Table 8: Gap Analysis and Linear Extrapolation**

| Indicator | 2023 Value | Target | β (annual) | Projected Year to Target |
|-----------|------------|--------|------------|--------------------------|
| P1 — Poverty (%) | 17.8 | 0 | −0.76 | ~2047 |
| P2 — MPI | 0.095 | 0 | −0.0094 | ~2033 |
| U1 — Unemployment (%) | 4.2 | 0 | ~0 | Not achievable under current trend |
| U2 — Youth Unemp. (%) | 10.8 | 0 | ~0 | Not achievable under current trend |
| C1 — CO₂ Total (Mt) | 99.8 | 0 | +3.24 | Moving away from target |
| C2 — CO₂ per Capita (t) | 0.57 | 0 | +0.014 | Moving away from target |

The projections highlight the varying degrees of alignment between current trajectories and the three zero targets:

- **Poverty** is on a credible (if slow) path toward further reduction, with the MPI potentially nearing zero by the early 2030s and the headcount ratio by the mid-2040s under linear assumptions.
- **Unemployment** shows no discernible linear trend toward zero. The official rate is low but essentially static; structural change in the employment market — addressing underemployment, informality, and youth joblessness — requires interventions beyond what current trends reflect.
- **Carbon emissions** are moving in the wrong direction entirely. Under the current linear trend, emissions will continue to rise. Reaching zero net emissions would require not just a reversal of the trend but an order-of-magnitude transformation of the energy and industrial base.

### 4.7 Inter-Pillar Correlation Analysis

Pearson correlation coefficients were computed between the annual pillar scores.

**Table 9: Correlation Matrix of Pillar Scores**

|   | Poverty (P) | Unemployment (U) | Carbon (C) |
|---|-------------|-------------------|------------|
| **Poverty (P)** | 1.000 | 0.329 | −0.939 |
| **Unemployment (U)** | 0.329 | 1.000 | −0.595 |
| **Carbon (C)** | −0.939 | −0.595 | 1.000 |

The correlation results reveal important structural relationships:

**P–C correlation (r = −0.939):** The strongest finding is the near-perfect negative correlation between the poverty and carbon pillars. This means that over the study period, years in which Bangladesh made the most progress on poverty reduction were the same years in which carbon performance deteriorated the most. This is not coincidental — the economic growth that drives poverty reduction (industrial expansion, energy consumption, urbanization) is also the primary driver of emission increases. This represents the central tension in Bangladesh's development model: the pathways currently used to reduce poverty are carbon-intensive.

The critical value for significance at the 5% level with $df = 9$ is $|r| > 0.602$. The P–C correlation ($|r| = 0.939$) far exceeds this threshold and is statistically significant.

**U–C correlation (r = −0.595):** A moderate negative correlation exists between employment and carbon performance. When employment conditions improve (often through industrial expansion), carbon performance tends to worsen. This correlation approaches but does not quite reach the 5% significance threshold, partly because the COVID-19 disruption in 2020 (when employment collapsed but carbon temporarily improved) introduces noise.

**P–U correlation (r = 0.329):** The weakest relationship is between poverty and employment. While one might expect strong positive correlation (employment gains should reduce poverty), the observed relationship is only weakly positive. This may reflect several factors: much of Bangladesh's employment is in low-wage informal work that does not reliably lift households above the poverty line; poverty reduction has been driven partly by remittances and social protection rather than domestic employment; and the COVID-19 shock created a year (2020) in which employment collapsed while poverty increased only moderately (due to government support measures).

---

## 5. Discussion

### 5.1 The Imbalanced Triangle

The overarching finding of this study is that Bangladesh's progress toward the three zeros is structurally imbalanced. The poverty pillar has seen genuine, sustained improvement. The employment pillar has shown capacity for progress but remains vulnerable to shocks and is held back by informal labor market structures. The carbon pillar is deteriorating.

This imbalance is not unique to Bangladesh — it is characteristic of many developing economies pursuing growth-led poverty reduction strategies. Economic growth, particularly in manufacturing and energy-intensive sectors, generates employment and raises incomes, but it also increases emissions. The question for Bangladesh is whether this trade-off is inevitable or whether alternative development pathways exist that can reduce poverty and create employment without proportionally increasing carbon output.

The strong negative correlation between the poverty and carbon pillars (r = −0.94) quantifies this trade-off. From a policy perspective, this finding argues against approaches that treat the three zeros independently. A ministry of finance focused solely on poverty might pursue policies (e.g., coal-based industrialization, infrastructure expansion) that advance its mandate while worsening another ministry's carbon targets. The 3 Zero framework's insistence on treating the goals as interconnected is supported by the data — but the data also shows that interconnection currently manifests as tension rather than synergy.

### 5.2 Poverty Reduction: Strong but Incomplete

The poverty pillar's performance is the clearest success story in the data. The headcount ratio declined from 26.4% to 17.8%, and the MPI roughly halved over the decade. These gains reflect the cumulative effect of several factors: sustained economic growth, expansion of the RMG sector, remittance inflows from migrant workers, microfinance penetration, and government social safety net programs (BBS, 2022; World Bank, 2023).

However, several qualifications are important. First, the pace of poverty reduction appears to be slowing. The linear regression slope of −0.76 pp/year, if extrapolated, suggests it would take until approximately 2047 to reach zero — a timeline that would miss the SDG target by 17 years. Second, the COVID-19 reversal demonstrated that poverty gains are fragile in the absence of strong social protection. Third, inequality of outcomes persists: rural poverty rates remain substantially higher than urban rates, and specific regions (Rangpur, Mymensingh) continue to lag behind national averages.

The 3 Zero Movement's emphasis on social business and entrepreneurship as pathways out of poverty has merit, but the data does not allow us to isolate the specific contribution of Yunus-inspired programs from broader macroeconomic trends. This is a limitation that future research with more granular data could address.

### 5.3 Employment: Structural Weaknesses Masked by Headline Numbers

The employment pillar presents the most complex picture. The headline unemployment rate of approximately 4.2% is low by international standards but conceals deep structural issues. The near-zero linear trend in unemployment ($\beta \approx 0$, $R^2 \approx 0$) indicates that the labor market is not undergoing meaningful structural transformation — it is simply fluctuating around a stable (and misleadingly low) baseline.

The real employment challenge in Bangladesh is not unemployment per se but the quality of employment. Underemployment, informal work without contracts or benefits, low wages in the garment sector, and the mismatch between educational credentials and available jobs collectively define a labor market that is far from the "zero unemployment" vision of the 3 Zero Movement.

Female labour force participation, however, is a bright spot. The increase from 33.5% to 42.0% over the decade, with a strong linear trend ($\beta = +0.72$ pp/year, $R^2 = 0.85$), reflects both the pull of the RMG sector and broader social changes. If this trend continues, female LFPR could approach 50% by the early 2030s, which would represent a significant structural shift in a traditionally conservative labor market.

The COVID-19 collapse of the employment pillar (from 0.886 to 0.129 in one year) was the most dramatic single-year movement in the entire dataset. It highlights that the 3 Zero framework must account for resilience — not just progress, but the capacity to maintain gains in the face of shocks.

### 5.4 Carbon Emissions: The Critical Bottleneck

The carbon pillar is the most concerning dimension of the analysis. Total CO₂ emissions grew by approximately 54% over the decade, from 64.8 Mt to 99.8 Mt. Per capita emissions, while still low in global terms, increased by 36%. The linear trend is strongly positive ($\beta = +3.24$ Mt/year, $R^2 = 0.95$), with no sign of the trajectory bending toward reduction, let alone toward zero.

The tension between economic development and emission reduction is well-documented in the literature on developing countries (Stern, 2007). Bangladesh's case follows the pattern: energy demand rises with industrialization and urbanization, and the energy mix remains dominated by fossil fuels (primarily natural gas, with growing coal capacity). The ambitious plans for coal-fired power generation, including the controversial Rampal and Payra plants, represent a deliberate policy choice to prioritize energy access and industrial competitiveness over emission reduction (Ahmed & Hossain, 2018).

The renewable energy dimension offers some encouragement. The share of renewables grew from 2.8% to 4.5%, and the Solar Home System program has demonstrated that decentralized solar can be deployed at scale. But the rate of renewable growth (+0.17 pp/year) is an order of magnitude too slow to offset fossil fuel expansion. Under linear extrapolation, it would take centuries for renewables to reach dominance — an obviously impractical timeline.

For Bangladesh to make meaningful progress on the carbon pillar without sacrificing the poverty and employment gains, a fundamental reorientation of energy and industrial policy would be required. This might include accelerated deployment of grid-scale solar and wind; phase-down of coal plant construction; energy efficiency mandates for industry; and international climate finance to support the transition. The 3 Zero Movement's social business concept could potentially contribute through green microenterprises (e.g., solar installation, e-waste recycling, sustainable agriculture), but these remain niche activities relative to the scale of the emissions challenge.

### 5.5 The COVID-19 Disruption as a Stress Test

The year 2020 serves as an unintended stress test of the 3 Zero framework. The pandemic's impact was asymmetric across pillars: the employment pillar collapsed, the poverty pillar dipped moderately, and the carbon pillar temporarily improved (as reduced economic activity lowered emissions). The composite 3ZPI dropped from 0.669 to 0.430, erasing roughly five years of progress in a single year.

The recovery trajectory is equally informative. By 2023, the 3ZPI had not only recovered but exceeded its pre-pandemic peak (0.752 vs. 0.669). However, this recovery was driven primarily by the poverty and employment pillars bouncing back, while the carbon pillar continued its decline. The pandemic briefly demonstrated what reduced economic activity means for emissions — and the rapid post-pandemic rebound in emissions shows that the improvement was entirely a side-effect of economic contraction rather than any structural shift.

### 5.6 Limitations

This study has several important limitations that should be considered when interpreting the results.

First, the analysis relies entirely on secondary data from institutional sources. While these sources are credible, they involve measurement assumptions, survey methodologies, and estimation procedures that introduce uncertainty. Poverty and MPI figures, in particular, are available only for survey years and were interpolated for intermediate years — this smoothing may mask year-to-year volatility.

Second, the sample size for time-series analysis is small ($n = 11$). With only eleven data points, the statistical power of the linear regression and correlation analyses is limited. The $R^2$ values and correlation coefficients should be interpreted as descriptive summaries of the observed pattern rather than as evidence for strong causal claims.

Third, the 3ZPI formulation involves methodological choices — indicator selection, normalization bounds, weighting — that influence the results. The sensitivity analysis demonstrates that the qualitative conclusions are robust to alternative weights, but other choices (e.g., different indicators, geometric rather than arithmetic aggregation, or absolute rather than relative normalization) could produce different numerical outcomes.

Fourth, the study does not establish causation. The strong negative correlation between poverty and carbon pillars reflects co-movement over time, but the underlying causal mechanisms (economic growth driving both poverty reduction and emission increases) are inferred rather than formally tested.

Fifth, the single-country focus limits generalizability. While the methodology is designed to be replicable, the specific findings about pillar trajectories and inter-pillar relationships are particular to Bangladesh's development context.

### 5.7 Regional Comparison

For contextual perspective, a brief comparison with other South Asian economies is informative:

- **India:** Similar GDP growth trajectory with far larger absolute emissions. Per capita CO₂ is approximately 1.9 tonnes (about 3× Bangladesh), while the poverty headcount has also declined substantially. India faces the same growth-emissions tension at a larger scale.
- **Sri Lanka:** Higher per-capita income and lower poverty rates, but the 2022 economic crisis demonstrated the fragility of development gains. Per capita emissions (~1.0 t CO₂) are lower than India but higher than Bangladesh.
- **Nepal:** Lower emissions per capita than Bangladesh, but much higher poverty rates and limited industrial base. Nepal's challenge is accelerating development without replicating the emission trajectory of its neighbors.

Bangladesh's position is distinctive: relatively strong poverty reduction performance, a large and expanding (if precarious) employment base, and rising but still low per-capita emissions. The window for pursuing a lower-carbon development pathway may be narrowing as infrastructure investment decisions made now will lock in emission trajectories for decades.

---

## 6. Conclusion and Recommendations

### 6.1 Summary of Findings

This study evaluated Bangladesh's progress toward the three zero targets — zero poverty, zero unemployment, and zero net carbon emissions — over the period 2013–2023 using eight secondary data indicators aggregated into a composite 3 Zero Progress Index (3ZPI).

The principal findings are as follows:

1. **The composite 3ZPI increased from 0.392 to 0.752 over the decade**, indicating meaningful aggregate progress toward the three zero goals, though with a significant COVID-19 disruption in 2020.

2. **Progress is highly uneven across pillars.** The poverty pillar showed the strongest improvement (score: 0.00 → 1.00), the employment pillar showed strong but volatile progress (0.51 → 0.92), and the carbon pillar deteriorated (0.67 → 0.33).

3. **A strong negative correlation (r = −0.94) exists between the poverty and carbon pillars**, indicating that the economic growth processes driving poverty reduction simultaneously increase carbon emissions. This represents the central structural challenge for the 3 Zero Movement in Bangladesh.

4. **Linear extrapolation suggests that poverty targets are approachable** (MPI near zero by ~2033, headcount by ~2047), **unemployment shows no trend toward reduction** due to structural labor market rigidities, and **carbon emissions are moving in the wrong direction** with no projected reversal under current trends.

5. **The 3ZPI is robust to alternative weighting schemes.** The carbon-heavy weighting produces the lowest score, confirming the carbon pillar as the binding constraint on overall progress.

### 6.2 Recommendations

Based on the quantitative findings, the following recommendations are offered:

**For policymakers:**

1. **Adopt an integrated 3 Zero monitoring framework.** The siloed treatment of poverty, employment, and environmental goals across different ministries is a structural impediment. A composite index like the 3ZPI, updated annually and disaggregated to the division level, would provide a common reference point for cross-ministerial coordination.

2. **Prioritize the carbon pillar.** The analysis identifies carbon emissions as the most off-track dimension and the only pillar moving away from its target. Policy interventions should focus on accelerating renewable energy deployment (grid-scale solar, wind), phasing down new coal capacity, and implementing energy efficiency standards in industry and construction.

3. **Improve employment quality, not just quantity.** The near-zero trend in headline unemployment masks deeper problems of underemployment, informality, and educated youth joblessness. Labor market reforms should target formalization of informal employment, skills alignment with industry demand, and support for micro and small enterprises.

4. **Strengthen shock resilience.** The COVID-19 disruption demonstrated that development gains — especially in employment — can evaporate rapidly. Expanding social protection coverage and building fiscal buffers for countercyclical spending would reduce vulnerability to future shocks.

**For the 3 Zero Movement and allied organizations:**

5. **Invest in green social businesses.** The intersection of employment creation and emission reduction is an underdeveloped space. Social business models in solar energy distribution, sustainable agriculture, waste management, and energy-efficient construction could advance both the employment and carbon pillars simultaneously.

6. **Publish regular 3 Zero progress assessments.** The Yunus Centre and affiliated organizations are well-positioned to commission and disseminate annual data-driven progress reports. This would shift the discourse from aspirational messaging to evidence-based accountability.

**For future research:**

7. **Extend the 3ZPI to subnational analysis.** Division-level or district-level application of the index would reveal spatial inequalities in 3 Zero progress and enable more targeted interventions.

8. **Explore nonlinear trend models.** Linear extrapolation is a useful baseline but unrealistic for long-term projection. Logistic or polynomial models would capture the likely deceleration of poverty reduction as the headcount approaches zero and the acceleration required for emission reduction.

9. **Incorporate primary data.** This study relied entirely on secondary data. Future research should include primary surveys and interviews with beneficiaries of 3 Zero-aligned programs to capture qualitative dimensions — perceived quality of employment, barriers to clean energy adoption, and the lived experience of poverty reduction — that aggregate statistics cannot convey.

10. **Conduct multi-country comparative studies.** Applying the 3ZPI methodology to other South Asian countries (India, Nepal, Sri Lanka) would enable comparative analysis of development trajectories and illuminate whether the poverty–carbon trade-off observed in Bangladesh is a regional pattern or a country-specific phenomenon.

### 6.3 Concluding Remarks

Professor Muhammad Yunus's 3 Zero Movement offers a compelling vision for the future of economic organization — a world without poverty, without unemployment, and without the environmental destruction that threatens both. This study has attempted to bring quantitative rigor to the evaluation of that vision in the context of Bangladesh, where Yunus's ideas first took root and where the challenges of development are most acutely felt.

The numbers tell a story that is neither wholly optimistic nor wholly pessimistic. Bangladesh has made real progress on poverty and employment. But the carbon dimension — the third zero — is moving in the wrong direction, and the strong negative correlation between poverty reduction and emission growth suggests that the current development model cannot deliver all three zeros without fundamental structural changes to energy production, industrial processes, and economic incentives.

The 3 Zero Progress Index proposed in this study is a small contribution: a simple mathematical tool for tracking whether aspirational goals are being translated into measurable reality. Its value lies not in the specific numbers it produces but in the questions it forces us to ask — which pillar is lagging, why, and what can be done about it. If this framework helps shift even a small part of the conversation from aspiration to accountability, it will have served its purpose.

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

*Corresponding author: Minhajul Abedin, Department of Applied Mathematics. 4th year undergraduate with research interests in applied data analysis, quantitative modeling for development, and computational methods in social science.*
