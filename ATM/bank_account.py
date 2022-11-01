from ATM import ATM

class BankAccount(ATM):
    def __init__(self, first_name, last_name, reg_no):
        self.first_name = first_name
        self.last_name = last_name
        self.id = reg_no
    
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, fname):
        if not isinstance(fname, str):
            return TypeError("Enter a valid name")
        self.__first_name = fname

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, lname):
        if not isinstance(lname, str):
            return TypeError("Enter a valid name")
        self.__last_name = lname

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, passwd):
        self.__password = passwd
    
    

    
    
    
    
    
    
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
