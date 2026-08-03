class RecommendationEngine:



    def generate(
        self,
        name,
        metric,
        value,
        rank,
        total_count
    ):



        recommendations = []



        # -----------------------------
        # Top Performer
        # -----------------------------

        if rank == 1:


            recommendations.append(
                f"Increase investment in {name} because it is the top performing area."
            )


            recommendations.append(
                "Run targeted marketing campaigns."
            )


            recommendations.append(
                "Analyze customer behaviour to replicate success."
            )



        # -----------------------------
        # Low Performer
        # -----------------------------


        else:


            recommendations.append(
                f"Improve performance of {name}."
            )


            recommendations.append(
                "Review pricing, customer demand and product availability."
            )


            recommendations.append(
                "Create promotional offers to improve sales."
            )



        return "\n".join(

            [
                "💡 AI Recommendations:",
                *recommendations
            ]

        )