
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

class Student:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def display(self):
    print(self.name)
    print(self.age)

student1=Student("ashok",22)
student2=Student("john",20)
student1.display()
student2.display()