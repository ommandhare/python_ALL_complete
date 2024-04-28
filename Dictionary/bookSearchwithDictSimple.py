## 102,Dasbodh,Ramadas Swami,504,2000
## bookId,bookName,authorName,numPages,price

path=r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\Dictionary\books.txt'

### create dictionary to store books with book name as key
### write a program to help find books in library

## read books file and store the data in dict
bookPriceDict = {}
for line in open(path):
    print(line)
    bookId,bookName,authorName,numPages,price = \
        line.strip().split(",")
    bookid = int(bookId)
    numPages = int(numPages)
    price = float(price)
    bookName = bookName.lower()
    print("BOOK ID: ",bookId)
    bookPriceDict[bookName] = price


print(bookPriceDict)
ch=""
while(ch!='q'):
    ch = input("Enter any key/q to exit: ")
    if(ch=='q'):
        continue
    name = input("Enter book name to be searched: ")
    name = name.lower()
    if name in bookPriceDict:
        prc = bookPriceDict[name]
        print("BOOK NAME: ",name," PRICE: ",prc)
    else:
        print("BOOK NOT FOUND")
