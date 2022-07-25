# Parents imports
from bankAccount import BankAccount
from businessBankAccount import BusinessBankAccount
from studentBankAccount import StudentBankAccount

# External imports
import xml.etree.cElementTree as et
import statistics
import re
import sys


class Bank:

    def __init__(self):
        """
        Main Bank Constructor
        """
        bba = BankAccount('Katia Barak','141525829','052-5554442','katiab@sela.co.il',1400)
        bba2 = BankAccount('Katia Barak', '131525829', '052-5554442', 'katiab@sela.co.il',17200)

        self.bank = {'StudentBankAccount': [], 'BankAccount': [bba,bba2], 'BusinessBankAccount': []}

    def __str__(self):
        """
        to String
        :return:
        """
        sba = 'Student bank Accounts : \n'
        ba = 'Bank accounts : \n'
        bba = 'BusinessBankAccount \n'
        for i in range(len(self.bank['StudentBankAccount'])):
            # result.append((self.bank['StudentBankAccount'][i]))
            sba+=f"{str(self.bank['StudentBankAccount'][i])}\n"

        for i in range(len(self.bank['BankAccount'])):
            # result.append((self.bank['BankAccount'][i]))
            ba += f"{str(self.bank['BankAccount'][i])}\n"

        for i in range(len(self.bank['BusinessBankAccount'])):
            # result.append((self.bank['BusinessBankAccount'][i]))
            bba += f"{str(self.bank['BusinessBankAccount'][i])}\n"
        result = f"{sba} \n{ba} \n{bba}"

        return result

    def load_and_parse_init_data(self):
        """
        Function for load and parse data from XML file to dictionary
        :return: dict with all data from XML
        """

        # Create variables
        tree = et.parse(sys.argv[1])
        root = tree.getroot()


        # Check if personal info is valid
        d = {}
        for tag in root.findall('.account'):

            if tag.attrib['type'] == 'BankAccount':

                for el in tag.findall('.//'):
                    d[el.tag] = el.text

                if self.personlInfoValidator(d) != True:
                    raise ValueError(f'{d} is not correct !!')


            if tag.attrib['type'] == 'BusinessBankAccount':

                for el in tag.findall('.//'):
                    d[el.tag] = el.text

                if self.personlInfoValidator(d) != True:
                    raise ValueError(f'{d} is not correct !!')

            if tag.attrib['type'] == 'StudentBankAccount':

                for el in tag.findall('.//'):
                    d[el.tag] = el.text

                if self.personlInfoValidator(d) != True:
                    print("aaa?")
                    raise ValueError(f'{d} is not correct !!')

        return root

    def add_new_account(self):
        """
        Function for add all accounts from XML file to Bank
        :return: Bank + all accounts from xml with valid personal info
        """

        # Create variable with parse and load function from XML file
        accounts_for_adding = self.load_and_parse_init_data()


        for tag in accounts_for_adding.findall('.account'):

            if tag.attrib['type'] == 'BankAccount':

                ba = BankAccount('None None', '000000000', '052-0000000', 'kkkkkk@sela.co.il')

                for el in tag.findall('.//'):

                    if el.tag=='name':
                        ba.name=el.text
                    if el.tag == 'id':
                        ba.id = el.text
                    if el.tag == 'phone':
                        ba.phone = el.text
                    if el.tag == 'email':
                        ba.email = el.text

                self.bank['BankAccount'].append(ba)


            if tag.attrib['type'] == 'StudentBankAccount':
                sa = StudentBankAccount('None None', '000000000', '052-0000000', 'kkkkkk@sela.co.il','college')

                for el in tag.findall('.//'):
                    if el.tag == 'name':
                        sa.name = el.text
                    if el.tag == 'id':
                        sa.id = el.text
                    if el.tag == 'phone':
                        sa.phone = el.text
                    if el.tag == 'email':
                        sa.email = el.text
                    if el.tag == 'college' :
                        sa.college_name = el.text

                self.bank['StudentBankAccount'].append(sa)

            if tag.attrib['type'] == 'BusinessBankAccount':
                bba = BusinessBankAccount('None None', '000000000', '052-0000000', 'kkkkkk@sela.co.il','Town','HR','Profit','FreeInfo')
                d = {}
                for el in tag.findall('.//'):

                    if el.tag == 'name':
                        bba.name = el.text
                    if el.tag == 'id':
                        bba.id = el.text
                    if el.tag == 'phone':
                        bba.phone = el.text
                    if el.tag == 'email':
                        bba.email = el.text

                    if el.tag == 'town':
                        bba.town = el.text
                    if el.tag == 'hr':
                        bba.hr = el.text
                    if el.tag == 'profit':
                        bba.profit = el.text
                    if el.tag == 'free_information':
                        bba.free_information = el.text

                self.bank['BusinessBankAccount'].append(bba)

    def withdraw_by_user_id(self,id:int,withdraw:int):
        """
        Function for withdraw money by id
        :param id: client id
        :param withdraw: amount of money
        :return: self deposit - amount of money - self commission
        """
        id = str(id)
        for k, v in self.bank.items():
            for objc in v:
                if id == objc.id:
                    objc.withdraw(int(withdraw))

    def deposit_by_user_id(self,id:str,deposit:str):
        """
        Deposit money to self balance by id
        :param id: client id
        :param deposit: amount of money
        :return:
        """
        id = str(id)
        for k, v in self.bank.items():
            for objc in v:
                if id == objc.id:
                    objc.deposit(int(deposit))

    def calc_balance_statistics(self):
        """
        Function for calculate avg / median / 90th percentile and 10th
        percentile of balances of all already added clients of the bank
        :return: string with all data avg,median,90th,10th
        """
        avg,median,prcntl_90,prcntl_10 = 0,0,0,0
        balances = []
        for k,v in self.bank.items():
            for objc in v:
                balances.append(objc.balance)
                avg+=objc.balance

        prcntl_90 = avg*0.9
        prcntl_10 = avg*0.1
        avg/=len(balances)
        median = statistics.median(balances)
        result = f'Avg is          : {avg}\n' \
                 f'Median is       : {median}\n' \
                 f'90th percentile : {prcntl_90}\n' \
                 f'10th percentile : {prcntl_10}'
        return result

    def delete_by_user_id(self,id : str):
        d = []
        id = str(id)
        for k,v in self.bank.items():
            for account in range(len(v)):
                if v[account].id != id:
                    d.append(v[account])

            self.bank[k]=d
            d = []

    # ------ Helper Function --------
    def personlInfoValidator(self,dict:dict) -> bool:
        """
        Check if personal info is valid
        :return: True/Falce
        """
        mobile = ('050-', '051-', '052-', '053-', '054-', '055-', '056-', '058-', '059-', '076-', '074-', '073-', '072-', '071-')
        keys = ['name', 'id', 'phone', 'email']
        cnt = 0


        for k, v in dict.items():
            if k in keys:
                if k == 'name':
                    if v.replace(' ', '').isalpha():
                        cnt += 1
                if k == 'email':
                    if re.findall(r'[\w.-]+@[\w.-]+', v):
                        cnt += 1
                if k == 'id':
                    if re.findall('[0-9]', v):
                        cnt += 1
                if k == 'phone':
                    if v[:4] in mobile and len(v) == 11:
                        cnt += 1
        if cnt == 4:
            return True

def main():
    b = Bank()
    print(sys.argv[1])
    if sys.argv[1] == "init.xml":
        et.parse(sys.argv[1])
        b.load_and_parse_init_data()
if __name__ == '__main__':
    main()

