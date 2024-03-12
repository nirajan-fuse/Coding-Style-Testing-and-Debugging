# Create a function that validates email addresses based on following set of
# rules:
# Proper email format such as presence of “@”, no space in the address
# Presence of valid email providers such as yahoo, gmail and outlook. Make sure
# there are no disposable email providers such as yopmail.
# Write unit tests to validate different email addresses against the rules,
# including valid and invalid addresses (Use unittest module).

import re


def validate_email(email):
    """
    Validates an email address based on specified rules.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    # Check if email matches the format
    if not re.match(email_regex, email):
        return False

    valid_providers = ["yahoo", "gmail", "outlook"]
    domain = email.split("@")[1]
    provider = domain.split(".")[0]

    if provider in valid_providers:
        return True
    return False
