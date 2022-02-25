from sys import exit
from register import register_user_name, register_user_password
import ATM_CARD
import ATM_prompt


# Creates an ATM Card instance for a new user
new_user = ATM_CARD.AtmCard()


#   Registration of new user --> Prompt(1)
def register_user():
    register_user_name(new_user)
    register_user_password(new_user)

    if new_user.get_user_name() and new_user.get_password():
        print(f"Welcome {new_user.get_user_name()}! You have successfully registered\n")
    call_next_action()


#   Check User details --> Prompt(2)
def check_details():
    print(f"Your user name is: {new_user.get_user_name()} \n"
          f"Your password is: {new_user.get_password()}")
    if new_user.get_user_name() is None or new_user.get_password() is None:
        print("User details not set..... ")
    call_next_action()


def change_password():
    old_password = int(input("Enter the old password: "))
    if old_password == new_user.get_password():
        register_user_password(new_user)
        print("New password registered successfully ")
        call_next_action()
    else:
        print(new_user.get_password())
        print("Password Mismatch")
        call_next_action()
    pass


def deposit_cash():
    pass


def withdraw_cash():
    pass


def check_balance():
    pass


def call_next_action():
    next_action = input("Do you want to perform another operation (y = yes): ")
    if next_action.lower() == 'y' or next_action.lower == 'yes':
        ATM_prompt.prompt()
    else:
        print("Exiting program.....")
        exit()
