# Public Reporting Transparency in Human Gene-Editing Clinical Trials: A Systematic Registry Analysis of Consent, Ethics Oversight, and Long-Term Follow-Up

**Author:** Sara Shahid Abbas  
**Affiliation:** Lahore, Pakistan  

---

## Abstract

**Background:** Human somatic gene-editing technologies—including CRISPR-Cas9, base editing, prime editing, and RNA-targeting Cas13 systems—have rapidly transitioned into clinical trials. Because genome editing carries irreversible biological risks such as off-target mutagenesis and delayed oncogenesis, international bodies emphasize rigorous informed consent, independent ethics review, and extended long-term follow-up (LTFU). However, public clinical trial registries vary in how transparently these governance safeguards are reported.  
**Methods:** We extracted 314 unique records from ClinicalTrials.gov (up to November 2026) and applied a two-stage automated and manual verification protocol to isolate interventional therapeutic human gene-editing trials from diagnostic, observational, and non-edited control studies. Each verified therapeutic protocol was coded for disease category, informed consent and minor assent disclosures, Institutional Review Board (IRB)/ethics committee reporting, off-target safety monitoring, and LTFU duration (benchmarked against the 15-year FDA/EMA standard). Registry findings were evaluated against the WHO Human Genome Editing Governance Framework and national regulatory systems in Pakistan, Spain (EU), and the United Kingdom.  
**Results:** Out of 314 deduplicated registry records, **199 (63.4%)** were verified as interventional therapeutic human gene-editing trials, alongside **69 (22.0%)** non-gene-editing or comparator records, **20 (6.4%)** CRISPR diagnostic studies, **14 (4.5%)** research/biobank cohorts, and **12 (3.8%)** standalone gene-editing-linked follow-up protocols. Therapeutic trials remain concentrated in early clinical phases (Phase 1 and Phase 1/2) and focus predominantly on oncology and inherited hemoglobinopathies, alongside emerging *in vivo* base and prime editing trials for metabolic, cardiovascular, and ophthalmic disorders. While informed consent is frequently referenced in eligibility criteria, granular details regarding minor assent, IRB/ethics committee approval, and off-target sequencing plans are frequently omitted from public narrative fields, and 15-year LTFU commitments are fragmented between primary trial descriptions and separate rollover registry records.  
**Conclusions:** Public registry entries prioritize clinical eligibility and dosing over ethical and post-trial governance transparency. Standardized registry fields—specifically mandatory linkage between parent gene-editing trials and rollover LTFU studies, structured ethics approval metadata, and explicit off-target monitoring disclosures—are needed to align clinical trial registries with WHO governance recommendations.

---

## 1. Introduction

Clinical genome editing has expanded beyond first-generation *ex vivo* nuclease therapies into *in vivo* lipid nanoparticle (LNP) and adeno-associated virus (AAV) platforms utilizing base editors, prime editors, and RNA-targeting nucleases. While these modalities offer potentially curative interventions for monogenic disorders and refractory cancers, they introduce distinct ethical and governance challenges. Unlike conventional small-molecule drugs, permanent genomic alterations cannot be discontinued once administered, requiring robust participant comprehension during informed consent, stringent independent ethics oversight, and multi-year post-trial surveillance.

In 2021, the World Health Organization (WHO) Expert Advisory Committee on Developing Global Standards for Governance and Oversight of Human Genome Editing published its Governance Framework and Recommendations. A central pillar of the WHO framework is **registry transparency**: clinical trials involving human genome editing should be publicly registered with clear, accessible information regarding ethical review, informed consent processes, risk-mitigation strategies, and long-term follow-up plans.

This study evaluates public reporting transparency across **314** gene-editing-related clinical trial records registered on ClinicalTrials.gov and contextualizes registry practices within comparative national governance regimes across **Pakistan**, **Spain (European Union)**, and the **United Kingdom**.

---

## 2. Methods

We retrieved clinical trial records from ClinicalTrials.gov up to **11 November 2026** using two complementary search queries (`studies_search1.csv` and `studies_search2_wide.csv`) and merged them by unique National Clinical Trial (`NCT`) identifier, yielding **314 unique records**. Using a standardized coding protocol (`docs/coding_protocol.md`), each record was classified into five mutually exclusive categories and evaluated for disease area, clinical phase, funder type, pediatric inclusion, informed consent and minor assent disclosures, IRB/ethics committee mentions, off-target safety monitoring, and long-term follow-up (LTFU) duration.

---

## 3. Results

### 3.1 Overall Trial Screening and Classification (N = 314)
Across all **314** unique ClinicalTrials.gov records, **199 (63.4%)** met the criteria for interventional human therapeutic gene editing. The remaining **115 (36.6%)** records comprised **69 (22.0%)** non-gene-editing or comparator studies (such as non-gene-edited allogeneic CAR-T products, unmodified stem cell transplants, and dietary/surgical controls), **20 (6.4%)** CRISPR-based diagnostic assays, **14 (4.5%)** observational biobank or *in vitro* iPSC modeling studies, and **12 (3.8%)** standalone non-interventional follow-up rollover protocols linked to prior gene-editing treatments.

#### Table 1: Overall Classification of Deduplicated Registry Records (N = 314)

| Trial Category | Count (n) | Share (%) | Key Examples in Dataset |
| :--- | :---: | :---: | :--- |
| **Therapeutic gene editing** | **199** | **63.4%** | `NCT06328764` (CS-101), `NCT06128629` (NTLA-2001), `NCT05397184` (BE-CAR7), `NCT06559176` (PM359), `NCT04637763` (CB-010) |
| **Not gene editing or unclear** | **69** | **22.0%** | `NCT04652310` (femur nail), `NCT07142759` (tomato soup), `NCT04934774` & `NCT05640713` (non-edited CAR-T) |
| **CRISPR used in diagnostics** | **20** | **6.4%** | `NCT04074369` (TB assay), `NCT07870265` (BRAF V600E Cas12a), `NCT07580001` (NuRapid-CRISPR Sepsis), `NCT07399873` (STI CRISPR) |
| **Research use / Biobank / Observational** | **14** | **4.5%** | `NCT03612310` (iPSC modeling), `NCT07396285` (UCSF Genome Surgery Biobank), `NCT04671212` (discarded bone marrow) |
| **Follow-up or non-interventional (gene-editing linked)** | **12** | **3.8%** | `NCT06685536` & `NCT06717932` (CS-101 LTFU), `NCT06208878` (CRISPR CAR-T LTFU), `NCT06363760` (EDIT-301 LTFU), `NCT06112327` (Verve LTFU) |
| **Total Deduplicated Records** | **314** | **100.0%** | — |

---

### 3.2 Clinical Landscape and Governance Transparency Findings
Within the **199** therapeutic gene-editing trials:
1. **Early-Phase & Geographic Concentration:** Trials are heavily concentrated in Early Phase 1, Phase 1, and Phase 1/2 testing, led geographically by the **United States** and **China**, with smaller active trial footprints in the **United Kingdom** and **Spain**, and **0% (0/199)** active study sites in **Pakistan**.
2. **Therapeutic Focus:** Oncology (allogeneic CRISPR CAR-T and checkpoint-knockout TIL/T-cell therapies) and inherited hemoglobinopathies (sickle cell disease and β-thalassemia via *BCL11A* enhancer editing) represent the largest clinical areas, followed by *in vivo* base-editing, prime-editing, and Cas13 RNA-editing trials for metabolic, cardiovascular, infectious, ophthalmic, and neuromuscular disorders.
3. **Fragmented 15-Year Long-Term Follow-Up (LTFU):** At least **12** standalone observational rollover trials (`NCT06685536`, `NCT06717932`, `NCT06208878`, `NCT06363760`, `NCT06112327`, `NCT05377307`, among others) and multiple interventional LTFU studies (`NCT04208529`, `NCT05143307`, `NCT06479616`) were registered separately from their parent treatment trials to satisfy 15-year safety surveillance mandates, without relational NCT links in the registry schema.
4. **Consent, IRB, and Off-Target Reporting Gaps:** While basic informed consent eligibility criteria appear in roughly three-quarters of therapeutic records, pediatric minor assent rules, explicit narrative mentions of IRB/Ethics Committee approval, and off-target genome-editing safety assays (such as GUIDE-seq, CHANGE-seq, or longitudinal whole-genome sequencing) are omitted from the majority of public protocol descriptions.

---

## 4. Comparative Regulatory & Governance Frameworks

| Governance Dimension | WHO Framework (2021) | United Kingdom (MHRA / HRA) | Spain / European Union (AEMPS / EMA) | Pakistan (DRAP / NBC) |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Regulatory Instruments** | WHO Governance Framework & Recommendations on Human Genome Editing (2021) | Medicines for Human Use (Clinical Trials) Regulations; UK GDPR; GTAC legacy guidance | EU Clinical Trials Regulation (CTR 536/2014); EU GMO Directives (2001/18/EC & 2009/41/EC); EMA ATMP Guidelines | Drug Regulatory Authority of Pakistan (DRAP) Act 2012; Clinical Trial Rules 2017; National Bioethics Committee (NBC) Guidelines |
| **Ethics & Scientific Review** | Dual review: specialized scientific oversight + independent research ethics committee | Integrated review via MHRA + Health Research Authority (HRA) Research Ethics Committee (REC) | Coordinated EU CTIS assessment (Part I scientific by AEMPS; Part II ethical by CEIm) + GMO environmental risk assessment | Dual mandatory clearance: Institutional Review Board (IRB) + National Bioethics Committee (NBC) + DRAP Clinical Studies Committee (CSC) |
