class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit_cash(self, amount):
        self.__balance += amount

    def withdraw_cash(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print(f'Insufficient fund')

    def get_balance(self):
        return self.__balance


class AtmCard(BankAccount):

    def __init__(self):
        BankAccount.__init__(self, balance=None)
        self.__password = None
        self.__user_name = None
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
