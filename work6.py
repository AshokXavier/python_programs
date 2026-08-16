#1
class Student:
  def __init__(self,name,roll_no,marks):
    self.name=name
    self.roll_no=roll_no
    self.marks=marks

  def display(self):
    print(self.name,"\n",self.roll_no,"\n",self.marks)

  def check(self):
    if self.marks>40:
      print(self.name,": Pass")
    else:
      print(self.name," :Fail")

s=Student("ashok",18,88)
s.display()
s.check()

#2
class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
  def area(self):
    area=self.length*self.breadth
    print("Area is: ",area)
  def perimeter(self):
    perimeter=2*(self.length+self.breadth)
    print("Perimeter is: ",perimeter)

r=Rectangle(5,6)
r.area()
r.perimeter()

#3
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

#4
class Car_Info:
  def __init__(self,brand,model,year):
    self.brand=brand
    self.model=model
    self.year=year

  def display(self):
    print("Brand : ",self.brand,"\nModel : ",self.model,"\nYear : ",self.year)
    
c=Car_Info("BMW","2 Series Gran Coupe",2024)
c.display()

#5
class Emp_Salary:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary

  def annual_salary(self):
    annual_salary=12*self.salary
    print("Annual Salary : ",annual_salary)

e=Emp_Salary(input("Name: "),int(input("Salary:")))
e.annual_salary()

#6
class Book:
  def __init__(self,title,author,price):
    self.title=title
    self.author=author
    self.price=price

  def dispaly(self):
    print(self.title,"\n",self.author,"\n",self.price)

  def discount(self):
    discount_price=self.price-(self.price/100*10)
    print("After Dicount: ",discount_price)

b=Book("Fire and Ice","George",1000)
b.dispaly()
b.discount()


#7
class Mobile:
  def __init__(self,brand,model,price):
    self.brand=brand
    self.model=model
    self.price=price

  def display(self):
    print(f"Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}")

m=Mobile("RealMe","GT Series",30000)
m.display()


#8
class Circle:
  pi=3.14
  def __init__(self,radius):
    self.radius=radius
  def claculate(self):
    self.area=Circle.pi*self.radius*self.radius
    self.circumfrence=2*Circle.pi*self.radius
    print(f"Area: {self.area}\nCircumfrence: {self.circumfrence}")

c=Circle(5)
c.claculate()


#9
class Product:

  def __init__(self,name,price,quantity):
     self.name=name
     self.price=price
     self.quantity=quantity

  def total(self):
    self.total=self.quantity*self.price
    print("Total Bill: ",self.total)

p=Product("phone",30000,5)
# p.name="phone"
# p.price=30000
# p.quantity=5
p.total()


#10
class ATM:
  def __init__(self,pin,balance):
    self.pin=pin
    self.balance=balance

  def check_pin(self):
    if self.pin=="1988":
      print("PIN Verified")
      return True
    else:
      print("Wrong Pin")
      return False

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

b=ATM("1988",25000)
if b.check_pin():
  b.deposit()
  b.withdrawal()
  b.balance_display()