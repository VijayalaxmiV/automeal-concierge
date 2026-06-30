from datetime import datetime


class OrderScheduler:


    def create_schedule(
        self,
        food_item,
        schedule
    ):

        print("📅 Creating meal schedule")

        return {
            "scheduled": True,
            "food": food_item,
            "frequency": schedule.get("frequency"),
            "day": schedule.get("day"),
            "time": schedule.get("time"),
            "created_at": str(datetime.now())
        }