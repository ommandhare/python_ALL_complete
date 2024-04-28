

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
bookref=[]
path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\data\books.txt"

for line in open(path):
    id,name,author,pages,price = line.strip().split(',')
    id= int(id)
    price=int(price)
    pages = int(pages)
    books.append(line)
    bookref.append(book)
    tempbook = (id, name, author, pages, price)
    bookref.append(book)
    print(tempbook)



print(books)
print(bookref)