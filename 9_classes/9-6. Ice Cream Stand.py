# Write a class called that inherits the `Restaurant`  from Exercise 9-4.
# Add attribute called `IceCreamStand` that stores a list of ice cream flavors.
# Write a method that displays flavors these flavors.
# Create an instance # of IceCreamStand, and call this method.

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints restaurant name and cuisine type."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        msg = self.name + " is open!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """A simple attempt to describe an ice cream stand."""

    def __init__(self, name, cuisine_type='ice cream'):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Print a list of flavors avaliable."""
        print("\nWe have the following ice cream flavors:")
        for flavor in self.flavors:
            print("- " + flavor.title())


my_stand = IceCreamStand("Tony's Wonderful Gelattos")
my_stand.flavors = ['strawberry', 'blueberry', 'pistacchio', 'chocolate']

my_stand.describe_restaurant()
my_stand.show_flavors()
