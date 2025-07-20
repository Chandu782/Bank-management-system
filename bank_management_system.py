class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def display(self):
        print("----------- Account Info -----------")
        print(f"Account Number : {self.account_number}")
        print(f"Name           : {self.name}")
        print(f"Balance        : ₹{self.balance}")
        print("------------------------------------")

# ---------------------------

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        acc_no = input("Enter Account Number: ")
        name = input("Enter Customer Name: ")
        account = Account(acc_no, name)
        self.accounts.append(account)
        print("✅ Account created successfully!\n")

    def find_account(self, acc_no):
        for acc in self.accounts:
            if acc.account_number == acc_no:
                return acc
        return None

    def deposit_money(self):
        acc_no = input("Enter Account Number: ")
        acc = self.find_account(acc_no)
        if acc:
            amount = float(input("Enter amount to deposit: "))
            acc.deposit(amount)
        else:
            print("❌ Account not found.")

    def withdraw_money(self):
        acc_no = input("Enter Account Number: ")
        acc = self.find_account(acc_no)
        if acc:
            amount = float(input("Enter amount to withdraw: "))
            acc.withdraw(amount)
        else:
            print("❌ Account not found.")

    def display_account(self):
        acc_no = input("Enter Account Number: ")
        acc = self.find_account(acc_no)
        if acc:
            acc.display()
        else:
            print("❌ Account not found.")

    def show_all_accounts(self):
        if not self.accounts:
            print("No accounts created yet.")
        for acc in self.accounts:
            acc.display()

# ---------------------------

def main():
    bank = Bank()
    while True:
        print("\n========= Bank Menu =========")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Account Info")
        print("5. Show All Accounts")
        print("6. Exit")
        print("=============================")
        choice = input("Enter your choice: ")

        if choice == '1':
            bank.create_account()
        elif choice == '2':
            bank.deposit_money()
        elif choice == '3':
            bank.withdraw_money()
        elif choice == '4':
            bank.display_account()
        elif choice == '5':
            bank.show_all_accounts()
        elif choice == '6':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
