"""_summary_

    Returns:
        _type_: _description_
"""

# from ATM.ATM_Machine import ATM


class BankAccount():
    """_summary_

    Args:
        ATM (_type_): _description_

    Returns:
        _type_: _description_
    """

    #__id = 0

    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name
        #BankAccount.id = __id + 1
    @property
    def first_name(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, fname):
        if not isinstance(fname, str):
            raise TypeError("Enter a valid name")
        self.__first_name = fname

    @property
    def last_name(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, lname):
        if not isinstance(lname, str):
            raise TypeError("Enter a valid name")
        self.__last_name = lname


    #def __init__(self, balance):
    #    self.__balance = balance

    #def deposit_cash(self, amount):
    #    self.__balance += amount

    #def withdraw_cash(self, amount):
    #    if self.__balance >= amount:
    #        self.__balance -= amount
    #    else:
    #        print(f'Insufficient fund')

    #def get_balance(self):
    #    return self.__balance
