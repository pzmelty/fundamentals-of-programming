class BankAccount:

    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds on the account")

    def display_info(self):
        print("Bank Account No:", self.account_number)
        print("Balance: PLN", f"{self.balance:.2f}".replace(".", ","))


# Main program

# Create a bank account
account = BankAccount("12 3456 5555 9090 1111 0000 7722")

# Display account balance
account.display_info()
print()

# Deposit PLN 25.30
account.deposit(25.30)

# Display account balance
account.display_info()
print()

# Withdraw PLN 31.70
account.withdraw(31.70)

# Display account balance
account.display_info()
print()

# Withdraw PLN 14
account.withdraw(14)

# Display account balance
account.display_info()
