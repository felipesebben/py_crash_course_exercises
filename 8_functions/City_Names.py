def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())

city = city_country('santiago', 'chile')
print(city)

city = city_country('porto alegre', 'brazil')
print(city)

city = city_country('los angeles', 'united states')
print(city)