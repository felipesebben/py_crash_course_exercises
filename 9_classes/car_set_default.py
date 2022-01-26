# Setting a Default Value for an Attribute
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    # Modifies mileage through method
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('alfa romeo', 'giulietta', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying Attribute Values

# 1.Modifying an Attribute’s Value Directly

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 2. Modifying an Attribute’s Value Through a Method
my_new_car.update_odometer(5)
my_new_car.read_odometer()

# 3. Incrementing an Attribute’s Value Through a Method
