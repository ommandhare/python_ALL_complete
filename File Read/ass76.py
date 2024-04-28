"""
read file product and print lines containing category = "baked goods"

"""
path=r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\product.csv"
count=0
lineCnt=-1
for line in open(path):
    lineCnt += 1
    product_id, description, price, category, max_qty=line.strip().split(",")
    if (lineCnt == 0):
        continue
    else:
        if(category=="Baked goods"):
                print(line, end="")