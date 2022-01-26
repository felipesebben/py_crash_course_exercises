favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#looping through all key-value pairs:
for name, language in favorite_languages.items(): #keys() is optional
    print(f"\n{name.title()}'s favorite language is {language.title()}.")

#looping through all the keys in a dictionary:
for name in favorite_languages.keys():
    print(name.title())    

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")

#looping through a dictionary's keys in a particular order:
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#looping through all values in a dictionary:
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#avoiding repeated results:
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

list_people = ['erin','mark','phil','felicia']

for name in list_people:
    if name in favorite_languages.keys():
        print(f"Thank you for having taken the poll, {name.title()}.")
    else:
        print(f"Please, take the poll, {name.title()}!")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(language) < 2:
        print(f"\n{name.title()}'s language is:")
    else:
        print(f"\n{name.title()}'s languages are:")
    for language in languages:
        print(f"\t{language.title()}")