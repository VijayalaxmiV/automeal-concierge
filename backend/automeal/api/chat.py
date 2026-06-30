from fastapi import APIRouter

from automeal.agents.concierge_agent import ConciergeAgent
from automeal.models.chat_models import ChatRequest, ChatResponse

router = APIRouter(prefix="/api")


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    agent = ConciergeAgent()

    reply = agent.chat(request.message)

    return ChatResponse(reply=reply)