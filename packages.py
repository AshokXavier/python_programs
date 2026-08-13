"""import sys
print(sys.builtin_module_names)

import math
import inspect
# help(math) #documentation
print(dir(math)) #Shows everything available in math
# functions=inspect.getmembers(math,inspect.isfunction)
# print(functions)
from math import sqrt
print(sqrt(16))
print(math.factorial(5))"""

# from math import sqrt
# print(sqrt(16))

"""from math import sqrt as  squareroot
print(squareroot(25))
from math import pow as power
print(power(5,2))"""

"""import random
print(random.randint(1,10))
print(random.random())
li=["ash","sanj","sayo","achu"]
print(random.choice(li))
random.shuffle(li)
print(li)"""

"""import os
# interacting with OS
print(os.getcwd())
# os.mkdir("test")
print(os.path.exists("work1.py"))
print(os.listdir())

print(os.rmdir("test"))
print(os.remove("filename.extension"))"""


"""import sys
print(sys.version)
print(sys.argv)
print(sys.path)
print("program started")
sys.exit()
print("program ended")"""

"""import pandas
print(pandas.__version__)

import pandas as pd

data={
  "Name":["ashok","john","don"],
  "Mark":[85,96,88]
}

df=pd.DataFrame(data)
print(df)"""

"""#dunder convention
__init__ #used to initialize an object when its created
__str__  #control what is displayed when you use print(object)
__len__  #allow an object to work with the len() function
__name__ #name of a function
__main__ # indicate main program execution 

#special methods or magic methods"""

