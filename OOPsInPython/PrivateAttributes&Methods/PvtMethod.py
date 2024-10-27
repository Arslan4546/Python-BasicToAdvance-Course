# Private Methods
# Private methods are created similarly by adding two underscores (__) as a prefix to the method name. This restricts the method's use to only within the class and prevents it from being called from outside the class.

# Example of Private Method:

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    # Public method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__log_transaction("Deposit", amount)  # Calling private method
        else:
            print("Deposit amount must be positive.")

    # Private method
    def __log_transaction(self, transaction_type, amount):
        print(f"{transaction_type} of {amount} recorded for account {self.__account_number}.")

# Creating an instance of BankAccount
account = BankAccount("12345", 100)

# Using the public method, which internally calls the private method
account.deposit(50)  # Output: "Deposit of 50 recorded for account 12345."

# Attempt to directly call private method (will raise an AttributeError)
# account.__log_transaction("Withdrawal", 30)  # Uncommenting this will cause an error


# In this example:

# __log_transaction is a private method and cannot be called directly from outside the BankAccount class.
# It’s accessible only within the class, allowing secure logging of transactions.
# Key Takeaways
# Private attributes and methods are denoted by a double underscore prefix (__).
# They are only accessible within the class where they are defined.
# This concept is useful for encapsulation, protecting data and methods from external access and modification.