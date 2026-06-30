from automeal.services.gemini_service import GeminiService


class ConciergeAgent:

    def __init__(self):
        self.gemini = GeminiService()


    def chat(self, message):

        prompt = f"""
You are AutoMeal Concierge.

Analyze the food request.

Return ONLY JSON.

Schema:

{{
 "intent": "",
 "food_item": "",
 "restaurant": "",
 "schedule": {{
    "frequency": "",
    "day": "",
    "time": ""
 }},
 "needs_clarification": false,
 "confidence": 0.0
}}

User:
{message}

"""

        return self.gemini.generate(prompt)