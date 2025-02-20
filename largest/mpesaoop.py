class User:
    def __init__(self, user_id,name,phone):
        self.user_id = user_id
        self.name = name
        self.phone = phone
        self.account=Account(self)
    def __repr__(self):
        return f"User({self.user_id},{self.name},{self.phone})" #Representation of the user object
    #define account class


class Account:
    def __init__(self, user):
        self.user = user
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0 : #check if the deposit is more than zero
            self.balance += amount
            print(f"Amount deposited. New balance is: {self.balance}")
        else:

            print("deposited Amount must be positive")
    def withdraw(self, amount):
        if 0< amount <= self.balance: #check if the amount is valid
            self.balance -= amount
            print(f"{amount} is withdrawn. New balance is: {self.balance}")
        else:
            print("Insufficient funds")


    def __repr__(self):
        return f"Account(user: {self.user,"name"},Balance: {self.balance})"
#define the transaction class
class Transaction:
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
    def process(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)

        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print(f"invalid transaction type")
    def __repr__(self):
        return f"Transaction(Account: {self.account},Amount {self.amount}, Type{self.transaction_type})"



#example usage
user1=User(1,"James","+254798685468")
print(user1)

user1.account.deposit(1000)
print(user1)
user1.account.withdraw(500)
print(user1)
transaction1 = Transaction(user1.account,200,"deposit")
transaction1.process()
transaction2 = Transaction(user1.account,100,"withdraw")
transaction2.process()

print(user1.account)


user2=User(2,"Janet","+254799665468)")
print(user2)
user1.account.deposit(10000)
print(user2)
user2.account.withdraw(6000)
print(user2)
transaction1 = Transaction(user1.account,100,"deposit")
transaction1.process()
transaction2 = Transaction(user1.account,50,"withdraw")
transaction2.process()
print(user2.account)






user3=User(3,"Lisa","+254792665498)")
print(user3)
user3.account.deposit(100000)
print(user3)
user3.account.withdraw(30000)
print(user3)
transaction1 = Transaction(user1.account,6000,"deposit")
transaction1.process()
transaction2 = Transaction(user1.account,500,"withdraw")
transaction2.process()
print(user3.account)



user4=User(4,"Abby","+257599325468)")
print(user4)
user4.account.deposit(150000)
print(user4)
user4.account.withdraw(70000)
print(user4)
transaction1 = Transaction(user1.account,20000,"deposit")
transaction1.process()
transaction2 = Transaction(user1.account,5000,"withdraw")
transaction2.process()
print(user4.account)



user5=User(5,"Rina","+254783285468)")
print(user5)
user1.account.deposit(200000)
print(user5)
user5.account.withdraw(10000)
print(user5)
transaction1 = Transaction(user1.account,40000,"deposit")
transaction1.process()
transaction2 = Transaction(user1.account,4000,"withdraw")
transaction2.process()
print(user5.account)


