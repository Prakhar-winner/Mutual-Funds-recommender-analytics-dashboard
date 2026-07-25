import pandas as pd
import joblib
import sqlite3
# ----------------------------------
# LOAD MODEL
# ----------------------------------

model = joblib.load("model.pkl")

features = joblib.load("model_features.pkl")




conn = sqlite3.connect("mutual_funds.db")

df = pd.read_sql("SELECT * FROM scheme_performance", conn)

conn.close()

# ----------------------------------
# RECOMMENDATION FUNCTION
# ----------------------------------

def recommend_funds(risk_profile):

    data = df.copy()

    # ----------------------------------
    # FILTER BASED ON RISK
    # ----------------------------------

    if risk_profile == "Low":

        data = data[
            data["risk_grade"] <= 1
        ]

    elif risk_profile == "Medium":

        data = data[
            data["risk_grade"] <= 2
        ]

    else:

        data = data.copy()

    # ----------------------------------
    # ML PREDICTION
    # ----------------------------------

    X = data[features]

    probability = model.predict_proba(X)

    data["ML Score"] = probability[:,1] * 100

    # ----------------------------------
    # NORMALIZE MORNINGSTAR
    # ----------------------------------

    data["Morningstar Score"] = (

        data["morningstar_rating"] / 5

    ) * 100

    # ----------------------------------
    # LOW EXPENSE BONUS
    # ----------------------------------

    maximum = data["expense_ratio_pct"].max()

    minimum = data["expense_ratio_pct"].min()

    data["Expense Bonus"] = (

        (maximum - data["expense_ratio_pct"])

        /

        (maximum - minimum + 0.0001)

    ) * 100

    # ----------------------------------
    # FINAL SCORE
    # ----------------------------------

    data["Recommendation Score"] = (

        0.70 * data["ML Score"]

        +

        0.20 * data["Morningstar Score"]

        +

        0.10 * data["Expense Bonus"]

    )

    # ----------------------------------
    # SORT
    # ----------------------------------

    data = data.sort_values(

        by="Recommendation Score",

        ascending=False

    )

    # ----------------------------------
    # RETURN
    # ----------------------------------

    return data[

        [

            "scheme_name",

            "fund_house",

            "category",

            "return_5yr_pct",

            "expense_ratio_pct",

            "morningstar_rating",

            "Recommendation Score"

        ]

    ].head(5)