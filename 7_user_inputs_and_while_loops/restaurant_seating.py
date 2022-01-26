restaurant_seating = input("How many people are there in your dinner group? ")
restaurant_seating = int(restaurant_seating)

if restaurant_seating > 8:
    print(f"\nI'm sorry, but you'll have to wait for a table!")
else:
    print(f"\nOk, your table is ready!")

