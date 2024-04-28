"""
read grocery file, create instance of grocery class for every line,
store it in dictionary with grocery name as key.
Ask user to enter grocery name and quantity and calculate total amout for user grocery purchase.

"""
import grocery as g

path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\grocery.txt"

groceryDict={}
groceryList=[]
for line in open(path):
    name,price = line.strip().split(",")
    price=int(price)
    temp=g.grocery(name,price)

    groceryDict[name]=temp

print(groceryDict)

amt=0



while True:
    product = input("Enter the product name : ")
    if (product in groceryDict):
     Qty=int(input("Enter the quantity "))
     print(Qty)
     print(groceryDict[product].price)
     amt =  groceryDict[product].price * Qty
     print(f"Total amount is :: ",amt)
     break
    else:
     print("invalid product name......")
     break