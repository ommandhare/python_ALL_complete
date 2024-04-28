## program is to browse over list of items

listOfItems = ['cake','butter','bread','potato','tomato','orange','apple','lemon','banana','sweet lemon','pineapple']

## browse over list using content of the list
for item in listOfItems:
    print("PURCHASE OF ",item," IS DONE")

listOfNumbers = [23,72,1,20,34,55,22,75]
for num in listOfNumbers:
    if(num > 70):
        print("RESPECTED SENIOR CITIZEN: ",num," PLEASE TAKE CHAIR")
    print("NUMBER: ",num)

# Browse list using index
# print idx 3
print("ITEM AT IDX 3: ", listOfItems[3])


## browse over list using index of the list
size = len(listOfItems)
for idx in range(size):
    print("PURCHASE OF ",listOfItems[idx]," at idx: ",idx, " IS DONE")