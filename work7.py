"""#1
class Student:
  def __init__(self,mark1,mark2,mark3):
    self.mark1=mark1
    self.mark2=mark2
    self.mark3=mark3

  def grade(self):
    self.avg=(self.mark1+self.mark2+self.mark3)/3
    if self.avg>90:
      self.grade="A"
    elif self.avg>75:
      self.grade="B"
    elif self.avg>60:
      self.grade="C"
    elif self.avg>40:
      self.grade="D"
    else:
      self.grade="Fail"

c=Student(80,90,70)
c.grade()
print("Average Marks: ",c.avg) 
print("Grade: ",c.grade)   

#2
class BankAccount:
  def __init__(self,name,balance):
    self.name=name
    self.balance=balance

  def deposit(self):
    deposit=int(input("Enter Deposit Amount: "))
    self.balance+=deposit
    print("Deposited Succesfully")

  def withdrawal(self):
    withdraw=int(input("Enter the amount to be withdraw: "))
    if withdraw>self.balance:
      print("Withdrawal not possible. Insufficient Balance")
    else:
      self.balance-=withdraw
      print("Succesfully Withdraws")

  def balance_display(self):
    print("Balance Ammount: ",self.balance)

b=BankAccount("ashok",25000)
b.deposit()
b.withdrawal()
b.balance_display()
"""
#3
class Vehicle:
  def show(self):
    print("Vehicle")

class Car(Vehicle):
  def show(self):
    print("Car")

class Bike(Vehicle):
  def show(self):
    print("Bike")

c=Car()
c.show()
b=Bike()
b.show()