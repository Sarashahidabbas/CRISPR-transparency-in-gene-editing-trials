import pandas as pd
from sklearn.metrics import cohen_kappa_score

def evaluate_agreement(coder1_csv, coder2_csv, columns):
    df1 = pd.read_csv(coder1_csv).sort_values("nct_id").reset_index(drop=True)
    df2 = pd.read_csv(coder2_csv).sort_values("nct_id").reset_index(drop=True)
    
    assert (df1["nct_id"] == df2["nct_id"]).all(), "NCT IDs do not align between coders."
    
    results = []
    for col in columns:
        kappa = cohen_kappa_score(df1[col].astype(str), df2[col].astype(str))
        pct_agree = (df1[col] == df2[col]).mean() * 100
        results.append({
            "Variable": col,
            "Percent_Agreement": round(pct_agree, 2),
            "Cohens_Kappa": round(kappa, 3)
        })
    return pd.DataFrame(results)

if __name__ == "__main__":
    cols_to_check = ["refined_category", "consent_reporting", "ethics_irb_reporting", "ltfu_reporting"]
    report = evaluate_agreement("data/coding/coder1.csv", "data/coding/coder2.csv", cols_to_check)
    report.to_csv("results/tables/intercoder_reliability.csv", index=False)
    print(report)
