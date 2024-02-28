#  Write a Python program that simulates a banking system. Implement a class called BankAccount with methods to
#  initialize an account with a starting balance, withdraw funds,
#  and handle a custom exception called NegativeBalanceError when the account balance goes below zero.


class NegativeBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                raise NegativeBalanceError("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

if __name__ == "__main__":
    # Example usage of BankAccount class
    account = BankAccount(1000)  # Starting balance $1000
    try:
        account.deposit(500)
        account.withdraw(200)
        account.withdraw(1500)  # This should raise NegativeBalanceError
    except NegativeBalanceError as e:
        print("Error:", e)
