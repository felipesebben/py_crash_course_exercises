person1 = {
    'first_name': 'livia',
    'last_name': 'adams',
    'age': 30,
    'city': 'porto alegre',
}
first_name = person1['first_name'].title()
last_name = person1['last_name'].title()
age = person1['age']
city = person1['city'].title()

print(f"The person's name is {first_name}.")
print(f"Her last name is {last_name}.")
print(f"She is {age} years old.")
print(f"She lives in {city}.")


person2 = {
    'first_name': 'michael',
    'last_name': 'scott',
    'age': 45,
    'city': 'scranton',
}

person3 = {
    'first_name': 'dwight',
    'last_name': 'schrute',
    'age': 40,
    'city': 'scranton',
}
 
people = [person1, person2, person3]

for person_value in people:
    first_name = f"{person_value['first_name']}"
    full_name = f"{person_value['first_name']} {person_value['last_name']}"
    age = person_value['age']
    city = person_value['city']
    if person_value['first_name'] == 'livia':
        print(f"\nThis is what I know about {first_name.title()}:")
        print(f"\tHer full name is {full_name.title()}.")
        print(f"\tShe is {age} years old and lives in {city.title()}.")
    else:
        print(f"\nThis is what I know about {first_name.title()}:")
        print(f"\tHis full name is {full_name.title()}.")
        print(f"\tHe is {age} years old and lives in {city.title()}.")
    
