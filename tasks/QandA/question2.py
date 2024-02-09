# #Python Program to replicate bank transaction: min balance 500, ask user to the amount to withdraw, 
# print the balance amount after withdrawal, if user enters an amount greater than balance: print:: insufficient balance. 
# if balance is below 500 print an alert message : your account balance is "available_balance",
# Please keep your account balance above Rs.500 to avoid unwanted charges.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif self.balance - amount < 500:
            print(f"Your account balance is {self.balance}. Please keep your account balance above Rs. 500 "
                  f"to avoid unwanted charges.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Balance amount: {self.balance}")


initial_balance = 1000
account = BankAccount(initial_balance)

amount_to_withdraw = float(input("Enter the amount to withdraw: "))
account.withdraw(amount_to_withdraw)