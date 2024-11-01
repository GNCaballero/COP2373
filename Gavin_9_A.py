class BankAcct:
    def __init__(self,name,accountNum,amount,interest):
        self.name = name
        self.accountNum = accountNum
        self.amount = amount
        self.interest = interest

    def interestAdjust(self,interest):
        self.interest = interest
    
    def withdraw(self,amount):
        self.amount -= amount

    def deposit(self,amount):
        self.amount += amount

    def setBalance(self,amount):
        self.amount = amount

    def calculateInterest(self,days):
        gain = self.interest * (days/365) * self.amount
        return gain
    
    def __str__(self):
        return f"Name: {self.name}\nAccount Number: {self.accountNum}\nBalance: ${self.amount:,.2f}\nInterest Rate: {self.interest}"

def test():
    bank = BankAcct("John Doe",123456,1000,0.05)
    print(bank,"\n")
    bank.interestAdjust(0.03)
    print(bank,"\n")
    bank.setBalance(1234.56)
    print(bank,"\n")
    bank.withdraw(500)
    print(bank,"\n")
    bank.deposit(750)
    print(bank,"\n")
    days = 30
    calculated_interest = bank.calculateInterest(days)
    print("Interest after ",days,f" days: ${calculated_interest:,.2f}")

test()