#Fibanocci Series
#0 1 1 2 3 5 8 13 ....
"""num=int(input("Enter the number of iterations: "))
a=0
b=1
print(a,b,end=" ")
for i in range(2,num):
  c=a+b
  print(c,end=" ")
  a=b
  b=c
  
  or
for i in range(num):
  print(a,end=" ")
  c=a+b
  a=b
  b=c
"""

"""
a=0,b=1,c=a+b=0+1=1
a=b,b=c
a=1,b=1,c=a+b=1+1=2
a=1,b=2,c=a+b=1+2=3
a=2,b=3,c=a+b=2+3=5
"""

#Find the largest and smallest from a list of elements
# li=list(map(int,input().split(" ")))
# or

"""user_input=[]
num_of_iterations=int(input("Enter the noof Elements: "))
for i in range(num_of_iterations):
  # user_input.append(int(input()))
  num=int(input(f"Enter item {i+1}: "))
  user_input.append(num)
largest=user_input[0]
smallest=user_input[0]"""
"""
12,34,56,78,4
largest=12, smallest=12, num=12
num>largest then swap
num<smallest then swap
12>12 - false, 12<12 false
num=34
34>12 - true so largest=34
num=56
56>34 - true so largest=56
num=78
78>56 - true so largest=78
num=4
4<12 - true so smallest=4
"""
"""for i in range(1,num_of_iterations):
  if user_input[i]>largest:
    largest=user_input[i]
  elif user_input[i]<smallest:
    smallest=user_input[i]

print(f"Largest number is : {largest}\n Smallest number is : {smallest}")"""

"""li=[]
num_of_iterations=int(input("Enter number of iterations: "))
for i in range(num_of_iterations):
  num=int(input(f"Entet item {i+1}: "))
  li.append(num)
positive,negative=[],[]

for num in li:
  if num>0:
    positive.append(num)
  elif num<0:
    negative.append(num)
print(f"Positive List: {positive} .\nNegative List: {negative}")"""



#Collect as a set of tuple elements and count the no occurence of a given elemnts

"""number=int(input("Enter the no of elements: "))
user_tuple=()
for i in range(number):
  n=int(input("Enter Item: "))
  user_tuple=user_tuple+(n,)"""

"""user_tuple=tuple(map(int,input("Enter Tuple ELement").split()))
num=int(input("enter the number: "))
c=0
for i in user_tuple:
 if i==num:
   c+=1
print("Tuple Elements are ",user_tuple)
print(f"Occurrence of number {num} = {c}")"""

"""#Collect as a set of tuple elements and count the no occurence of each elemnts
user_tuple=tuple(map(int,input("Enter Tuple ELement").split()))
li=[]
for i in user_tuple:
  c=0
  if i not in li:
    for j in user_tuple:
      if i==j:
        c+=1
    print(f"Occurence of Element {i} = {c}")
    li.append(i)"""

#Not using list
user_tuple=tuple(map(int,input.split()))
for i in range(len(user_tuple)):
  found=False
  # Check if this element has already appeared
  for j in range(i):
    if user_tuple[i]==user_tuple[j]:
      found=True
      break
  if found==False:
    count=0

    for k in range(len(user_tuple)):
      if user_tuple[i]==user_tuple[k]:
        count+=1

    print(user_tuple[i]," = ",count)


#Reverse a Dictionary
"""
data={
  "a":1,
  "b":2,
  "c":3
}
reverse_dict={}
keys=list(data.keys()) #["a","b","c"] - list
for key in keys[::-1]:
  reverse_dict[key]=data[key]

print(reverse_dict)
"""


""" #Linear Search
user_marks=list(map(int,input("Enter the Elements to be Inserted: ").split()))
search_element=int(input("Enter the Element to Search: "))
for i in range(len(user_marks)):
  if user_marks[i]==search_element:
    print(f"Element found at position {i+1} ")
    break
else:
  print("Element not found")"""

#Bubble Sort

"""user_input=list(map(int,input("Enter the Elements: ").split()))
for i in range(0,len(user_input)-1):
  for j in range(0,len(user_input)-1):
    if(user_input[j]>user_input[j+1]):
      user_input[j],user_input[j+1]=user_input[j+1],user_input[j]

print(user_input)"""

# or

"""def bubble_sort(numbers):
  n=len(numbers)
  for i in range(n-1):
    for j in range(i+1,n):
      if numbers[i]>numbers[j]:
        numbers[i],numbers[j]=numbers[j],numbers[i]
  return numbers
user_input=list(map(int,input("Enter the Elements: ").split()))
print(bubble_sort(user_input))
"""