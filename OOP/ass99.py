"""
read book file (create book class and functions oop)
and
store objects in a list

"""

class book:
    def __init__(self,id,name,author,pages,price):
     self.id = id
     self.name = name
     self.author = author
     self.pages = pages
     self.price = price

    def printBook(self):
     print("bookId : ", self.id)
     print("Name : ",self.name)
     print("Pages : ", self.author)
     print("Types : ",self.pages)
     print("Publisher : ", self.price)


books = []

with open(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\data\books.txt", 'r') as file:
    for line in file:
        id,name,author,pages,price = line.strip().split(',')
        id= int(id)
        price=int(price)
        pages = int(pages)
        books.append(line)




print(books)
