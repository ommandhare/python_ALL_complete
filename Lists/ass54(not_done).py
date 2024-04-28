"""
get a large list of numbers
a = [32,43,55,11,2,3,4,5,66,33,66,7,567,89,87,54,32,12,34,567,333,256,242,121],
sort the list and search a user given number in list using binary search technique

"""

arr=[32,43,55,11,2,3,4,5,66,33,66,7,567,89,87,54,32,12,34,567,333,256,242,121]
x = 32

if r >= l:

    mid = l + (r - l) // 2

    # If element is present at the middle itself
    if arr[mid] == x:
        print("mid")

    # If element is smaller than mid, then it
    # can only be present in left subarray
    elif arr[mid] > x:
        return binarySearch(arr, l, mid - 1, x)

    # Else the element can only be present
    # in right subarray
    else:
        return binarySearch(arr, mid + 1, r, x)

# Element is not present in the array
else:
    return -1

    # Function call
    result = binarySearch(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
