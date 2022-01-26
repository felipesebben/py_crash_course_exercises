# You can use a loop to see how hard it might be to win the kind
# of lottery you just modeled. Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins.
# Print a message reporting how many times the loop had to run
#  to give you a winning ticket.

from random import choice


def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # As we don't want repeated numbers, let's use a while loop.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

    # Only add the pulled item to the winning ticket if it hasn't
    # already been pulled.
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)

    return winning_ticket


def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the
    # winning ticket, return false.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We gotta have a winning ticket!
    return True


def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # As we don't want repeated numbers, let's use a while loop.
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

    # Only add the pulled item to the winning ticket if it hasn't
    # already been pulled.
    if pulled_item not in ticket:
        ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 9, 7, 10, 23, 12, 11, 'a', 'f', 'g', 'q', 'd']

winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of attempts, otherwise it will take forever!
max_tries = 100_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
