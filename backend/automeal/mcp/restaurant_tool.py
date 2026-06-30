class RestaurantTool:


    def place_order(
        self,
        food_item,
        restaurant=None
    ):

        selected_restaurant = (
            restaurant
            if restaurant
            else "AI Recommended Restaurant"
        )


        return {
            "status": "order_created",
            "restaurant": selected_restaurant,
            "item": food_item
        }