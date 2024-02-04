class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. Current balance is {self.balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal of {amount} accepted. Current balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

# Test the Account class
if __name__ == "__main__":
    # Instantiate the account
    my_account = Account("John")

    # Make several deposits
    my_account.deposit(100)
    my_account.deposit(50)

    # Make several withdrawals
    my_account.withdraw(30)
    my_account.withdraw(80)
    my_account.withdraw(60)
