"""
read file category data and write all the lines containing category = "C1" to another file

"""

path=r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\product.csv"
count=0
lineCnt=-1
list=[]
for line in open(path):
    lineCnt += 1
    product_id, description, price, category, max_qty=line.strip().split(",")
    if (lineCnt == 0):
        continue
    else:
        if(category=="Baked goods"):
                print(line, end="")
                list.append(line)

fp=open("category.txt","w")
for i in list:
    fp.write(i)
fp.close()