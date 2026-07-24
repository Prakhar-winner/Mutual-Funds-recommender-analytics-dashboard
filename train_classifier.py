import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (

    accuracy_score,

    precision_score,

    recall_score,

    f1_score,

    confusion_matrix,

    classification_report

)

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv("processed_dataset.csv")

# -----------------------------
# FEATURES
# -----------------------------

features = [

    "return_1yr_pct",

    "return_3yr_pct",

    "benchmark_3yr_pct",

    "alpha",

    "beta",

    "sharpe_ratio",

    "sortino_ratio",

    "std_dev_ann_pct",

    "max_drawdown_pct",

    "aum_crore",

    "expense_ratio_pct",

    "morningstar_rating",

    "fund_house",

    "category",

    "plan",

    "risk_grade",

    "excess_return",

    "expense_efficiency",

    "risk_adjusted_return",

    "drawdown_score"

]

X = df[features]

y = df["high_performer"]

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

# -----------------------------
# MODEL
# -----------------------------

model = RandomForestClassifier(

    n_estimators=300,

    max_depth=10,

    random_state=42

)

model.fit(

    X_train,

    y_train

)

# -----------------------------
# PREDICTION
# -----------------------------

prediction = model.predict(X_test)

probability = model.predict_proba(X_test)

# -----------------------------
# EVALUATION
# -----------------------------

print()

print("Accuracy :", round(

    accuracy_score(

        y_test,

        prediction

    ),2

))

print("Precision :", round(

    precision_score(

        y_test,

        prediction

    ),2

))

print("Recall :", round(

    recall_score(

        y_test,

        prediction

    ),2

))

print("F1 Score :", round(

    f1_score(

        y_test,

        prediction

    ),2

))

print()

print(

    classification_report(

        y_test,

        prediction

    )

)

print()

print(

    confusion_matrix(

        y_test,

        prediction

    )

)

# -----------------------------
# FEATURE IMPORTANCE
# -----------------------------

importance = pd.DataFrame({

    "Feature":features,

    "Importance":model.feature_importances_

})

importance = importance.sort_values(

    by="Importance",

    ascending=False

)

print()

print(importance)

# -----------------------------
# SAVE MODEL
# -----------------------------

joblib.dump(

    model,

    "model.pkl"

)

joblib.dump(

    features,

    "model_features.pkl"

)

print()

print("Model Saved Successfully")