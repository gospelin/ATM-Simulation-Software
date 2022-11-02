"""
This is the user module.

This module is concerned with registering and validating user credentials.
"""

import sys
from atm.register import register_user_name, register_user_password
from atm.atm_card import AtmCard
#from atm.atm_prompt import prompt
import atm.atm_prompt


# Creates an ATM Card instance for a new user
new_user = AtmCard()


#   Registration of new user --> Prompt(1)
def register_user():
    """_summary_
    """
    register_user_name(new_user)
    register_user_password(new_user)

    if new_user.first_name and new_user.password:
        print(f"Welcome {new_user.first_name} {new_user.last_name}! \
            You have successfully registered\n")
    call_next_action()


#   Check User details --> Prompt(2)
def check_details():
    """_summary_"""
    print(f"Your user name is: {new_user.first_name} {new_user.last_name} \n"
        f"Your password is: {new_user.password}")
    if new_user.first_name is None or new_user.last_name is None or new_user.password is None:
        print("User details not set..... ")
    call_next_action()


def change_password():
    """_summary_"""
    old_password = int(input("Enter the old password: "))
    if old_password == new_user.password:
        register_user_password(new_user)
        print("New password registered successfully ")
        call_next_action()
    else:
        print(new_user.password)
        print("Password Mismatch")
        call_next_action()

def deposit_cash():
    """_summary_"""


def withdraw_cash():
    """_summary_
    """


def check_balance():
    """_summary_"""


def call_next_action():
    """_summary_"""
    next_action = input("Do you want to perform another operation (y = yes): ")
    if next_action.lower() == 'y' or next_action.lower == 'yes':
        prompt()
    else:
        print("Exiting program.....")
        sys.exit()
