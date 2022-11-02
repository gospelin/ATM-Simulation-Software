"""
This is the ATM_CARD Module.

@AUTHOR: Gospel Isaac
@email: gospelin.gi@gmail.com
"""

from .bank_account import BankAccount

class AtmCard(BankAccount):
    """
    This is the ATM_CARD class.

    This class embeds all the functionalites of a typical ATM_CARD.
    """

    def __init__(self, first_name, last_name, password):
        super().__init__(first_name, last_name)
        # self.account_number = super().account_number()
        self.password = password

    #   Gets each user's password
    @property
    def password(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__password

    #   Sets each user's password
    @password.setter
    def password(self, password):
        self.__password = password

    #@property
    #def first_name(self):
    #    """_summary_

    #    Returns:
    #        _type_: _description_
    #    """
    #    return super().first_name

    #@first_name.setter
    #def first_name(self, first_name):
    #    super().first_name = first_name

    #@property
    #def last_name(self):
    #    """_summary_"""
    #    return super().last_name

    #@last_name.setter
    #def last_name(self, last_name):
    #    super().last_name = last_name
