"""name="Python"
name.append("Programming") #Attribute Error
"""
"""
try:
  a=int(input("Enter a number: "))
  b=int(input("Enter a number: "))

  print(a/b)

except ZeroDivisionError:
  print("Zero division error")

except ValueError:
  print("type error")

else:
  print("Try block is execute")

finally:
  print("This block always executes")

#raising an error
age=int(input("Enter a age: "))
if age<18:
  raise ValueError("Not valid")
else:
  print("Valid")


#Exception handling using file
try:
  with open("file.txt","r") as f:
    print(f.read())
except FileNotFoundError:
  print("File not Found")
"""

