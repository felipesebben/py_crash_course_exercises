from admin import Admin

felipe = Admin('felipe', 'sebben', 'fsebben', 'fsebben@joj.com', 'garopaba')
felipe.describe_user()

felipe_privileges = [
    'create new accounts',
    'suspend user accounts',
    'change the website interface',
    'sing sade'
]

felipe.privileges.privileges = felipe_privileges

print(f"\nThe admin {felipe.username} has these privileges: ")
felipe.privileges.show_privileges()
