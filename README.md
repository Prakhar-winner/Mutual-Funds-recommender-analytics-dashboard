# Mutual Fund Analytics & Recommendation Platform

## Overview

This project is a Machine Learning based Mutual Fund Recommendation and Risk Analytics Platform developed using Python, Streamlit, Scikit-learn and Plotly.

The application recommends mutual funds based on historical performance, risk metrics and expense characteristics using a Random Forest Classifier.

---

## Features

- Random Forest based Recommendation Engine
- Risk Profile Based Fund Recommendations
- Feature Engineering
- Risk Analytics Dashboard
- Monthly SIP Trend Analysis
- Category-wise Inflow Analysis
- Industry Folio Trend Visualization
- Interactive Streamlit Dashboard

---

## Machine Learning Pipeline

Raw Dataset

↓

Feature Engineering

↓

Processed Dataset

↓

Random Forest Classifier

↓

Prediction Probability

↓

Recommendation Score

↓

Top Recommended Mutual Funds

---

## Feature Engineering

The following features were engineered:

- Excess Return
- Expense Efficiency
- Risk Adjusted Return
- Drawdown Score

---

## Datasets

### Scheme Performance
Contains historical mutual fund performance, returns and risk metrics.

### Monthly SIP Inflows
Monthly SIP investment trends.

### Category Inflows
Net inflows across mutual fund categories.

### Industry Folio Count
Overall mutual fund industry growth.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Streamlit
- Joblib

---

## Project Structure

```
feature_engineering.py

train_classifier.py

recommendation.py

risk_metrics.py

app.py

processed_dataset.csv

model.pkl
```

---

## Installation

```bash
pip install -r requirements.txt
```

Run Feature Engineering

```bash
python feature_engineering.py
```

Train Model

```bash
python train_classifier.py
```

Launch Dashboard

```bash
streamlit run app.py
```

---

## Future Improvements

- Larger dataset
- Live NAV Integration
- Personalized Investor Recommendation
- Portfolio Optimization

---

## Author

Prakhar Singh