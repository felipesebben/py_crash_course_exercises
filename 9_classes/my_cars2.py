# Importing an Entire Module

import car

my_alfa = car.Car('alfa romeo', 'giulietta', '2020')
print(my_alfa.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'model s', '2021')
print(my_tesla.get_descriptive_name())
