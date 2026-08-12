"""name="ashok"
age=22

file=open("filename","mode")"""
file=open("student.txt","w") #write mode - if no such file exists it will automatically create a file
# r- read
# w- write
# a- append
# x- create
# r+ - read+write
# w+ - write+ read
# a+ - append+read
# b - binary
# t- text mode

file.write("ashok")
file.close()
file=open("student.txt","r")
data=file.read()
print(data)
file.close()
file=open("student.txt","w+")
file.write("xavier")

file.write("\nhello")
file.writelines(["\npython ","django ","react"])
file.seek(0)
data=file.read()
print(data)
file.close()

with open("employee.txt","w+") as file: # file.colse() not needed
  file.writelines(["rahul","\nanju"])
  file.seek(0)
  print(file.read())
# print(file.readline())
# print(file.readlines())

#read() readline() readlines()
#write() writeline()

"""with open("message.txt","r") as file:
  print(file.tell())#0
  data=file.read(5)
  print(data)#5
  print(file.tell())
  file.seek(0)
  print(file.tell())"""

with open("message.txt","r") as file:
  print(file.tell())
  file.seek(3)
  print(file.read())
  print(file.tell()) 

with open("message.txt","a+") as file:
  file.write(" program")
  file.seek(0)
  print(file.read())


# with open("sample.txt", "x") as file:
#     file.write(" program")



import os
source="message.txt"
destination="message_copy.txt"

with open(source,"r") as f:
   data=f.read()
with open(destination,"w") as f:
   f.write(data)

print("File copied sucessfully")
