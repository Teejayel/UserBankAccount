from bank_account import BankAccount

class User:

    all_users = []

    # All users begin with a checking with no interest, and savings account with 2% interest.
    # Each user created is stored in a class array for retrieval purposes.
    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email
        self.checking = BankAccount(.00, 0)
        self.savings = BankAccount(.02, 0)
        User.all_users.append(self)

    @classmethod # Returns true if the username exists in all_users, else returns false
    def search_names(cls, name):
        for user in cls.all_users:
            if name == user.user_name:
                return True
        return False

    @classmethod # Returns true if the email exists in all_users, else returns false
    def search_emails(cls, email):
        for user in cls.all_users:
            if email == user.email:
                return True
        return False

    @classmethod # Function serves as a switchboard for which instance method will be used
    def selected_action(cls, option, current_user, account, amount):
        for user in cls.all_users:
            if current_user == user.user_name:
                current_user = user
                break
        if option == 0:
            current_user.display_user_balance(account)
        if option == 1:
            current_user.make_deposit(account, amount)
        if option == 2:
            current_user.make_withdrawal(account, amount)


    # All functions below will display account balance before and after the actions.
    # All functions below will also require knowing which account will be accessed.

    @classmethod # Unique function that requires finding two user objects to withdraw and deposit
    # There is probably a better way to deal with one user at a time.
    def make_transfer(cls, user1, account1, user2, account2, amount):
        for user in cls.all_users: 
            if user1 == user.user_name:
                user1 = user
                break
        for user in cls.all_users:
            if user2 == user.user_name:
                user2 = user
                break
        if account1 == "Savings":
            user1.savings.withdraw(amount)
        else:
            user1.checking.withdraw(amount)
        if account2 == "Savings":
            user2.savings.deposit(amount)
        else:
            user2.checking.deposit(amount)
        user1.display_user_balance(account1)
        user2.display_user_balance(account2)


    def make_deposit(self, account, amount):
        if account == "Savings":
            self.savings.deposit(amount)
        else:
            self.checking.deposit(amount)
        self.display_user_balance(account)
        return self

    def make_withdrawal(self, account, amount):
        if account == "Savings":
            self.savings.withdraw(amount)
        else:
            self.checking.withdraw(amount)
        self.display_user_balance(account)
        return self

    def display_user_balance(self, account):
        if account == "Savings":
            self.savings.display_account_info(self.user_name, account)
        else:
            self.checking.display_account_info(self.user_name, account)
        return self




# user1 = User("Samgee", "samgee@email.com")

# user1.display_user_balance().make_deposit(1000).display_user_balance().make_withdrawal(500).display_user_balance()
