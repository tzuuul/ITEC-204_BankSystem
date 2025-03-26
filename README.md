Bank! Bank! - Python Banking System

Banking system implemented in Python that allows users to:
- Deposit money
- Withdraw money
- Check their balance
- Apply for a loan
- Exit the program

The system keeps track of the users account balance and loan amount while ensuring transactions are properly validated.

Features
- Register and Login: Users can create their bank account and login.
- Accounts database: The account information can store into JSON file once users register it. 
- Deposit Funds: Users can deposit money into their account.
- Withdraw Funds: Ensures sufficient funds before allowing withdrawals.
- Check Balance: Displays the user's current balance and any outstanding loans.
- Loan Request: Users can apply for a loan if the bank reserve allows it.
- Transaction Logging: Stores account details in a file.
- Interest Calculation: Applies a 5% interest calculation.

Python Keywords Used
This program implements the following Python keywords:

1. import - Used to import the OS module, JSON, and arguments.w
2. class - Defines the BankAccount class.
3. def - Defines functions such as deposit, withdraw, check_balance, apply_loan, and main.
4. global - Used to declare bank_reserve as a global variable.
5. assert - Ensures valid deposit amounts.
6. if - Used for conditional checks.
7. else - Provides alternative execution paths.
8. elif - Used to check multiple conditions.
9. raise - Throws an error when withdrawal funds are insufficient.
10. try - Handles exceptions.
11. except - Catches exceptions for invalid user inputs.
12. finally - Ensures execution of final statements after an exception.
13. while - Runs the main banking menu loop.
14. break - Exits the loop when the user chooses to exit.
15. continue - Skips to the next iteration of the loop.
16. with - Manages file handling for logging account data.
17. lambda - Implements an inline function for interest calculation.
18. yield - Generates account statements.
19. is - Checks if a value is None.
20. not - Used for logical negation.
21. or - Evaluates multiple conditions.
22. and - Ensures both conditions are met.
23. del - Deletes an account object when removed.
24. for - used to loop through each item in the sequence
25. in - checks each item inside generate_statements() one by one
26. pass - to indicate future code
27. nonlocal - to modify the outer variable
28. none - to check NoneType in account.balance
29. true - used to loop for menu
30. from - used to import command-line arguments
31. as - used to import command-line arguments
32. false - to exit the function if username and password is incorrect
33. return - to exit the function in apply_loan

How to Use
1. Run the Python script.
2. Follow the on-screen menu options.
3. Enter deposit, withdrawal, or loan amounts as required.
4. Exit when finished.


