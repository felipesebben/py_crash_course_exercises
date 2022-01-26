favorite_places = {
    'livia': ['london', 'garopaba', 'sao paulo'],
    'felipe': ['porto alegre', 'geneva', 'new york'],
    'rafael': ['gravatai','picada cafe'],
    'barberina': ['santa terezinha'],
}

for name, cities in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for city in cities:
        print(f"\t{city.title()}") 
    