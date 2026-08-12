#practice 1
'''
class Person:
    def __init__(self,name,lname):
        self.name=name
        self.lastname=lname

    def printinf(self):
        print(f"i'm {self.name} {self.lastname}")

class Mom(Person):
    def __init__(self, name, lname,child):
        Person.__init__(self,name,lname)
        self.child=child

    def printinffromMom(self):
        print(f"i'm {self.name} {self.lastname} and i have {self.child} child .")

p1=Person("zahra","alizadeh")
p1.printinf()
m1=Mom("Mari","tgh",2)
print(m1.name)
m1.printinf()
m1.printinffromMom()
'''
#===========================
#practice 2
"""
class Car :
    def __init__(self,brand,name):
        self.name=name
        self.__brand=brand#private
    def printBrand(self):
        print(self.__brand) #access private properties
    def set_brand(self,brand):
        self.__brand=brand #change private properties with function

car1=Car("benz",2026)
print(car1.name)
car1.printBrand()
car1.set_brand("2019")
car1.printBrand()
car1.__brand=2009 #not change becuase it's private
car1.printBrand()
car1.name="bmw"
print(car1.name) #but this propertie change becuase it's public
"""
#============================
#practice 3:
"""
class Animal :
    def make_sound(self):
        print(":)))))))))))))")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Dog(Animal):
    def make_sound(self):
        print("Woof")

animal1=Animal()
cat1=Cat()
dog1=Dog()
animal1.make_sound()
cat1.make_sound()
dog1.make_sound()
"""
#=============================
#practice 4:
"""
class Employee:
    def __init__(self,name):
        self.name=name
    def work(self):
        print(f"{self.name} is work hard.")

class Programmer(Employee):
    def work(self):
        print(f"{self.name} is coding.")

class Designer(Employee):
    def work(self):
        print(f"{self.name} is designing.")

class Manager(Employee):
    def work(self):
        print(f"{self.name} is managering.")

e1=Employee("Mr alizadeh")
p1=Programmer("Mr hosseini")
d1=Designer("Mr Lashani")
m1=Manager("Mr shamekhi")
employees=[e1,p1,d1,m1]
for x in employees:
    x.work()
"""
#==========================
#practice 5:
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def get_price(self):
        print(f"your receipt is {self.price}")

class Book(Product):
    pass

class Clothing(Product):
    def get_price(self,darasad):
        n=self.price/100*darasad
        print("your receipt is" , self.price)


class Food(Product):
    def get_price(self,darasad):
        n=self.price/100*darasad
        print("your receipt is" ,self.price-n)

p1=Book("melat Eshgh",250)
p2=Food("Pasta",100)
p3=Clothing("Tshirt",200)

p1.get_price()
p2.get_price(10)
p3.get_price(10)
