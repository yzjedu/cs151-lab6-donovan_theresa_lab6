# Algorithm Document


#### Name: display menu
#### Parameter:None
#### Return: whatever user chooses 
#### Algorithm
1. Ask user for their option 
2.  While input is not equal to 'D or W or V or E' 
    1. prompt user to enter one of the specified letters


#### Name: valid number
#### Parameter: amount
#### Return: Integer
#### Algorithm:
1. if amount of money is not a digit 
   2. return false
2. otherwise
   2. change the amount of money to an integer and return it


#### Name:main
#### Parameter: valid number, valid integer, decisions
#### Return: none
#### Algorithm:
1. Explain the purpose
2. sets the variable balance to 1000
3. create a variable choice set to an empty string
4. while choice is not E
   2. call the function to display the menu
      4. Show menu presenting options of atm machine 
      5. prompt the user to input their choice
   4. Start a while loop that continues until the user enters a valid choice:
      5. Show menu presenting options of atm machine 
      5. prompt the user to input their choice
   1. If the choice is 'D' (Deposit):
      1. Prompt the user to enter the amount to deposit set to the variable amount.
      2. set amount to amount after running it through the valid number function
      3. add the amount to balance and update to new balance
      4. Display the new balance to the user.
   4. Otherwise if the choice is 'V' (View Balance):
      1. Output the current balance to the user.
   5. Otherwise if the choice is 'W' (Withdraw):
      1. Prompt the user to enter the amount to withdraw.
      2. set amount to amount after running it through the valid number function
      3. subtract the amount to balance and update to new balance
      4. Display the new balance to the user.
   6. Otherwise if the choice is 'E' (Exit):
      - Output a message thanking the user and indicate the program is ending.
