from datetime import datetime


class OrderScheduler:

    def schedule(self, order):

        print("📅 Order scheduled:")
        print(order)

        return {
            "status": "scheduled",
            "scheduled_for": order.scheduled_time
        }