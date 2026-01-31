
from Day14.sampath_bank.account import Account


class SavingsAccount(Account):
    def __init__(self,account_no, balance, branch,user, atm_card_id):
        Account.__init__(self, account_no, balance, branch, user)
        self.atm_card_id = atm_card_id

    def check_balance(self): #Pholymorphism
        return f"Checking balance of {self.atm_card_id} has balance: {self.get_account_balance()}"


class VanithaSavings(SavingsAccount):
    def __init__(self,account_no, balance, branch, user, atm_card_id):
        SavingsAccount.__init__(self, account_no, balance, branch, user, atm_card_id)
        self.atm_card_id = atm_card_id

    def check_balance(self):
        return f"Checking balance of {self.atm_card_id} has balance: {self.get_account_balance()}"





# user2 = SavingsAccount(2445566, 25000, "Bla", "AMal", 564 )
# print(user2.check_balance())