import json

favorite_number = input("Tell me your favorite number: ")

filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)
    print(f"I'll remember that your favorite number is {favorite_number}!")
