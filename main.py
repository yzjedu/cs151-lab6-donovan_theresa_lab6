# Programmers: Theresa and Donovan
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 9/16/2024
# Lab Assignment: 6
# Problem Statement: Build a simulation of an ATM (Automatic Teller Machine), where users can view their balance,
#deposit (e.g. add money to the account), or withdraw (e.g. take money from the account).
# Data In: Letter of the function chosen by user
# Data Out:  Operation of chosen function and balance
# Credits: In Class


#Function for options of ATM
def display_menu():
        print("\nPlease select an option:"
              "\n\t D - Deposit"
              "\n\t W - Withdraw"
              "\n\t V - View Balance"
              "\n\t E - Exit")
#Function to determine if inputed value is a number and if so make it an integer
def valid_num(amount):
    if not amount.isdigit():
        return False
    else:
        return int(amount)

#Function containing while loops to operate the chosen option
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
#Calling the main function so the code operates
main()
