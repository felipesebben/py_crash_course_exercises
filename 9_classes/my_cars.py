# Importing multiple classes from a module:

from car import Car, ElectricCar

my_alfa = Car('alfa romeo', 'giulietta', '2020')
print(my_alfa.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', '2021')
print(my_tesla.get_descriptive_name())
