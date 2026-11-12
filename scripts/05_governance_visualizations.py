import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans"]
plt.rcParams["axes.edgecolor"] = "#333333"
plt.rcParams["axes.linewidth"] = 0.8

INPUT_CSV = Path("data/processed/trials_ethics_coded.csv")
FIGURES_DIR = Path("results/figures")
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

def load_therapeutic_data():
    df = pd.read_csv(INPUT_CSV)
    tx_df = df[df["refined_category"] == "Therapeutic gene editing"].copy()
    return df, tx_df

def plot_disease_areas(tx_df):
    counts = tx_df["disease_area"].value_counts()
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(counts.index[::-1], counts.values[::-1], color="#1f4e78", height=0.65)
    
    ax.set_xlabel("Number of Registered Therapeutic Trials", fontsize=11, fontweight="bold")
    ax.set_title("Therapeutic Gene-Editing Clinical Trials by Disease Area", fontsize=13, fontweight="bold", pad=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    
    for bar in bars:
        width = bar.get_width()
        pct = (width / len(tx_df)) * 100
        ax.text(width + 0.5, bar.get_y() + bar.get_height()/2, f"{int(width)} ({pct:.1f}%)",
                va="center", ha="left", fontsize=9.5, color="#222222")
    
    ax.set_xlim(0, counts.max() * 1.18)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "fig4_therapeutic_by_disease_area.png", dpi=300)
    plt.close()

def plot_governance_transparency(tx_df):
    metrics = {
        "Informed Consent\n(Explicit Mention)": (tx_df["consent_reporting"] != "Not stated in public text").mean() * 100,
        "Minor Assent / Guardian\n(Where Applicable/Stated)": (tx_df["consent_reporting"] == "Explicit (Consent + Minor Assent/Guardian)").mean() * 100,
        "Ethics / IRB Approval\n(Stated in Narrative)": (tx_df["ethics_irb_reporting"] == "Explicitly stated in record").mean() * 100,
        "Long-Term Follow-Up\n(Any Duration Stated)": (tx_df["ltfu_reporting"] != "Not stated in public text").mean() * 100,
        "15-Year LTFU Mandate\n(Explicitly Stated)": (tx_df["ltfu_reporting"] == "15-year LTFU stated (FDA/EMA standard)").mean() * 100,
        "Off-Target / WGS\nSafety Monitoring": (tx_df["off_target_monitoring"] == "Yes").mean() * 100,
    }
    
    labels = list(metrics.keys())[::-1]
    values = list(metrics.values())[::-1]
    
    fig, ax = plt.subplots(figsize=(9, 5.2))
    colors = ["#2e75b6" if v >= 50 else "#c55a11" for v in values]
    bars = ax.barh(labels, values, color=colors, height=0.6)
    
    ax.set_xlabel("Percentage of Therapeutic Trials (%)", fontsize=11, fontweight="bold")
    ax.set_title("Public Reporting Transparency in Therapeutic Gene-Editing Trials", fontsize=13, fontweight="bold", pad=12)
    ax.set_xlim(0, 112)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 1.5, bar.get_y() + bar.get_height()/2, f"{width:.1f}%",
                va="center", ha="left", fontsize=9.5, fontweight="bold", color="#222222")
        
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "fig5_governance_transparency_rates.png", dpi=300)
    plt.close()

def plot_ltfu_breakdown(tx_df):
    ltfu_counts = tx_df["ltfu_reporting"].value_counts()
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    palette = sns.color_palette("Blues_r", len(ltfu_counts))
    bars = ax.barh(ltfu_counts.index[::-1], ltfu_counts.values[::-1], color=palette[::-1], height=0.6)
    
    ax.set_xlabel("Number of Trials", fontsize=11, fontweight="bold")
    ax.set_title("Long-Term Follow-Up (LTFU) Disclosure in Therapeutic Protocols", fontsize=12.5, fontweight="bold", pad=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.4, bar.get_y() + bar.get_height()/2, f"{int(width)}",
                va="center", ha="left", fontsize=9.5)
        
    ax.set_xlim(0, ltfu_counts.max() * 1.15)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "fig6_ltfu_disclosure_breakdown.png", dpi=300)
    plt.close()

def main():
    _, tx_df = load_therapeutic_data()
    plot_disease_areas(tx_df)
    plot_governance_transparency(tx_df)
    plot_ltfu_breakdown(tx_df)
    print(f"Generated 3 governance and disease-area figures in {FIGURES_DIR}/")

if __name__ == "__main__":
    main()
