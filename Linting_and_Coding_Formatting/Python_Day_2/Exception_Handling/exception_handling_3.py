"""This module contains functions for user input manipulation."""

# Write a Python program that takes a user input and converts it to an
# integer. Handle the ValueError and display a custom error
# message when the input cannot be converted to an integer.


def convert_to_integer():
    """
    Convert user input to an integer.

    This function prompts the user to enter a number and attempts to convert
    the input to an integer. If the input cannot be converted to an integer,
    it raises a ValueError.

    Parameters
    ----------
    None

    Returns
    -------
    int or str
        The integer representation of the user input, or an error message if
        the input cannot be converted.

    Raises
    ------
    ValueError
        If the user input cannot be converted to an integer.
    """
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        return "Error: Cannot convert to integer!"


print(convert_to_integer())
