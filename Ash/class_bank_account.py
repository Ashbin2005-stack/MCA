
class BankAccount:

    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("\nAccount Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Account Type:", self.acc_type)
        print("Available Balance:", self.balance)


# Creating an object
acc = BankAccount(101, "Ashbin", "Savings", 5000)

# Performing operations
acc.display()
acc.deposit(2000)
acc.withdraw(1000)
acc.display()
