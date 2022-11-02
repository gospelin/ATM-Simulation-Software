"""
This is the user module.

This module is concerned with registering and validating user credentials.
"""

import sys
from . import atm_prompt
from .atm_card import AtmCard

new_user = ""

#   Registration of new user --> Prompt(1)
def create_user():
    """_summary_"""
    first_name, last_name = register_user_name()
    password = register_user_password()

    global new_user
    new_user = AtmCard(first_name, last_name, password)

    if new_user.first_name and new_user.password:
        print(
            f"Welcome {new_user.first_name} {new_user.last_name}! \
            You have successfully registered\n"
        )
    call_next_action()


def register_user_name():
    """_summary_"""
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    return first_name, last_name


#   Register user's password
def register_user_password():
    """_summary_

    Args:
        new_user (_type_): _description_
    """
    password = input("Enter a four-digit password: ")
    confirm_password = input("Re-enter password: ")

    #   This checks the password to ensure
    #   1. The length of the password entered and reentered is 4
    #   2. The password and the password reentered is a digit not alphabets or alphanumeric
    #   Thus, while the length of the password and password reentered is not 4
    #   or, the password and the password reentered is a digit

    while not (len(password) and len(confirm_password)) == 4 or not (
        password.isdigit() and confirm_password.isdigit()
    ):
        print("Invalid password, Must be four digit")
        password = input("Enter a four-digit password: ")
        confirm_password = input("Re-enter password: ")

    password = int(password)
    confirm_password = int(confirm_password)

    # If the password is validated accurately assign the
    # password to the user in the ATM_CARD class
    if password == confirm_password:
        return password
    else:
        print("Password Mismatch...... Try again!!!")
        register_user_password()


#   Check User details --> Prompt(2)
def check_details():
    """_summary_"""
    print(
        f"Your user name is: {new_user.first_name} {new_user.last_name} \n"
        f"Your password is: {new_user.password}"
    )
    if (
        new_user.first_name is None
        or new_user.last_name is None
        or new_user.password is None
    ):
        print("User details not set..... ")
    call_next_action()


def change_password():
    """_summary_"""
    old_password = int(input("Enter the old password: "))
    if old_password == new_user.password:
        register_user_password()
        print("New password registered successfully ")
        call_next_action()
    else:
        print(new_user.password)
        print("Password Mismatch")
        call_next_action()


def deposit_cash():
    """_summary_"""


def withdraw_cash():
    """_summary_"""


def check_balance():
    """_summary_"""


def call_next_action():
    """_summary_"""
    next_action = input("Do you want to perform another operation (y = yes): ")
    if next_action.lower() == "y" or next_action.lower == "yes":
        atm_prompt.prompt()
    else:
        print("Exiting program.....")
        sys.exit()
