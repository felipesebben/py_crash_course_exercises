prompt = "\nPlease enter the name of your pizza toppings: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"You got it, I'll add {topping} to your pizza!")