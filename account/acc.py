
class Account:
    """This class is a generic account class"""
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """This class generates checking account objects"""
    type = 'checking'

    def __init__(self, filepath, fee):
        self.filepath = filepath
        self.fee = fee
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance -= amount + self.fee

jack_checking = Checking('jack.txt', 1)
jack_checking.transfer(110)
jack_checking.commit()
print(jack_checking.balance)

john_checking = Checking('john.txt', 1)
john_checking.transfer(110)
john_checking.commit()
print(john_checking.balance)
print(john_checking.__doc__)