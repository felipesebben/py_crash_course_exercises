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


res_1 = Restaurant("Sbarro", "italian")
print(f"\nThe restaurant is called {res_1.restaurant_name}.")
print(f"It is known for its {res_1.cuisine_type} cuisine.")

res_1.describe_restaurant()
res_1.open_restaurant()


res_1.cuisine_type
