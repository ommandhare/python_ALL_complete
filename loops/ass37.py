"""
Read product file and tran_dtl file and implement inner join using loops (use two for loops)

"""
with open(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\product.csv", 'r') as product_file:
    product_data = [line.strip().split(',') for line in product_file]


with open(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_dtl_1_2019.csv", 'r') as tran_dtl_file:
    tran_dtl_data = [line.strip().split(',') for line in tran_dtl_file]


inner_join_result = []

for product_row in product_data:
    for tran_dtl_row in tran_dtl_data:
        if product_row[0] == tran_dtl_row[1]:
            inner_join_result.append(product_row + tran_dtl_row)


for row in inner_join_result:
    print(row)

