# product Id and amt

path = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\analysis_project\daily_files\product.csv"
productAmt = {}
i = 1

for line in open(path):
    # print(line)
    productId,description,amt,category,max_qty = line.strip().split(',')
    if i != 1:
        # print(productId)
        productAmt[productId] = amt
    i+=1
    
print(productAmt)