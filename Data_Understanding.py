class DataUnderstanding:


    def __init__(self, df):

        self.df = df



    def find_column(self, keywords):


        for column in self.df.columns:


            name = column.lower()


            for word in keywords:

                if word in name:

                    return column



        return None




    def analyze_columns(self):


        return {


            "sales":

            self.find_column(

                [
                    "sales",
                    "revenue",
                    "amount",
                    "income"
                ]

            ),




            "profit":

            self.find_column(

                [
                    "profit",
                    "gain",
                    "margin"
                ]

            ),




            "city":

            self.find_column(

                [
                    "city",
                    "location",
                    "region"
                ]

            ),




            "category":

            self.find_column(

                [
                    "category",
                    "type",
                    "segment"
                ]

            ),




            "product":

            self.find_column(

                [
                    "product",
                    "item",
                    "name"
                ]

            ),




            # ==============================
            # DATE COLUMN FOR FORECASTING
            # ==============================

            "date":

            self.find_column(

                [
                    "date",
                    "order_date",
                    "transaction_date",
                    "time",
                    "created",
                    "day"
                ]

            )

        }