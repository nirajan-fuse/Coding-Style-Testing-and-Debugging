"""This module contains a function for adding data to a JSON file."""

# Create a function add_to_json that takes a filename and a new_data as
# input. The function should read the JSON data from the file, add the
# new new_data to it, and write the updated data back to the same file.

# Sample Json:
# [
#   {
#     "name": "Ram",
#     "age": 30
#   },
#   {
#     "name": "Sita",
#     "age": 25
#   }
# ]

import json


def add_to_json(filename: str, new_data: dict):
    """
    Add new data to a JSON file.

    This function reads data from the specified JSON file, adds the new
    data to it, and then writes the updated data back to the file. If
    the file does not exist, it creates a new JSON file with the provided
    data.

    Parameters
    ----------
    filename : str
        The name of the JSON file to which data will be added or created.
    new_data : dict
        The new data to be added to the JSON file.

    Returns
    -------
    None
    """
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open(filename, "w", encoding="UTF-8") as new_file:
            data_list = [new_data]
            json.dump(data_list, new_file, indent=4)
            return

    data.append(new_data)

    with open(filename, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)


data_1 = {"Name": "Shyam", "Age": 23}

add_to_json("data.json", data_1)
