class NLPEngine:


    def __init__(self):

        pass



    # -----------------------------------------
    # Understand User Question
    # -----------------------------------------

    def understand(self, question):

        question = question.lower()


        intent = "unknown"
        metric = None
        group = None



        # ==============================
        # SALES FORECASTING
        # ==============================

        if (
            "predict" in question
            or
            "forecast" in question
            or
            "future sales" in question
            or
            "next month sales" in question
        ):


            intent = "sales_forecast"

            metric = "Sales"




        # ==============================
        # SALES ANALYSIS
        # ==============================

        elif (
            "sales" in question
            and
            (
                "highest" in question
                or
                "maximum" in question
                or
                "top" in question
                or
                "best" in question
            )
        ):


            intent = "highest_sales"


            if "city" in question:

                group = "City"


            elif "category" in question:

                group = "Category"


            elif "product" in question:

                group = "Product"



            metric = "Sales"




        # ==============================
        # PROFIT ANALYSIS
        # ==============================

        elif (
            "profit" in question
            and
            (
                "highest" in question
                or
                "maximum" in question
                or
                "top" in question
            )
        ):


            intent = "highest_profit"



            if "city" in question:

                group = "City"



            elif "category" in question:

                group = "Category"



            elif "product" in question:

                group = "Product"



            metric = "Profit"




        # ==============================
        # LOW PERFORMANCE
        # ==============================

        elif (
            "lowest" in question
            or
            "worst" in question
            or
            "poor" in question
            or
            "least" in question
        ):


            intent = "lowest_performance"




        return {


            "intent": intent,


            "metric": metric,


            "group": group

        }