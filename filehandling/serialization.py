"""
import json

student={
  "name":"Rahul",
  "age":20,
  "skills":["Python","HTML"]
}

# Serialization: Python dictionary -> JSON file
with open("student.json","w") as file:
  json.dump(student,file)

# Deserialization: JSON file -> Python Dictionary
with open("student.json","r") as file:
  data=json.load(file)

print(data)
print(type(data))
print(data["skills"])  

 """

#Serialization using pickle
import pickle

student={
  "name":"ashok",
  "age":22,
  "skills":["python","HTML"]
}    

with open("student.pkl","wb") as file:
  pickle.dump(student,file)

with open("student.pkl","rb") as file:
  data=pickle.load(file)

print(data)
print(data["skills"])