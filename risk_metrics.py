import pandas as pd
conn = sqlite3.connect("mutual_funds.db")

df = pd.read_sql("SELECT * FROM scheme_performance", conn)

conn.close()

def overall_risk_metrics():

    return {

        "Average Alpha":
            round(df["alpha"].mean(),2),

        "Average Beta":
            round(df["beta"].mean(),2),

        "Average Sharpe":
            round(df["sharpe_ratio"].mean(),2),

        "Average Sortino":
            round(df["sortino_ratio"].mean(),2),

        "Average Expense Ratio":
            round(df["expense_ratio_pct"].mean(),2),

        "Average Drawdown":
            round(df["max_drawdown_pct"].mean(),2),

        "Average 5Y Return":
            round(df["return_5yr_pct"].mean(),2)

    }


def highest_return_funds():

    return df.sort_values(

        by="return_5yr_pct",

        ascending=False

    ).head(10)


def top_risk_adjusted_funds():

    return df.sort_values(

        by="sharpe_ratio",

        ascending=False

    ).head(10)


def low_expense_funds():

    return df.sort_values(

        by="expense_ratio_pct"

    ).head(10)