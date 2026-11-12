import json
import re
import pandas as pd
from pathlib import Path

# File path set to your main folder where you uploaded the JSON file
RAW_JSON_PATH = Path("studies.ClinicalTrials.Transparency.json")
OUTPUT_CODING_CSV = Path("data/processed/trials_ethics_coded.csv")
OUTPUT_SUMMARY_DIR = Path("results/tables")
OUTPUT_SUMMARY_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_CODING_CSV.parent.mkdir(parents=True, exist_ok=True)

def load_trials(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("studies", [])

def classify_intervention(text):
    """Refines classification based on the project's working definition."""
    t = text.lower()
    
    # Exclude non-gene-editing controls or unrelated studies
    if any(k in t for k in [
        "without genetic modification", "non-gene edited", "genetic-modification-free",
        "intramedullary nail", "inguinal hernia", "tomato soup", "barley", "prehabilitation"
    ]):
        return "Not gene editing or unclear"
    
    # Diagnostics
    if any(k in t for k in ["diagnostic", "detection", "point-of-care", "assay", "screening", "ctdna", "cfdna"]) and not any(k in t for k in ["infusion", "injection", "transplantation"]):
        return "CRISPR used in diagnostics"
    
    # Long-term follow-up (non-interventional rollover)
    if "long-term follow-up" in t or "ltfu" in t:
        if any(k in t for k in ["no investigational drug", "no study drug", "non-interventional", "will not be administered"]):
            return "Follow-up (gene-editing linked)"
            
    # Therapeutic gene editing (in vivo & ex vivo)
    editing_tools = [
        "crispr", "cas9", "cas12", "cas13", "base editing", "base-edited",
        "prime editing", "zinc finger", "zfn", "talen", "arcus",
        "gene editing", "gene-edited", "genome editing"
    ]
    if any(tool in t for tool in editing_tools):
        if any(model in t for model in ["ipsc", "organoid", "in vitro", "biobank", "observational", "discarded bone marrow"]):
            return "Preclinical / Observational / Biobank"
        return "Therapeutic gene editing"
        
    return "Not gene editing or unclear"

def categorize_disease(text):
    """Maps trial text into standardized clinical disease areas."""
    t = text.lower()
    if any(k in t for k in ["thalassemia", "sickle cell", "hemoglobin", "hemophilia", "factor ix"]):
        return "Hematologic & Coagulation Disorders"
    if any(k in t for k in ["leukemia", "lymphoma", "myeloma", "car-t", "car t", "car-nk", "til", "tumor", "cancer", "carcinoma", "glioma", "melanoma", "glioblastoma", "astrocytoma"]):
        return "Oncology (Hematologic & Solid Tumors)"
    if any(k in t for k in ["hiv", "hepatitis", "hbv", "herpes", "hsv", "covid", "sars-cov-2", "tuberculosis", "enterovirus", "bordetella", "malaria", "norovirus"]):
        return "Infectious Diseases"
    if any(k in t for k in ["retinitis pigmentosa", "stargardt", "macular degeneration", "lca10", "corneal", "glaucoma", "keratitis"]):
        return "Ophthalmic Disorders"
    if any(k in t for k in ["hypercholesterolemia", "hyperlipidemia", "dyslipidemia", "amyloidosis", "attr", "angioedema", "hae", "hyperoxaluria", "wilson disease", "urea cycle", "otc deficiency", "pku", "gsdia", "mps i", "mps ii", "alpha-1 antitrypsin", "aatd", "hypertension", "diabetes"]):
        return "Metabolic, Cardiovascular & Rare Monogenic"
    if any(k in t for k in ["lupus", "sle", "sclerosis", "myopathy", "autoimmune", "immunodeficiency", "xscid", "cgd", "granulomatous", "whim", "hyperigm"]):
        return "Primary Immunodeficiencies & Autoimmune"
    if any(k in t for k in ["duchenne", "dmd", "muscular dystrophy", "rett syndrome", "chd3", "hearing loss", "otof"]):
        return "Neuromuscular & Neurodevelopmental"
    return "Other / Unclassified"

def extract_governance_metrics(study):
    """Extracts transparency indicators for Consent, Ethics/IRB, and Follow-up."""
    proto = study.get("protocolSection", {})
    ident = proto.get("identificationModule", {})
    desc = proto.get("descriptionModule", {})
    arms = proto.get("armsInterventionsModule", {})
    elig = proto.get("eligibilityModule", {})

    nct_id = ident.get("nctId", "")
    title = ident.get("briefTitle", "")
    summary = desc.get("briefSummary", "")
    detailed = desc.get("detailedDescription", "")
    criteria = elig.get("eligibilityCriteria", "")
    
    interventions = " ".join([i.get("description", "") for i in arms.get("interventions", [])])
    full_text = f"{title} {summary} {detailed} {interventions} {criteria}"
    t_lower = full_text.lower()

    # 1. Trial Category & Disease Area
    category = classify_intervention(full_text)
    disease_area = categorize_disease(f"{title} {summary} {detailed}")

    # 2. Informed Consent & Assent Transparency
    has_consent = "informed consent" in t_lower or "icf" in t_lower
    has_assent_guardian = any(k in t_lower for k in ["assent", "legal guardian", "legally authorized representative", "parent"])
    if has_consent and has_assent_guardian:
        consent_status = "Explicit (Consent + Minor Assent/Guardian)"
    elif has_consent:
        consent_status = "Explicit (Informed Consent Mentioned)"
    else:
        consent_status = "Not stated in public text"

    # 3. Ethics Committee / IRB Approval Transparency
    if any(k in t_lower for k in ["institutional review board", "irb", "ethics committee", "ethical requirements", "human ethics"]):
        ethics_status = "Explicitly stated in record"
    else:
        ethics_status = "Not stated in public text"

    # 4. Long-Term Follow-Up (LTFU) Transparency
    ltfu_match = re.search(r"(\d+)[\s-]*(year|month|week)s?\s*(long-term|follow-up|followup|ltfu|post-infusion|post-transplant)", t_lower)
    if "15 year" in t_lower or "15-year" in t_lower:
        ltfu_status = "15-year LTFU stated (FDA/EMA standard)"
    elif ltfu_match:
        ltfu_status = f"Stated ({ltfu_match.group(1)} {ltfu_match.group(2)}s)"
    elif "long-term follow" in t_lower or "ltfu" in t_lower:
        ltfu_status = "Stated (Duration unspecified)"
    else:
        ltfu_status = "Not stated in public text"

    # 5. Off-Target & Safety Monitoring Mentions
    off_target_stated = "Yes" if any(k in t_lower for k in ["off-target", "off target", "unintended edit", "whole genome sequencing", "guide-seq", "change-seq"]) else "Not stated"

    return {
        "nct_id": nct_id,
        "brief_title": title,
        "refined_category": category,
        "disease_area": disease_area,
        "consent_reporting": consent_status,
        "ethics_irb_reporting": ethics_status,
        "ltfu_reporting": ltfu_status,
        "off_target_monitoring": off_target_stated
    }

def main():
    studies = load_trials(RAW_JSON_PATH)
    records = [extract_governance_metrics(s) for s in studies]
    df = pd.DataFrame(records)
    df.to_csv(OUTPUT_CODING_CSV, index=False)

    # Generate summary tables for Therapeutic Gene Editing trials
    tx_df = df[df["refined_category"] == "Therapeutic gene editing"]
    
    tx_df["disease_area"].value_counts().to_csv(OUTPUT_SUMMARY_DIR / "therapeutic_by_disease_area.csv")
    tx_df["consent_reporting"].value_counts().to_csv(OUTPUT_SUMMARY_DIR / "therapeutic_consent_transparency.csv")
    tx_df["ethics_irb_reporting"].value_counts().to_csv(OUTPUT_SUMMARY_DIR / "therapeutic_ethics_irb_transparency.csv")
    tx_df["ltfu_reporting"].value_counts().to_csv(OUTPUT_SUMMARY_DIR / "therapeutic_ltfu_transparency.csv")
    
    print(f"Processed {len(df)} total records. Identified {len(tx_df)} therapeutic gene-editing trials.")

if __name__ == "__main__":
    main()
