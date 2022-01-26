# Write a program that prompts for the user’s favorite number.
# Use json.dump() to store this number in a file. Write a separate program
# that reads in this value and prints the message,
# “I know your favorite number! It’s _____.”
import json

favorite_number = input("Tell me your favorite number: ")

filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)
    print(f"I'll remember that your favorite number is {favorite_number}!")
