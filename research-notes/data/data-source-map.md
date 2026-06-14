# Data Source Map: 3 Zero Progress Index Indicators
> Last updated: 2026-03-28
> Status: Active

## Overview

This file maps every data requirement in the research article to its verified source. Three core indicators are tracked across the study period 2000–2023 for Bangladesh (country code: BGD).

---

## Indicator 1: Poverty Headcount Ratio at $3.00/day (2021 PPP)

**Table references:** Tables 1, 2, 3, 4, 5, 7, 8, 9

| Field | Value |
|-------|-------|
| Organization | World Bank |
| Dataset | World Development Indicators |
| Indicator code | `SI.POV.DDAY` |
| Description | % of population living below $3.00/day (2021 PPP) |
| Unit | % of population |
| Direction | Lower is better (inverted normalization) |
| URL | https://data.worldbank.org/indicator/SI.POV.DDAY?locations=BD |
| Access method | `wbgapi` Python API — `wb.data.DataFrame('SI.POV.DDAY', economy='BGD')` |
| Coverage | Available for survey years only |
| Known survey years | ~2000, 2005, 2010, 2016, 2022 |
| Status | [x] Fetched — `data/processed/three_zero_raw.csv` |

> **Gap:** Annual data is NOT available. Only ~5 data points exist for the 2000–2023 period. Linear interpolation is required for non-survey years and must be flagged as a limitation in the paper.

> **Assumption:** Linear interpolation between survey years provides a reasonable approximation of the poverty trajectory. This assumption may understate short-term shocks (e.g., COVID-19 impact in 2020).

---

## Indicator 2: Youth Unemployment Rate (ages 15–24, ILO modeled estimate)

**Table references:** Tables 1, 2, 3, 4, 5, 7, 8, 9

| Field | Value |
|-------|-------|
| Organization | World Bank / International Labour Organization |
| Dataset | World Development Indicators (sourced from ILOSTAT) |
| Indicator code | `SL.UEM.1524.ZS` |
| Description | Unemployment, youth total (% of total labor force ages 15–24) |
| Unit | % of labor force ages 15–24 |
| Direction | Lower is better (inverted normalization) |
| URL | https://data.worldbank.org/indicator/SL.UEM.1524.ZS?locations=BD |
| Access method | `wbgapi` Python API — `wb.data.DataFrame('SL.UEM.1524.ZS', economy='BGD')` |
| Coverage | Annual, 1991–2024 (ILO modeled estimates) |
| Status | [x] Fetched — `data/processed/three_zero_raw.csv` |

> **Note:** The ILO modeled estimates combine nationally reported observations with imputed data. These are not direct survey measurements but modeled values with associated uncertainty. This must be noted in the paper's Methodology and Limitations sections.

> **Note:** Previous draft used age range 15–29 (from BBS Labour Force Survey). This version uses 15–24 (World Bank/ILO standard). The change affects both the data values and the text.

**Verified reference values (from FRED/ILO):**
- 2021: 12.72%
- 2022: 10.99%
- 2023: 7.91%

---

## Indicator 3: CO₂ Emissions Per Capita

**Table references:** Tables 1, 2, 3, 4, 5, 7, 8, 9

| Field | Value |
|-------|-------|
| Organization | Global Carbon Project via Our World in Data |
| Dataset (primary) | OWID CO₂ dataset (GitHub mirror) |
| Indicator code (primary) | `co2_per_capita` |
| Dataset (supplement) | World Development Indicators `EN.ATM.CO2E.PC` (API fails via wbgapi) |
| URL (WB) | https://data.worldbank.org/indicator/EN.ATM.CO2E.PC?locations=BD |
| URL (GCP) | https://zenodo.org/records/13981696 |
| URL (OWID mirror) | https://ourworldindata.org/co2/country/bangladesh |
| Access method (WB) | `wbgapi` Python API — `wb.data.DataFrame('EN.ATM.CO2E.PC', economy='BGD')` |
| Access method (GCP) | CSV download from Zenodo or OWID GitHub |
| Unit | Metric tonnes CO₂ per capita |
| Direction | Lower is better (inverted normalization) |
| WB Coverage | Annual, 1960–~2020 |
| GCP Coverage | Annual, 1750–2023 |
| Status | [x] Fetched — `data/processed/three_zero_raw.csv` |

> **Note (pipeline):** `analysis.py` uses OWID/GCP only for CO₂ per capita. World Bank `EN.ATM.CO2E.PC` is documented here but not merged due to API fetch failure.

> **Gap:** World Bank CO₂ data (sourced from Climate Watch) typically lags 2–3 years. OWID/GCP provides continuous annual data through 2023.

**Verified reference values (from GCP via countryeconomy.com):**
- 2021: 0.68 t/capita
- 2022: 0.72 t/capita
- 2023: 0.71 t/capita

---

## Derived Tables (computed from the 3 indicators above)

| Table | What it shows | Data source | Computation |
|-------|---------------|-------------|-------------|
| Table 1 | Indicator definitions | Metadata (this file) | Manual |
| Table 2 | Raw indicator data (2000–2023) | WB API + GCP CSV | `analysis.py` fetch |
| Table 3 | Min-max normalization bounds | Table 2 | `min()`, `max()` per indicator |
| Table 4 | Normalized scores [0,1] | Table 2 + Table 3 | Min-max formula |
| Table 5 | 3ZPI composite index | Table 4 | Weighted average |
| Table 6 | Sensitivity analysis (alt. weights) | Table 4 | 3 alternative weight schemes |
| Table 7 | Linear regression results | Table 2 | `scipy.stats.linregress` |
| Table 8 | Gap analysis / projections | Table 7 | Linear extrapolation to zero |
| Table 9 | Correlation matrix | Table 4 | `numpy.corrcoef` or `DataFrame.corr` |

---

## Data Files Expected

| File | Location | Source |
|------|----------|--------|
| GCP fossil CO₂ CSV | `data/raw/gcb_fossil_co2.csv` | Zenodo / OWID GitHub |
| Cleaned merged data | `data/processed/three_zero_raw.csv` | `analysis.py` output |
| Normalized scores | `data/processed/three_zero_normalized.csv` | `analysis.py` output |
| 3ZPI composite | `data/processed/three_zero_3zpi.csv` | `analysis.py` output |
| Regression results | `data/processed/regression_results.csv` | `analysis.py` output |
| Correlation matrix | `data/processed/correlation_matrix.csv` | `analysis.py` output |
| Secondary context | `data/processed/secondary_context.csv` | `fetch_secondary.py` output |

---

## Secondary Context Indicators (Monograph v2 — not in 3ZPI)

Fetched by `code/fetch_secondary.py` for contextual interpretation only.

| Indicator | Code / column | Source | Status |
|-----------|---------------|--------|--------|
| National poverty headcount | `SI.POV.NAHC` / `poverty_national` | World Bank WDI | [x] Fetched (2022 only: 18.7%) |
| Total unemployment | `SL.UEM.TOTL.ZS` / `unemployment_total` | World Bank WDI | [x] Fetched |
| Renewable energy share | `EG.FEC.RNEW.ZS` / `renewable_energy_pct` | World Bank WDI | [x] Fetched (ends 2021) |
| GDP per capita growth | `NY.GDP.PCAP.KD.ZG` / `gdp_pc_growth` | World Bank WDI | [x] Fetched |
| Population | `SP.POP.TOTL` / `population` | World Bank WDI | [x] Fetched |
| Total CO₂ emissions | `co2` (Mt) / `co2_total_mt` | OWID / GCP | [x] Fetched |

**Figures:** `fig7_unemployment_comparison`, `fig8_emissions_energy_context` in `figures/`

**Paper outputs:**
- Conference article (v3): `drafts/paper-article-v3-data-verified.md`, `drafts/paper-article-v3.tex`
- Enriched monograph (v2): `drafts/paper-monograph-v2-enriched.md`, `drafts/paper-monograph-v2.tex` → `paper-monograph-v2.pdf`
