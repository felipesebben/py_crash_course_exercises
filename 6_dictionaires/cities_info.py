cities = {
    'porto alegre': {
        'country' : 'brazil',
        'population': 1492530,
        'fact': 'southernmost regional capital'
        },
    'montevideo': {
        'country': 'uruguay',
        'population': 1310000,
        'fact': 'country capital'},
    'london': {
        'country': 'united kingdom',
        'population': 8900000, 
        'fact': '3rd most populated european city'},
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']

    print("\n" + city.title() + " is in " + country + ".")
    print(" It has a population of about " + str(population) + ".")
    print(" Fun fact: it is the " + fact + "." )  