"""This module contains a function for searching for keyword in a log file."""

# Create a function search_log that takes a log file and a search
# keyword as input. The function should find and display all lines
# containing the search keyword.

# import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="log.log",
#     filemode="w",
#     format="%(asctime)s - %(levelname)s - %(message)s",
# )


# logging.info("Searching")
# logging.warning("The file is already in use!")
# logging.error("An error occurred!")


def search_log(log_file, keyword):
    """
    Search for a keyword in a log file and print matching lines.

    This function opens the specified log file, reads it line by line, and prints
    any lines that contain the specified keyword.

    Parameters
    ----------
    log_file : str
        The path to the log file to be searched.
    keyword : str
        The keyword to search for in the log file.

    Returns
    -------
    None
    """
    try:
        with open(log_file, "r", encoding="UTF-8") as file:
            for line in file:
                if keyword in line:
                    print(line)
    except FileNotFoundError:
        print("Error: File not found!")


search_log("log.log", "WARNING")
