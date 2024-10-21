# Programmers: Theresa and Donovan
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 9/16/2024
# Lab Assignment: 5
# Problem Statement: Build a simulation of an ATM (Automatic Teller Machine), where users can view their balance,
#deposit (e.g. add money to the account), or withdraw (e.g. take money from the account).
# Data In: Letter of the function chosen by user
# Data Out:  Operation of chosen function
# Credits: In Class



count = 0
balance = 1000
amount = 0

def display_menu():
        print("\nPlease select an option:"
              "\n\t D - Deposit"
              "\n\t W - Withdraw"
              "\n\t V - View Balance"
              "\n\t E - Exit")

def valid_num(amount):
    if not amount.isdigit():
        print("\nPlease enter a valid number above 0.")
    else:
        count += 1
        amount = int(amount)

def valid_integer(amount):
    if amount < 0:
        print('error')
    else:
        count += 1

def main():
    print('This program operates like an ATM. You can deposit, withdraw, or view your balance.')
    choicezee = ''

    while choicezee != 'D' and choicezee != 'W' and choicezee != 'V' and choicezee != 'E':
        display_menu()
        choicezee = input('Enter your option here: ').upper().strip()

    if choicezee == 'D':
        amount = input('Enter amount of money you want deposited')
        while amount != 2:
            valid_num()
            valid_integer()
        balance = balance + amount
        print(balance)
        decision()
    elif choicezee == 'V':
        print (balance)
        decision()
    elif choicezee == 'W':
        amount = input('Enter amount of money you want withdrawn')
        while count != 2:
            valid_num()
            valid_integer()
        balance = balance - amount
        print(balance)
        decision()
    elif choicezee == 'E':
        print('You are now exiting, thank you for using the program!')
main()









