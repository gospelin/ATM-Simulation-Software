import user


# Display a Welcome prompt message
def prompt():
    menu = "Welcome to GIGO Bank....".upper() + \
        """
        Select an Option: 
        1.  Register a new user: 
        2.  Check User Details:  
        3.  Change password: 
        4.  Deposit Cash:
        5.  Withdraw Cash:
        6.  Check Balance:
        7.  Quit
        """
    print(f"{menu}")
    reply = input()
    while not reply.isdigit():
        print(menu)
        reply = input()
    reply = int(reply)

    while not (0 < reply <= 7):
        print("Invalid Input.....")
        print(menu)
        reply = int(input())

    if reply == 1:
        # Register the users
        user.register_user()
    elif reply == 2:
        user.check_details()
    elif reply == 3:
        user.change_password()
    elif reply == 4:
        user.deposit_cash()
    elif reply == 5:
        user.withdraw_cash()
    elif reply == 6:
        user.check_balance()
    else:
        print("Exiting program.....")
        user.exit()
