"""# Write binary data
with open("image_copy.jpg","wb") as file:
  file.write(b"Hello Binary File")

# Read Binary data
with open("image_copy.jpg","rb") as file:
  data=file.read()

print(data)"""

with open("sunflower.jpg","rb") as source:
  with open("copy.jpg","wb") as destination:
    destination.write(source.read())