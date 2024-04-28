a = [
    [1, 2, 3],
    [4, 5, 6]
]

b = [
    [7, 8],
    [9, 10],
    [11, 12]
]
result=[]

for i in range(len(a)):
    row=[]
    for j in range(len(b[0])):
        mul=0
        for k in range(len(b)):
           mul   += a[i][k] * b[k][j]
           row.append(mul)
        result.append(row)

print(result)