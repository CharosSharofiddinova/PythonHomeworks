import json

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    
    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        print(f"Account created successfully! Account Number: {account_number}")
        self.save_to_file()
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}, Name: {account.name}, Balance: {account.balance}")
        else:
            print("Account not found.")
    
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")
    
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")
    
    def save_to_file(self):
        with open("accounts.txt", "w") as f:
            json.dump({acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}, f)
    
    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as f:
                data = json.load(f)
                self.accounts = {int(acc_num): Account(**details) for acc_num, details in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}

if __name__ == "__main__":
    bank = Bank()
    while True:
        print("\n1. Create Account\n2. View Account\n3. Deposit\n4. Withdraw\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, initial_deposit)
        elif choice == "2":
            acc_num = int(input("Enter account number: "))
            bank.view_account(acc_num)
        elif choice == "3":
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(acc_num, amount)
        elif choice == "4":
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(acc_num, amount)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")