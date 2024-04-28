"""
start with hard coded list say a = [12,3,34,45,88,23,45,63,3,4,69,99] and find  maximum in this list (without using python readymade function)

"""

a = [12,3,34,45,88,23,45,63,3,4,69,99]
maximum=a[0]
for num in a:
    if num>maximum:
        maximum=num



print("The maximum value in the list is:", maximum)
    