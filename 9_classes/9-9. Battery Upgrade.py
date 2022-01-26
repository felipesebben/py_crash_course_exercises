# - Use the final version of electric_car.py from this section.
# - Add a method to the Battery class called upgrade_battery().
# - It should check the battery size and set capacity to 100 if it isn’t so.
# - Make an electric car with a default battery size, call get_range(), and
# then call get_range() a second time after upgrading the battery.
# - You should see an increase in the car’s range.

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

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Print an upgrade of the battery's size."""
        if self.battery_size == 75:
            self.battery_size = 100
            print("Let's upgrade the battery to 100kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


print("\nChecking the electric car's initial range:")
my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.get_range()

print("\nUpgrade the battery and check its range again.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
