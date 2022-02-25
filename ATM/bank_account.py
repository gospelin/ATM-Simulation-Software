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
