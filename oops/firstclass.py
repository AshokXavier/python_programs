
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

"""#use of variable inside a name
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
print(c.house)"""

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
    print("Hello")

c=Child()
c.show_bike()

