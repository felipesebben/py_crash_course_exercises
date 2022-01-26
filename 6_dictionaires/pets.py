pet1 = {
    'animal': 'dog',
    'owner': 'john',
}

pet2 = {
    'animal': 'cat',
    'owner': 'angela',
}

pet3 = {
    'animal': 'hamster',
    'owner': 'andrew',
}

pet4 = {
    'animal': 'python',
    'owner': 'voldemort',
}

pet5 = {
    'animal': 'guinea pig',
    'owner': 'james',
}
pets = [pet1, pet2, pet3, pet4, pet5]

for category in pets:
    animal = category['animal']
    owner = category['owner']
    print(f"\nThe animal is a {animal}.")
    print(f"Its owner's name is {owner.title()}")
    
