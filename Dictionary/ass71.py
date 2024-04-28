"""
read file book.txt store author name as key and list of books as value.
Print author name and list of books written by that author as output

"""




authorDict={}
with open(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\data\books.txt") as file:
    for line in file:
        id,name,author,pages,price=line.strip().split(",")
        id=int(id)
        pages=int(pages)
        price=int(price)
        aName = author
        # print("AUTHOR NAME: ", aName)
        if (aName in authorDict):
            bookList = authorDict[aName]
            bookList.append(name)
            authorDict[aName] = bookList
        else:
            bookList = []
            bookList.append(name)
            authorDict[aName] = bookList

print(authorDict)
