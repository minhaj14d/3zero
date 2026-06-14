"""
Secondary Context Data — Bangladesh 3 Zero Study
=================================================
Fetches verified contextual indicators from World Bank WDI and OWID/GCP
to supplement the core 3ZPI pillars. These are NOT part of the composite
index; they provide background for the monograph.

Sources:
  - World Bank WDI via wbgapi
  - Our World in Data CO2 dataset (Bangladesh extract)
"""

import os
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(SCRIPT_DIR, '..', 'data', 'raw')
PROCESSED_DIR = os.path.join(SCRIPT_DIR, '..', 'data', 'processed')
os.makedirs(PROCESSED_DIR, exist_ok=True)

STUDY_START = 2000
STUDY_END = 2023

# World Bank indicator codes for contextual series
WB_SECONDARY = {
    'unemployment_total': 'SL.UEM.TOTL.ZS',      # % of labour force
    'renewable_energy_pct': 'EG.FEC.RNEW.ZS',    # % of total final energy
    'gdp_pc_growth': 'NY.GDP.PCAP.KD.ZG',        # annual % growth
    'population': 'SP.POP.TOTL',
    'poverty_national': 'SI.POV.NAHC',           # national poverty line %
}


def fetch_wb_series(code: str) -> pd.DataFrame:
    """Fetch one World Bank series for Bangladesh."""
    import wbgapi as wb
    df = wb.data.DataFrame(code, economy='BGD', time=range(STUDY_START, STUDY_END + 1))
    df = df.T.reset_index()
    df.columns = ['year_code', 'value']
    df['year'] = df['year_code'].str.replace('YR', '').astype(int)
    return df[['year', 'value']]


def load_owid_co2() -> pd.DataFrame:
    """Load OWID Bangladesh CO2 columns from cached raw file or GitHub."""
    path = os.path.join(RAW_DIR, 'owid_co2_bangladesh.csv')
    if os.path.exists(path):
        raw = pd.read_csv(path)
    else:
        url = 'https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv'
        raw = pd.read_csv(url)
        raw = raw[raw['country'] == 'Bangladesh']
    raw = raw[(raw['year'] >= STUDY_START) & (raw['year'] <= STUDY_END)]
    return raw[['year', 'co2', 'co2_per_capita', 'population', 'gdp']].copy()


def build_secondary_dataset() -> pd.DataFrame:
    """Merge all secondary indicators onto a common year index."""
    years = pd.DataFrame({'year': range(STUDY_START, STUDY_END + 1)})
    out = years.copy()

    for col_name, wb_code in WB_SECONDARY.items():
        print(f"  Fetching {col_name} ({wb_code})...")
        series = fetch_wb_series(wb_code)
        series = series.rename(columns={'value': col_name})
        out = out.merge(series, on='year', how='left')

    owid = load_owid_co2()
    owid = owid.rename(columns={
        'co2': 'co2_total_mt',
        'co2_per_capita': 'co2_pc_owid',
        'population': 'population_owid',
        'gdp': 'gdp_nominal_usd',
    })
    out = out.merge(owid, on='year', how='left')

    # Per-capita CO2 from total emissions / WB population (cross-check)
    out['co2_pc_calc'] = out['co2_total_mt'] * 1e6 / out['population']

    return out


def print_summary(df: pd.DataFrame):
    """Print headline 2000 vs 2023 (or latest) comparisons."""
    def snap(col):
        v0 = df.loc[df['year'] == STUDY_START, col]
        v1 = df.loc[df['year'] == STUDY_END, col]
        if v0.notna().any():
            a = v0.dropna().iloc[0]
        else:
            a = float('nan')
        if v1.notna().any():
            b = v1.dropna().iloc[0]
        else:
            b = df[col].dropna().iloc[-1] if df[col].notna().any() else float('nan')
        return a, b

    print("\nSecondary indicators — start vs end of study period:")
    for col, label, fmt in [
        ('unemployment_total', 'Total unemployment (%)', '.2f'),
        ('renewable_energy_pct', 'Renewable energy share (%)', '.1f'),
        ('gdp_pc_growth', 'GDP per capita growth (%)', '.2f'),
        ('population', 'Population', ',.0f'),
        ('co2_total_mt', 'Total CO2 emissions (Mt)', '.1f'),
        ('poverty_national', 'National poverty line (%)', '.1f'),
    ]:
        if col not in df.columns:
            continue
        a, b = snap(col)
        if pd.notna(a) and pd.notna(b):
            print(f"  {label}: {a:{fmt}} -> {b:{fmt}}")
        elif pd.notna(b):
            print(f"  {label}: (sparse) latest = {b:{fmt}}")


def main():
    print("=" * 60)
    print("Secondary Context Data — Fetch Pipeline")
    print("=" * 60)
    df = build_secondary_dataset()
    out_path = os.path.join(PROCESSED_DIR, 'secondary_context.csv')
    df.to_csv(out_path, index=False)
    print(f"\nSaved: {out_path} ({len(df)} rows)")
    print_summary(df)
    print("\nNote: poverty_national has very sparse survey coverage (often one recent year).")
    print("Note: renewable_energy_pct may end before 2023 due to WB reporting lag.")


if __name__ == '__main__':
    main()
