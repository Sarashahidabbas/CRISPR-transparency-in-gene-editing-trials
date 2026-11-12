# Open Science Framework (OSF) Study Protocol Pre-Registration

**Title:** Public Reporting Transparency in Human Gene-Editing Clinical Trials: A Systematic Registry Analysis of Consent, Ethics Oversight, and Long-Term Follow-Up  
**Principal Investigator:** Sara Shahid Abbas (Lahore, Pakistan)  
**Date of Protocol Registration:** November 2026  

---

## 1. Study Information
### 1.1 Research Questions
1. How are registered human gene-editing clinical trials distributed across countries, clinical phases, disease areas, and sponsor types?
2. To what extent do public ClinicalTrials.gov records transparently report:
   * Informed consent and pediatric minor assent requirements;
   * Ethics committee or Institutional Review Board (IRB) approval;
   * Long-term follow-up (LTFU) commitments (benchmarked against the 15-year FDA/EMA standard);
   * Off-target genome-editing safety monitoring?
3. How do public registry disclosures align with the 2021 WHO Human Genome Editing Governance Framework and national regulations in Pakistan, Spain (EU), and the United Kingdom?

### 1.2 Hypotheses
* **H1:** Therapeutic gene-editing clinical trials will be heavily concentrated in early development phases (Phase 1 and Phase 1/2) and geographically clustered in the United States and China, with zero active trial sites in Pakistan.
* **H2:** Public registry narratives will exhibit high reporting rates for basic informed consent eligibility criteria (>70%) but low explicit reporting (<30%) for IRB/ethics committee approval and off-target safety assays.
* **H3:** Long-term follow-up (15 years) will be structurally fragmented between integrated primary protocol descriptions and standalone rollover registry records.

---

## 2. Sampling Plan & Data Source
* **Primary Registry:** ClinicalTrials.gov
* **Search & Download Date:** 11 November 2026
* **Sample Size:** 314 unique registry records retained after deduplication by NCT identifier.
* **Inclusion Criteria:** Interventional clinical trials in which human participants receive an *ex vivo* gene-edited cell product or an *in vivo* gene-editing therapeutic (e.g., CRISPR-Cas9, base editing, prime editing, Cas13, ZFN, TALEN, ARCUS).
* **Exclusion Criteria:** Diagnostic-only CRISPR assays, purely *in vitro* or animal studies, biobanking/observational cohorts without therapeutic editing, and non-gene-edited control arms.

---

## 3. Coding Variables & Reliability Plan
* **Coded Governance Variables:**
  1. `refined_category` (Therapeutic gene editing, Follow-up rollover, Diagnostics, Preclinical/Observational, Not gene editing)
  2. `disease_area` (7 standardized clinical categories)
  3. `consent_reporting` (Explicit with minor assent/guardian, Explicit consent only, Not stated)
  4. `ethics_irb_reporting` (Explicitly stated vs. Not stated in public text)
  5. `ltfu_reporting` (15-year LTFU stated, Other specified duration, Duration unspecified, Not stated)
  6. `off_target_monitoring` (Yes vs. Not stated)
* **Inter-Coder Reliability:** A second independent coder will evaluate a stratified subset of records using `docs/coding_protocol.md`. Agreement will be assessed using percentage agreement and **Cohen's kappa (κ)**, targeting κ ≥ 0.80. Discrepancies will be resolved by consensus.

---

## 4. Analysis Plan
Descriptive frequencies, proportions, and cross-tabulations will be computed in Python (`pandas`, `scikit-learn`) and visualized at 300 DPI (`matplotlib`, `seaborn`). All raw data, scripts, and coding sheets will be openly archived on GitHub and Zenodo.
