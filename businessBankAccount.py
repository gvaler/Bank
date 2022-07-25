from bankAccount import *
from businessInfo import *

class BusinessBankAccount (BankAccount,BusinessInfo):

    def __init__(self,name: str, id: str,phone_number: str, email: str ,town: str,hr: int,profit: int,free_information: str,balance=0):
        """
        Constructor
        :param name:
        :param id:
        :param phone_number:
        :param email:
        :param town:
        :param hr:
        :param profit:
        :param free_information:
        :param balance:
        """
        super().__init__(name,id,phone_number,email,balance)
        BusinessInfo.__init__(self,town,hr,profit,free_information)
        self.commission = 3

    def __str__(self):
        """
        To String
        :return:
        """
        return f"{super().__str__()},{BusinessInfo.__str__(self)}"

    def withdraw(self, num: int):
        """
        Withdraw money from self balance
        :param num: amount of money
        :return: self balance - amount of money  - self commission
        """
        if num <= 0 :
            raise ValueError("value must be bigger 0 ")
        self.balance-=num
        self.balance-=self.commission

    def deposit(self, num: int):
        """
        Deposit money to self balance
        :param num: amount of money
        :return: self balance + amount of money  - self commission
        """
        if num <= 0 :
            raise ValueError("value must be bigger 0 ")
        self.balance+=num
        self.balance-=self.commission

