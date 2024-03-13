"""
This module defines classes for managing bank accounts and customers.
"""

# Build a Python class to represent a simple banking system. Create a class for a BankAccount,
# and another for Customer. The BankAccount class should have a constructor to initialize the
# account details (account number, balance, account type). The Customer class should have a
# constructor to set the customer's details (name, age, address) and create a BankAccount
# object for each customer. Implement a destructor for both classes to display a message when
# objects are destroyed.


class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        account_number (int): The unique account number.
        balance (float): The current balance of the account.
        account_type (str): The type of the account, e.g., "Saving" or "Checking".
    """

    def __init__(self, account_number, balance, account_type):
        """
        Initializes a BankAccount object with the given attributes.

        Args:
            account_number (int): The unique account number.
            balance (float): The initial balance of the account.
            account_type (str): The type of the account, e.g., "Saving" or "Checking".
        """
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        """
        Destructor method called when the object is deleted.
        """
        print("Account deleted.")


class Customer:
    """
    A class to represent a bank customer.

    Attributes:
        name (str): The name of the customer.
        age (int): The age of the customer.
        address (str): The address of the customer.
        bank_account (BankAccount): The bank account associated with the customer.
    """

    def __init__(self, name, age, address, account_number, balance, account_type):
        """
        Initializes a Customer object with the given attributes.

        Args:
            name (str): The name of the customer.
            age (int): The age of the customer.
            address (str): The address of the customer.
            account_number (int): The unique account number.
            balance (float): The initial balance of the account.
            account_type (str): The type of the account, e.g., "Saving" or "Checking".
        """
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = BankAccount(account_number, balance, account_type)

    def __del__(self):
        """
        Destructor method called when the object is deleted.
        """
        print("Customer deleted.")


customer_1 = Customer("Nirajan", 24, "Hattiban", 12345, 1000, "Saving")

print(f"{customer_1.name}'s account balance: Rs.{customer_1.bank_account.balance}")
