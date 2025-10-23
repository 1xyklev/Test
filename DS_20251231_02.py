class BankAccount:

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        
        print("{self.owner}의 계좌가 생성되었습니다.")

    def get_balance(self):
        return self.balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.balance = amount
        else: 
            print("0 이상의 값만 허용합니다.")

    def depoist(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("입금 불가")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("출금 불가")



a = BankAccount("A")
b = BankAccount("B")

a.deposit(100)
b.deposit(200)
a.withdraw(30)
a.withdraw(30)
b.withdraw(50)

print(f"{a.owner} 계좌의 현재 잔액:", a.get_balance())
print(f"{b.owner} 계좌의 현재 잔액:", b.get_balance())

a.set_blance(500)
print(f"{a.owner} 계좌의 수정된 잔액", a.get_balance())