import streamlit as st
import pandas as pd
import plotly.express as px

from utils.theme import apply_theme
from AI_Analyst import AIEngine


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="InsightAI",
    page_icon="📊",
    layout="wide"
)


apply_theme()


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
"""
<style>

.title{
    font-size:45px;
    font-weight:bold;
    color:#0E4C92;
}

.subtitle{
    font-size:20px;
    color:gray;
}

</style>
""",
unsafe_allow_html=True
)



# =====================================================
# TITLE
# =====================================================

st.markdown(
"""
<div class="title">
📊 InsightAI
</div>
""",
unsafe_allow_html=True
)


st.markdown(
"""
<div class="subtitle">
AI Powered Data Analyst - Upload, Analyze and Ask Questions
</div>
""",
unsafe_allow_html=True
)


st.divider()



# =====================================================
# FILE UPLOAD
# =====================================================

uploaded_file = st.file_uploader(
    "Upload CSV or Excel Dataset",
    type=["csv","xlsx"]
)



if uploaded_file:


    # =================================================
    # LOAD DATA
    # =================================================

    try:

        if uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

        else:

            df = pd.read_excel(uploaded_file)


    except Exception as e:

        st.error(
            f"Dataset loading failed: {e}"
        )

        st.stop()



    # Remove spaces from columns

    df.columns = (
        df.columns
        .str.strip()
    )


    st.success(
        "Dataset uploaded successfully ✅"
    )



    st.session_state["df"] = df



    # Reset chat for new dataset

    if (
        "current_file" not in st.session_state
        or
        st.session_state.current_file 
        != uploaded_file.name
    ):

        st.session_state.messages=[]

        st.session_state.current_file = uploaded_file.name




    # =================================================
    # DATA PREVIEW
    # =================================================


    st.header(
        "📄 Dataset Preview"
    )


    st.dataframe(
        df,
        use_container_width=True
    )



    # =================================================
    # KPI SECTION
    # =================================================


    st.header(
        "📌 Business KPIs"
    )


    col1,col2,col3,col4 = st.columns(4)



    sales_column = None

    profit_column = None



    for col in df.columns:

        if col.lower()=="sales":

            sales_column=col


        if col.lower()=="profit":

            profit_column=col




    # Sales

    if sales_column:

        total_sales=df[sales_column].sum()

    else:

        total_sales=0



    # Profit

    if profit_column:

        total_profit=df[profit_column].sum()

    else:

        total_profit=0



    total_orders=len(df)



    category_column=None


    for col in df.columns:

        if col.lower()=="category":

            category_column=col



    if category_column:

        categories=df[category_column].nunique()

    else:

        categories=0




    col1.metric(
        "Total Sales",
        f"₹{total_sales:,.0f}"
    )


    col2.metric(
        "Total Profit",
        f"₹{total_profit:,.0f}"
    )


    col3.metric(
        "Orders",
        total_orders
    )


    col4.metric(
        "Categories",
        categories
    )



    # =================================================
    # DASHBOARD CHARTS
    # =================================================


    st.header(
        "📈 Business Dashboard"
    )


    chart1,chart2 = st.columns(2)



    with chart1:


        if (
            category_column
            and
            sales_column
        ):


            category_sales=(

                df.groupby(category_column)
                [sales_column]
                .sum()
                .reset_index()

            )


            fig=px.bar(

                category_sales,

                x=category_column,

                y=sales_column,

                title="Sales By Category",

                text=sales_column

            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


        else:

            st.warning(
                "Category/Sales column not found"
            )




    with chart2:


        city_column=None


        for col in df.columns:

            if col.lower()=="city":

                city_column=col



        if (
            city_column
            and
            profit_column
        ):


            city_profit=(

                df.groupby(city_column)
                [profit_column]
                .sum()
                .reset_index()

            )


            fig2=px.pie(

                city_profit,

                names=city_column,

                values=profit_column,

                title="Profit Distribution"

            )


            st.plotly_chart(

                fig2,

                use_container_width=True

            )


        else:

            st.warning(
                "City/Profit column not found"
            )





    # =================================================
    # AI ANALYST
    # =================================================


    st.divider()


    st.header(
        "🤖 Ask AI Analyst"
    )



    if "messages" not in st.session_state:

        st.session_state.messages=[]



    ai = AIEngine(df)



    for message in st.session_state.messages:


        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )



    question = st.chat_input(
        "Ask: Which city has highest sales?"
    )



    if question:


        st.session_state.messages.append(

            {
                "role":"user",

                "content":question
            }

        )



        with st.chat_message("user"):

            st.markdown(question)



        try:


            result = ai.answer(question)



            if result is None:

                result={

                    "answer":
                    "I could not understand this question.",

                    "chart":None,

                    "recommendation":
                    "Try asking about sales, profit, city or category."

                }



        except Exception as e:


            result={

                "answer":
                f"AI Error: {e}",

                "chart":None,

                "recommendation":
                "Check AI_Analyst.py logic."

            }




        with st.chat_message("assistant"):


            st.markdown(
                result.get(
                    "answer",
                    "No answer"
                )
            )


            if result.get("chart"):

                st.plotly_chart(

                    result["chart"],

                    use_container_width=True

                )



            st.info(

                "💡 Recommendation\n\n"
                +
                result.get(
                    "recommendation",
                    "No recommendation"
                )

            )



        st.session_state.messages.append(

            {

            "role":"assistant",

            "content":
            result.get(
                "answer",
                ""
            )

            }

        )



else:


    st.info(
        "📂 Upload your dataset to start analysis"
    )