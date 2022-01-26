"""A class that can be used to describe admins and their privileges."""


from user import User


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
