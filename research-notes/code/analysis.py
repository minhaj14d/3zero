"""
3 Zero Progress Index (3ZPI) — Analysis Script
===============================================
Author: Minhajul Abedin
Department of Applied Mathematics, NSTU

This script fetches, cleans, and analyzes three indicators for Bangladesh:
  1. Poverty headcount ratio at $3.00/day (World Bank: SI.POV.DDAY)
  2. Youth unemployment, ages 15-24 (World Bank/ILO: SL.UEM.1524.ZS)
  3. CO2 emissions per capita (Our World in Data / Global Carbon Project)

It computes the composite 3 Zero Progress Index, runs linear regression
on each indicator, and produces a correlation matrix. All results are
exported as CSVs to data/processed/.

Data sources:
  - World Bank WDI via wbgapi Python library
  - Our World in Data CO2 dataset (GitHub CSV, sourced from GCP)
"""

import os
import warnings
import numpy as np
import pandas as pd
from scipy import stats

warnings.filterwarnings('ignore')

# ── Paths ──────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, '..', 'data')
RAW_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DIR = os.path.join(DATA_DIR, 'processed')
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

STUDY_START = 2000
STUDY_END = 2023


# ── Step 1: Fetch raw data ────────────────────────────────────────────

def fetch_poverty():
    """Fetch poverty headcount at $3.00/day (2021 PPP) from World Bank API."""
    import wbgapi as wb
    print("[1/3] Fetching poverty data (SI.POV.DDAY) from World Bank...")
    df = wb.data.DataFrame(
        'SI.POV.DDAY', economy='BGD',
        time=range(STUDY_START, STUDY_END + 1)
    )
    # wbgapi returns years as columns like 'YR2000'; transpose and clean
    df = df.T.reset_index()
    df.columns = ['year_code', 'poverty']
    df['year'] = df['year_code'].str.replace('YR', '').astype(int)
    df = df[['year', 'poverty']].sort_values('year').reset_index(drop=True)
    return df


def fetch_youth_unemployment():
    """Fetch youth unemployment (15-24, ILO modeled) from World Bank API."""
    import wbgapi as wb
    print("[2/3] Fetching youth unemployment (SL.UEM.1524.ZS) from World Bank...")
    df = wb.data.DataFrame(
        'SL.UEM.1524.ZS', economy='BGD',
        time=range(STUDY_START, STUDY_END + 1)
    )
    df = df.T.reset_index()
    df.columns = ['year_code', 'youth_unemp']
    df['year'] = df['year_code'].str.replace('YR', '').astype(int)
    df = df[['year', 'youth_unemp']].sort_values('year').reset_index(drop=True)
    return df


def fetch_co2():
    """Fetch CO2 per capita from Our World in Data (GCP-sourced)."""
    print("[3/3] Fetching CO2 per capita from Our World in Data (GCP)...")
    url = 'https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv'
    raw = pd.read_csv(url)
    bd = raw[raw['country'] == 'Bangladesh'][['year', 'co2_per_capita']].dropna()
    bd = bd[(bd['year'] >= STUDY_START) & (bd['year'] <= STUDY_END)]
    bd = bd.rename(columns={'co2_per_capita': 'co2_pc'})
    bd = bd.sort_values('year').reset_index(drop=True)

    # Save the full OWID Bangladesh extract for reference
    raw_bd = raw[raw['country'] == 'Bangladesh']
    raw_bd.to_csv(os.path.join(RAW_DIR, 'owid_co2_bangladesh.csv'), index=False)

    return bd


# ── Step 2: Merge and interpolate ─────────────────────────────────────

def build_dataset():
    """Merge all three indicators into a single DataFrame.
    Poverty data has gaps (survey years only), so we interpolate linearly.
    """
    pov = fetch_poverty()
    yu = fetch_youth_unemployment()
    co2 = fetch_co2()

    # Create a complete year index
    years = pd.DataFrame({'year': range(STUDY_START, STUDY_END + 1)})

    # Merge all indicators onto the year index
    df = years.merge(pov, on='year', how='left')
    df = df.merge(yu, on='year', how='left')
    df = df.merge(co2, on='year', how='left')

    # Track which poverty values are real vs. interpolated
    df['poverty_interpolated'] = df['poverty'].isna()

    # Interpolate poverty linearly between survey years
    df['poverty'] = df['poverty'].interpolate(method='linear')

    # Drop any rows where we still have NaNs at the edges
    df = df.dropna(subset=['poverty', 'youth_unemp', 'co2_pc']).reset_index(drop=True)

    print(f"\nDataset built: {len(df)} years, {STUDY_START}-{STUDY_END}")
    print(f"Poverty survey years (actual data): "
          f"{df[~df['poverty_interpolated']]['year'].tolist()}")
    print(f"Poverty interpolated years: "
          f"{df[df['poverty_interpolated']]['year'].tolist()}")

    return df


# ── Step 3: Normalization ─────────────────────────────────────────────

def normalize(df):
    """Min-max normalization to [0, 1].
    All three indicators are 'lower is better', so we use inverted normalization:
      x_norm = (x_max - x) / (x_max - x_min)
    A score of 1 means the best observed value; 0 means the worst.
    """
    result = df[['year']].copy()
    bounds = {}

    for col in ['poverty', 'youth_unemp', 'co2_pc']:
        x_min = df[col].min()
        x_max = df[col].max()
        bounds[col] = {'min': x_min, 'max': x_max}
        # Inverted: lower raw value = higher normalized score
        result[col + '_norm'] = (x_max - df[col]) / (x_max - x_min)

    return result, bounds


# ── Step 4: Composite 3 Zero Progress Index ───────────────────────────

def compute_3zpi(norm_df, weights=None):
    """Compute the 3ZPI as a weighted average of the three normalized indicators.
    Default: equal weights (1/3 each).
    """
    if weights is None:
        weights = {'poverty': 1/3, 'youth_unemp': 1/3, 'co2_pc': 1/3}

    norm_df = norm_df.copy()
    norm_df['3ZPI'] = (
        weights['poverty'] * norm_df['poverty_norm'] +
        weights['youth_unemp'] * norm_df['youth_unemp_norm'] +
        weights['co2_pc'] * norm_df['co2_pc_norm']
    )
    return norm_df


# ── Step 5: Sensitivity analysis ──────────────────────────────────────

def sensitivity_analysis(norm_df):
    """Run 3ZPI with four different weighting schemes."""
    schemes = {
        'equal':     {'poverty': 1/3, 'youth_unemp': 1/3, 'co2_pc': 1/3},
        'pov_heavy': {'poverty': 0.5, 'youth_unemp': 0.25, 'co2_pc': 0.25},
        'emp_heavy': {'poverty': 0.25, 'youth_unemp': 0.5, 'co2_pc': 0.25},
        'co2_heavy': {'poverty': 0.25, 'youth_unemp': 0.25, 'co2_pc': 0.5},
    }
    results = norm_df[['year']].copy()
    for name, w in schemes.items():
        results[name] = (
            w['poverty'] * norm_df['poverty_norm'] +
            w['youth_unemp'] * norm_df['youth_unemp_norm'] +
            w['co2_pc'] * norm_df['co2_pc_norm']
        )
    return results


# ── Step 6: Linear regression ─────────────────────────────────────────

def trend_analysis(df):
    """Run linear regression on each raw indicator over time.
    Time is coded as t = 0 for the first year in the dataset.
    """
    t = df['year'] - df['year'].min()
    results = []
    for col in ['poverty', 'youth_unemp', 'co2_pc']:
        slope, intercept, r_value, p_value, std_err = stats.linregress(t, df[col])
        last_val = df[col].iloc[-1]
        last_year = df['year'].iloc[-1]
        # Projected year to reach zero (only meaningful if slope < 0)
        if slope < 0 and last_val > 0:
            years_to_zero = last_val / abs(slope)
            proj_year = last_year + years_to_zero
        elif slope >= 0:
            proj_year = float('inf')  # moving away from zero
        else:
            proj_year = float('nan')

        results.append({
            'indicator': col,
            'slope_beta': round(slope, 4),
            'intercept_alpha': round(intercept, 4),
            'r_squared': round(r_value**2, 4),
            'p_value': round(p_value, 6),
            'last_value': round(last_val, 3),
            'projected_year_to_zero': round(proj_year) if np.isfinite(proj_year) else 'Never / wrong direction'
        })
    return pd.DataFrame(results)


# ── Step 7: Correlation analysis ──────────────────────────────────────

def correlation_analysis(norm_df):
    """Compute Pearson correlation matrix between the three normalized indicators."""
    cols = ['poverty_norm', 'youth_unemp_norm', 'co2_pc_norm']
    labels = ['Poverty', 'Youth Unemployment', 'CO2 per Capita']
    corr = norm_df[cols].corr()
    corr.index = labels
    corr.columns = labels
    return corr


# ── Step 8: Gap analysis ─────────────────────────────────────────────

def gap_analysis(df, regression_results):
    """Compute remaining gap to zero and projected achievement year."""
    rows = []
    for _, reg in regression_results.iterrows():
        rows.append({
            'indicator': reg['indicator'],
            'value_2023': reg['last_value'],
            'target': 0,
            'annual_change_beta': reg['slope_beta'],
            'projected_year': reg['projected_year_to_zero']
        })
    return pd.DataFrame(rows)


# ── Main ──────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("3 Zero Progress Index — Analysis Pipeline")
    print("=" * 60)

    # Fetch and merge data
    raw_df = build_dataset()
    raw_df.to_csv(os.path.join(PROCESSED_DIR, 'three_zero_raw.csv'), index=False)
    print(f"\n✓ Raw data saved to data/processed/three_zero_raw.csv")

    # Print raw data table (for the paper)
    print("\n" + "=" * 60)
    print("TABLE 2: Raw Indicator Data")
    print("=" * 60)
    display = raw_df[['year', 'poverty', 'youth_unemp', 'co2_pc']].copy()
    display.columns = ['Year', 'Poverty ($3.00/day %)', 'Youth Unemp (%)', 'CO2 pc (t)']
    print(display.to_string(index=False))

    # Normalize
    norm_df, bounds = normalize(raw_df)
    print("\n" + "=" * 60)
    print("TABLE 3: Min-Max Bounds")
    print("=" * 60)
    for k, v in bounds.items():
        print(f"  {k}: min={v['min']:.3f}, max={v['max']:.3f}")

    # Compute 3ZPI
    norm_df = compute_3zpi(norm_df)
    norm_df.to_csv(os.path.join(PROCESSED_DIR, 'three_zero_normalized.csv'), index=False)
    print(f"\n✓ Normalized data + 3ZPI saved")

    print("\n" + "=" * 60)
    print("TABLE 5: Normalized Scores and 3ZPI")
    print("=" * 60)
    display5 = norm_df.round(3)
    display5.columns = ['Year', 'Poverty (norm)', 'Youth Unemp (norm)', 'CO2 pc (norm)', '3ZPI']
    print(display5.to_string(index=False))

    # Sensitivity analysis
    sens = sensitivity_analysis(norm_df)
    sens.to_csv(os.path.join(PROCESSED_DIR, 'three_zero_sensitivity.csv'), index=False)
    print("\n" + "=" * 60)
    print("TABLE 6: Sensitivity Analysis (Selected Years)")
    print("=" * 60)
    selected = sens[sens['year'].isin([2000, 2005, 2010, 2016, 2020, 2023])]
    print(selected.round(3).to_string(index=False))

    # Trend analysis
    reg = trend_analysis(raw_df)
    reg.to_csv(os.path.join(PROCESSED_DIR, 'regression_results.csv'), index=False)
    print("\n" + "=" * 60)
    print("TABLE 7: Linear Regression Results")
    print("=" * 60)
    print(reg.to_string(index=False))

    # Gap analysis
    gap = gap_analysis(raw_df, reg)
    gap.to_csv(os.path.join(PROCESSED_DIR, 'gap_analysis.csv'), index=False)
    print("\n" + "=" * 60)
    print("TABLE 8: Gap Analysis")
    print("=" * 60)
    print(gap.to_string(index=False))

    # Correlation
    corr = correlation_analysis(norm_df)
    corr.to_csv(os.path.join(PROCESSED_DIR, 'correlation_matrix.csv'))
    print("\n" + "=" * 60)
    print("TABLE 9: Correlation Matrix (Normalized Pillar Scores)")
    print("=" * 60)
    print(corr.round(3).to_string())

    # Statistical significance check (n=number of years, df=n-2)
    n = len(norm_df)
    df_stat = n - 2
    t_crit = stats.t.ppf(0.975, df_stat)  # two-tailed 5%
    r_crit = t_crit / np.sqrt(t_crit**2 + df_stat)
    print(f"\nSignificance threshold: |r| > {r_crit:.3f} (5% level, df={df_stat})")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    first_year = norm_df.iloc[0]
    last_year = norm_df.iloc[-1]
    print(f"Study period: {int(first_year['year'])} - {int(last_year['year'])}")
    print(f"3ZPI start: {first_year['3ZPI']:.3f}")
    print(f"3ZPI end:   {last_year['3ZPI']:.3f}")
    print(f"3ZPI change: +{last_year['3ZPI'] - first_year['3ZPI']:.3f}")
    print(f"\nPoverty: {raw_df['poverty'].iloc[0]:.1f}% -> {raw_df['poverty'].iloc[-1]:.1f}%")
    print(f"Youth Unemployment: {raw_df['youth_unemp'].iloc[0]:.1f}% -> {raw_df['youth_unemp'].iloc[-1]:.1f}%")
    print(f"CO2 per capita: {raw_df['co2_pc'].iloc[0]:.3f}t -> {raw_df['co2_pc'].iloc[-1]:.3f}t")

    print("\n✓ All outputs saved to data/processed/")
    print("  - three_zero_raw.csv")
    print("  - three_zero_normalized.csv")
    print("  - three_zero_sensitivity.csv")
    print("  - regression_results.csv")
    print("  - gap_analysis.csv")
    print("  - correlation_matrix.csv")


if __name__ == '__main__':
    main()
