#Write a function that stores information about a car in a dictionary.
#The function should always receive a manufacturer and a model name. It
#should then accept an arbitrary number of keyword arguments. Call the function
#with the required information and two other name-value pairs, such as a
#color or an optional feature. Your function should work for a call like this one:

"""
car = make_car('subaru', 'outback', color='blue', tow_package=True)
"""

def make_car(manufacturer, model, *color, **car_info):
    "Build a dictionary containing everything we know about a car."
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', 
               color='blue', 
               tow_package=True)
print(car)
