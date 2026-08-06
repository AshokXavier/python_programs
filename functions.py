"""
SYNTAX:

def function_name(parameters):
  code to be executed

"""
"""
TYPES:
1. Built-in Functions
2. User-defined Functions
3. Lambda or anonymous Functions

 User-defined Functions:
 2 Types-
  with argumnet:
     positional
     keyword
     default

  without argumnet
"""
"""
#user-defined functions without argument

def welcome():
  print("Welcome to python programming")

welcome()

#user-defined functions with argument

def greeting(user_name,user_age):
  print(f"Welcome {user_name}, you are {user_age} years old")

greeting("Ash",22)

def addition(num1,num2):
  return num1+num2

print(addition(2,3))

def addition(num1,num2):
  return num1+num2

num1=int(input())
num2=int(input())
print(addition(num1,num2))


#positional argument
def book_ticket(movie_name,cust_name,seats,ticket_price):
  total=seats*ticket_price
  return f"{cust_name} booked {seats} tickets for {movie_name}\n Total Amount: {total}"

print(book_ticket("Eko","ash",2,150))

#keyword arguments
def customer_details(customer_name,customer_age,city):
  print(f"{customer_name}\n{customer_age}\n{city}")
customer_details(customer_age=22,customer_name="ash",city="Ney York")
#default arguments

def booking_status(customer_name,status="confirmed",screen="screen1"):
  print(f"{customer_name}'s booking status: {status}\nScreen Allocated: {screen}")
booking_status("Ash")
booking_status("Ash","pending")
booking_status("Ash","pending","screen2")


#Passing multiple arguments
#  *args = multiple arguments
#  **kwargs = keyword arguments
def calculate_bill(*ticket_prices):
  print(f"Tickect Prices: {ticket_prices}")
  print(f"Total Bill: {sum(ticket_prices)}")

calculate_bill(200,300,400,500,600)

#Passing multiple keyword arguments
def passenger_info(**details):
  for key,value in details.items():
    print(f"{key} : {value}")

passenger_info(
              passenger_info="ash",
               seats=2,
               payment_status="pending",
               destination="punjab"
               )

"""

#built-in functions
"""print(len("Welcome"))
print(sum([45,36,53,23]))
print(max([45,36,53,23]))
print(min([45,36,53,23]))
print(sorted([45,36,53,23]))
print(sorted([45,36,53,23],reverse=True))


languages=["tamil","Malayalam","english"]#Capz has lower Ascci digit compared to lower case
# M=77,e=101,t=116
# t=116-77=39 (so swap tamil to right)
# M=77-116=-39 (so swap Malayalam to left)
print(sorted(languages))
print(sorted(languages,reverse=True))
print(sorted(languages,reverse=True,key=len))

# Try out Enumerate Function

#legb rule - l = local. e = enclosing, g = global, b = built-in

def student_details():
  name="Ash"  # Local Variable
  print("Student Name: ",name)

student_details()
#print("Student Name: ",name)
college_name="Carmel" #Global Variable
def display():
  print("College name is: ",college_name)

display()
print("College name is: ",college_name)
"""

"""#Enclosing example
def department():
  dept_name="CSE"
  def student():
    print("Department : ",dept_name)
  student()
department()

# Billing System
# tax - global variable, discount enclosing, amount - local

tax=100
def shopping():
  discount=20
  def bill():
    amount=500
    total_amount=amount+tax-discount
    print("Total Bill : ",total_amount)

  bill()
shopping()


fact=1
num=int(input())
for i in range(1,num+1):
  fact=fact*i

print(fact)


#Recursion
def factorial(number):
  if number==1:
    return 1
  else:
    return number*factorial(number-1)

num=int(input("Enter a number"))
print(f"Factorial of {num} is {factorial(num)}")


#Working : 
#  3*factorial(2)
#  3*2*factorial(1)
#  3*2*1=6



#lambda function
def add(num1,num2):
  return num1+num2
print(add(3,6))
"""
"""
SYNTAX:
 lambda arguments: expressions

add= lambda a,b: a+b
print(add(3,6))

square=lambda c:c**2
print(square(3))

largest=lambda a,b: a if a>b else b
print(largest(2,4))
"""

#Prime Number
