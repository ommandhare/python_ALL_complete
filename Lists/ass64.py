"""
get a matrix of height = m and width=n
from user (or hard code one),
where m!=n and get one variable testSize from user.
Write a program to print all possible testSize X testSize sub matrix
"""

def print_sub_matrices(matrix, test_size):
    m = len(matrix)
    n = len(matrix[0])

    if test_size > m or test_size > n:
        print("Invalid test size")
        return

    for i in range(m - test_size + 1):
        for j in range(n - test_size + 1):
            sub_matrix = [row[j:j + test_size] for row in matrix[i:i + test_size]]
            print("Sub-matrix:")
            for row in sub_matrix:
                print(row)
            print()



matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

m = len(matrix)
n = len(matrix[0])

if m != n:
    print("Matrix must be square (m != n)")

test_size = int(input("Enter the test size: "))

print_sub_matrices(matrix, test_size)

