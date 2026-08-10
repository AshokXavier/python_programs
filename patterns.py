"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
for i in range(5):
  for j in range(5):
    print("*",end=" ")
  print()

"""
*
* *
* * *
* * *
* * * * *
"""
for i in range(5):
  for j in range(i+1):
    print("*",end=" ")
  print()
# or
for i in range(5):
  print("* "*(i+1))

"""
* * * * *
* * * *
* * *
* *
*
"""

for i in range(5):
  for j in range(i,5):
    print("*",end=" ")
  print()

#hollow square
"""
* * * * *
*       *
*       *
*       *
* * * * *"""
n=int(input("Enter rows: "))
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j==0 or j==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

"""
        * 
      * *
    * * *
  * * * *
* * * * *
"""
print()

for i in range(5):
  for j in range(i,4):
    print(" ",end=" ")
  for j in range(i+1):
    print("*",end=" ")
  print()

"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
print()
for i in range(5):
  for j in range(i,4):
    print(" ",end=" ")

  for j in range(i):
    print("*",end=" ")

  for j in range(i+1):
    print("*",end=" ")

  print()

# inverse pyramid
print()
for i in range(5):

  
  for j in range(i):
    print(" ",end=" ")

  for j in range(i,4):
    print("*",end=" ")

  for j in range(i,5):
    print("*",end=" ")


  print()


print()
for i in range(4):
  for j in range(i,4):
    print(" ",end=" ")

  for j in range(i):
    print("*",end=" ")

  for j in range(i+1):
    print("*",end=" ")

  print()


for i in range(5):

  
  for j in range(i):
    print(" ",end=" ")

  for j in range(i,4):
    print("*",end=" ")

  for j in range(i,5):
    print("*",end=" ")


  print()


for i in range(5):
  for j in range(5):
    print(i,end=" ")
  print()

for i in range(5):
  for j in range(5):
    print(j,end=" ")
  print()

for i in range(5):
  for j in range(5):
    print(chr(65 + i),end=" ")
  print()

for i in range(5):
  for j in range(5):
    print(chr(65 + j),end=" ")
  print()