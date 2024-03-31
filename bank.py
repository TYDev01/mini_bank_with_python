
class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.initial_amount = initial_amount
        self.account_name = account_name

    def __str__(self):
        return f"Account: '{self.account_name}' created.\nBalance = ${self.initial_amount:,.2f}"
    
    def getBalance(self):
        print(f"{self.account_name} account balance is ${self.initial_amount:,.2f}")

    def deposit(self, amount):
        self.initial_amount =  self.initial_amount + amount
        print(f"{self.account_name} deposited {amount:,.2f}")
        self.getBalance()

    
    def withdraw(self, amount):
        if self.initial_amount >= amount:
            self.initial_amount = self.initial_amount - amount
            self.getBalance()
        else:
            print("Amount requested is more than available balance.")

#     def withdraw(self):
#         pass
    

# class WithdrawError:
#     def __init__(self, amount):
#         self.amount = amount
#         try:
#             if self.amount <= amount:
#                 self.initial_amount - amount
#         except:
#             print("Amount entered is more than available balance")
