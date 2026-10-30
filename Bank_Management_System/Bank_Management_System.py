class BankAccount:

    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance
        self.history = []

    # Show Account Details
    def show_details(self):
        print("\n----- ACCOUNT DETAILS -----")
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)

    # Deposit Money
    def deposit(self):
        amount = int(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Invalid amount!")

        else:
            self.balance += amount

            self.history.append(f"Deposit: {amount}")

            print("Money deposited successfully!")
            print("Updated Balance:", self.balance)

    # Withdraw Money
    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount!")

        elif amount > self.balance:
            print("Insufficient Balance!")

        else:
            self.balance -= amount

            self.history.append(f"Withdraw: {amount}")

            print("Money withdrawn successfully!")
            print("Updated Balance:", self.balance)

    # Transaction History
    def show_history(self):
        print("\n----- TRANSACTION HISTORY -----")

        if len(self.history) == 0:
            print("No transactions yet.")

        else:
            for transaction in self.history:
                print(transaction)


# Store Multiple Accounts
accounts = []


# Search Account Function
def search_account(accounts, acc_no):

    for account in accounts:

        if account.account_no == acc_no:
            return account

    return None


# Create Account Function
def create_account(accounts):

    acc_no = int(input("Enter account number: "))

    # Check Duplicate Account
    if search_account(accounts, acc_no) is not None:
        print("Account number already exists!")
        return

    name = input("Enter customer name: ")

    balance = int(input("Enter initial balance: "))

    if balance < 0:
        print("Invalid initial balance!")
        return

    new_account = BankAccount(acc_no, name, balance)

    accounts.append(new_account)

    print("\nAccount created successfully!")

    new_account.show_details()


# Main Menu
while True:

    print("\n========== BANK MANAGEMENT SYSTEM ==========")

    print("1. Create Account")
    print("2. Search Account")
    print("3. Show Account Details")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Show Transaction History")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    # Create Account
    if choice == "1":

        create_account(accounts)

    # Search Account
    elif choice == "2":

        acc_no = int(input("Enter account number: "))

        account = search_account(accounts, acc_no)

        if account is not None:
            print("Account Found!")

        else:
            print("Account Not Found!")

    # Show Account Details
    elif choice == "3":

        acc_no = int(input("Enter account number: "))

        account = search_account(accounts, acc_no)

        if account is not None:
            account.show_details()

        else:
            print("Account Not Found!")

    # Deposit Money
    elif choice == "4":

        acc_no = int(input("Enter account number: "))

        account = search_account(accounts, acc_no)

        if account is not None:
            account.deposit()

        else:
            print("Account Not Found!")

    # Withdraw Money
    elif choice == "5":

        acc_no = int(input("Enter account number: "))

        account = search_account(accounts, acc_no)

        if account is not None:
            account.withdraw()

        else:
            print("Account Not Found!")

    # Transaction History
    elif choice == "6":

        acc_no = int(input("Enter account number: "))

        account = search_account(accounts, acc_no)

        if account is not None:
            account.show_history()

        else:
            print("Account Not Found!")

    # Exit
    elif choice == "7":

        print("Thank you for using our Bank Management System!")
        break

    else:
        print("Invalid Choice! Please try again.")