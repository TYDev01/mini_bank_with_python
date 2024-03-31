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

    
