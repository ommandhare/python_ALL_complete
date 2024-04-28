"""
read grocery file, create instance of grocery class for every line,
store it in dictionary with grocery name as key.
Ask user to enter grocery name and quantity and calculate total amout for user grocery purchase.

"""

path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\file operation\grocery.txt"

class Grocery:
    def __init__(self,item,price):
     self.item=item
     self.price=price



grocerDict={}
tempList=[]
for line in open(path):
    item,price=line.strip().split(",")
    price=int(price)
    grocerDict[item]=price
    grocery=Grocery(item,price)
    tempList.append(grocery)

print(tempList)
print(grocerDict)

name=input("Enter the Name of item :")
for item,price in grocerDict.items():
 if name in grocerDict:
    print(f"{name} is present ")
    qty=input("Enter the quantity of item to purchase : ")
    qty=int(qty)
    print(qty)
    total=qty * grocerDict[name]
    print(f"total bill is {total}")
    break
 else:
     print("Item is not present ")
     break