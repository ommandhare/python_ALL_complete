def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]
        print(mid_val)
        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1



a = [32, 43, 55, 11, 2, 3, 4, 5, 66, 33, 66, 7, 567, 89, 87, 54, 32, 12, 34, 567, 333, 256, 242, 121]
print(a)
a.sort()
print(a)

user_input = int(input("Enter a number to search in the list: "))

index = binary_search(a, user_input)

if index != -1:
    print(f"The number {user_input} is found at index {index} in the sorted list.")
else:
    print(f"The number {user_input} is not found in the list.")
