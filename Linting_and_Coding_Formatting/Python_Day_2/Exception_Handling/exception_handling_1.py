"""This module contains a function for division."""

# Write a Python program that takes two integers as input and performs
# division (num1 / num2).
# Handle the ZeroDivisionError and display a custom error message when the
# second number is zero.


def division(num1: int | float, num2: int | float) -> float:
    """
    Divide two numbers.

    Parameters
    ----------
    num1 : int or float
        The numerator.
    num2 : int or float
        The denominator.

    Returns
    -------
    float
        The result of dividing num1 by num2.

    Raises
    ------
    ZeroDivisionError
        If num2 is zero.
    """
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "ZeroDivisionError: Cannot divide by zero."


print(division(45, 8))

print(division(4, 0))
