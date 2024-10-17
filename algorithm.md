# Algorithm Document


#### Name: decisions
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
   2. output error message
2. otherwise
   2. add 1 to count 
   2. change the amount of money to an integer

#### Name: valid integer
#### Parameter: amount
#### Return: positive integer
#### Algorithm:
1. if the amount of money is less than zero
   1. output error
2. otherwise
   2. add 1 to count 

#### Name:main
#### Parameter: valid number, valid integer, decisions
#### Return: none
#### Algorithm:
1. Explain the purpose
2. call the function decisions
3. set count equal to 0
4. Show menu presenting options of atm machine
4. Start a while loop that continues until the user enters 'E' to exit:
   1. If the choice is 'D' (Deposit):
      1. Prompt the user to enter the amount to deposit set to the variable amount.
      2. while is not count equal 2
         3. call valid number
         3. call valid integer
      4. Display the new balance to the user.
   4. Otherwise if the choice is 'V' (View Balance):
      1. Output the current balance to the user.
   5. Otherwise if the choice is 'W' (Withdraw):
      1. Prompt the user to enter the amount to withdraw.
      2. while count is not equal 2
         2. call valid number
         3. call valid integer
      4. Display the new balance to user
   6. Otherwise if the choice is 'E' (Exit):
   - Output a message thanking the user and indicate the program is ending.
   - Thank the user

