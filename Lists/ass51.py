"""
get a list a = [2,3,4,55,33,4,55,343,66,77,88,99]
and write a program to find maximum sum of non-adjacent numbers

"""


def max_sum_non_adjacent(a):
    if len(a) <= 2:
        return max(0, max(a))

    max_sum = [0] * len(a)
    max_sum[0] = max(0, a[0])
    max_sum[1] = max(max_sum[0], a[1])

    for i in range(2, len(a)):
        max_sum[i] = max(max_sum[i - 1], max_sum[i - 2] + a[i])

    return max_sum[-1]


a = [2, 3, 4, 55, 33, 4, 55, 343, 66, 77, 88, 99]

result = max_sum_non_adjacent(a)
print("Maximum sum of non-adjacent numbers:", result)
