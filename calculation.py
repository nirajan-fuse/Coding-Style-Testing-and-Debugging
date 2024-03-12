# Design a function that takes a list of numerical data and performs
# calculations for mean, median and standard deviation. Write unit tests to
# verify the correctness of the statistical calculations for various inputs,
# including edge cases like an empty list or a list with one element
# (Use unittest module).

import math


def calculate_stats(data):
    """
    Calculates the mean, median, and standard deviation of numerical data.

    Args:
        data (list): A list of numerical data.

    Returns:
        dict: A dictionary containing the mean, median, and standard deviation.
    """
    if not data:
        raise ValueError("Data list cannot be empty")

    n = len(data)

    mean = sum(data) / n

    sorted_data = sorted(data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]

    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)

    return {"mean": mean, "median": median, "std_dev": std_dev}
