def greet_user():  # function definition
    # body of the function
    """Display a simple greeting"""  # docstring - describes the function
    print("Hello!")  # only line of actual code


greet_user()

# Passing Information to a Function


def greet_user_mod(username):  # parameter - piece of information needed
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")


greet_user_mod('jesse')  # argument - value we want the function to work with
