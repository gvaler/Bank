from bankAccount import *

class StudentBankAccount(BankAccount):

    def __init__(self,name: str, id: str,phone_number: str, email: str ,college_name: str,balance=0):
        """
        Constructor,
        Data are checked immediately after initialization
        :param name:
        :param id:
        :param phone_number:
        :param email:
        :param college_name:
        :param balance:
        """
        super().__init__(name,id,phone_number,email,balance)
        self.college_name = college_name
        self.balanceValidator()

    def __str__(self):
        """
        to String
        :return:
        """
        return f"{super().__str__()}, Name of college : {self.college_name}"

    def balanceValidator(self):
        """
        Balance validator for student bank account
        :return: None/Value Error
        """
        if self.balance < 0 :
            raise ValueError("Student can’t have negative balance ")

    def withdraw(self, num: int):
        """
        Withdraw money from self balance and call to balanceValidator()
        :param num: amount of money
        :return: self balance - amount of money  - commission /Value Error
        """
        if num <= 0 :
            raise ValueError("value must be bigger 0 ")
        try:
            self.balance-=num
            self.balance-=self.commission
            self.balanceValidator()
        except :
            raise ValueError("Student can’t have negative balance ")

    def deposit(self, num: int):
        """
        Deposit money from self balance and call to balanceValidator()
        :param num: amount of money
        :return: self balance + amount of money  - commission / Value Error
        """
        if num <= 0 :
            raise ValueError("value must be bigger 0 ")
        try:
            self.balance += num
            self.balance -= self.commission
            self.balanceValidator()
        except:
            raise ValueError("Student can’t have negative balance,add cash for deposit")