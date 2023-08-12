"""
Question-2:
Nested Dictionaries You are managing a library. Here's the information about some books:

books = { 'book1': { 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925 }, 'book2': { 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960 }, 'book3': { 'title': '1984', 'author': 'George Orwell', 'year': 1949 } }

a) Add a new book to the dictionary with the title, author, and year.
b) Print the titles of all the books.
c) Determine the book with the earliest publication year and print its title and author.
"""

books = { 'book1': { 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925 }, 'book2': { 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960 }, 'book3': { 'title': '1984', 'author': 'George Orwell', 'year': 1949 } }

books['book4'] = {'title': 'Charlie and the Chocolate Factory', 'author': 'Roald Dahl', 'year': 2005}

print(books['book1']['title'])
print(books['book2']['title'])
print(books['book3']['title'])
print(books['book4']['title'])

print()

if books['book1']['year'] < books['book2']['year'] and books['book1']['year'] < books['book3']['year'] and books['book1']['year'] < books['book4']['year']:
    print(books['book1']['title'], "by", books['book1']['author'])
elif books['book2']['year'] < books['book1']['year'] and books['book2']['year'] < books['book3']['year'] and books['book2']['year'] < books['book4']['year']:
    print(books['book2']['title'], "by", books['book2']['author'])
elif books['book3']['year'] < books['book1']['year'] and books['book3']['year'] < books['book2']['year'] and books['book3']['year'] < books['book4']['year']:
    print(books['book3']['title'], books['book3']['author'])
else:
    print(books['book4']['title'], "by", books['book4']['author'])
