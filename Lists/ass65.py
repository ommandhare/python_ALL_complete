def sum_of_sub_matrices(matrix, test_size):
    m = len(matrix)
    n = len(matrix[0])

    max_sum = float('-inf')
    max_sum_sub_matrix = []

    if test_size > m or test_size > n:
        print("Invalid test size")
        return

    for i in range(m - test_size + 1):
        for j in range(n - test_size + 1):
            sub_matrix = [row[j:j + test_size] for row in matrix[i:i + test_size]]
            sub_matrix_sum = sum(sum(row) for row in sub_matrix)
            if sub_matrix_sum > max_sum:
                max_sum = sub_matrix_sum
                max_sum_sub_matrix = sub_matrix

    return max_sum, max_sum_sub_matrix


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

m = len(matrix)
n = len(matrix[0])

if m == n:
    print("Matrix must be non-square (m != n)")

test_size = int(input("Enter the test size: "))

max_sum, max_sum_sub_matrix = sum_of_sub_matrices(matrix, test_size)

print("Sub-matrix with maximum sum:")
for row in max_sum_sub_matrix:
    print(row)
print("Maximum Sum:", max_sum)

