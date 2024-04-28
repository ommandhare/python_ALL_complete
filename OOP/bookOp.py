# write a program that does following
# 1.create a book class (separate file)
# 2.create bookOp python file
# 3.In bookOp python file - set path to book data
# 4.Read book file
# 5.For every line create an object of book class
# 6.Print ref to the newly created object on screen
# 7.Print author name on screen using newly created object
# 8.Create a data structure to store all refs to book objects
# 9.Browse over collection to print all obj ref and book name
# for every object
# 10.Write a simple function to search books
# that fall between certain price range
import book as b

def printBookInRange(hi,low,bookRecord):
    print("ELIGIBLE LIST IS AS GIVE BELOW ------------>>>>> ")
    for book in bookRecord:
        if(book.price < hi and book.price >= low):
            print("Book Name: ",book.book_name,end="")
            print("\tBook Price: ",book.price)

# function to search books based on author name
def searchBookByAuthor(bookRecord,author):
    authorName = author.lower()
    flag=0
    for book in bookRecord:
        aName = book.author_name.lower()
        if(authorName == aName):
            flag=1
            print("BOOK NAME: ",book.book_name,end="")
            print("\t AUTHOR: ",book.author_name)
    if(flag==0):
        print("NO BOOK IS FOUND FOR THIS AUTHOR: ",author)
# write a function to build a dictionary that keeps
# author name (lower case) as key and list of books writeen
# by that author as value
def buildAuthorBookDict(bookRecord,authorDict):
    for book in bookRecord:
        aName = book.author_name.lower().strip()
        print("AUTHOR NAME: ",aName)
        if(aName in authorDict):
           bookList = authorDict[aName]
           bookList.append(book)
           authorDict[aName] = bookList
        else:
            bookList = []
            bookList.append(book)
            authorDict[aName] = bookList


bookRecord = []
path=r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\data\books.txt'

for line in open(path):
    print(line,end="")
    #id,bName,author,numPages,prc = line.strip().split(",")
    attribList = line.strip().split(",")
    if(len(attribList) != 5):
        print("Error line skipping this line ....")
        continue

    id = int(attribList[0])
    bName = attribList[1]
    author = attribList[2]
    numPages = int(attribList[3])
    prc = float(attribList[4])
    tempBook = b.Book(id,bName,author,numPages,prc)
    print(tempBook)
    bookRecord.append(tempBook)

print(bookRecord)
hi = 250
low = 200
printBookInRange(hi,low,bookRecord)

author="Gayatri Kale"
searchBookByAuthor(bookRecord,author)

# build author Dict
authorDict = {}
buildAuthorBookDict(bookRecord,authorDict)
print("AUTHOR DICTIONARY: ",authorDict)
## search by author in authorDict
author = "shivaji sawant"
if(author in authorDict):
    bookList = authorDict[author]
    print("BOOKS WRITTEN BY AUTHOR: ",author)
    for book in bookList:
        print("BOOKS Name: ",book.book_name)
else:
    print("NO BOOK IS WRITTEN BY THIS AUTHOR: ",author)


