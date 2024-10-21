# Programmers: Theresa and Donovan
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 9/16/2024
# Lab Assignment: 5
# Problem Statement: Build a simulation of an ATM (Automatic Teller Machine), where users can view their balance,
#deposit (e.g. add money to the account), or withdraw (e.g. take money from the account).
# Data In: Letter of the function chosen by user
# Data Out:  Operation of chosen function
# Credits: In Class



def display_menu():
        print("\nPlease select an option:"
              "\n\t D - Deposit"
              "\n\t W - Withdraw"
              "\n\t V - View Balance"
              "\n\t E - Exit")

def valid_num(amount):
    if not amount.isdigit():
        return False
    else:
        return int(amount)


def main():
    balance = 1000
    print('This program operates like an ATM. You can deposit, withdraw, or view your balance.')
    choicezee = ''
    while choicezee != 'E':
        display_menu()
        choicezee = input('Enter your option here: ').upper().strip()

        while choicezee != 'D' and choicezee != 'W' and choicezee != 'V' and choicezee != 'E':
            display_menu()
            choicezee = input('Enter your option here: ').upper().strip()

        if choicezee == 'D':
            amount = input('Enter amount of money you want deposited ')
            amount = valid_num(amount)
            balance = balance + amount
            print(balance)

        elif choicezee == 'V':
            print (balance)

        elif choicezee == 'W':
            amount = input('Enter amount of money you want withdrawn')
            amount = valid_num(amount)
            balance = balance - amount
            print(balance)

        elif choicezee == 'E':
            print('You are now exiting, thank you for using the program!')
main()