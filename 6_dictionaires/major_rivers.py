major_rivers = {
    'amazon': 'brazil',
    'nile': 'egypt',
    'mississipi': 'USA',
}

for river, country in major_rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")

for river in major_rivers.keys():
    print(river.title())

for country in major_rivers.values():
    print(country.title())