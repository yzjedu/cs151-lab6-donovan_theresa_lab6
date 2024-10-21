# Programmers: Theresa and Donovan
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 9/16/2024
# Lab Assignment: 5
# Problem Statement: Build a simulation of an ATM (Automatic Teller Machine), where users can view their balance,
#deposit (e.g. add money to the account), or withdraw (e.g. take money from the account).
# Data In: Letter of the function chosen by user
# Data Out:  Operation of chosen function
# Credits: In Class


def decision():
    Choice ='a'
    while (Choice != 'D'or
           Choice != 'W'or
           Choice != 'V'or
           Choice != 'E'):
        print("\nPlease select an option:"
              "\n\t D - Deposit"
              "\n\t W - Withdraw"
              "\n\t V - View Balance"
              "\n\t E - Exit")

    choice = input("Your choice: ").strip().upper()

def valid_num(amount):
    if not amount.isdigit():
        print("\nPlease enter a valid number above 0.")
    else:
        count += 1
        amount = int(amount)


