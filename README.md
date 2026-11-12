# Gene Editing Clinical Trials: A Registry Analysis for Ethics and Governance

**Author:** Sara Shahid Abbas  
**Location:** Lahore, Pakistan  
**Project Status:** Analysis & Governance Pipeline Complete  

---

## 1. Research Question & Rationale
Evaluates registered gene-editing clinical trials (CRISPR, base/prime editing, Cas13) from ClinicalTrials.gov (314 unique records as of 11 November 2026) to analyze geographic, phase, and disease distribution alongside public reporting transparency (informed consent, ethics approval, off-target safety monitoring, and long-term follow-up), benchmarked against WHO and regional frameworks.

---

## 2. Methodology & Scripts
The repository runs through a sequential Python pipeline:
1. `scripts/01_merge_and_classify.py`: Combines raw downloads and retains 314 unique NCT records.
2. `scripts/02_summary_and_figures.py`: Sorts trials by phase, status, funder, start year, and country.
3. `scripts/03_code_ethics_and_governance.py`: Extracts reporting indicators for consent, IRB approval, off-target monitoring, and 15-year LTFU.
4. `scripts/04_intercoder_reliability.py`: Computes percent agreement and Cohen's kappa (κ) between independent coders.
5. `scripts/05_governance_visualizations.py`: Generates high-resolution figures.

### Quick Start
```bash
pip install -r requirements.txt
python scripts/01_merge_and_classify.py
python scripts/02_summary_and_figures.py
python scripts/03_code_ethics_and_governance.py
python scripts/05_governance_visualizations.py
# Optional (after adding second-coder labels):
python scripts/04_intercoder_reliability.py
```

---

## 3. Repository Structure
* **data/**: Raw downloads, processed ethics-coded CSVs, and manual coding workbooks.
* **docs/**: Search strategy, coding protocol, and review queues.
* **manuscript/**: Full research paper and comparative regulatory analysis (`draft_report.md`).
* **results/**: High-resolution PNG figures and summary CSV tables.
* **scripts/**: Analysis and visualization Python modules.
* **requirements.txt**, **LICENSE**, **README.md**

---

## 4. Licence
Released under the **MIT License**.
