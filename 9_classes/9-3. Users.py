class User:
    """A class that prints user's first and last name."""
    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print(" Username: " + self.username)
        print(" Email: " + self.email)
        print(" Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")


felipe = User(
    'felipe', 'sebben', 'f_sebben',
    'f_sebben@example.com', 'porto alegre')
felipe.describe_user()
felipe.greet_user()

livia = User(
    'livia', 'adams', 'l_adams', 'ladams@iada.com', 'miami'
)

livia.describe_user()
livia.greet_user()
