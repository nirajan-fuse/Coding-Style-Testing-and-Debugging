"""This module contains classes and functions for password and age validation."""

# Implement a program that reads user input for a password. Create a
# custom exception WeakPasswordError to handle cases where the password
# is shorter than 8 characters.


class WeakPasswordException(Exception):
    "Raised when password is shorter than 8 characters."


def password_validation():
    """
    Validate the strength of a password.

    This function prompts the user to enter a password and checks if its
    length is at least 8 characters. If the password is shorter than 8
    characters, it raises a WeakPasswordException.

    Parameters
    ----------
    None

    Returns
    -------
    str
        A message indicating whether the password is valid or error message.

    Raises
    ------
    WeakPasswordException
        If the password is shorter than 8 characters.
    """
    try:
        password = input("Enter a password: ")
        length = len(password)
        if length < 8:
            raise WeakPasswordException
        return "Password is valid."
    except WeakPasswordException:
        return "WeakPasswordError: Password cannot be shorter than 8 characters!"


print(password_validation())
