class BankAccount:

    accounts = []

    def __init__(self, interest, balance = 0):
        self.interest= interest
        self.balance = balance
        BankAccount.accounts.append(self)

    @classmethod
    def display_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self, user, account):
        print(f"\nUser {user}: {account} Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest
        return self

# account1 = BankAccount(.01)
# account2 = BankAccount(.02, 100)

# account1.deposit(1000).deposit(400).deposit(6900).withdraw(4500).yield_interest().display_account_info()
# account2.deposit(2000).deposit(10000).withdraw(500).withdraw(600).withdraw(4000).withdraw(3000).yield_interest().display_account_info()

# BankAccount.display_all_accounts()