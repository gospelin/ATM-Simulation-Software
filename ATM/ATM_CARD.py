from bank_account import BankAccount

"""
This is the ATM_CARD Module.

@AUTHOR: Gospel Isaac
@email: gospelin.gi@gmail.com
"""

class AtmCard(BankAccount):
    """
    This is the ATM_CARD class.

    This class embeds all the functionalites of a typical ATM_CARD.
    """

    def __init__(self):
        pass

    #   Sets each user's password
    def set_password(self, password):
        self.__password = password

    #   Gets each user's password
    def get_password(self):
        return self.__password

    #   Sets each user's name
    def set_user_name(self, name):
        self.__user_name = name

    #   Gets each user's name
    def get_user_name(self):
        return self.__user_name
