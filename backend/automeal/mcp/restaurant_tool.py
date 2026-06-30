class RestaurantTool:


    def place_order(self, food, restaurant=None):

        return {
            "restaurant": restaurant or "AI selected restaurant",
            "food": food,
            "status": "order placed"
        }