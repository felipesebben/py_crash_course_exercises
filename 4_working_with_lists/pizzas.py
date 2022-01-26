pizza_flavours = ['pepperoni','margheritta','quattro formaggi']

for flavour in pizza_flavours:
    print(f"I really like {flavour} pizza.")

print("\nI really love pizza!")

friend_pizzas = pizza_flavours[:]
print(friend_pizzas)

friend_pizzas.append('marinara')
print(friend_pizzas)

print("\nMy favorite pizzas are:")
for pizza in pizza_flavours:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())