"""This module contains functions and exceptions for age validation."""

# Write a Python program that takes user input for age. Create a custom
# exception InvalidAgeError to handle cases where the age is below 0 or
# above 120.


class InvalidAgeException(Exception):
    "Raised when the input value is below 0 or above 120."


def age_validation():
    """
    Validate the age entered by the user.

    This function prompts the user to enter an age and checks if it is within
    the valid range of 0 to 120. If the age is not within this range, it
    raises an InvalidAgeException.

    Parameters
    ----------
    None

    Returns
    -------
    str
        A message indicating whether the age is valid or an error message.

    Raises
    ------
    InvalidAgeException
        If the age is below 0 or above 120.
    """
    try:
        age = int(input("Enter the age:"))
        if not 0 < age <= 120:
            raise InvalidAgeException
        return "Age is valid."
    except InvalidAgeException:
        return "InvalidAgeError: Age cannot be below 0 or above 120!"


print(age_validation())
