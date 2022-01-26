class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints restaurant name and cuisine type."""
        print(f"\nThe restaurant name is {self.restaurant_name.title()}")
        print(f"It's type of cuisine is {self.cuisine_type}.")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name.title()} is open!")


res_1 = Restaurant('Mamma Mia', 'italian')
res_2 = Restaurant('Sushito', 'japanese')
res_3 = Restaurant('Chez Ma Cuisine', 'french')

res_1.describe_restaurant()
res_2.describe_restaurant()
res_3.describe_restaurant()
