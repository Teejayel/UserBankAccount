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
            if not User.search_names(user): # Takes in a username and checks if it exists in the user's list
                # if the user doesn't exist, it offers to make a new account
                print("\nNo account with that Username exists")
                answer = ""
                while answer != "Y" and answer != "N": 
                    #Loop requires Y or N for an answer. If Y, go to create account method. Otherwise start again
                    answer = input("Would you like to create a user account? (Y or N): ")
                    if answer == "Y":
                        Atm.new_account()
            else: # If a valid user is entered, they are sent to the options list
                Atm.options(user)

    @staticmethod
    def new_account():
        # Takes a user through making a new account
        # Makes user retry if a username or email already exists
        name = ""
        email = ""
        while name == "": # Loop to make sure an unused username is entered
            name = input("Create a username ('exit' to cancel): ")
            if name == "exit":
                return
            if User.search_names(name):
                print("\nThis username is already used, please try a another one")
                name = ""
        while email == "": # Loop to make sure an unused and valid email is entered
            email = input("Enter email ('exit' to cancel): ")
            if email == "exit":
                return
            if User.search_emails(email):
                print("\nThis email is already associated with an existing account")
                email = ""
            if "@" not in email or ".com" not in email:
                print("\nPlease enter a valid email address")
                email = ""
        User(name, email) #creates the new user account and returns to the starting screen
        print("Thank you for creating an account with Dojo Banking!")

    @staticmethod
    def options(user):
        # This array was a quick and dirty way to have phrases for the account check method
        phrases = ["check the balance of", "deposit in", "withdraw from", "transfer from"]

        while True:
            print(f"\nHello {user}! What would you like to do?\n")
            print("1. Check Balance\n2. Make a Deposit\n3. Make a Withdrawal\n4. Transfer Money\n5. Exit")
            selection = input("Enter the number of your selection: ")
            # User selects an option that must be one of the numeric options. 
            # If it's not numeric, it will return to ask for a selection again.
            if selection.isnumeric():
                selection = int(selection)

                if selection == 5: # This cancels the function and returns to starting screen if exit is selected
                    return
                if selection < 5:
                    # Account to preform an action on is selected next
                    account_type = Atm.which_account(phrases[selection - 1])
                    amount = ""
                    # Amount for action is selected next, given that action wasn't to display balance
                    if selection != 1:
                        amount = Atm.how_much(selection - 2, user, account_type)
                    if account_type == "exit" or amount == 0:
                        continue
                    if selection == 4:
                        # Transfer function was trickier and required more pre-work before sending to the User class.
                        Atm.transfer(user, account_type, amount)
                    else:
                        # Sends the action, username, selected account, and amount to list of actions in User class
                        User.selected_action(selection - 1, user, account_type, amount)
                    while selection != "Y" and selection != "N": 
                        # This loop allows user to select another action or return to start screen
                        selection = input("\nWould you like to do something else? (Y or N): ")
                        if selection == "N":
                            return

    @staticmethod
    def which_account(str): # Function to select which account to use.
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
    def how_much(option, user, account): # Function to enter how much money will be used
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
        # These first conditionals are set up in case the user wants to transfer to their own account
        # They've already chosen one account, so they can only transfer to the other by default.
        if account1 == "Savings":
            account2 = "Checking"
        else:
            account2 = "Savings"
        while True: # First selection is transfer to their own account or another user
            print("\nSelect option to transfer to.")
            print(f"1. {account2} Account\n2. Another User\n3. Cancel")
            selection = input("Enter the number for your selection: ")
            if selection.isnumeric():
                selection = int(selection)
                if selection == 3: # Returns to main menu
                    return 
                if selection == 1: # Transfers to current users other account
                    User.make_transfer(user1, account1, user1, account2, amount)
                    return
                if selection == 2: # This asks for the other user, forces a retry if user doesn't exist
                    while True:
                        user2 = input("\nEnter the user to transfer to ('exit' to cancel): ")
                        if user2 == "exit":
                            return
                        if not User.search_names(user2):
                            print("\nThere is no account with this user name.")
                        else:
                            account2 = Atm.which_account(f"transfer to for {user2}") # Selects the user's account to transfer to
                            User.make_transfer(user1, account1, user2, account2, amount)
                            return

            
        

