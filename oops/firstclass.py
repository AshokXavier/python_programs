
"""
#attributes
class Student:
  pass

student1=Student()
student2=Student()
student1.name="ashok"
student1.age=22
student1.course="python"

student1.name="david"
student1.age=22
student1.course="python"

print(student1.name)"""

"""
#methods
class Student:
  def study(self):
    print("Student is Studying")

  def attend_class(self):
    print("Student is attending class")

student1=Student()
student2=Student()
student1.study()
student2.study()"""


"""
#constructor
class Student:
  def __init__(self):
    #init is a special method that automatically runs when we create an object. it is mainly used to initialize the object data.
    print("object initialized")

student1=Student()"""

"""class Student:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def display(self):
    print(self.name)
    print(self.age)

student1=Student("ashok",22)
student2=Student("john",20)
student1.display()
student2.display()"""

"""
#use of variable inside a name
class Employees:
  company="abc-company" #class attribute
  def __init__(self,empl_name):
    self.empl_name=empl_name

e1=Employees("ashok") #e1 and e2 are instance attribute
e2=Employees("david")

print(e1.empl_name,e2.empl_name)
print(Employees.company)
print(e1.company)
"""


"""
#scope
class Student:
  school="xyz school" #class scope - accesible in all instance and  class(class variable).
  def __init__(self,name):
    self.name=name     #instance scope - accesible only via objects (instance variable)
    print(self.school)
  def show(self):
    marks=90    #local scope - accesible only inside instance method
    print(self.name,marks)
    print(self.school)

s1=Student("ashok")
s1.show()
print(Student.school)
print(s1.name)"""

"""
#shading (shadowing variable)

class Student:
  school="xyz school" #class scope - accesible in all instance and  class(class variable).
  def __init__(self,name):
    self.name=name
    self.school="abc school"   #instance scope - accesible only via objects (instance variable)
    print(self.school)
  def show(self):
    marks=90    #local scope - accesible only inside instance method
    print(self.name,marks)
    print(self.school)

s1=Student("ashok")
s1.show()
print(s1.school)
print(Student.school)
print(s1.name)
"""
"""
# protected atrribute

class Account:
  _balance=1000 #protected atrribute

class SavingsAccount(Account):
  def show_balance(self):
    print(self._balance)

acc=SavingsAccount()
acc.show_balance()  #allowed
print(acc._balance) #Allowed, but discouraged
"""

"""#private attribute

class Example:
  __password="123"
  def show(self):
    print(self.__password)

e=Example()
e.show()

# print(e.__password) Not allowed
"""
"""
#Inheritance

class Animal:
  def speak(self):
    print("Animal can make Sound")

class Dog(Animal):
  def bark(self):
    print("Dog can bark")

d=Dog()
d.bark()
d.speak()
"""
"""#multilevel inheritance

class GrandParent:
  def __init__(self):
    self.house="Big House"

  def show_grandparent(self):
    print(self.house)

class Parent(GrandParent):
  def __init__(self):
    super().__init__()
    self.car="BMW"
  def show_car(self):
    print(self.car)

class Child(Parent):
  def __init__(self):
    super().__init__()
    self.bike="Pulsar"

  def show_bike(self):
    print(self.bike)

c=Child()
c.show_bike()
c.show_car()
c.show_grandparent()
print(c.house)

class GrandParent:


  def show_grandparent(self):
    print("Hello1")

class Parent(GrandParent):

  def show_car(self):
    super().show_grandparent()
    print("Hello2")

class Child(Parent):

  def show_bike(self):
    super().show_car()
    print("Hello3")

c=Child()
c.show_bike()
c.show_car()



class Animal:
  def __init__(self,name):
    self.name=name
    print(self.name)

  def sound(self):
    print("Some Sound")

class Dog(Animal):
  def __init__(self,name, breed):
    super().__init__(name)
    self.breed=breed
    print(self.breed)

  def speak(self):
    super().sound()
    print("Woof")

d=Dog("Bruno","Labrador")
d.speak()


# or

class Animal:
  def __init__(self,name):
    self.name=name
    print(self.name)

  def sound(self):
    print("Some Sound")

class Dog(Animal):
  def __init__(self,breed):
    super().__init__("Bruno")
    self.breed=breed
    print(self.breed)

  def speak(self):
    super().sound()
    print("Woof")

d=Dog("Labrador")
d.speak()


#multipele inheritance
class Father:
  def house(self):
    print("Fathers House")

class Mother:
  def car(self):
    print("Mothers Car")

class Child(Father,Mother):
  pass

c=Child()
c.car()
c.house()

class Father:
  def __init__(self,house):
    self.house=house
    print("Fathers House: ",self.house)
class Mother:
  def __init__(self,car):
    self.car=car
    print("Mothers Car : ",self.car)

class Child(Father,Mother):
  def __init__(self):
    Father.__init__(self,"ABC")
    Mother.__init__(self,"BMW")


c=Child()


#Heirarchical Inheritance
class Animal:
  def __init__(self,name):
    self.name=name
    print(f"Animal name:{self.name}")

  def eat(self):
    print(f"{self.name} is eating")

class Dog(Animal):
  def __init__(self, name,breed):
    Animal.__init__(self,name)
    Animal.eat(self)
    self.breed=breed
    print(f"Dog breed: {self.breed}")

  def bark(self):
    print(f"{self.name} is barking")
class Cat(Animal):
  def __init__(self, name,color):
    Animal.__init__(self,name)
    Animal.eat(self)
    self.color=color
    print(f"Cat color: {self.color}")
  def meow(self):
    print(f"Cat name: {self.name}")

d=Dog("Tomy","Lab")
d.bark()
c=Cat("kitty","white")
c.meow()


class Person:
  def show_name(self,name):
    self.name=name
    print(self.name)
  
class Student(Person):
  def study(self):
    print("Student is Studying")

class Sports:
  def play(self):
    print("Student plays football")

class sports_student(Student,Sports):
  def attend_competition(self):
    print("Student attemps competition")

s1=sports_student()
s1.show_name("ashok")
s1.attend_competition()
s1.study()
s1.attend_competition()



class Dog:
  def speak(self):
    print("Dog is eating")
class Cat:
  def speak(self):
    print("Cat is eating" )
class Cow:
  def speak(self):
    print("Cow is eating" )

animal=[Dog(),Cat(),Cow()]
for a in animal:
  a.speak()


class CreditCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CashOnDelivery:
    def pay(self, amount):
        print(f"Pay ₹{amount} when product is delivered")


class Order:
    def checkout(self, payment_method, amount):
        payment_method.pay(amount)


order = Order()

order.checkout(CreditCard(), 1000)
order.checkout(UPI(), 750)
order.checkout(CashOnDelivery(), 500)



#Problems
#1
class Vehicle:
  def __init__(self,brand,speed):
    self.brand=brand
    self.speed=speed

class Car(Vehicle):
  def __init__(self, brand, speed,doors):
    self.doors=doors
    super().__init__(brand,speed)

  def display(self):
    print(f"Brand: {self.brand}\nSpeed: {self.speed}\nDoors: {self.doors}")

c=Car("BMW",100,4)
c.display() 

#2
class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary

class Developer(Employee):
  def __init__(self, name, salary):
    super().__init__(name, salary)
  def calaculate_bonus(self):
    self.salary=self.salary+(self.salary/100*5)



#Method Overriding
class Parent:
  def show_name(self):
    print("My name is ashok")

class Child(Parent):
  def show_name(self):
    print("Hello")

c=Child()
c.show_name()


#Encapsulation

class Student:
  def __init__(self,name,mark):
    self.name=name
    self.__mark=mark

  def get_mark(self):
    return self.__mark
  def set_mark(self,mark):
    if mark>=0 and mark<=100:
      self.__mark=mark
      return self.__mark


s=Student("ashok",85)
s1=Student("david",90)
print("Name: ",s.name)
print("Mark: ",s.get_mark())
print(s.set_mark(95))
# print(s.__mark) it will show error bcoz it is encapsulted data
print("Mark: ",s1.get_mark())
print(s.set_mark(105))

#Abstraction
from abc import ABC,abstractmethod

class Animal(ABC):
  @abstractmethod
  def sound(self):
   pass
class Dog(Animal):
  def sound(self):
    print("Dog barks")

class Cat(Animal):
  def sound(self):
    print("Meow")

c=Cat()
c.sound()
d=Dog()
d.sound()
a=Animal()



#Method Types

#1selfMethod
#2classMethod
class Student:
  mark=90
  @classmethod
  def change_mark(cls,mark):  #cls - refers to class itself
    cls.mark=mark
    return cls.mark

s1=Student()
print(s1.change_mark(100))
print(s1.mark)

#3StaticMethod
class Student:
  @staticmethod
  def college_name():
    print("ABC College")
Student.college_name()


class Calculator:
  def add(self,a,b):
    print(a+b)
  def add(self,a,b,c):
    print(a+b+c)

a1=Calculator()
a1.add(20,30,40)
# a1.add(20,30) not possible in python
#so
class Calculator:
  def add(self,a,b,c=0):
    print(a+b+c)

a1=Calculator()
a1.add(20,30,40)
a1.add(20,30) 


#Operator Overloading
class Student:
  def __init__(self,mark):
    self.mark=mark

  def __add__(self,other):
    return self.mark+other.mark

s1=Student(80)
s2=Student(85)
result=s1+s2
print(result)

class Student:
  def __init__(self,mark):
    self.mark=mark
  def __sub__(self,other):
    return self.mark-other.mark

s1=Student(90)
s2=Student(80)
result=s1-s2
print(result)

class Student:
  def __init__(self,mark):
    self.mark=mark
  def __mul__(self,other):
    return self.mark*other.mark

s1=Student(10)
s2=Student(2)
result=s1*s2
print(result)

class Student:
  def __init__(self,mark):
    self.mark=mark
  def __truediv__(self,other):
    return self.mark/other.mark

s1=Student(90)
s2=Student(80)
result=s1/s2
print(result)


class Student:
  def __init__(self,mark):
    self.mark=mark
  def __floordiv__(self,other):
    return self.mark//other.mark

s1=Student(90)
s2=Student(80)
result=s1//s2
print(result)

class Student:
  def __init__(self,mark):
    self.mark=mark
  def __mod__(self,other):
    return self.mark%other.mark

s1=Student(10)
s2=Student(3)
result=s1%s2
print(result)

class Student:
  def __init__(self,mark):
    self.mark=mark
  def __pow__(self,other):
    return self.mark**other.mark

s1=Student(2)
s2=Student(3)
result=s1**s2
print(result)

class Student:
  def __init__(self,mark):
    self.mark=mark
  def __eq__(self,other):
    return self.mark==other.mark

s1=Student(90)
s2=Student(80)
result=s1==s2
print(result)

class Student:
  def __init__(self,mark):
    self.mark=mark
  def __ne__(self,other):
    return self.mark!=other.mark

s1=Student(90)
s2=Student(80)
result=s1!=s2
print(result)

class Student:
  def __init__(self,mark):
    self.mark=mark
  def __lt__(self,other):
    return self.mark<other.mark

s1=Student(90)
s2=Student(80)
result=s1<s2
print(result)

class Student:
  def __init__(self,mark):
    self.mark=mark
  def __gt__(self,other):
    return self.mark>other.mark

s1=Student(90)
s2=Student(80)
result=s1>s2
print(result)

class Student:
  def __init__(self,mark):
    self.mark=mark
  def __le__(self,other):
    return self.mark<=other.mark

s1=Student(90)
s2=Student(80)
result=s1<=s2
print(result)


class Student:
  def __init__(self,mark):
    self.mark=mark
  def __ge__(self,other):
    return self.mark>=other.mark

s1=Student(90)
s2=Student(80)
result=s1>=s2
print(result)
"""

"""
#Iterator
numbers=[10,20,30,40] #Iterable: iter(),

# for i in numbers:
#   print(i)


a=iter(numbers) # a is an iter
# print(a)
print(next(a))
print(next(a))

#Generators in python
def num():
  yield 1
  yield 2
  yield 3

a=num()
print(next(a))
print(next(a))

def num():
  return 1
  return 2 #doesnot work
  return 3

a=num()
print(a)
"""

#Decarator


def message(func):
  def wrapper():
    print("Good Morning")
    func()
    print("Ashok")

  return wrapper

@message
def hello():
  print("Hello")

hello()

