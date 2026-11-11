
# Gene Editing Clinical Trials: A Registry Analysis for Ethics and Governance

**Author:** Sara Shahid Abbas  
**Location:** Lahore, Pakistan  
**Project Status:** Work in Progress  
**Results:** Preliminary, pending manual verification

---

## 1. Research Question

How are registered gene-editing clinical trials distributed by country, disease, phase, and funder? What do their registry records reveal about informed consent, ethics approval, and long-term follow-up?

## 2. Background and Research Rationale

Gene-editing clinical trials raise important questions about research ethics, clinical governance, transparency, and accountability.

Countries follow different regulatory frameworks for gene-editing research. Public clinical trial registries offer a useful source for examining where these trials take place and what ethical information researchers report.

This project examines the reporting of informed consent, ethics approval, and participant follow-up in gene-editing trials registered on ClinicalTrials.gov.

Registry records are not designed to report consent or ethics approval in detail. A finding of "Not stated" therefore describes what is visible in the public record, not what happened in the trial. The study measures public reporting transparency, not ethical conduct.

The research also connects with broader discussions on:

- Research ethics and responsible innovation.
- Dual-use research of concern (DURC).
- Health data governance.
- Transparency in clinical research.
- International differences in research regulation.

## 3. Data Sources

**Primary source:** ClinicalTrials.gov  
**Download date:** 11 November 2026  
**Total unique records:** 314, after duplicate removal.

Two searches were conducted to identify relevant clinical trial records. The full search strategy is available in `docs/search_strategy.md`.

The repository includes the original downloads without modification. Processed datasets, classification decisions, and analysis scripts are provided separately.

Please review the ClinicalTrials.gov Terms of Use before reusing registry data: https://clinicaltrials.gov/about-site/terms-conditions

Some registry records may contain third-party copyrighted material.

## 4. Methodology

The project uses a structured approach to identify, classify, and examine gene-editing clinical trial records.

### Working definition

A gene-editing trial is a study in which participants receive an edited cell product or a gene-editing drug. Studies that use CRISPR only in a diagnostic test, or only in the laboratory, are not counted as gene-editing trials. Long-term follow-up studies of gene-edited products are kept as a separate category. This definition was written before the manual coding and will not be changed without a note.

### Step 1: Data Merging and Deduplication

- Combine the two ClinicalTrials.gov downloads.
- Identify duplicate records using NCT numbers.
- Retain 314 unique trial records.

**Script:** `scripts/01_merge_and_classify.py`

### Step 2: Initial Trial Classification

Apply keyword-based rules and a list of product codes to assign preliminary trial categories. The product code list was made by the author and has not yet been verified against sponsor pages or publications.

Each classification receives a confidence level to support later verification.

### Step 3: Manual Verification

Review all medium- and low-confidence classifications against individual trial records.

**Review file:** `docs/review_queue.csv`

### Step 4: Ethics and Consent Coding

Examine individual registry records and record information about:

- Informed consent.
- Ethics committee or institutional review board approval.
- Participant follow-up.
- Long-term follow-up information.

The coding process follows the protocol in `docs/coding_protocol.md`.

### Step 5: Data Analysis and Visualisation

Generate descriptive summary tables and figures using Python, by category, status, phase, funder, start year, and country.

**Script:** `scripts/02_summary_and_figures.py`

## 5. Preliminary Classification Results

The initial automated classification sorted the 314 unique records into the categories below.

| Trial Category | Number of Trials |
|---|---:|
| Therapeutic gene editing | 199 |
| Follow-up or non-interventional, gene-editing linked | 12 |
| CRISPR used in diagnostics | 20 |
| Research use or unclear | 14 |
| Not gene editing or unclear | 69 |
| **Total** | **314** |

### Confidence Assessment of Therapeutic Trials

The initial classification identified 199 potential therapeutic gene-editing trials.

| Confidence Category | Number |
|---|---:|
| High confidence | 78 |
| Product code match only | 88 |
| Weak supporting evidence | 33 |
| **Total** | **199** |

These figures reflect the initial automated classification. Manual verification will determine the final classification and trial counts.

## 6. Early Observations

The initial analysis suggests the following patterns:

- The United States and China have the largest numbers of identified trials.
- Most therapeutic trials appear in early development phases. 153 of 199 are Phase 1, Phase 1/2, or Early Phase 1, and 28 have no phase listed.
- No therapeutic trial currently has a listed study site in Pakistan. This counts study sites only. It does not show whether a Pakistani sponsor or investigator is involved.

These observations require further verification before inclusion in the final research report.

**Figures and Tables**

- Figures: `results/figures/`
- Summary tables: `results/tables/`

## 7. Study Limitations

The project has several limitations:

- **Automated classification:** Keyword-based rules and product code matching may produce incorrect classifications.
- **Incomplete registry information:** A record marked as "Not stated" does not establish whether the information was absent from the actual trial.
- **Multiple study locations:** Trials with sites in several countries are counted in each relevant country, so country counts add up to more than the number of trials.
- **Search limitations:** The search strategy may miss relevant trials whose registry records do not contain explicit gene-editing terminology.
- **Single registry:** ClinicalTrials.gov has more United States trials than other registries, so the geographic picture may be biased.
- **Preliminary findings:** The current results require manual verification and completion of ethics coding.

## 8. How to Run the Project

### Requirements

Install the Python packages listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Run the Data Processing Script

Merge the original downloads, remove duplicates, and generate the initial classifications.

```bash
python scripts/01_merge_and_classify.py
```

### Generate Summary Tables and Figures

Run the analysis and visualisation script.

```bash
python scripts/02_summary_and_figures.py
```

Run both commands from the main project directory.

## 9. Repository Structure

```text
crispr-transparency-in-gene-editing-trials/
│
├── data/
│   ├── raw/                 # Original ClinicalTrials.gov downloads
│   ├── processed/           # Merged and classified records
│   └── coding/              # Excel workbook for manual coding
│
├── docs/
│   ├── search_strategy.md
│   ├── coding_protocol.md
│   └── review_queue.csv
│
├── results/
│   ├── figures/             # Generated research figures
│   └── tables/              # Summary tables
│
├── scripts/
│   ├── 01_merge_and_classify.py
│   └── 02_summary_and_figures.py
│
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

## 10. Planned Next Steps

The next stage will focus on completing the research and improving the reliability of the findings.

- Complete manual verification of medium- and low-confidence trial classifications.
- Verify the product code list.
- Group the registry conditions into disease areas, so the disease part of the research question can be answered.
- Register the research protocol, the question and the coding rules, on the Open Science Framework before the manual coding.
- Finish coding informed consent, ethics approval, and participant follow-up.
- Introduce a second independent coder.
- Calculate inter-coder agreement using Cohen's kappa.
- Compare the findings with WHO human genome editing recommendations.
- Examine relevant national regulatory frameworks in Pakistan, Spain, and the United Kingdom.
- Compare with other registries, such as the WHO ICTRP.
- Prepare a research report based on the verified results.

## 11. Licence and Data Use

The original code and author-created text are released under the MIT License. See the `LICENSE` file.

ClinicalTrials.gov registry data remain subject to the ClinicalTrials.gov Terms of Use.

The MIT License applies to the author's original contributions. It does not grant additional rights over third-party content included in registry records.

**Project maintained by:** Sara Shahid Abbas  
**Location:** Lahore, Pakistan  
**Research area:** Gene Editing, Research Ethics, Clinical Trial Transparency, and Health Data Governance
