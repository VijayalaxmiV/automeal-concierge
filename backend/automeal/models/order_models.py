from pydantic import BaseModel
from typing import Optional


class OrderSchedule(BaseModel):
    frequency: str
    day: Optional[str] = None
    time: Optional[str] = None


class MealOrderPlan(BaseModel):
    intent: str
    food_item: Optional[str] = None
    restaurant: Optional[str] = None
    schedule: Optional[OrderSchedule] = None
    needs_clarification: bool
    confidence: float