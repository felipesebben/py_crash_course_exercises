name = input("Please enter your name: ")
print(f"\nHello, {name}!")

#You can assign your prompt to a variable and pass that variable to input() function:
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}!")