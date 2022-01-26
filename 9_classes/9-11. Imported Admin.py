from user import Admin


john = Admin('john', 'smith', 'jsmith', 'smith@okok.com', 'las vegas')
john.describe_user()

john_privileges = [
    'can reset passwords',
    'can delete accounts',
    'can accept new users'
]

john.privileges.privileges = john_privileges

print(f"\nThe admin {john.username} has these privileges: ")
john.privileges.show_privileges()
