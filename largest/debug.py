class User:
    def __init__(self,user_id,name,phone):
        self.user_id = user_id   #initialize user id
        self.name = name           #initilize username
        self.phone = phone          #initialize user phone number
        self.account=Account(self)   #creating an account for the user
    def __repr__(self):
        return f"User( {self.user_id}, {self.name}, {self.phone})"   #Representation of the user Object
# define account class
class Account:
    def __init__(self,user):
        self.user = user
        self.balance=0.0
    def deposit(self,amount):
        if amount > 0:          #check if the deposit is more than 0
            self.balance+=amount
            print(f"amount deposited. New balance: {self.balance}")
        else:
            print("deposited Amount must be positive")


def withdraw(self,amount):
        if 0< amount <=self.balance:  #check if the withdrawal amount is valid
            self.balance-=amount
            print(f"amount withdrawn. New balance is: {self.balance}")
        else:
            print("Insufficient funds or invalid amount")



def __repr__(self):
        return f"Account( User: {self.user.name}, Balance: {self.balance}"  #Represenation of Account object
# define the transaction class
class Transaction:
    def __init__(self,account,amount,transcation_type):
        self.account=account
        self.amount=amount
        self.transaction_type=transcation_type
def process(self):
    if self.transaction_type == 'deposit':
        self.account.deposit(self.amount)
    elif self.transaction_type == "withdraw":
        self.account.withdraw(self.amount)
    else:
        print("Invalid transaction type")
def __repr__(self):
    return f"Transaction(Account: {self.account.user.name},Amount : {self.amount},Type{self.transaction_type}"

user1=User(1,"Erick Were",723633522)
print(user1)


user1.account.deposit(1000)
print(user1)

user1.account.withdraw(5000)
print(user1)


transaction1 = Transaction(user1.account,200,"deposit")
transaction1.process()

transaction1 = Transaction(user1.account,200,"withdraw")
transaction2.process()

print(user1.account)