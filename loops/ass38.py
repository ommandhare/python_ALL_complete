"""
Read product file and tran_dtl file and implement inner join using loops (use two for loops)
-- implement left, right and full outer join

"""

with open(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\product.csv", 'r') as product_file:
    product_data = [line.strip().split(',') for line in product_file]


with open(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_dtl_1_2019.csv", 'r') as tran_dtl_file:
    tran_dtl_data = [line.strip().split(',') for line in tran_dtl_file]

# inner join
inner_join_result = []

for product_row in product_data:
    for tran_dtl_row in tran_dtl_data:
        if product_row[0] == tran_dtl_row[1]:
            inner_join_result.append(product_row + tran_dtl_row)

for row in inner_join_result:
    print(row)

#
#
# left join
left_join_result = []
print("Left Join :   ")

for product_row in product_data:
    for tran_dtl_row in tran_dtl_data:
        if product_row[0] == tran_dtl_row[1]:
            left_join_result.append(product_row + tran_dtl_row )
            left_join_result.append("INN joined")
        else:
            left_join_result.append(product_row)
            left_join_result.append("LEFT remaining")
for row in left_join_result:
    print(row)



# right join
right_join_result = []
print("Right Join :   ")

for product_row in product_data:
    for tran_dtl_row in tran_dtl_data:
        if product_row[0] != tran_dtl_row[1]:
           right_join_result.append(tran_dtl_row)
           right_join_result.append("right remaining")

        else:
            right_join_result.append(product_row + tran_dtl_row)
            right_join_result.append("INN joined")

for row in right_join_result:
    print(row)



# outer join
outer_join_result = []
print("Outer Join :   ")


for product_row in product_data:
    for tran_dtl_row in tran_dtl_data:
        if product_row[0] == tran_dtl_row[1]:
            outer_join_result.append(product_row + tran_dtl_row)
            outer_join_result.append("in")
        else:
            outer_join_result.append(tran_dtl_row)
            outer_join_result.append(product_row)
            outer_join_result.append("OUT")

for row in outer_join_result:
    print(row)

