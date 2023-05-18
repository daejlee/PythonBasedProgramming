class BankAccout:
    def __init__(self, balance, name, number):
        self.balance = balance
        self.name = name
        self.number = number
    def withdraw(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount

class SavingsAccount(BankAccout):
    def __init__(self, balance, name, number, interest_rate):
        BankAccout.__init__(self, balance, name, number)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance *= (1 + self.interest_rate)

class CheckingAccount(BankAccout):
    def __init__(self, balance, name, number, withdraw_charge = 10000):
        BankAccout.__init__(self, balance, name, number)
        self.withdraw_charge = withdraw_charge
    def withdraw(self, amount):
        self.balance -= (amount + self.withdraw_charge)

a1 = SavingsAccount(10000, "홍길동", 123456 , 0.05)
a1.add_interest()
print(a1.balance)

a2 = CheckingAccount(2000000, "김철수", 123457)
a2.withdraw(100000)
print(a2.balance)
