"""user_name="ashok"
# 0 1 2 3 4 (Positive Indexing)
# a s h o k
#-5-4-3-2-1 
print(user_name[2])
print(user_name[-3])
print(user_name[5])"""

"""data="Python is a Programming Language" 
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 
# P y t h o n - i s - a - P r  o  g  r  a  m  m  i  n  g  -  L  a  n  g  u  a  g  e
print(data[1:8])
print(data[0:14])
print(data[-10:-3])
print(data[0:14:2])
print(data[:-6])
print(data[6:])
print(data[::3])
print(data[-32:])
print(data[::-1])"""

"""# String Concatenation
string1="hello"
string2=" world"
print(string1+string2)

#String Repetition
print(string1*3)

#Membership
print("he" in string1)"""

"""#String Methods
car="Driven by passion, powered by BMW. Built to thrill."
print(car.upper())
print(car.lower())
print(car.capitalize())
print(car.title())

print(car.startswith("Dr"))
print(car.endswith("thrill."))

#car[3]="t"
#print(car)

print(id(car))
upper_case=car.upper()
print(id(upper_case))"""

"""#Lists

user_data = ["Ashok",22,"Alappuzha"]
print(user_data)
user_data.insert(2,"Carmel")
user_data.append(2026)
user_data.extend("Python")
print(user_data)
user_data.append(["English","Maayalam"])
user_data.extend(["HTML","CSS"])
print(user_data)
print(user_data[11])
print(user_data[11][0])

user_data.remove("HTML")
user_data.pop(2)
print(user_data)

user_data.reverse()
print(user_data)"""

"""#Tuple
tuple1=(2,5,7,8)
print(tuple1)
#Nested Tuple
nested_tuple=("David","Sanjay","Sayooj",(22,25,45,55))
print(nested_tuple)

# tuple1[1]=12
# print(tuple1)

#Try out Indexing and Slicing

#Tuple Unpacking
person=("ashok",22,"alappuzha")
print(person)
name,age,place=person
print(age)

numbers=(10,20,30,40,50)
a,b,*c=numbers
print(c)

d,*e,f=numbers
print(d)
print(e)
print(f)

number_repeated=(2,4,5,6,2,7,8,3,1,5,7,3)
print(len(number_repeated))
print(number_repeated.count(3))
print(number_repeated.index(3))
print(number_repeated[3])"""

"""user_input=input("Enter a String: ")
c=0
for char in user_input:
  c+=1
print(c)"""

"""# First non-repeating character in a string
user_input=input("Enter the string: ")
for char in user_input:
  if user_input.count(char) == 1:
    print("First non repeating character is: ",char,"at index position",user_input.index(char))
    break
else:
  print("No non repeating character")
  """
"""user_input=input("Enter the string: ")
for i in range(len(user_input)):
  flag=True

  for j in range(len(user_input)):
    if i!=j and user_input[i]==user_input[j]:
      flag=False
      break
  if flag==True:
    print("First non repeating character is: ",user_input[i])
    break
else:
  print("No Non repeating characters")
"""

# SET - set is an unordered collection of mutable data structure that doesnot allow duplicate values
# Functionality - Union, Intersection and Difference
"""
student1={"english","hindi","malayalam"}
student2={"english","hindi","python"}
student3={"python","urdu"}
print(student1)
print(student2)
print(student3)

student1.add("Java")
# student1.add("C","C++")
student1.update(["C","C++"]) # Like extend in List

print(student1)
student1.update(["marathi","malayalam"])
print(student1)

# student1.pop()
# print(student1) 
    
student1.remove("hindi")
# student1.remove("html") while removing it shows error if the elent is not present
# student1.discard("html") Doesnot show error
      
print(student1)
print(student2)
print(student3)
print(student1.union(student2))
# print(student1|student2)
print(student1.intersection(student2))
# print(student1&student2)
print(student1.difference(student2))
print(student1.symmetric_difference(student2))

print(student1.isdisjoint(student3))

# Checkout subset and superset"""

"""# FROZENSET - immutable set
fs1=frozenset("asha")
numbers=frozenset([1,2,3,4,4])
print(numbers)"""


# DICTIONARY - It's a mutable DS that stores elemnts as key - value pairs
"""student={
  "name":"ashok",
  "age":22,
  "place":"Alapuzha"
}
print(student)
print(student["name"])
print(student.keys())
info=dict(city="New York",country="america")
print(info.keys())
print(info.keys())
print(student.get("marks"))
student["marks"]=96
print(student)
print(student.get("marks"))
student.pop("age")
print(student)
del student["place"
]
print(student)
"""

employee={
  "emp1":{
    "name":"ashok",
    "age":22
  },

  "emp2":{
    "name":"David","age":24
  },

  "emp3":{
    "name":"sanjay","age":20
  },
  "emp4":{
    "name":"sayoo","age":20
  }



}
print(employee["emp2"])
print(employee["emp2"]["age"])