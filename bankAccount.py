from personalInfo import PersonalInfo

class BankAccount(PersonalInfo):

    def __init__(self,name: str, id: str,phone_number: str, email: str ,balance = 0):
        """
        Constructor
        :param name:
        :param id:
        :param phone_number:
        :param email:
        :param balance:
        """
        super().__init__(name,id,phone_number,email)
        self.balance = balance
        self.commission = 2

    def __str__(self):
        """
        to String
        :return:
        """
        return f"{super().__str__()}, Balance : {self.balance}"

    def withdraw(self, num: int):
        """
        Withdraw money from self balance and commission
        :param num: amount of money
        :return: self deposit - amount of money - self commission
        """
        if num <= 0 :
            raise ValueError("value must be bigger 0 ")
        self.balance-=num
        self.balance-=self.commission

    def deposit(self, num: int):
        """
        Deposit money to self balance and withdraw commission
        :param num: amount of money
        :return: self balance + amount of money  - self commission
        """
        if num <= 0 :
            raise ValueError("value must be bigger 0 ")
        self.balance += num
        self.balance -= self.commission







