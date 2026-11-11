"""
Step 2. Make summary tables and figures from data/processed/trials_classified.csv.

Run from the main project folder:  python scripts/02_summary_and_figures.py
Results are preliminary until the manual check of Medium and Low confidence trials is finished.
"""
from collections import Counter
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/trials_classified.csv")
TABLES = Path("results/tables"); FIGS = Path("results/figures")
TABLES.mkdir(parents=True, exist_ok=True); FIGS.mkdir(parents=True, exist_ok=True)

ther = df[df["Auto Category"] == "Therapeutic gene editing"]

# Tables
df["Auto Category"].value_counts().rename_axis("Category").reset_index(name="Trials").to_csv(
    TABLES / "category_counts.csv", index=False)
pd.crosstab(df["Auto Category"], df["Confidence"]).to_csv(TABLES / "category_by_confidence.csv")
ther["Study Status"].value_counts().rename_axis("Status").reset_index(name="Trials").to_csv(
    TABLES / "therapeutic_by_status.csv", index=False)
ther["Phase label"].value_counts().rename_axis("Phase").reset_index(name="Trials").to_csv(
    TABLES / "therapeutic_by_phase.csv", index=False)
ther["Funder Type"].value_counts().rename_axis("Funder type").reset_index(name="Trials").to_csv(
    TABLES / "therapeutic_by_funder.csv", index=False)
country_counts = Counter(c for s in ther["Countries"].dropna() for c in s.split("; ") if c)
country_df = pd.DataFrame(country_counts.most_common(), columns=["Country", "Trials with at least one site"])
country_df.to_csv(TABLES / "therapeutic_by_country.csv", index=False)

NOTE = "Preliminary: first pass categories, manual check not finished. Source: ClinicalTrials.gov"

# Figure 1, trials by start year
yr = ther["Start year"].dropna().astype(int).value_counts().sort_index()
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(yr.index.astype(str), yr.values, color="#1F3864")
ax.set_xlabel("Start year"); ax.set_ylabel("Number of trials")
ax.set_title("Therapeutic gene editing trials by start year")
plt.xticks(rotation=60); fig.text(0.01, 0.01, NOTE, fontsize=7)
plt.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(FIGS / "trials_by_start_year.png", dpi=200); plt.close()

# Figure 2, top countries
top = country_df.head(10).iloc[::-1]
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.barh(top["Country"], top["Trials with at least one site"], color="#1F3864")
ax.set_xlabel("Trials with at least one site")
ax.set_title("Top 10 countries, therapeutic gene editing trials")
fig.text(0.01, 0.01, NOTE, fontsize=7)
plt.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(FIGS / "top_countries.png", dpi=200); plt.close()

# Figure 3, phase
order = ["Early phase 1", "Phase 1", "Phase 1/2", "Phase 2", "Phase 2/3", "Phase 3", "Not listed"]
ph = ther["Phase label"].value_counts().reindex(order).dropna()
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(ph.index, ph.values, color="#1F3864")
ax.set_ylabel("Number of trials"); ax.set_title("Therapeutic gene editing trials by phase")
plt.xticks(rotation=30); fig.text(0.01, 0.01, NOTE, fontsize=7)
plt.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(FIGS / "trials_by_phase.png", dpi=200); plt.close()
print("Tables and figures saved.")
