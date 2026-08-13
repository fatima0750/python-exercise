#practice 1: Encapsulation
'''
class BankAccount:
    def __init__(self,name,balance):
        self.owner=name
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount
        print(f"{amount} has been deposited into your account.")

    def withdraw(self,amount):
        if amount>self.__balance:
            print("The requested amount for withdrawl exeeds your account balance.")
        else:
            self.__balance-=amount
            print(f"{amount} has been withdrawn from your account .")

    def get_balance(self):
        print(f"your account balance is {self.__balance}.")

a1=BankAccount("fatima eskandari",300)
a1.deposit(200)
a1.withdraw(100)
a1.get_balance()
'''
#================================================
#practice 2:
'''
class Student:
    def __init__(self,name,grade):
        self.name=name
        self.__grade=grade

    def set_grade(self,grade):
        if 0<=grade<=20:
            self.__grade=grade
        else:
            print("invalied grade.")

    def get_grade(self):
        print(f"{self.name}'s grade is {self.__grade}. ")

s1=Student("Fatima Eskandari", 19)
s1.set_grade(18)
s1.get_grade()
'''
