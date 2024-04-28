a = [2, 3, 4, 55, 33, 4, 55, 343, 66, 77, 88, 99]


def max_sum_non_adjacent(arr):
    incl = 0
    excl = 0

    for i in arr:
        # Current max excluding i
        new_excl = max(incl, excl)

        # Current max including i
        incl = excl + i
        excl = new_excl

    # Return maximum of incl and excl
    return max(incl, excl)


max_sum = max_sum_non_adjacent(a)
print("Maximum sum of non-adjacent numbers:", max_sum)
