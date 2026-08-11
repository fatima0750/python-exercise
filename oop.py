#practice 1
"""class Person:
    name="fatima"
    lastname="hoseini"

p1=Person()
p2=Person()

print(p2.lastname)
p2.lastname="Eskandari"
print(p2.lastname)

del p1
"""
#===============================================
#Pratice 2
'''
class Person:
    def __init__(self,name="Fatima",lastname="Eskandari"):
        self.name=name
        self.lastname=lastname
    
    def Hello(self):
        print(f"hello {self.name} {self.lastname}")

p1=Person()
p1.Hello()

class Teacher(Person):  #child
    def __init__(self,name,lastname,lesson):
        Person.__init__(self,name,lastname)
        self.lesson=lesson 

    def Teaching(self):
        print(f"Hello I'm {self.name} {self.lastname} and i teach {self.lesson}.")

t1=Teacher("Nahid","Ghodrati","Math")
t1.Teaching()
'''
#=========================================
#practice 3
'''
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(self.balance)

    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(self.balance)    
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f" Balane : {self.balance} ")

account1=BankAccount("fatima",1000)
account1.deposit(500)
account1.withdraw(300)
account1.show_balance()
'''
#==========================================
#practice 4 :sssooooooo hard for me
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class ShoppingCard:
    def __init__(self):
        self.Products=[]

    def add_product(self,product):
        self.Products.append(product)
        print(f"{product.name} is added.")

    def remove_product(self,product):
        if product in self.Products:
            self.Products.remove(product)
            print(f"{product.name} is removed.")
        else:
            print(f"{product.name} is not found.")

    def show_product(self):
        for product in self.Products:
            print(product.name ,'-', product.price)

    def total_price(self):
        total=0
        for product in self.Products:
            total+= product.price
        return total

p1=Product("book",1500)
p2=Product("pen",750)
cart=ShoppingCard()
cart.add_product(p1)
cart.add_product(p2)
cart.show_product()
print("Total:" , cart.total_price())

