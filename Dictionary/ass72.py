"""

read product file and tran_dtl file.
Store product file in dictionary and implement inner, left, right and full outer join.
-- take join option as command line argument

"""

path1=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\data\tran_dtl.csv"
path2=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\data\product.csv"

productDict={}
productList=[]
cnt=0
for line in open(path2):
    if cnt==0:
        cnt += 1
        continue

    product_id,description,price,category,max_qty =line.strip().split(",")
    product_id =int(product_id)
    price = float(price)
    max_qty =int(max_qty)
    # print(line)
    productList.append(line)
    productDict[product_id]=[description,price,category,max_qty]


# print(productList)
# print(productDict)


tranList=[]
cnt=0
for line in open(path1):
    if cnt==0:
        cnt += 1
        continue

    tran_id, product_id, qty, amt, tran_dt=line.strip().split(",")
    product_id = int(product_id)
    qty =int(qty)
    amt =float(amt)
    # print(line)
    tranList.append([tran_id, product_id, qty, amt, tran_dt])

# print(tranList)
#


# print("inner join")
# tranList=[]
# cnt=0
# for line in open(path1):
#     if cnt==0:
#         cnt += 1
#         continue
#     tran_id, product_id, qty, amt, tran_dt=line.strip().split(",")
#     # print(productDict[product_id][0])
#     line=f"{tran_id},{product_id},{productDict[product_id][0]}"
#     print(line)




# print("right join")
#
# # print(tranList)
# for k,v in productDict.items():
#     for i in tranList:
#         if k == i[1]:
#             print(f"{k} product Id {i[0]} tran_id  IN")




print("left join")

for k,v in productDict.items():
    print(f"left {k} : {v} side")
    for i in tranList:
        if k==i[1]:
         line=[f"{k} product Id {i[0]} tran_id  IN"]
         print(line)


# remaining code will try out on another day
