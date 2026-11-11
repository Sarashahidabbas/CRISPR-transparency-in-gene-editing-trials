"""
Step 1. Merge the two ClinicalTrials.gov downloads and give each trial a first pass category.

Run from the main project folder:  python scripts/01_merge_and_classify.py

The category is made with simple word rules. It is a first pass only.
Every Medium and Low confidence trial must be checked by hand (see docs/coding_protocol.md).
"""
import re
from pathlib import Path
import pandas as pd

RAW = Path("data/raw")
OUT = Path("data/processed")
OUT.mkdir(parents=True, exist_ok=True)

# 1. Read both downloads and remove duplicates by NCT number
a = pd.read_csv(RAW / "studies_search1.csv")
b = pd.read_csv(RAW / "studies_search2_wide.csv")
a["Batch"] = "Search 1"
new = b[~b["NCT Number"].isin(a["NCT Number"])].copy()
new["Batch"] = "Search 2 (wider terms)"
df = pd.concat([a, new], ignore_index=True)
print("Search 1:", len(a), "| Search 2 total:", len(b), "| new from search 2:", len(new), "| merged:", len(df))


def join_text(columns):
    return df[columns].fillna("").agg(" ".join, axis=1).str.lower()


# 2. Text used for the word rules (acronym is left out on purpose, it caused a false match)
core = join_text(["Study Title", "Interventions"])
full = join_text(["Study Title", "Brief Summary", "Interventions", "Primary Outcome Measures",
                  "Secondary Outcome Measures", "Study Design", "Conditions"])

EDIT_WORDS = (r"crispr|cas9|cas12|cas13|gene[- ]edit|genome[- ]edit|base[- ]edit|prime[- ]edit|"
              r"\btalens?\b|zinc[- ]finger|\bzfns?\b|knock[- ]?out|knocked[- ]out|gene disruption|"
              r"\w+ko\b|\bko\b|nuclease|arcus|edited|epigenome editing")
# Product codes of known gene editing products. These are matched by name only, so they need checking.
PRODUCT_CODES = (r"cs-101|cs-121|ntla-\d+|ctx\d{3}|verve-\d+|edit-\d+|exa-cel|nula-cel|kl003|bd11\d|ebt-101|"
                 r"vor33|cd33ko|γ-globin reactivated|regv131|vctx21\d|stx-1150|yolt-\d+|abo-101|pbgene|"
                 r"sb-318|sb-913|sb-fix|sb-728|ecur-506|zvs203e|gen6050x|beam-101|brl-101|et-01|ct125a|"
                 r"tt52car19|ucart\w*|beam-\d+|allo-501a|thiscart19a|lnp\.ucd\.abe|gc203")
THERAPY_TYPES = {"BIOLOGICAL", "GENETIC", "DRUG", "COMBINATION_PRODUCT"}

types = df["Interventions"].fillna("").apply(
    lambda s: {i.split(":")[0].strip() for i in s.split("|") if ":" in i})
summary_start = df["Brief Summary"].fillna("").str.lower().str[:300]

categories, confidence, reason = [], [], []
for i in range(len(df)):
    edit_core = bool(re.search(EDIT_WORDS, core[i]))
    edit_any = bool(re.search(EDIT_WORDS, full[i]))
    code = bool(re.search(PRODUCT_CODES, full[i]))
    t = types[i]
    gives_therapy = bool(t & THERAPY_TYPES)
    only_diagnostic = ("DIAGNOSTIC_TEST" in t) and not gives_therapy
    crispr_test = bool(re.search(r"crispr|cas12|cas13|cas9", full[i])) and bool(
        re.search(r"detect|diagnos|test|screening|identification|assay|point-of-care|biomarker|liquid biopsy",
                  core[i] + summary_start[i]))
    if re.search(r"non[- ]gene[- ]edit", full[i]):
        c, cf, w = "Not gene editing or unclear", "Medium", "text says non gene edited"
    elif only_diagnostic and edit_any:
        c, cf, w = "CRISPR used in diagnostics", "Medium", "diagnostic test and CRISPR words"
    elif gives_therapy and edit_core:
        c, cf, w = "Therapeutic gene editing", "High", "editing word in title or interventions"
    elif gives_therapy and code:
        c, cf, w = "Therapeutic gene editing", "Medium", "known product code only, verify"
    elif gives_therapy and edit_any:
        c, cf, w = "Therapeutic gene editing", "Low", "editing word only in summary or outcomes"
    elif (not gives_therapy) and (edit_core or code):
        c, cf, w = "Follow-up or non-interventional (gene editing linked)", "Medium", "no drug or cell given, editing word or code in title"
    elif (not gives_therapy) and edit_any and crispr_test:
        c, cf, w = "CRISPR used in diagnostics", "Low", "CRISPR words and test words"
    elif edit_any:
        c, cf, w = "Research use or unclear", "Low", "editing words in text only"
    else:
        c, cf, w = "Not gene editing or unclear", "Low", "no editing words found"
    categories.append(c); confidence.append(cf); reason.append(w)

df["Auto Category"], df["Confidence"], df["Why (auto)"] = categories, confidence, reason


# 3. Tidy columns used later
def countries(x):
    if pd.isna(x):
        return ""
    return "; ".join(sorted({p.split(",")[-1].strip() for p in x.split("|") if p.strip()}))


def phase_label(x):
    if pd.isna(x):
        return "Not listed"
    names = {"EARLY_PHASE1": "Early phase 1", "PHASE1": "Phase 1", "PHASE2": "Phase 2", "PHASE3": "Phase 3"}
    p = [names.get(i, i) for i in x.split("|")]
    return {"Phase 1/Phase 2": "Phase 1/2", "Phase 2/Phase 3": "Phase 2/3"}.get("/".join(p), " / ".join(p))


df["Countries"] = df["Locations"].apply(countries)
df["Phase label"] = df["Phases"].apply(phase_label)
df["Start year"] = pd.to_datetime(df["Start Date"], errors="coerce").dt.year
df["Children included"] = df["Age"].fillna("").str.contains("CHILD").map({True: "Yes", False: "No"})

keep = ["NCT Number", "Study Title", "Study URL", "Study Status", "Phase label", "Start year", "Sponsor",
        "Funder Type", "Enrollment", "Age", "Conditions", "Interventions", "Countries", "Study Type",
        "Last Update Posted", "Auto Category", "Confidence", "Why (auto)", "Children included", "Batch"]
df[keep].to_csv(OUT / "trials_classified.csv", index=False)

# 4. List of trials that need a manual check
queue = df[df["Confidence"].isin(["Low", "Medium"])][
    ["NCT Number", "Study Title", "Study URL", "Auto Category", "Confidence", "Why (auto)"]]
queue.sort_values(["Confidence", "Auto Category"], ascending=[True, True]).to_csv(
    Path("docs") / "review_queue.csv", index=False)
print(df["Auto Category"].value_counts().to_string())
print("Trials to check by hand:", len(queue))
