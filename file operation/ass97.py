"""
read file booklist and create class and functions for class book.
Instantiate book oject for every line.
Findout total number of pages written by every author, number of books written by every author

"""
class Book:
    def __init__(self, book_id, name, author, num_pages, price):
        self.book_id = book_id
        self.book_name = name
        self.author_name = author
        self.num_pages = int(num_pages)
        self.price = price

    def print_book_details(self):
        print("::::::::::::::::::::BOOK DETAILS::::::::::::::::: ")
        print("BOOK ID: ", self.book_id)
        print("BOOK NAME: ", self.book_name)
        print("AUTHOR NAME: ", self.author_name)
        print("NUMBER OF PAGES: ", self.num_pages)
        print("PRICE: ", self.price)


path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\data\books.txt"
bookRecord=[]
author_pages={}
author_books={}
cnt = 0
for line in open(path):
    book_id, name, author, num_pages, price=line.strip().split(",")
    num_pages=int(num_pages)
    tempbook=Book(book_id, name, author, num_pages, price)
    # print(tempbook)
    bookRecord.append(tempbook)

    if author in author_pages:
        author_pages[author] += num_pages
    else:
        author_pages[author] = num_pages



    if author in author_books:
        author_books[author] += [name]
    else:
        cnt=0
        author_books[author]= [name]




print(author_pages)


for k,v in author_books.items():
  print(k,v)
