"""
**ATM class**

The ATM class is the superclass for all other classes in this software.
It contains the essential functionalities of the ATM Machine.
"""

class ATM:
    """The ATM class. """

    money = 500000

    def __init__(self, money):
        ATM.money += money
