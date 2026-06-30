from fastapi import APIRouter

from automeal.models.chat_models import ChatRequest
from automeal.agents.concierge_agent import ConciergeAgent


router = APIRouter(prefix="/api")

agent = ConciergeAgent()


@router.post("/chat")
def chat(request: ChatRequest):

    result = agent.chat(
        request.message
    )

    return result