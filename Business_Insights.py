from Chart_Engine import ChartEngine
from Recommendation_Engine import RecommendationEngine



class BusinessInsights:


    def __init__(self, df):

        self.df = df

        # Chart Intelligence Engine

        self.chart = ChartEngine()


        # AI Recommendation Engine

        self.recommend = RecommendationEngine()



    # ==================================
    # Highest Value Analysis
    # ==================================

    def highest_value(self, metric, group):


        if metric not in self.df.columns:

            return {

                "answer": f"{metric} column not found",

                "chart": None,

                "recommendation": "Check dataset columns"

            }



        if group not in self.df.columns:

            return {

                "answer": f"{group} column not found",

                "chart": None,

                "recommendation": "Check dataset columns"

            }




        result = (

            self.df

            .groupby(group)[metric]

            .sum()

            .reset_index()

            .sort_values(
                by=metric,
                ascending=False
            )

        )



        top = result.iloc[0]


        name = top[group]

        value = top[metric]



        # Chart Engine

        fig = self.chart.create_chart(

            result,

            group,

            metric,

            "bar",

            f"{metric} by {group}"

        )



        return {


            "answer":

            f"🏆 {name} has the highest {metric} with {value:,.0f}",



            "chart":

            fig,



            "recommendation":

            self.recommend.generate(

                name,

                metric,

                value,

                1,

                len(result)

            )

        }





    # ==================================
    # Lowest Performance
    # ==================================

    def lowest_value(self, metric, group):


        if metric not in self.df.columns:


            return {

                "answer":
                f"{metric} column not found",

                "chart":
                None,

                "recommendation":
                "Check dataset columns"

            }



        if group not in self.df.columns:


            return {

                "answer":
                f"{group} column not found",

                "chart":
                None,

                "recommendation":
                "Check dataset columns"

            }




        result = (

            self.df

            .groupby(group)[metric]

            .sum()

            .reset_index()

            .sort_values(
                by=metric
            )

        )



        worst = result.iloc[0]



        # Chart Engine

        fig = self.chart.create_chart(

            result,

            group,

            metric,

            "horizontal",

            f"Low Performing {group}"

        )



        return {


            "answer":

            f"⚠️ {worst[group]} has the lowest {metric}",



            "chart":

            fig,



            "recommendation":

            self.recommend.generate(

                worst[group],

                metric,

                worst[metric],

                len(result),

                len(result)

            )

        }