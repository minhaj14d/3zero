"""
3 Zero Progress Index — Figure Generation
==========================================
Author: Minhajul Abedin
Department of Applied Mathematics, NSTU

Generates 6 publication-quality figures from the processed CSV data.
All figures saved as both PNG (300 DPI) and PDF.

Run analysis.py first to generate the CSV files this script reads.
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ── Paths ──────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, '..', 'data', 'processed')
FIG_DIR = os.path.join(SCRIPT_DIR, '..', 'figures')
os.makedirs(FIG_DIR, exist_ok=True)

# ── Style ──────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'legend.fontsize': 10,
    'figure.figsize': (8, 5),
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})
sns.set_palette('colorblind')
COLORS = sns.color_palette('colorblind')


def save_fig(fig, name):
    """Save figure as both PNG and PDF."""
    fig.savefig(os.path.join(FIG_DIR, f'{name}.png'))
    fig.savefig(os.path.join(FIG_DIR, f'{name}.pdf'))
    plt.close(fig)
    print(f"  Saved: {name}.png, {name}.pdf")


# ── Load data ──────────────────────────────────────────────────────────
raw = pd.read_csv(os.path.join(DATA_DIR, 'three_zero_raw.csv'))
norm = pd.read_csv(os.path.join(DATA_DIR, 'three_zero_normalized.csv'))
sens = pd.read_csv(os.path.join(DATA_DIR, 'three_zero_sensitivity.csv'))
reg = pd.read_csv(os.path.join(DATA_DIR, 'regression_results.csv'))
corr = pd.read_csv(os.path.join(DATA_DIR, 'correlation_matrix.csv'), index_col=0)

print("Generating figures...")


# ── Figure 1: Poverty trend ───────────────────────────────────────────
def fig1_poverty():
    fig, ax = plt.subplots()
    ax.plot(raw['year'], raw['poverty'], marker='o', markersize=4,
            color=COLORS[0], linewidth=1.8, label='Poverty headcount')

    # Add regression line
    t = raw['year'] - raw['year'].min()
    r = reg[reg['indicator'] == 'poverty'].iloc[0]
    fit = r['intercept_alpha'] + r['slope_beta'] * t
    ax.plot(raw['year'], fit, '--', color=COLORS[0], alpha=0.5,
            label=f"Linear fit (β={r['slope_beta']:.2f}, R²={r['r_squared']:.3f})")

    # Mark survey years
    survey_years = [2000, 2005, 2010, 2016, 2022]
    survey_vals = raw[raw['year'].isin(survey_years)]
    ax.scatter(survey_vals['year'], survey_vals['poverty'],
               s=60, zorder=5, color=COLORS[0], edgecolors='black', linewidth=0.8)

    ax.set_title('Bangladesh: Poverty Headcount Ratio at $3.00/day (2000–2023)')
    ax.set_xlabel('Year')
    ax.set_ylabel('% of population below $3.00/day (2021 PPP)')
    ax.set_xlim(1999, 2024)
    ax.set_ylim(0, 45)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right')
    return fig

save_fig(fig1_poverty(), 'fig1_poverty_trend')


# ── Figure 2: Youth unemployment trend ────────────────────────────────
def fig2_unemployment():
    fig, ax = plt.subplots()
    ax.plot(raw['year'], raw['youth_unemp'], marker='s', markersize=4,
            color=COLORS[1], linewidth=1.8, label='Youth unemployment (15–24)')

    t = raw['year'] - raw['year'].min()
    r = reg[reg['indicator'] == 'youth_unemp'].iloc[0]
    fit = r['intercept_alpha'] + r['slope_beta'] * t
    ax.plot(raw['year'], fit, '--', color=COLORS[1], alpha=0.5,
            label=f"Linear fit (β=+{r['slope_beta']:.2f}, R²={r['r_squared']:.3f})")

    ax.set_title('Bangladesh: Youth Unemployment Rate, Ages 15–24 (2000–2023)')
    ax.set_xlabel('Year')
    ax.set_ylabel('% of labor force ages 15–24')
    ax.set_xlim(1999, 2024)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left')
    return fig

save_fig(fig2_unemployment(), 'fig2_unemployment_trend')


# ── Figure 3: CO2 per capita trend ────────────────────────────────────
def fig3_co2():
    fig, ax = plt.subplots()
    ax.plot(raw['year'], raw['co2_pc'], marker='^', markersize=4,
            color=COLORS[2], linewidth=1.8, label='CO₂ per capita')

    t = raw['year'] - raw['year'].min()
    r = reg[reg['indicator'] == 'co2_pc'].iloc[0]
    fit = r['intercept_alpha'] + r['slope_beta'] * t
    ax.plot(raw['year'], fit, '--', color=COLORS[2], alpha=0.5,
            label=f"Linear fit (β=+{r['slope_beta']:.4f}, R²={r['r_squared']:.3f})")

    ax.set_title('Bangladesh: CO₂ Emissions Per Capita (2000–2023)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Metric tonnes CO₂ per capita')
    ax.set_xlim(1999, 2024)
    ax.set_ylim(0, 0.75)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left')
    return fig

save_fig(fig3_co2(), 'fig3_co2_trend')


# ── Figure 4: Combined normalized + 3ZPI ──────────────────────────────
def fig4_combined():
    fig, ax = plt.subplots()

    ax.plot(norm['year'], norm['poverty_norm'], marker='o', markersize=3,
            color=COLORS[0], linewidth=1.5, label='Poverty (normalized)')
    ax.plot(norm['year'], norm['youth_unemp_norm'], marker='s', markersize=3,
            color=COLORS[1], linewidth=1.5, label='Youth unemployment (normalized)')
    ax.plot(norm['year'], norm['co2_pc_norm'], marker='^', markersize=3,
            color=COLORS[2], linewidth=1.5, label='CO₂ per capita (normalized)')
    ax.plot(norm['year'], norm['3ZPI'], marker='D', markersize=4,
            color=COLORS[3], linewidth=2.5, label='3ZPI (composite)')

    ax.set_title('Three Zero Progress Index — Bangladesh (2000–2023)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Normalized score (0 = worst, 1 = best)')
    ax.set_xlim(1999, 2024)
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='center left', bbox_to_anchor=(0.0, 0.45))
    return fig

save_fig(fig4_combined(), 'fig4_three_zero_index')


# ── Figure 5: Correlation heatmap ─────────────────────────────────────
def fig5_heatmap():
    fig, ax = plt.subplots(figsize=(6, 5))
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    sns.heatmap(corr.astype(float), annot=True, fmt='.3f', cmap='RdBu_r',
                vmin=-1, vmax=1, center=0, square=True,
                linewidths=1, ax=ax,
                cbar_kws={'label': 'Pearson r'})
    ax.set_title('Correlation Matrix — Normalized Pillar Scores')
    return fig

save_fig(fig5_heatmap(), 'fig5_correlation_heatmap')


# ── Figure 6: Regression slopes bar chart ─────────────────────────────
def fig6_regression():
    fig, ax = plt.subplots(figsize=(7, 5))
    indicators = ['Poverty\n($3.00/day %)', 'Youth Unemp.\n(% 15–24)', 'CO₂ per capita\n(tonnes)']
    slopes = reg['slope_beta'].values
    colors = [COLORS[0] if s < 0 else COLORS[2] for s in slopes]

    bars = ax.bar(indicators, slopes, color=colors, edgecolor='black', linewidth=0.5)

    for bar, slope in zip(bars, slopes):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                f'{slope:+.3f}', ha='center',
                va='bottom' if slope >= 0 else 'top',
                fontsize=10, fontweight='bold')

    ax.axhline(y=0, color='black', linewidth=0.8)
    ax.set_title('Annual Rate of Change (Linear Regression Slope β)')
    ax.set_ylabel('Annual change (units per year)')
    ax.grid(True, alpha=0.3, axis='y')
    return fig

save_fig(fig6_regression(), 'fig6_regression_summary')


print("\n✓ All 6 figures generated in research-notes/figures/")
