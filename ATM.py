class Account:
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
    
        return f'Account owner: {self.owner}\nAccournt balance: ${self.balance}'
    
    def deposit(self, amount=0):
        self.balance += amount
        print('Deposit Success!')
        print(f'The account balance is ${self.balance}')
    
    def withdraw(self, amount=0):
        if self.balance >= amount:
            self.balance -= amount
            print('Withdraw Success!')
            print(f'The account balance is ${self.balance}')
        else:
            print('Funds unavaliable')

acct = Account('Wentao', 100)
print(acct)

acct.deposit(50)
acct.withdraw(75)
acct.withdraw(100)