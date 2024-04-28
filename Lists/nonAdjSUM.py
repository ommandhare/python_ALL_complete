def nonAdjSum(array):
    inc=0
    einc=0
    for num in array:
        newEinc = max(inc,einc)
        # print(inc,einc)
        # print(newEinc)
        inc=einc+num
        einc=newEinc

    print(max(inc,einc))

a = [2,3,4,55,33,4,55,343,66,77,88,99]


nonAdjSum(a)