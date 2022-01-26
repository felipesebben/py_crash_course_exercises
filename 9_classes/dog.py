class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):  # method that runs when class created
        """Initialize name and age attiributes."""
        self.name = name  # self - required in method def and must come 1st
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# Making an Instance from a Class

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Accessing Attributes
my_dog.name

# Calling Methods
my_dog.sit()
my_dog.roll_over()

# Creating Multiple Instances
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
