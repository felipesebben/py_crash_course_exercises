# Importing a Module into a Module with Aliases

from car import Car
from electric_car import ElectricCar as EC

my_alfa = Car('alfa romeo', 'giulietta', '2020')
print(my_alfa.get_descriptive_name())

my_tesla = EC('tesla', 'model s', '2021')
print(my_tesla.get_descriptive_name())
