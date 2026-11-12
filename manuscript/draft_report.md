# Public Reporting Transparency in Human Gene-Editing Clinical Trials: A Systematic Registry Analysis of Consent, Ethics Oversight, and Long-Term Follow-Up

**Author:** Sara Shahid Abbas  
**Affiliation:** Lahore, Pakistan  

---

## Abstract

**Background:** Human somatic gene-editing technologies—including CRISPR-Cas9, base editing, prime editing, and RNA-targeting Cas13 systems—have rapidly transitioned into clinical trials. Because genome editing carries irreversible biological risks such as off-target mutagenesis and delayed oncogenesis, international bodies emphasize rigorous informed consent, independent ethics review, and extended long-term follow-up (LTFU). However, public clinical trial registries vary in how transparently these governance safeguards are reported.  
**Methods:** We extracted 314 unique records from ClinicalTrials.gov (up to November 2026) and applied a two-stage automated and manual verification protocol to isolate interventional therapeutic human gene-editing trials from diagnostic, observational, and non-edited control studies. Each verified therapeutic protocol was coded for disease category, informed consent and minor assent disclosures, Institutional Review Board (IRB)/ethics committee reporting, off-target safety monitoring, and LTFU duration (benchmarked against the 15-year FDA/EMA standard). Registry findings were evaluated against the WHO Human Genome Editing Governance Framework and national regulatory systems in Pakistan, Spain (EU), and the United Kingdom.  
**Results:** Most therapeutic gene-editing trials remain concentrated in early clinical phases (Phase 1 and Phase 1/2) and focus predominantly on oncology (hematologic malignancies and solid tumors) and inherited hemoglobinopathies (sickle cell disease and β-thalassemia), alongside emerging *in vivo* base and prime editing trials for metabolic, cardiovascular, and ophthalmic disorders. While informed consent is frequently referenced in eligibility criteria, granular details regarding minor assent, IRB/ethics committee approval, and off-target sequencing plans are frequently omitted from public narrative fields. Furthermore, 15-year LTFU requirements are fragmented between integrated protocol descriptions and standalone rollover registry records, creating traceability gaps.  
**Conclusions:** Public registry entries prioritize clinical eligibility and dosing over ethical and post-trial governance transparency. Standardized registry fields—specifically mandatory linkage between parent gene-editing trials and rollover LTFU studies, structured ethics approval metadata, and explicit off-target monitoring disclosures—are needed to align clinical trial registries with WHO governance recommendations.

---

## 1. Introduction

Clinical genome editing has expanded beyond first-generation *ex vivo* nuclease therapies into *in vivo* lipid nanoparticle (LNP) and adeno-associated virus (AAV) platforms utilizing base editors, prime editors, and RNA-targeting nucleases. While these modalities offer potentially curative interventions for monogenic disorders and refractory cancers, they introduce distinct ethical and governance challenges. Unlike conventional small-molecule drugs, permanent genomic alterations cannot be discontinued once administered, requiring robust participant comprehension during informed consent, stringent independent ethics oversight, and multi-year post-trial surveillance.

In 2021, the World Health Organization (WHO) Expert Advisory Committee on Developing Global Standards for Governance and Oversight of Human Genome Editing published its Governance Framework and Recommendations. A central pillar of the WHO framework is **registry transparency**: clinical trials involving human genome editing should be publicly registered with clear, accessible information regarding ethical review, informed consent processes, risk-mitigation strategies, and long-term follow-up plans.

This study evaluates public reporting transparency across gene-editing clinical trials registered on ClinicalTrials.gov and contextualizes registry practices within comparative national governance regimes across **Pakistan**, **Spain (European Union)**, and the **United Kingdom**.

---

## 2. Comparative Regulatory & Governance Frameworks

To interpret public registry disclosures in an international context, we examined how global guidance and three distinct national regulatory environments govern gene-editing clinical research:

| Governance Dimension | WHO Framework (2021) | United Kingdom (MHRA / HRA) | Spain / European Union (AEMPS / EMA) | Pakistan (DRAP / NBC) |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Regulatory Instruments** | WHO Governance Framework & Recommendations on Human Genome Editing (2021) | Medicines for Human Use (Clinical Trials) Regulations; UK GDPR; GTAC legacy guidance | EU Clinical Trials Regulation (CTR 536/2014); EU GMO Directives (2001/18/EC & 2009/41/EC); EMA ATMP Guidelines | Drug Regulatory Authority of Pakistan (DRAP) Act 2012; Clinical Trial Rules 2017; National Bioethics Committee (NBC) Guidelines |
| **Ethics & Scientific Review** | Dual review: specialized scientific oversight + independent research ethics committee | Integrated review via MHRA + Health Research Authority (HRA) Research Ethics Committee (REC) | Coordinated EU CTIS assessment (Part I scientific by AEMPS; Part II ethical by CEIm) + GMO environmental risk assessment | Dual mandatory clearance: Institutional Review Board (IRB) + National Bioethics Committee (NBC) + DRAP Clinical Studies Committee (CSC) |
| **Informed Consent & Assent** | Emphasizes plain-language communication of irreversible risks, uncertainty, and LTFU commitment | Statutory written informed consent; strict pediatric assent and parental responsibility rules | Mandatory written consent under EU CTR; specific protections for minors and incapacitated adults | Written informed consent in English and Urdu/local languages; mandatory parental consent + minor assent |
| **Long-Term Follow-Up (LTFU)** | Calls for systematic long-term health surveillance and international registry linkage | Follows EMA/ICH principles (up to 15 years for integrating/gene-editing vectors) | EMA Guideline on Follow-up of Patients Administered with Gene Therapy Medicinal Products (up to 15 years) | Governed case-by-case under DRAP pharmacovigilance rules; no dedicated statutory 15-year gene-editing LTFU guideline yet |
| **Public Registry Mandate** | Mandatory prospective registration in WHO ICTRP primary registries with transparent protocol fields | Mandatory registration in public registry (ISRCTN / ClinicalTrials.gov) and HRA research summaries | Mandatory public disclosure via EU Clinical Trials Information System (CTIS) with transparency rules | Mandatory registration with DRAP Clinical Trial Registry and WHO-recognized public registries |

### Key Comparative Insights
1. **Absence of Clinical Sites in Pakistan:** While no registered therapeutic gene-editing clinical trials currently list active study sites in Pakistan, hereditary hemoglobinopathies (particularly β-thalassemia) represent a major public health burden in the country. Strengthening DRAP and NBC regulatory guidance on Advanced Therapy Medicinal Products (ATMPs) and 15-year LTFU infrastructure is essential before clinical trials expand into South Asia.
2. **EU/Spain Dual ATMP and GMO Oversight:** Trials conducted in Spain and across the EU face stringent dual oversight under Regulation (EU) 536/2014 and GMO deliberate-release rules, resulting in standardized public disclosures within CTIS that are not always mirrored when sponsors cross-register abbreviated records on ClinicalTrials.gov.
3. **UK Centralized Ethical Transparency:** The UK Health Research Authority (HRA) publishes plain-language research summaries and REC approval statuses publicly, compensating for ClinicalTrials.gov narrative fields that frequently omit ethics committee details.

---

## 3. Discussion & Policy Recommendations

### 3.1 Explaining "Not Stated" Findings in Public Registries
A critical methodological finding of this audit is that **"Not stated" in ClinicalTrials.gov does not equate to unethical conduct**. ClinicalTrials.gov XML/JSON schemas store board approval metadata separately from narrative text fields (`briefSummary`, `detailedDescription`, and `eligibilityCriteria`). However, because patients, clinicians, and bioethicists rely on public narrative records to evaluate trial safety and governance, omitting IRB details, off-target assay methodologies, and LTFU durations creates an avoidable transparency deficit.

### 3.2 Structural Fragmentation of 15-Year Follow-Up
Regulatory agencies (FDA and EMA) mandate up to 15 years of safety monitoring for genome-editing interventions to detect delayed insertional mutagenesis or clonal expansion. In our registry audit, sponsors operationalize this requirement in two ways:
* **Integrated LTFU Protocols:** Stating the 15-year follow-up commitment directly within the primary interventional trial record.
* **Standalone Rollover Studies:** Registering a separate observational LTFU study (e.g., rollover protocols for `CS-101`, `exa-cel/CTX001`, `EDIT-301`, `EBT-101`, and `PBGENE-HBV`) that participants enter after completing the 1- to 2-year primary trial.

Without standardized relational linking between parent NCT numbers and rollover LTFU NCT numbers, external auditors and patients cannot easily verify whether a given phase 1/2 trial fulfills long-term safety tracking.

### 3.3 Actionable Recommendations for Registry Governance
1. **Mandatory Parent–Rollover NCT Linkage:** ClinicalTrials.gov and WHO ICTRP should implement a structured relational field linking interventional gene-editing trials directly to their corresponding 15-year LTFU rollover studies.
