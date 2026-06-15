# recommendation.py

import pandas as pd

def get_recommendations(risk_level):

    df = pd.read_csv("07_scheme_performance.csv")

    if risk_level == "Low":
        rec = df.sort_values(
            ["sharpe_ratio"],
            ascending=False
        ).head(5)

    elif risk_level == "Medium":
        rec = df.sort_values(
            ["alpha"],
            ascending=False
        ).head(5)

    else:
        rec = df.sort_values(
            ["return_5yr_pct"],
            ascending=False
        ).head(5)

    return rec[
        [
            "scheme_name",
            "category",
            "return_5yr_pct",
            "sharpe_ratio",
            "alpha"
        ]
    ]