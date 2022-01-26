sandwich_orders = ['pastrami', 'blt', 'ham and cheese', 'meat ball', 'vegetarian']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"Verifying that you've ordered a {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("The following sandwiches were ordered:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())