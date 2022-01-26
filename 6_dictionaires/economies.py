economies = {
    'china': {
        'GDP': 14000000000000,
        'GDP rank': '2nd',
        'GDP per capita': 11819,
        'sector': 'industrial',
        'dynamic city': 'shangai'
        },
    'the united states': {
        'GDP': 22000000000000,
        'GDP rank': '1st',
        'GDP per capita': 68309,
        'sector': 'services',
        'dynamic city': 'new york',
        },
    'brazil': {
        'GDP': 1400000000000,
        'GDP rank': '11st',
        'GDP per capita': 7061,
        'sector': 'services',
        'dynamic city': 'sao paulo'
        }
    }

for country, economy_info in economies.items():
    GDP = economy_info['GDP']
    GDP_rank = economy_info['GDP rank']
    GDP_per_cap = economy_info['GDP per capita']
    sector = economy_info['sector']
    dyn_city = economy_info['dynamic city']

    print("\n" + country.title() + "'s GDP is " + str(GDP) + ".")
    print(" It is the " + GDP_rank + " economy of the world in size.")
    print(" Its GDP per capita is " + str(GDP_per_cap) + ".")
    print(" Its " + sector + " sector is very dynamic, while " + dyn_city.title() + " is one of its most economically relevant cities.")
