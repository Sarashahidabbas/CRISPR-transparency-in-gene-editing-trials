# Coding Protocol for Gene-Editing Clinical Trial Transparency

**Author:** Sara Shahid Abbas  
**Last Updated:** November 2026  

---

## 1. Purpose
This document defines the standardized classification and governance coding rules applied to all 314 ClinicalTrials.gov records in this study. Both automated Python scripts and independent human coders must follow these exact definitions.

---

## 2. Step 1: Trial Classification (`refined_category`)
Assign each NCT record to exactly **one** of the following five categories:

1. **Therapeutic gene editing:** Interventional trials where human participants receive an *ex vivo* genetically edited cell product (e.g., CRISPR CAR-T, base-edited CD34+ HSPCs) or an *in vivo* gene-editing drug (e.g., LNP-CRISPR, AAV-base/prime editor, ZFN, TALEN, ARCUS).
2. **Follow-up (gene-editing linked):** Non-interventional, observational rollover studies designed specifically to monitor long-term safety (typically up to 15 years) in participants who previously received a gene-editing therapy in a parent trial.
3. **CRISPR used in diagnostics:** Studies using CRISPR/Cas systems (e.g., Cas12a, Cas13) strictly on biological samples (blood, sputum, swabs) to detect pathogens or tumor DNA without administering edited therapies to patients.
4. **Preclinical / Observational / Biobank:** Studies collecting human tissue, blood, or urine to generate *in vitro* iPSCs, organoids, or animal models using CRISPR, without treating human participants.
5. **Not gene editing or unclear:** Non-edited cell therapies (e.g., standard lentiviral CAR-T without targeted nuclease editing), nutritional/surgical trials, or records lacking sufficient detail to confirm genome editing.

---

## 3. Step 2: Disease Area Grouping (`disease_area`)
Classify every **Therapeutic gene editing** trial into one of seven clinical categories:
* **Oncology (Hematologic & Solid Tumors):** Leukemia, lymphoma, multiple myeloma, solid tumors, glioblastoma, melanoma.
* **Hematologic & Coagulation Disorders:** Sickle cell disease, β-thalassemia, hemophilia A/B.
* **Metabolic, Cardiovascular & Rare Monogenic:** Hypercholesterolemia, ATTR amyloidosis, hereditary angioedema (HAE), primary hyperoxaluria (PH1), Wilson disease, urea cycle disorders, PKU, GSDIa, MPS I/II, AATD.
* **Infectious Diseases:** HIV-1, chronic hepatitis B (HBV), herpes simplex keratitis (HSV-1), HPV-related cervical neoplasia, COVID-19.
* **Ophthalmic Disorders:** Retinitis pigmentosa, Stargardt disease, Leber congenital amaurosis (LCA10), age-related macular degeneration (AMD), glaucoma, corneal dystrophy.
* **Primary Immunodeficiencies & Autoimmune:** X-SCID, chronic granulomatous disease (CGD), WHIM syndrome, Hyper-IgM syndrome, systemic lupus erythematosus (SLE), systemic sclerosis, ITP, wAIHA.
* **Neuromuscular & Neurodevelopmental:** Duchenne muscular dystrophy (DMD), limb-girdle muscular dystrophy (LGMD), Rett syndrome, OTOF hearing loss.

---

## 4. Step 3: Ethics & Governance Transparency Coding

### 4.1 Informed Consent Reporting (`consent_reporting`)
* **Explicit (Consent + Minor Assent/Guardian):** Record mentions both written informed consent and pediatric minor assent or parent/legally authorized representative (LAR) consent.
* **Explicit (Informed Consent Mentioned):** Record explicitly states informed consent is required, without mentioning minor assent or guardian rules.
* **Not stated in public text:** No mention of informed consent in the public summary, description, or eligibility fields.

### 4.2 Ethics Committee / IRB Approval (`ethics_irb_reporting`)
* **Explicitly stated in record:** Narrative text explicitly mentions Institutional Review Board (IRB), Ethics Committee, or human ethics approval.
* **Not stated in public text:** Board approval is not mentioned in the narrative fields (Note: reflects public narrative reporting, not whether approval occurred).

### 4.3 Long-Term Follow-Up (`ltfu_reporting`)
* **15-year LTFU stated (FDA/EMA standard):** Explicitly specifies 15 years of post-treatment follow-up (either within the main protocol or via mandatory enrollment in a 15-year LTFU rollover study).
* **Stated ([X] years/months):** Specifies a defined follow-up duration shorter than 15 years (e.g., 2 years, 5 years, 10 years).
* **Stated (Duration unspecified):** Mentions long-term follow-up without stating the exact number of years.
* **Not stated in public text:** No long-term follow-up commitment is described in the public record.

### 4.4 Off-Target Safety Monitoring (`off_target_monitoring`)
* **Yes:** Explicitly mentions evaluating off-target editing, unintended edits, GUIDE-seq, CHANGE-seq, or longitudinal whole-genome sequencing (WGS) for editing specificity.
* **Not stated:** Off-target monitoring is not mentioned in the public protocol text.
