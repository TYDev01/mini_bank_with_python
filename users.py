from bank import *

Tony = BankAccount(10000000, "Tony")
Som = BankAccount(2000000, "Som")

Tony.getBalance()

add_money = int(input("Deposit amount? "))
Tony.deposit(add_money)
