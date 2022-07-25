class BusinessInfo():

    def __init__(self,town: str,hr: int,profit: int,free_information: str):
        """
        Constructor
        :param town:
        :param hr:
        :param profit:
        :param free_information:
        """
        self.town = town
        self.hr = hr
        self.profit = profit
        self.free_information = free_information

    def __str__(self):
        """
        to String
        :return:
        """
        return f"Town : {self.town}, Human Resources : {self.hr}, Profit {self.profit} $ in year , About business : {self.free_information}"
