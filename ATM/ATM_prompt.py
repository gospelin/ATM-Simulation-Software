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

    match reply:
        case 1:
            user.register_user()
        case 2:
            user.check_details()
        case 3:
            user.change_password()
        case 4:
            user.deposit_cash()
        case 5:
            user.withdraw_cash()
        case 6:
            user.check_balance()
        case _:
            print("Exiting program.....")
            user.exit()
