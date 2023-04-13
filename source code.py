class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. \nCurrent balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
atm = ATM()
while True:
    print("\nWelcome to SBI")
    print("Insert Your Card")
    a = int(input("Enter Your PIN:"))
    p=1234
    if a == p:
        print("\nSelect an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit\n")
        choice = int(input())
        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == 3:
            atm.check_balance()
        elif choice == 4:
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Please try again.")
    else:
        print("\nInvalid Pin. Please try again.")
