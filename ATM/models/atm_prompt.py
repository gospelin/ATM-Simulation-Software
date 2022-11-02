"""_summary_
"""

import sys
from .user import check_details,\
    change_password, create_user, deposit_cash, withdraw_cash, check_balance


# Display a Welcome prompt message
def prompt():
    """_summary_"""
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

    while not 0 < reply <= 7:
        print("Invalid Input.....")
        print(menu)
        reply = int(input())

    match reply:
        case 1:
            create_user()
        case 2:
            check_details()
        case 3:
            change_password()
        case 4:
            deposit_cash()
        case 5:
            withdraw_cash()
        case 6:
            check_balance()
        case _:
            print("Exiting program.....")
            sys.exit()
