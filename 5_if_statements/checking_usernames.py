current_users = ['Francisca', 'Robert', 'Jair', 'Livia', 'Mariana',
                 'FRANCISCA', 'ROBERT', 'JAIR', 'LIVIA', 'MARIANA']

new_users = ['Jair', 'Mariana', 'ROBERT', 'Felipe', 'Jorge', 'Alice']

for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry, the username {new_user} has been taken, please enter a new username!")
    else:
        print(f"The username {new_user} is available!")