print("---- ONLINE LIBRARY MANAGEMENT SYSTEM ----")

book_name = "Python Programming"
author_name = "John Smith"
member_name = "  ashok  "

available_books = ["Python", "Java", "C++"]
issued_books = ["HTML"]
members = ["Ashok", "Rahul", "Anu"]


print(book_name[0])
print(book_name[:-1])
print(book_name[0:6])

print(available_books[0])
print(available_books[-1])
print(available_books[0:2])

print(book_name.upper())
print(book_name.lower())
print(book_name.capitalize())
print(book_name.title())
print(book_name.replace("Python","Advanced Python"))
print(book_name.split())
print(member_name.strip())

books="python"
# book[0]="j"
# print(book)

available_books.append("SQL")
available_books.insert(1,"C")
print(available_books)
available_books.remove("C")
available_books.pop()
available_books.sort()
available_books.sort(reverse=True)
print(available_books)

display_books=[book for book in available_books]
uppercase_books=[book.upper() for book in available_books]
p_books=[book for book in available_books if book.startswith("P")]
print(display_books)
print(uppercase_books)
print(p_books)

categories = ("Programming", "Database", "Networking")
cat1,cat2,cat3=categories

print(cat1)
print(cat2)
print(cat3)

# categories[0]="AI"
genres={"Python","Java","Python","C++"}
memeber_ids={101,102,103}
genres.add("Networking")
genres.remove("Java")

set1={"Python","Java"}
set2={"Java","C++"}
print(set1.union(set2))
print(set1.intersection(set2))

dict_book={
  "book_id":101,
  "title":"Python Basics",
  "author":"John"
  }
print(dict_book["book_id"])
print(dict_book["author"])

print(dict_book.keys())
print(dict_book.values())
print(dict_book.items())

print(dict_book.get("title"))
print(dict_book.update({"author":"alex"}))
print(dict_book.pop("book_id"))

library={
  101:{
    "title":"Python",
    "author":"Alex"
  },
  102:{
    "title":"Java",
    "author":"David"
  }
}
print(library[101]["title"])

d = {
    "Python":1,
    101:"Book",
    (1,2):"Tuple"
}
"""d = {
    [1,2]:"Book"
}"""

print(hash("Python"))

print(hash(101))

print(hash((1,2)))

issued_to = None

fine = None

print(issued_to)

print(type(None))

