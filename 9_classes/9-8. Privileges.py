# Write a separate Privileges class. The class should have one attribute,
# privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class.
# Make a Privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges

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


class Admin(User):
    """A user with administrative privileges."""

    def __init__(
            self, first_name, last_name,
            username, email, location):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to the adminsitrator.
        """
        super().__init__(
                first_name, last_name,
                username, email, location)

        # Initialize  an empty set of privileges.
        self.privileges = Privileges()

    def show_privileges(self):
        """Print a list of admin privileges."""
        print("\nThe adminstrator has the following privileges:")
        for privilege in self.privileges:
            print("- " + privilege.capitalize() + ";")


class Privileges():
    """Display privileges of the user administrator."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege.capitalize()};")
        else:
            print("- This user has no privileges.")


felipe = Admin('felipe', 'sebben', 'f_sebben', 'fsebben@k.com', 'porto alegre')
felipe.describe_user()

felipe_privileges = [
    'can add post',
    'can delete post',
    'can delete user',
    ]

felipe.privileges.privileges = felipe_privileges
felipe.privileges.show_privileges()
