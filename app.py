import streamlit as st
import pandas as pd
import plotly.express as px

from recommendation import recommend_funds
from risk_metrics import (
    overall_risk_metrics,
    highest_return_funds,
    top_risk_adjusted_funds,
    low_expense_funds
)

st.set_page_config(
    page_title="Mutual Fund Analytics Platform",
    page_icon="📈",
    layout="wide"
)

# --------------------------
# LOAD DATA
# --------------------------

scheme_df = pd.read_csv("processed_dataset.csv")
sip_df = pd.read_csv("04_monthly_sip_inflows.csv")
category_df = pd.read_csv("05_category_inflows.csv")
folio_df = pd.read_csv("06_industry_folio_count.csv")

# --------------------------
# SIDEBAR
# --------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(

    "Go To",

    [

        "Dashboard",

        "Recommendation Engine",

        "Fund Analytics",

        "Industry Trends"

    ]

)

# ==========================
# DASHBOARD
# ==========================

if page == "Dashboard":

    st.title("📈 Mutual Fund Analytics Platform")

    metrics = overall_risk_metrics()

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Funds",len(scheme_df))
    c2.metric("Avg Return",metrics["Average 5Y Return"])
    c3.metric("Avg Sharpe",metrics["Average Sharpe"])
    c4.metric("Avg Alpha",metrics["Average Alpha"])

    st.divider()

    left,right=st.columns([2,1])

    with left:

        fig=px.bar(

            highest_return_funds(),

            x="scheme_name",

            y="return_5yr_pct",

            color="return_5yr_pct",

            title="Top Performing Mutual Funds"

        )

        st.plotly_chart(fig,use_container_width=True)

    with right:

        st.subheader("Dataset")

        st.write("Fund Houses :",scheme_df["fund_house"].nunique())

        st.write("Categories :",scheme_df["category"].nunique())

        st.write("Risk Grades :",scheme_df["risk_grade"].nunique())

        st.write("Total Schemes :",len(scheme_df))

# ==========================
# RECOMMENDATION ENGINE
# ==========================

elif page=="Recommendation Engine":

    st.title("🤖 AI Recommendation Engine")

    risk=st.selectbox(

        "Select Risk Profile",

        [

            "Low",

            "Medium",

            "High"

        ]

    )

    rec=recommend_funds(risk)

    st.dataframe(

        rec,

        use_container_width=True

    )

# ==========================
# FUND ANALYTICS
# ==========================

elif page=="Fund Analytics":

    st.title("📊 Fund Analytics")

    tab1,tab2,tab3=st.tabs(

        [

            "Highest Return",

            "Sharpe Ratio",

            "Lowest Expense"

        ]

    )

    with tab1:

        fig=px.bar(

            highest_return_funds(),

            x="scheme_name",

            y="return_5yr_pct",

            color="return_5yr_pct"

        )

        st.plotly_chart(fig,use_container_width=True)

    with tab2:

        fig=px.bar(

            top_risk_adjusted_funds(),

            x="scheme_name",

            y="sharpe_ratio",

            color="sharpe_ratio"

        )

        st.plotly_chart(fig,use_container_width=True)

    with tab3:

        fig=px.bar(

            low_expense_funds(),

            x="scheme_name",

            y="expense_ratio_pct",

            color="expense_ratio_pct"

        )

        st.plotly_chart(fig,use_container_width=True)

# ==========================
# INDUSTRY
# ==========================

else:

    st.title("📈 Industry Trends")

    fig=px.line(

        sip_df,

        x="month",

        y="sip_inflow_crore",

        markers=True,

        title="Monthly SIP Inflows"

    )

    st.plotly_chart(fig,use_container_width=True)

    fig=px.bar(

        category_df,

        x="category",

        y="net_inflow_crore",

        color="category"

    )

    st.plotly_chart(fig,use_container_width=True)

    fig=px.line(

        folio_df,

        x="month",

        y="total_folios_crore",

        markers=True,

        title="Industry Folio Growth"

    )

    st.plotly_chart(fig,use_container_width=True)