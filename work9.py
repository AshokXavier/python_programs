"""
#Sum of digits of a number
num=int(input("Enter the number: "))
sum=0
while num>0:
  digit=num%10
  sum+=digit
  num=num//10
print(sum)

#Count of digits in a number
num=int(input("Enter the number: "))
count=0
while num>0:
  num=num//10
  count+=1
print(count)

#Largest digit in a number
num=int(input("Enter the number: "))
largest=0
while num>0:
  digit=num%10
  if digit>largest:
    largest=digit
  num=num//10
print(largest)


#Fibbonacci Series
num=int(input("Enter the number of terms: "))
x,y=0,1
print(x," ",y,end=" ")
for i in range(2,num):
  z=x+y
  x=y
  y=z
  print(" ",y,end=" ")


#Multiplication Table generator
num=int(input("enter the number"))
for i in range(1,11):
  print(f"{i} * {num} = {i*num}")

#Frequency of each digit
num=int(input("Enter the number"))
freq={}
while num>0:
  digit=num%10
  if digit not in freq:
    freq[digit]=1
  else:
    freq[digit]+=1
  num=num//10
freq=dict(sorted(freq.items()))
print(freq)

#prime nubers between 1 and 100
count=0
for num in range(2,101):
  i=2
  flag=True
  while i<num:
    if num%i==0:
      flag=False
      break
    i+=1
  if flag==True:
    count+=1
print(count)
       

#numbers divisible by both 3 and 5
for i in range(1,100):
  if i%3==0 and i%5==0:
    print(i)

#Sum of fatorials from 1 to n
sum=0
n=int(input("Enter the numbers:"))
for i in range(1,n+1):
  fact=1
  for j in range(1,i+1):
    fact=fact*j
  sum+=fact
print(sum)

#Numbers skipping multiples of 3
for i in range(1,100):
  if i%3!=0:
    print(i)

#Replace multiples of 5 with Five
num=[10,12,15,20,22,30]
for i in range(len(num)):
  if num[i]%5==0:
    num[i]="Five"
print(num)


#Count odd digits in a number
num=int(input("Enter the number: "))
count=0
while num>0:
  digit=num%10
  if digit%2!=0:
    count+=1
  num=num//10
  
print(count)



#Product of digits
num=int(input("Enter the number: "))
product=1
while num>0:
  digit=num%10
  product*=digit
  num=num//10
  
print(product)

#Elements greater then average
num=[10,20,30,40,50,60]
sum=0
for i in num:
  sum+=i
avg=sum/len(num)
for i in num:
  if i>avg:
    print(i)
"""
