# Bubble sort in Python

def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


data = [3,4,5,86,34,2,3,4,7,33,44,66,88,34,32,11,22]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)