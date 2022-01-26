#Positional Arguments
#Python must match each argument according to the order of parameters.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry') #needs to follow the order 'type' and 'name'

#Multiple Function Calls
describe_pet('parrot', 'fernando')
describe_pet('dog', 'sarah')

#Keyword Arguments
#Name-value pair that you pass to a funcion to avoid confusion.
#You don't have to worry about ordering your arguments.

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

#Default values
#If no argument is provided, Python uses the parameter's default value.

def describe_pet(pet_name, animal_type= 'dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

#simplest way to call the function:
describe_pet('willie')

#To describe an animal other than a dog:
describe_pet(pet_name='jupyter', animal_type='goat')

## Note: When you use default values, any parameter with a 
# default value needs to be listed after all the parameters
#  that don’t have default values


#Equivalent Function Calls




#A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')     

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#Avoiding Argument Errors
def describe_pet(pet_name, animal_type):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()
# TypeError: describe_pet() missing 2 required positional arguments: 'pet_name' and 'animal_type'

