from automeal.services.gemini_service import GeminiService


class ConciergeAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def chat(self, message: str) -> str:

        prompt = f"""
You are AutoMeal Concierge.

The user is scheduling food orders.

Return a helpful response.

User:
{message}
"""

        return self.gemini.generate(prompt)