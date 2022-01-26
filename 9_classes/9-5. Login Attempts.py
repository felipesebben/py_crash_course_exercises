# Add an attribute called login_attempts
# Write a method called increment_login _attempts()
# that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets
# the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times.
# Print the value of login_attempts to make sure it was incremented properly,
# and then call reset_login_attempts().
# Print login_attempts again to make sure it was reset to 0.

class User:
    """A class that prints user's first and last name."""
    def __init__(
            self, first_name, last_name,
            username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print(" Username: " + self.username)
        print(" Email: " + self.email)
        print(" Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Add the amount of times a user tried to login."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0


felipe = User(
    'felipe', 'sebben', 'f_sebben',
    'f_sebben@example.com', 'porto alegre')
felipe.describe_user()
felipe.greet_user()

print("\nMaking 3 login attempts...")
felipe.increment_login_attempts()
felipe.increment_login_attempts()
felipe.increment_login_attempts()
print(" Login attempts: " + str(felipe.login_attempts))

print("Resetting login attempts...")
felipe.reset_login_attempts()
print(" Login attempts:" + str(felipe.login_attempts))
