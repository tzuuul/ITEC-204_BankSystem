# Import necessary module
import os  # Using 'import' to include the OS
import json # Using 'import' to include JSON

# Defining a BankAccount class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # Account owners name
        self.balance = balance  # Account balance
        self.loan_amount = 0  # Track loan amount

    def deposit(self, amount):
        assert amount > 0, "Deposit amount must be greater than 0"  # 'assert' ensures the deposit is valid
        self.balance += amount  # Increase the balance
        print(f"\nDeposited Php.{amount}. \nCurrent balance: Php. {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:  # 'if' condition to check sufficient balance
            raise ValueError("Insufficient funds")  # 'raise' an error if withdrawal is invalid
        self.balance -= amount  # Decrease the balance
        print(f"\nWithdrew Php. {amount}. \nBalance: Php. {self.balance}")

    def check_balance(self):
        print(f"\n{self.owner} balance: Php. {self.balance} \nLoan Amount: Php. {self.loan_amount}")

    def apply_loan(self, amount):
        global bank_reserve
        if amount == 0:
            print("Loan request canceled.")
            return # 'return' to exit the function
        bank_reserve -= amount
        self.balance += amount
        self.loan_amount += amount  
        print(f"Loan of Php. {amount} approved! New balance: Php. {self.balance}")

    def __del__(self):  # Using 'del' to delete an object
        print(f"Account of {self.owner} is being removed!\n")

# Define a global variable
global bank_reserve  # 'global' keyword to define a variable accessible everywhere in the module
bank_reserve = 500000  # Set an initial bank reserve amount

users_file = "users.json"

def load_users():
    if os.path.exists(users_file):
        with open(users_file, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(users_file, "w") as f:
        json.dump(users, f)

def register():
    users = load_users()
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please try logging in.")
        return None
    password = input("Enter a password: ")
    users[username] = {"password": password, "balance": 0}
    save_users(users)
    print("Registration successful! You can now log in.")
    return None

def login():
    users = load_users()
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found. Please register first.")
        return False # 'return' to exit the function
    password = input("Enter your password: ")
    if users[username]["password"] != password:
        print("Incorrect password. Please try again.")
        return False # 'return' to exit the function
    print("Login successful!")
    return BankAccount(username, users[username]["balance"])

def main():
    print("Welcome to Bank! Bank!")
    account = None
    while account is None:
        print("1. Register\n2. Login")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            account = login()
    
    while True:  # 'while' loop for menu
        print("__________________________________________________________________")
        print("\nOptions: \n1. Deposit \n2. Withdraw \n3. Check Balance \n4. Loan \n5. Exit")
        action = input("Please enter the number of your choice. \n").strip()
        print("__________________________________________________________________")

        if action == "1":
            try:  # 'try' block to handle errors
                amount = float(input("Enter deposit amount: \n"))
                account.deposit(amount)    
            except Exception as e:  # 'except' block for handling exceptions
                print(f"Error: {e}\n")
        elif action == "2":
            try:
                amount = float(input("Enter withdrawal amount: \n"))
                account.withdraw(amount)
            except ValueError as e:
                print(f"Error: {e}\n")
            finally:  # 'finally' always runs
                print("Transaction attempt complete.\n")
        elif action == "3":
            account.check_balance()
        elif action == "4":
            try:
                amount = float(input("Enter loan amount: \n"))
                account.apply_loan(amount)
            except ValueError as e:
                print(f"Error: {e}\n")
        elif action == "5":
            print("Thank you for using Bank! Bank!\n")
            break  # 'break' to exit the loop
        else:
            print("Invalid option. Please try again.")
            continue  # 'continue' skips the rest of the loop iteration

    # Using 'with' for file handling
    with open("bank_log.txt", "w") as log:
        log.write(f"__________________Bank! Bank!_____________________")
        log.write(f"\n_____________________Reciept_______________________")
        log.write(f"\n{account.owner}'s Balance: Php. {account.balance}")
        log.write(f"\nLoan Amount: Php. {account.loan_amount}")
        log.write(f"\n___________________________________________________")
        log.write(f"\n___________________________________________________")
        
    # Using 'yield' to generate statements
    def generate_statements():
        yield f"Statement for {account.owner} Bank Account. \nBalance: Php. {account.balance}\nLoan Amount: Php. {account.loan_amount}"
        
    # Using 'lambda' for quick computation
    interest = lambda balance: balance * 1.05  # 5% interest
    print("Balance after interest: ", interest(account.balance))

    for statement in generate_statements():  # 'for' is used to loop through each item in the sequence
        print(statement)  # 'in' checks each item inside generate_statements() one by one


    # Using 'or' and 'and' for logical operations
    high_balance = account.balance > 1000 and bank_reserve > 5000
    low_balance = account.balance < 500 or bank_reserve <= 5000  # Fixed 'not' condition
    
    print(f"High Balance: {'Yes' if high_balance else 'No'}")
    print(f"Low Balance: {'Yes' if low_balance else 'No'}")

    if account.balance is None:  # Using 'is' to check NoneType
        print("Balance is not set")
    elif not account.balance:  # Using 'not' to check false condition
        print("Account has no balance")
        

if __name__ == "__main__":
    main()
