class Account:
    def __init__(self, account_no, balance, branch, user):
        self.__account_no = account_no
        self.__balance = balance
        self.__branch = branch
        self.__user = user   #composition

    def set_account_no(self,account_no):#setters
        self.__account_no = account_no

    def get_account_no(self): #getters
        return self.__account_no

    def set_balance(self,balance):
        self.__balance = balance

    def get_account_balance(self):
        return self.__balance

    def check_balance(self):
        return f" Your Account Balance is: {self.__balance}"

    def set_user(self, user):
        self.__user = user

    def get_user(self):
        return self.__user


    def deposit(self, deposit_amount):
        self.__balance += deposit_amount
        return f" Your Account Balance is: {self.__balance}"

    def withdraw(self, withdrawal_amount):
        if self.__balance > withdrawal_amount:
            self.__balance -= withdrawal_amount
            return f" Withdrawn {withdrawal_amount}. Your Account Balance is: {self.__balance}"
        return "Insufficient balance!"







