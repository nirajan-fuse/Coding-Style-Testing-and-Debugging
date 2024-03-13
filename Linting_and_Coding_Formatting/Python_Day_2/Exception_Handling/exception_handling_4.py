"""This module contains functions for division with user input."""

# Write a Python program that takes two integers as input and performs
# division (num1 / num2). Handle both ValueError (if non-integer input)
#  and ZeroDivisionError and display appropriate error messages.


def division_with_input():
    """
    Perform division operation on two user-input integers.

    Returns:
    str: A message indicating the result of the division operation if successful.

    Raises:
    ValueError: If the user inputs are not valid integers.
    ZeroDivisionError: If the second number is zero.
    """
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        return f"Result of division: {result}"
    except ValueError:
        return "Error: Please enter integers only."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


print(division_with_input())
