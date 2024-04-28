"""
read book file (create book class and functions oop)
and
store objects in a list and sort object list using book price
"""
from book import Book

path = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\data\books.txt"
bookList=[]
with open(path) as f:
    for line in f:
        line=line.strip().split(',')
        mybook =Book(int(line[0]),line[1],line[2],int(line[3]),float(line[4]))
        bookList.append(mybook)

def sortBook(bookList):
    for i in range(len(bookList)):
        min_idx=i
        for j in range(i+1,len(bookList)):
            if(bookList[min_idx].price > bookList[j].price):
                min_idx=j
        bookList[min_idx],bookList[i] = bookList[i],bookList[min_idx]

sortBook(bookList)
for book in bookList:
    print(f"{book.book_name} => {book.price}")





