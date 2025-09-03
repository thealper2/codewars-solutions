class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    
    def add_cash(self, value):
        self.balance += value
        return f"{self.name} has {self.balance}."
        
    def withdraw(self, value):
        if self.balance < value:
            raise ValueError()
            
        self.balance -= value
        return f"{self.name} has {self.balance}."
    
    def check(self, other, value):
        if not other.checking_account:
            raise ValueError()
        
        if other.balance < value:
            raise ValueError()
            
        other.balance -= value
        self.balance += value
        return f"{self.name} has {self.balance} and {other.name} has {other.balance}."
