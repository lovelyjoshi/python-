#class and methods
class Account:
    def __init__(self, bal,acc):
        self.balance = bal
        self.account_no = acc
#debit method
    def debit(self, amount):
        self.balance -= amount
        print(amount,"was debited")
#crdit method
    def credit(self, amount):
        self.balance += amount
        print(amount,"was credited")
    def get_balance(self):
        return self.balance
acc1=Account(1000000,23456)
acc1.credit(200000)
acc1.debit(50000)                    
