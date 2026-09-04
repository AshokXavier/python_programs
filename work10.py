#Exception Handling 
#1
try:
  a=10
  b=0
  print(a/b)
except ZeroDivisionError:
  print("Zero Division error")

#2
try:
  a=int(input("enter value for a: "))
  b=int(input("enter value for b: "))
  print(a/b)
except ZeroDivisionError:
  print("Zero Division error")


#3
try:
  num=int(input("Enter number: "))
except ValueError:
  print("please enter integer value")

#4
try:
  li=[2,4,6,8]
  print(li[4])

except IndexError:
  print("Invalid index")


#5
try:
  di={"name":"ashok","age":22}
  print(di["address"])
except KeyError:
  print("Key not found")


#6
try:
  num1=int(input("Enter first number: "))
  num2=int(input("Enter second number: "))
  result=num1/num2
  print(result)

except ZeroDivisionError:
  print("Cannot divide by zero")

except ValueError:
  print("Please enter numbers only")

except TypeError:
  print("Invalid Data Type")

#7
try:
  a=int(input("Enter a number: "))
  b=int(input("Enter a number: "))

  print(a/b)

except ZeroDivisionError:
  print("Zero division error")

else:
  print("Try block is executed")

finally:
  print("This block always executes")

#8
age=int(input("Enter age: "))
if age<18:
  raise ValueError("Not Valid")
print("Valid")



#9
try:
  num=int(input("Enter number: "))
  if num>0:
    print("Positive")
  elif num<0:
    print("Negative")
  else:
    print("Zero")
except ValueError:
  print("Invalid Input. Please enter a number")


#10
class InvalidMarkError(Exception):
  pass

try:
  mark=int(input("Enter student's mark: "))

  if mark<0 or mark>100:
    raise InvalidMarkError("Mark must be between 0 and 100")
  print("Valid mark")

except InvalidMarkError as e:
  print("Invalid Mark: ",e)

except ValueError:
  print("Please enter a valid number")
  



#File handling
 
#1
file=open("sample.txt","w")
file.write("ashok")
file.close()

#2
with open("sample.txt") as file:
  data=file.read()
  print(data)

#3
with open("sample.txt","a") as file:
  file.write(" xavier")

#4
with open("sample.txt","r") as file:
  lines=file.readlines()
print("Number of lines: ",len(lines))

#5
with open("sample.txt","r") as file:
  content=file.read()
word=content.split()
print("No of words: ",len(word))

#6
with open("sample.txt","r") as file:
  content=file.read()
  content.replace(" ","")
  print(len(content))

#7
with open("sample.txt","r") as file:
  data=file.read()

with open("sample1.txt","w") as file:
  file.write(data)

#8
with open("sample.txt","r") as file:
  content=file.read()
  words=content.split()
  if "ashok" in words:
    print("Found")
  else:
    print("Not Found")

#9
with open("sample.txt","r") as file:
  lines=file.readlines()
for i in lines:
  if "has" in i:
    print(i)

#10
with open("sample.txt","r") as file:
  content=file.read()
  print(content[::-1])

#11
name = input("Enter student name: ") 
age = input("Enter student age: ") 
mark = input("Enter student mark: ")

with open("student.txt", "w+") as file: 
  file.write("Name: " + name + "\n") 
  file.write("Age: " + age + "\n") 
  file.write("Mark: " + mark + "\n")

  file.seek(0)
  print(file.read())
  
#12
import os 
filename = input("Enter the file name: ") 
if os.path.exists(filename):
   print("File exists.") 
else: 
  print("File does not exist.")


#13

with open("sample3.txt","r") as file:
  content=file.read()
values=content.split()
total=0
count=0
for value in values:
  try:
    total+=int(value)
    count+=1
  except ValueError:
    pass

if count>0:
  avg=total/count
  print("Sum is: ",total)
  print("Average is: ,",avg)
else:
  print("No numbers Found")


#14
with open("sample4.txt","r") as file:
  text=file.read()

vowels=0
consonants=0
digits=0
spaces=0

for ch in text:
  if ch.lower() in "aeiou":
    vowels+=1
  elif ch.isalpha():
    consonants+=1
  elif ch.isdigit():
    digits+=1
  elif ch==" ":
    spaces+=1

print("Vowels:", vowels) 
print("Consonants:", consonants) 
print("Digits:", digits) 
print("Spaces:", spaces)

#15
with open("sample3.txt") as file1:
  data1=file1.read()

with open("sample4.txt") as file2:
  data2=file2.read()

with open("sample5.txt","w") as file3:
  file3.write(data1)
  file3.write("\n")
  file3.write(data2)