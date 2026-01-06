class Bank_Account:
    def __init__(self, number, name, acc_type, balance):
        self.number = number
        self.name = name
        self.type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def display(self):
        print("Account No:", self.number)
        print("Name:", self.name)
        print("Type:", self.type)
        print("Balance:", self.balance)


# Create account
account1 = Bank_Account(1, "John", "Personal", 100)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # SWITCH STATEMENT (using if-elif)
    if choice == 1:
        amt = int(input("Enter amount to deposit: "))
        account1.deposit(amt)

    elif choice == 2:
        amt = int(input("Enter amount to withdraw: "))
        account1.withdraw(amt)

    elif choice == 3:
        account1.display()

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Invalid choice")


         