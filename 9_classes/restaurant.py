"""A class that can be used to describe a restaurant."""


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints restaurant name and cuisine type."""
        msg = self.name.title() + " serves " + self.cuisine_type + " food."
        print("\n" + msg)

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        msg = self.name.title() + " is open!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served
