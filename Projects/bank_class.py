class BankAccount:

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"LKR{amount} has been added. Now balance is LKR{self.balance}.")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"LKR{amount} has been withdrawn. Now balance is LKR{self.balance}.")
        else:
            print("Can't withdraw that amount!")

    def show_balance(self):
        print(f"{self.owner}'s account balance is : LKR{self.balance}\n")

acc1 = BankAccount("Nimal")
acc1.deposit(5400)
acc1.withdraw(500)
acc1.show_balance()

acc2 = BankAccount("Kamal")
acc2.deposit(4500)
acc2.withdraw(400)
acc2.show_balance()



