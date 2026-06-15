# risk_metrics.py

import pandas as pd
import numpy as np

def calculate_metrics():

    df = pd.read_csv("07_scheme_performance.csv")

    return {
        "Average Alpha":
            round(df["alpha"].mean(),2),

        "Average Sharpe":
            round(df["sharpe_ratio"].mean(),2),

        "Average Beta":
            round(df["beta"].mean(),2),

        "Average Drawdown":
            round(df["max_drawdown_pct"].mean(),2)
    }