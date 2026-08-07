"""
for variable in sequence:
  code to be executed

for variable in range(start,stop,skip):
  code to be executed
  
start- defaultvalue is 0
stop - number-1
skip - default 1(for +ve numbers)

WHILE LOOP SYNTAX

initialization
while condition:
  code to be ececuted
  updation

for and while are entry controlled loops
"""

"""
word=input("Enter a word")
for char in word:
  print(char,end="")



for i in range(5):
  print(i)
for i in range(1,10):
  print(i)
for i in range(5,36,3):
  print(i)
for m in range(10,1,-1):
  print(m)

for j in range(17,3,-3):
  print(j)


num=int(input())
for i in range(1,11):
  print(f"{num} x {i} = {num*i}")

val=1
while val<=10:
  print(val)
  val+=1
sum=0
val=1
iterations=int(input("Enter the no of Iterations: "))
while val<=iterations:
  sum+=val
  val+=1
print(sum)

rev=0
num=int(input())
temp=num
while temp>0:
  rem=temp%10
  rev=rev*10+rem
  temp//=10

print(rev)

if rev==num:
  print("Palindrome")

sum=0
num=int(input())
while num>0:
  rem=num%10
  sum+=rem
  num//=10 
print(sum)


fact=1
num=int(input())
for i in range(1,num+1):
  fact=fact*i
print(fact)
"""
#Prime Number
num=int(input())
flag=1
if num<=1:
  print("Not a prime")
else:
  for i in range(2,num):
    if num % i==0:
      flag=0
      break
  if flag==1:
    print("Prime Number")
  else:
    print("Not Prime")
      
