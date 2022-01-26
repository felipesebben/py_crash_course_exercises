usernames = ['admin','Jones','Livia','Rebecca','Mikonos']

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for loggin in again.")
else:
    print("\nWe need to find some users!")
