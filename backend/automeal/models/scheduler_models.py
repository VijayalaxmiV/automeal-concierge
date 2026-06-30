from pydantic import BaseModel
from datetime import datetime


class ScheduledOrder(BaseModel):
    user_id: str
    food_item: str
    restaurant: str | None = None
    scheduled_time: datetime
    status: str = "pending"