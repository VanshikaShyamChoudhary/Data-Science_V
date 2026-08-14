# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

        # Debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"had been debited from the account",acc1.account_no)
        print("ttl amount",self.get_balance())

        # credit method
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"had been credited from the account",acc1.account_no)
        print("ttl amount",self.get_balance())


    def get_balance(self):
        return self.balance    

        

acc1=Account(100000,"ABCDEFGHIJKLM")
print(acc1.balance)
print(acc1.account_no)
acc1.debit(50000)
acc1.credit(10000)