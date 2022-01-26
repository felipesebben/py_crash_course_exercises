def describe_city(city, country= 'niger'):
    """Displays city and country"""
    print(f"{city.title()} is in {country.title()}.")

describe_city('niamey')
describe_city(country='brazil', city='sao paulo')
describe_city('paris', 'france')
