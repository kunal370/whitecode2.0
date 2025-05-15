"""
42	Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance
"""

class Account:
    def __init__(self,account_no,balance):
        self.acc_bal=balance
        self.acc_no=account_no

    def debit(self,amount):
        if amount<0:
            print("must be positive value")
        else:
            self.acc_bal=self.acc_bal-amount
            print("amount debited, available balance is: ",self.acc_bal)

    def credit(self, amount):
        if amount < 0:
            print("must be positive value")
        else:
            self.acc_bal = self.acc_bal + amount
            print("amount debited, available balance is: ", self.acc_bal)

a1=Account(12345,12500)
a1.credit(500)
a1.debit(2000)