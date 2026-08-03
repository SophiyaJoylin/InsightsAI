from NLP_Engine import NLPEngine
from Business_Insights import BusinessInsights
from Data_Understanding import DataUnderstanding
from Forecasting_Engine import ForecastingEngine



class AIEngine:


    # ======================================
    # INITIALIZE AI ENGINE
    # ======================================

    def __init__(self, df):

        self.df = df


        # Automatic dataset understanding

        self.data_map = (
            DataUnderstanding(df)
            .analyze_columns()
        )


        # NLP Engine

        self.nlp = NLPEngine()



        # Business Intelligence Engine

        self.insights = BusinessInsights(df)



        # Forecasting Engine

        self.forecast = ForecastingEngine(df)





    # ======================================
    # MAIN AI FUNCTION
    # ======================================

    def answer(self, question):


        analysis = self.nlp.understand(question)



        intent = analysis["intent"]

        metric = analysis["metric"]

        group = analysis["group"]





        # ==================================
        # SALES FORECAST
        # ==================================

        if intent == "sales_forecast":


            date_column = self.data_map.get("date")

            sales_column = self.data_map.get("sales")



            if date_column and sales_column:


                return self.forecast.predict_sales(

                    date_column,

                    sales_column

                )



            else:


                return {


                    "answer":

                    """
                    ⚠️ Forecasting requires:

                    • Date column
                    • Sales column
                    """,


                    "chart":

                    None,


                    "recommendation":

                    """
                    Add a Date column and Sales column
                    to enable future sales prediction.
                    """

                }





        # ==================================
        # Map NLP terms to real columns
        # ==================================


        if metric == "Sales":

            metric = self.data_map.get("sales")



        elif metric == "Profit":

            metric = self.data_map.get("profit")





        if group == "City":

            group = self.data_map.get("city")



        elif group == "Category":

            group = self.data_map.get("category")



        elif group == "Product":

            group = self.data_map.get("product")







        # ==================================
        # Highest Analysis
        # ==================================

        if intent in [

            "highest_sales",

            "highest_profit"

        ]:


            return self.insights.highest_value(

                metric,

                group

            )







        # ==================================
        # Lowest Analysis
        # ==================================

        elif intent == "lowest_performance":



            product_column = self.data_map.get("product")


            sales_column = self.data_map.get("sales")



            if product_column and sales_column:



                return self.insights.lowest_value(

                    sales_column,

                    product_column

                )



            else:



                return {


                    "answer":

                    "Product or Sales information is missing.",


                    "chart":

                    None,


                    "recommendation":

                    "Upload a dataset containing product and sales details."

                }





        # ==================================
        # Unknown Question
        # ==================================

        else:


            return {


                "answer":

                """
                ❌ I could not understand your question.

                Try asking:

                • Which city has highest sales?
                • Which category gives maximum profit?
                • Show top products by sales?
                • Predict future sales?
                """,



                "chart":

                None,



                "recommendation":

                """
                Use business keywords:

                Sales
                Profit
                City
                Category
                Product
                Forecast
                """

            }