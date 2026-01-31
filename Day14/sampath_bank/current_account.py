from Day14.sampath_bank.account import Account


class CurrentAccount(Account):
    def __init__(self,account_no, balance, branch, user, cheque_ids):
        Account.__init__(self, account_no, balance, branch, user)
        self.cheque_ids = cheque_ids

    def get_cheque_ids(self):
        return  self.cheque_ids

    def set_cheque_ids(self, cheque_ids):
        self.cheque_ids = cheque_ids

    def add_cheque_ids(self, cheque_id):
        self.cheque_ids.append(cheque_id)