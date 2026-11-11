# Gene editing clinical trials: a registry analysis for ethics and governance

Author: Sara Shahid Abbas, Lahore, Pakistan
Status: work in progress. Results are preliminary.

## Research question
How are registered gene editing clinical trials distributed by country, disease, phase and funder, and what do their registry records say about consent, ethics approval and long term follow up?

## Why this matters
Gene editing trials are growing fast. Governance rules differ between countries. A registry analysis shows where trials take place and how much ethics information is visible to the public. This links to my interests in research ethics, dual use research of concern and health data governance.

## Data
Source: ClinicalTrials.gov, downloaded in November 2026.
Two searches were run, see docs/search_strategy.md. After removing duplicates there are 314 unique trials.
Please read the ClinicalTrials.gov terms of use: https://clinicaltrials.gov/about-site/terms-conditions
The data come from ClinicalTrials.gov. Raw files are included here unchanged. My changes are described below. Some records may carry third party copyright.

## Method
1. Merge the two downloads and remove duplicates by NCT number (scripts/01_merge_and_classify.py).
2. Give each trial a first pass category using word rules and a list of known product codes. Each category has a confidence level.
3. Check every Medium and Low confidence trial by hand (docs/review_queue.csv).
4. Code ethics and consent items by reading each registry record (docs/coding_protocol.md).
5. Make tables and figures (scripts/02_summary_and_figures.py).

## First pass results, not yet checked by hand
| Category | Trials |
|---|---|
| Therapeutic gene editing | 199 |
| Follow-up or non-interventional, gene editing linked | 12 |
| CRISPR used in diagnostics | 20 |
| Research use or unclear | 14 |
| Not gene editing or unclear | 69 |

Of the 199 therapeutic trials, only 78 are high confidence. 88 are matched by product code only and 33 have weak evidence. The final number will change after the manual check.

Early observations, to be confirmed:
- Most trials are in the United States and China.
- Most trials are early phase, phase 1 or phase 1 and 2.
- No therapeutic trial has a listed site in Pakistan.

Figures are in results/figures and tables are in results/tables.

## Limitations
- The first pass category is made with word rules and can be wrong.
- Registry records can be incomplete, so Not stated does not mean the item was missing in the real trial.
- A trial with sites in several countries is counted in each country.
- The search may miss trials that do not use editing words in the record.

## How to run
```
pip install -r requirements.txt
python scripts/01_merge_and_classify.py
python scripts/02_summary_and_figures.py
```
Run both commands from the main project folder.

## Folder guide
- data/raw: original downloads, unchanged
- data/processed: merged and classified trials
- data/coding: Excel workbook for manual coding
- docs: search strategy, coding protocol, review queue
- results: tables and figures
- scripts: Python code

## Next steps
- Finish the manual check and the ethics coding.
- Add a second coder and report agreement.
- Compare findings with WHO genome editing recommendations and national rules in Pakistan, Spain and the United Kingdom.
- Write a short report.

## Licence
Code and my own text: MIT licence, see LICENSE. Registry data: see the ClinicalTrials.gov terms above.
