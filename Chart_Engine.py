import plotly.express as px



class ChartEngine:


    def create_chart(
        self,
        df,
        category,
        value,
        chart_type,
        title
    ):


        # -------------------------
        # Bar Chart
        # -------------------------

        if chart_type == "bar":


            fig = px.bar(

                df,

                x=category,

                y=value,

                text=value,

                title=title

            )


        # -------------------------
        # Horizontal Bar
        # -------------------------

        elif chart_type == "horizontal":


            fig = px.bar(

                df,

                x=value,

                y=category,

                orientation="h",

                title=title

            )



        # -------------------------
        # Pie Chart
        # -------------------------

        elif chart_type == "pie":


            fig = px.pie(

                df,

                names=category,

                values=value,

                title=title

            )



        # -------------------------
        # Line Chart
        # -------------------------

        elif chart_type == "line":


            fig = px.line(

                df,

                x=category,

                y=value,

                markers=True,

                title=title

            )



        # -------------------------
        # Scatter Chart
        # -------------------------

        elif chart_type == "scatter":


            fig = px.scatter(

                df,

                x=category,

                y=value,

                title=title

            )


        else:


            fig = px.bar(

                df,

                x=category,

                y=value,

                title=title

            )



        return fig