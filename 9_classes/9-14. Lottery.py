from random import choice

lottery_list = [1, 2, 3, 4, 9, 7, 10, 23, 12, 11, 'a', 'f', 'g', 'q', 'd']

winning_ticket = []
print("Let's see who's the lucky winner:")

# As we don't want repeated numbers, let's use a while loop.
while len(winning_ticket) < 4:
    pulled_item = choice(lottery_list)

    # Only add the pulled item to the winning ticket if it hasn't
    # already been pulled.
    if pulled_item not in winning_ticket:
        print(f" We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)
        print(f"\nThe final winning ticket is: {winning_ticket}")
