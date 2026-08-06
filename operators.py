# 1.Arithmetic 
# 2.Assignment
# 3.Logocal
# 4.Comparison
# 5 Bitwise
# 6 Membership
# 7 Identity
'''
price_per_book=500
quantity=25
total_price=price_per_book*quantity
average=total_price/quantity
extra_charge=50
final_price=total_price+extra_charge
discount_amount=25
final_price=final_price-discount_amount
rem=final_price%quantity
floor_div=final_price//7
squared_value=final_price**2
print(f"Price of one book is: {price_per_book}.\n\
Quantity of books is: {quantity}.\n\
Final amount is: {final_price}.\n\
Remainder:{rem}\n\
Floor Dvision: {floor_div}\n\
Squared Value is: {squared_value}\n")

#Assignment Operators
score=100
score+=50
score-=20
score*=2
print(score)

#Logical Operators

user_name="admin"
password="admin123"

entered_user_name=input("Enter Username: ")
entered_password=input("Enter Password: ")

if entered_user_name==user_name and entered_password==password:
  print("Login Succesfull")
else:
  print("Invalid Login")

day=input("Enter a Day: ")
if day=="Saturday" or day=="Sunday":
  print("Holiday")
else:
  print("Working Day") 

is_logged_in=False
if not is_logged_in:
  print("Please Log in") 
else:
  print("Welcome")


#membership operator

movies_list=["Avatar","Osyssey","GOT"]
movie=input("Enter your favourite movie: ")
if movie in movies_list:
  print("Movie Available")
else:
  print("Movie is not available")


employee_list=["Ravi","Shankar","Adam"]
employee=input("Enter Employee name: ")
if employee not in employee_list:
  print("Access Denied")
else:
  print("Acess Granted")

#Idenity Operator
value1=5
value2=8
print(value1 is value2)


num_list1=[1,2,3,4]
num_list2=[1,2,3,4]
print(num_list1 is num_list2)
print(num_list1 is not num_list2)
print(num_list1 == num_list2)

list1=[10,20,30,40]
list2=[10,25,30,45]
print(list1[0] is list2[0])
print(id(list1[0]))
print(id(list2[0]))
list3=list2
print(list3 is list2)


age=int(input("Enter your age: "))
if age>=18:
  print("Eligible to vote")
else:
  print("Not eligible to vote")

student_name=input("Enter student name: ")
student_mark=int(input("Enter student marks:"))
print("Pass: ",student_mark>=40)
print("Distinction:",student_mark>=80)
print("Full Marks:",student_mark==100)
print("Needs Improvement:",student_mark<40)
print("Not Zero: ",student_mark!=0)
print("Below A Grade: ",student_mark<=85)
'''
num1=5 #0101
num2=3 #0011
print(num1 & num2)
print(num1 | num2)
print(num1^num2)
print(~num1)

print(5<<2)
print(5>>2)

