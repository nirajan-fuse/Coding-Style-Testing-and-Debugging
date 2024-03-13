"""This module contains functions for displaying file."""

# Implement a program that takes user input for a filename, opens the file
# in read mode, and displays its contents.
# Handle the FileNotFoundError and display an error message if the file is
# not found.


def display_file_content():
    """
    Display the content of a file.

    This function prompts the user to enter a filename, then attempts to open
    and read the content of the file. If the file is not found, it raises a
    FileNotFoundError.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Raises
    ------
    FileNotFoundError
        If the specified file is not found.
    """
    try:
        filename = input("Enter the filename: ")
        with open(filename, "r", encoding="UTF-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: File not found!")


display_file_content()
