from user import User

class Atm():
    #This class acts like an ATM terminal for a user to interact with an existing account or create a new one.
    @staticmethod
    def start_atm(): # Turns on the ATM 
        while True: 
            user = ""
            #Used as a while loop to allow retrying without having to recall the function and use more memory
            print("\nWelcome to Dojo Banking ATM")
            user = input("\nEnter Username ('exit' to close session): ")
            if user == "exit":
                print("\nThank you for banking with Dojo Banking!\nGoodbye\n")
                return
            if not User.search_names(user): 
                print("\nNo account with that Username exists")
                answer = ""
                while answer != "Y" and answer != "N": 
                    #Loop requires Y or N for an answer. If Y, go to create account method. Otherwise start again
                    answer = input("Would you like to create a user account? (Y or N): ")
                    if answer == "Y":
                        Atm.new_account()
            else:
                Atm.options(user)

    @staticmethod
    def new_account():
        # Takes a user through making a new account
        # Makes user retry if a username or email already exists
        name = ""
        email = ""
        while name == "":
            name = input("Create a username ('exit' to cancel): ")
            if name == "exit":
                return
            if User.search_names(name):
                print("\nThis username is already used, please try a another one")
                name = ""
        while email == "":
            email = input("Enter email ('exit' to cancel): ")
            if email == "exit":
                return
            if User.search_emails(email):
                print("\nThis email is already associated with an existing account")
                email = ""
            if "@" not in email or ".com" not in email:
                print("\nPlease enter a valid email address")
                email = ""
        User(name, email)
        print("Thank you for creating an account with Dojo Banking!")

    @staticmethod
    def options(user):

        phrases = ["check the balance of", "deposit in", "withdraw from", "transfer from"]

        while True:
            print(f"\nHello {user}! What would you like to do?\n")
            print("1. Check Balance\n2. Make a Deposit\n3. Make a Withdrawal\n4. Transfer Money\n5. Exit")
            selection = input("Enter the number of your selection: ")

            if selection.isnumeric():
                selection = int(selection)

                if selection == 5:
                    return
                if selection < 5:
                    account_type = Atm.which_account(phrases[selection - 1])
                    amount = ""
                    if selection != 1:
                        amount = Atm.how_much(selection - 2, user, account_type)
                    if account_type == "exit" or amount == 0:
                        continue
                    if selection == 4:
                        Atm.transfer(user, account_type, amount)
                    else:
                        User.selected_action(selection - 1, user, account_type, amount)
                    while selection != "Y" and selection != "N": 
                        selection = input("\nWould you like to do something else? (Y or N): ")
                        if selection == "N":
                            return

    @staticmethod
    def which_account(str):
        account = ["Savings", "Checking", "exit"]
        while True:
            print(f"\nSelect the account to {str}: ")
            print("1. Savings\n2. Checking\n3. Cancel")
            selection = input("Enter the number for your selection: ")
            if selection.isnumeric():
                selection = int(selection)
                if 0 < selection < 4:
                    return account[selection - 1]

    @staticmethod
    def how_much(option, user, account):
        phrase = ["deposit", "withdraw", "transfer"]
        while True:
            User.selected_action(0, user, account, 0)
            amount = input(f"\nHow much would you like to {phrase[option]}? ('exit' to cancel): ")
            if amount == "exit":
                return 0
            if amount.isnumeric():
                amount = int(amount)
                return amount


    @staticmethod
    def transfer(user1, account1, amount):
        if account1 == "Savings":
            account2 = "Checking"
        else:
            account2 = "Savings"
        while True:
            print("\nSelect option to transfer to.")
            print(f"1. {account2} Account\n2. Another User\n3. Cancel")
            selection = input("Enter the number for your selection: ")
            if selection.isnumeric():
                selection = int(selection)
                if selection == 3:
                    return
                if selection == 1:
                    User.make_transfer(user1, account1, user1, account2, amount)
                    return
                if selection == 2:
                    while True:
                        user2 = input("\nEnter the user to transfer to ('exit' to cancel): ")
                        if user2 == "exit":
                            return
                        if not User.search_names(user2):
                            print("\nThere is no account with this user name.")
                        else:
                            account2 = Atm.which_account(f"transfer to for {user2}")
                            User.make_transfer(user1, account1, user2, account2, amount)
                            return

            
        

