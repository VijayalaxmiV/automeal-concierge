from fastapi import APIRouter
from automeal.agents.concierge_agent import ConciergeAgent

router = APIRouter(prefix="/api")


agent = ConciergeAgent()


@router.post("/chat")
def chat(request: dict):

    result = agent.chat(
        request["message"]
    )

    return result