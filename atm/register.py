"""
Registration module.

This module is concerned with all registration process and prompt
of users and respective cards.
"""


#   Register user's name
def register_user_name(new_user):
    """_summary_

    Args:
        new_user (_type_): _description_
    """
    new_user.first_name = input("Enter First Name: ")
    new_user.last_name = input("Enter Last name: ")


#   Register user's password
def register_user_password(new_user):
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

    while not (len(password) and len(confirm_password)) == 4 \
            or not(password.isdigit() and confirm_password.isdigit()):
        print("Invalid password, Must be four digit")
        password = input("Enter a four-digit password: ")
        confirm_password = input("Re-enter password: ")

    password = int(password)
    confirm_password = int(confirm_password)

    # If the password is validated accurately assign the
    # password to the user in the ATM_CARD class
    if password == confirm_password:
        new_user.password = password
    else:
        print("Password Mismatch...... Try again!!!")
        register_user_password(new_user)