class Account:
    def __init__(self,bal,act):
        self.balance=bal
        self.account_no = act
    def debit(self,amount):
        self.balance-=amount
        print("tk",amount,"was debiteed")
    def credit(self,amount):
        self.balance+=amount
        print("tk",amount,"was credited")
        def get_balance(self):
            return self.balance
act1=Account(10000,12345)
print(act1.balance)
print(act1.account_no)
act1. debit(1000)
act1.credit(456)