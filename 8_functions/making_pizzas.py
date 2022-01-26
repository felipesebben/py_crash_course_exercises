import pizza
# Importing specific Functions
from pizza import make_pizza
# Using 'as' to Give a Function an Alias
from pizza import make_pizza as mp
import pizza as p
# Importing All Functions in a Module
# from pizza import *

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


make_pizza(8, 'calabrese')


mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
