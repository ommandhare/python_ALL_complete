# product Id and amt

path = r"C:\Users\om\PycharmProjects\python_All\analysis_project\daily_files\product.csv"
productAmt = {}
i = 1


for line in open(path):
    # print(line)
    productId,description,amt,category,maxQty = line.strip().split(',')
    if i != 1:
        productAmt[productId] = amt
    i+=1
    
print(productAmt)

