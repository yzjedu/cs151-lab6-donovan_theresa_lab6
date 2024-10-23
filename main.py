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
# prints menu
def display_menu():
        print("\nPlease select an option:"
              "\n\t D - Deposit"
              "\n\t W - Withdraw"
              "\n\t V - View Balance"
              "\n\t E - Exit")
#Function to determine if inputted value is a number and if so make it an integer
#The parameter is amount
#returns a number in the form of an integer
def valid_num(amount):
    if not amount.isdigit():
        return False
    else:
        return int(amount)

#Main function containing while loops to operate the chosen option
def main():
    #set the localized variables choice balance while introducing the code
    print('This program operates like an ATM. You can deposit, withdraw, or view your balance.')
    choice = ''
    balance = 1000
    #while loop that repeats until we recieve our sentinel E
    while choice != 'E':
        display_menu()
        choice = input('Enter your option here: ').upper().strip()
        #while loop to validate the inputs for choice
        while choice != 'D' and choice != 'W' and choice != 'V' and choice != 'E':
            display_menu()
            choice = input('Enter your option here: ').upper().strip()
        #decisions for choices
        if choice == 'D':
            amount = input('Enter amount of money you want deposited ')
            amount = valid_num(amount)
            balance = balance + amount
            print(balance)

        elif choice == 'V':
            print (balance)

        elif choice == 'W':
            amount = input('Enter amount of money you want withdrawn')
            amount = valid_num(amount)
            balance = balance - amount
            print(balance)

        elif choice == 'E':
            print('You are now exiting, thank you for using the program!')
#Calling the main function so the code operates
main()
