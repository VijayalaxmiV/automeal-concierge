from automeal.services.gemini_service import GeminiService
from automeal.scheduler.order_scheduler import OrderScheduler
from automeal.mcp.restaurant_tool import RestaurantTool


class ConciergeAgent:
    def __init__(self):
        self.gemini = GeminiService()
        self.scheduler = OrderScheduler()
        self.restaurant = RestaurantTool()

    def chat(self, message: str):

        prompt = f"""
You are AutoMeal Concierge.

Your job is to understand meal ordering requests.

Return ONLY valid JSON.

Schema:

{{
    "intent": "",
    "food_item": "",
    "restaurant": null,
    "schedule": {{
        "frequency": "",
        "day": "",
        "time": ""
    }},
    "needs_clarification": false,
    "confidence": 0.95
}}

Examples:

User: I want biryani every Friday at 8 PM

Response:
{{
    "intent": "schedule_meal",
    "food_item": "biryani",
    "restaurant": null,
    "schedule": {{
        "frequency": "weekly",
        "day": "Friday",
        "time": "8 PM"
    }},
    "needs_clarification": false,
    "confidence": 0.98
}}

User request:
{message}
"""

        plan = self.gemini.generate(prompt)

        # Normalize intent so small wording differences don't break the workflow
        intent = plan.get("intent", "").lower().replace(" ", "_")

        if intent in [
            "schedule_meal",
            "schedule_food_order",
            "meal_schedule",
            "schedule_order",
        ]:

            schedule_result = self.scheduler.create_schedule(
                food_item=plan.get("food_item"),
                schedule=plan.get("schedule", {}),
            )

            order_result = self.restaurant.place_order(
                food_item=plan.get("food_item"),
                restaurant=plan.get("restaurant"),
            )

            return {
                "meal_plan": plan,
                "scheduler": schedule_result,
                "order": order_result,
            }

        return {
            "meal_plan": plan,
            "message": "No scheduling action required."
        }