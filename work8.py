"""numbers=list(map(int,input("Enter numbers: ").split()))
square_numbers=map(lambda x: x*x,numbers)
print(list(square_numbers))


numbers=list(map(int,input("Enter numbers: ").split()))
even_num=filter(lambda x: x%2==0,numbers)
print(list(even_num))


from functools import reduce
numbers=list(map(int,input("Enter numbers: ").split()))
average=reduce(lambda x,y:x+y,numbers)
average/=len(numbers)
print(average)


marks=list(map(int,input("Enter marks: ").split()))
total=0
for i in marks:
  total+=i
avg=total/len(marks)
print(avg)


students=[
  {"name":"Anu","age":20},
  {"name":"Rahul","age":22},
  {"name":"Meera","age":21},
  {"name":"Arun","age":23},
]
total=0
for i in range(len(students)):
  total+=students[i]["age"]
avg=total/len(students)
print(avg)


employees=[
  {"name":"Anu","salary":30000},
  {"name":"Rahul","salary":45000},
  {"name":"Meera","salary":55000},
  {"name":"Arun","salary":40000},
]
total=0
for i in range(len(employees)):
  total+=employees[i]["salary"]
avg=total/len(employees)
print(avg)


employees=[
  {"name":"Anu","salary":25000},
  {"name":"Rahul","salary":45000},
  {"name":"Meera","salary":55000},
  {"name":"Arun","salary":28000},
  {"name":"Vijay","salary":60000},
]
total=0
count=0
for i in range(len(employees)):
  if employees[i]["salary"]>30000:
    count+=1
    total+=employees[i]["salary"]
avg=total/count
print(avg)

numbers=[15,25,35,45,55,65]
total=0
count=0
for i in numbers:
  total+=i
  count+=1
avg=total/len(numbers)
print(total)
print(count)
print(avg)


products = [
 {"name": "Laptop", "price": 55000},
 {"name": "Mouse", "price": 1200},
 {"name": "Keyboard", "price": 2500},
 {"name": "Monitor", "price": 15000}
]
total=0
for i in range(len(products)):
  total+=products[i]["price"]
avg=total/len(products)
print(avg)


orders = [
 {"id": 101, "amount": 1500},
 {"id": 102, "amount": 2500},
 {"id": 103, "amount": 3500},
 {"id": 104, "amount": 2000}
]
amounts=[order["amount"] for order in orders]
from functools import reduce
total=reduce(lambda x,y:x+y,amounts)
avg=total/len(orders)
print(avg)


orders = [
 {"id": 101, "amount": 1500, "status": "completed"},
 {"id": 102, "amount": 2500, "status": "pending"},
 {"id": 103, "amount": 3500, "status": "completed"},
 {"id": 104, "amount": 2000, "status": "cancelled"},
 {"id": 105, "amount": 4000, "status": "completed"}
]
total=0
count=0
for i in range(len(orders)):
  if orders[i]["status"]=="completed":
    total+=orders[i]["amount"]
    count+=1
avg=total/count
print(avg)



students = [
 {"name": "Anu", "marks": 75},
 {"name": "Rahul", "marks": 55},
 {"name": "Meera", "marks": 90},
 {"name": "Arun", "marks": 65},
 {"name": "Vijay", "marks": 85}
]
total=0
for i in range(len(students)):
  total+=students[i]["marks"]
avg=total/len(students)
print(avg)
above_average={}
for i in range(len(students)):
  if students[i]["marks"]>=avg:
    above_average[students[i]["name"]]=students[i]["marks"]
print(above_average)

employees = [
 {"name": "Anu", "salary": 30000},
 {"name": "Rahul", "salary": 50000},
 {"name": "Meera", "salary": 40000},
 {"name": "Arun", "salary": 70000},
]
total=0
for i in range(len(employees)):
  total+=employees[i]["salary"]
avg=total/len(employees)
print(avg)
above_average={}
for i in range(len(employees)):
  if employees[i]["salary"]>=avg:
    above_average[employees[i]["name"]]=employees[i]["salary"]
print(above_average)

products = [
 {"name": "Laptop", "price": 60000},
 {"name": "Mouse", "price": 1000},
 {"name": "Keyboard", "price": 2500},
 {"name": "Monitor", "price": 18000},
 {"name": "Phone", "price": 40000}
]
total=0
for i in range(len(products)):
  total+=products[i]["price"]
avg=total/len(products)
print(avg)
below_average={}
for i in range(len(products)):
  if products[i]["price"]<avg:
    below_average[products[i]["name"]]=products[i]["price"]
print(below_average)


numbers = [10, 25, 30, 45, 50, 60, 75]
total=0
for i in numbers:
  total+=i
avg=total/len(numbers)
print(avg)
greater_average=[]
for i in numbers:
  if i >avg:
    greater_average.append(i)
print(greater_average)

temperatures = [28, 31, 29, 35, 32, 27, 30]
total=0
for i in temperatures:
  total+=i
avg=total/len(temperatures)
print(avg)
greater_average=[]
for i in temperatures:
  if i >avg:
    greater_average.append(i)
print(greater_average)

customers = [
 {"name": "Anu", "spent": 5000},
 {"name": "Rahul", "spent": 3500},
 {"name": "Meera", "spent": 7500},
 {"name": "Arun", "spent": 4000}
]
from functools import reduce
amount=[customer["spent"] for customer in customers]
total=reduce(lambda x,y:x+y,amount)
avg=total/len(customers)
print(avg)



users = [
 {"name": "Anu", "age": 22, "active": True},
 {"name": "Rahul", "age": 25, "active": False},
 {"name": "Meera", "age": 28, "active": True},
 {"name": "Arun", "age": 24, "active": True},
 {"name": "Vijay", "age": 30, "active": False}
]
total=0
count=0
for i in range(len(users)):
  if users[i]["active"]==True:
    total+=users[i]["age"]
    count+=1
avg=total/count
print(avg)



transactions = [
 {"id": 1, "amount": 1000, "status": "success"},
 {"id": 2, "amount": 2500, "status": "failed"},
 {"id": 3, "amount": 3000, "status": "success"},
 {"id": 4, "amount": 1500, "status": "success"},
 {"id": 5, "amount": 4000, "status": "failed"}
]
amounts=[transaction["amount"] for transaction in transactions if transaction["status"]=="success"]
from functools import reduce
total=reduce(lambda x,y:x+y,amounts)
avg=total/len(amounts)
print(avg)

"""

sales = [
 {"month": "January", "amount": 50000},
 {"month": "February", "amount": 65000},
 {"month": "March", "amount": 55000},
 {"month": "April", "amount": 70000},
 {"month": "May", "amount": 60000}
]
total=0
for i in sales:
  total+=i["amount"]
avg=total/len(sales)
print(avg)
