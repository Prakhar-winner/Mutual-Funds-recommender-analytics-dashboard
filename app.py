# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

from recommendation import get_recommendations
from risk_metrics import calculate_metrics

# -----------------------------
# PAGE TITLE
# -----------------------------

st.set_page_config(
    page_title="Mutual Fund Analytics",
    layout="wide"
)

st.title("Mutual Fund Recommendation & Risk Analytics Dashboard")

# -----------------------------
# RISK PROFILE
# -----------------------------

risk = st.selectbox(
    "Select Risk Profile",
    ["Low", "Medium", "High"]
)

# -----------------------------
# RECOMMENDATIONS
# -----------------------------

st.header("Recommended Funds")

rec = get_recommendations(risk)

st.dataframe(rec, use_container_width=True)

# -----------------------------
# RISK METRICS
# -----------------------------

st.header("Risk Metrics")

metrics = calculate_metrics()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Average Alpha", metrics["Average Alpha"])

with col2:
    st.metric("Average Sharpe", metrics["Average Sharpe"])

with col3:
    st.metric("Average Beta", metrics["Average Beta"])

with col4:
    st.metric("Average Drawdown", metrics["Average Drawdown"])

# -----------------------------
# SIP INFLOW TREND
# -----------------------------

st.header("Monthly SIP Trends")

df = pd.read_csv("04_monthly_sip_inflows.csv")

fig = px.line(
    df,
    x="month",
    y="sip_inflow_crore",
    title="Monthly SIP Inflows"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# CATEGORY INFLOWS
# -----------------------------

st.header("Category-wise Net Inflows")

df2 = pd.read_csv("05_category_inflows.csv")

fig2 = px.bar(
    df2,
    x="category",
    y="net_inflow_crore",
    title="Category Inflows"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# RAW DATA SECTION
# -----------------------------

with st.expander("View Raw SIP Data"):
    st.dataframe(df)

with st.expander("View Category Data"):
    st.dataframe(df2)

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")
st.caption(
    "Built using Python, Pandas, Plotly and Streamlit for Mutual Fund Risk Analytics."
)