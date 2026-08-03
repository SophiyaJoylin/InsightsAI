import streamlit as st
import pandas as pd
import plotly.express as px
from utils.theme import apply_theme


# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="InsightAI Dashboard",
    page_icon="📊",
    layout="wide"
)

apply_theme()
# -----------------------------------------------------
# Custom CSS
# -----------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:1.2rem;
    padding-left:2rem;
    padding-right:2rem;
}

.main-title{
    font-size:42px;
    font-weight:700;
    color:#1F3A93;
}

.subtitle{
    font-size:18px;
    color:#6c757d;
    margin-bottom:25px;
}

.section-title{
    font-size:28px;
    font-weight:600;
    color:#1F3A93;
    margin-top:20px;
    margin-bottom:15px;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:20px;
    border:1px solid #E5E7EB;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# Title
# -----------------------------------------------------

st.markdown(
    '<div class="main-title">📊 InsightAI Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI Powered Business Intelligence Dashboard</div>',
    unsafe_allow_html=True
)

st.divider()

# -----------------------------------------------------
# Upload Dataset
# -----------------------------------------------------

uploaded_file = st.file_uploader(
    "📂 Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # =====================================================
    # KPI SECTION
    # =====================================================

    st.markdown(
        '<div class="section-title">📊 Business KPIs</div>',
        unsafe_allow_html=True
    )

    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = len(df)
    total_categories = df["Category"].nunique()

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    kpi1.metric("💰 Total Sales", f"₹{total_sales:,.0f}")
    kpi2.metric("📈 Total Profit", f"₹{total_profit:,.0f}")
    kpi3.metric("📦 Orders", total_orders)
    kpi4.metric("🏷 Categories", total_categories)

    st.divider()

    # =====================================================
    # DATASET OVERVIEW
    # =====================================================

    st.markdown(
        '<div class="section-title">📐 Dataset Overview</div>',
        unsafe_allow_html=True
    )

    missing = df.isnull().sum().sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])
    c3.metric("Missing Values", missing)
    c4.metric("File Type", uploaded_file.name.split(".")[-1].upper())

    st.divider()

    # =====================================================
    # BUSINESS DASHBOARD
    # =====================================================

    st.markdown(
        '<div class="section-title">📈 Business Dashboard</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns(2)

    with left:

        category_sales = (
            df.groupby("Category")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            category_sales,
            x="Category",
            y="Sales",
            color="Category",
            text="Sales",
            title="Sales by Category"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        city_profit = (
            df.groupby("City")["Profit"]
            .sum()
            .reset_index()
        )

        fig2 = px.pie(
            city_profit,
            values="Profit",
            names="City",
            hole=0.45,
            title="Profit Distribution by City"
        )

        st.plotly_chart(fig2, use_container_width=True)

    left, right = st.columns([1.2, 1])

    with left:

        top_products = (
            df.groupby("Product")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
            .reset_index()
        )

        fig3 = px.bar(
            top_products,
            x="Product",
            y="Sales",
            color="Sales",
            text="Sales",
            title="Top 5 Products"
        )

        st.plotly_chart(fig3, use_container_width=True)

    with right:

        st.subheader("📄 Dataset Preview")
        st.dataframe(df.head(10), use_container_width=True)

    st.divider()

    # =====================================================
    # COLUMN INFORMATION
    # =====================================================

    st.markdown(
        '<div class="section-title">📝 Column Information</div>',
        unsafe_allow_html=True
    )

    info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum().values
    })

    st.dataframe(info, use_container_width=True)

    st.divider()

    # =====================================================
    # STATISTICAL SUMMARY
    # =====================================================

    st.markdown(
        '<div class="section-title">📊 Statistical Summary</div>',
        unsafe_allow_html=True
    )

    st.dataframe(df.describe(), use_container_width=True)

else:

    st.info("📂 Upload a CSV or Excel dataset to begin analysis.")