import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import joblib

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv("07_scheme_performance.csv")

print("Original Shape :", df.shape)

# -----------------------------
# HANDLE MISSING VALUES
# -----------------------------

numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

categorical_cols = [
    "fund_house",
    "category",
    "plan",
    "risk_grade"
]

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------

df["excess_return"] = (
    df["return_3yr_pct"] -
    df["benchmark_3yr_pct"]
)

df["expense_efficiency"] = (
    df["return_5yr_pct"] /
    (df["expense_ratio_pct"] + 0.001)
)

df["risk_adjusted_return"] = (
    df["return_3yr_pct"] /
    (df["std_dev_ann_pct"] + 0.001)
)

df["drawdown_score"] = (
    100 - abs(df["max_drawdown_pct"])
)

# -----------------------------
# TARGET VARIABLE
# -----------------------------

median_return = df["return_5yr_pct"].median()

df["high_performer"] = (
    df["return_5yr_pct"] >= median_return
).astype(int)

print()

print("Median 5 Year Return :", median_return)

print(df["high_performer"].value_counts())

# -----------------------------
# ENCODE CATEGORICAL FEATURES
# -----------------------------

encoders = {}

for col in categorical_cols:

    encoder = LabelEncoder()

    df[col] = encoder.fit_transform(df[col])

    encoders[col] = encoder

joblib.dump(
    encoders,
    "label_encoders.pkl"
)

# -----------------------------
# SAVE
# -----------------------------

df.to_csv(
    "processed_dataset.csv",
    index=False
)

print()

print("Processed Shape :", df.shape)

print("Feature Engineering Complete.")