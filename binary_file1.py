
with open("sunflower.jpg","rb") as source:
  with open("copy.jpg","wb") as destination:
    destination.write(source.read())

