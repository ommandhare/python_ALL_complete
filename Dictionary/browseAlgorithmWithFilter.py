# write a program to
# 1. get friend names in hard-coded list
# 2. browse over the list to invite friends to birthday party

friendList = [["Kiran","Satara"],\
              ["Nishad","Pune"],\
              ["Anurag","Nagpur"],\
              ["Sumesh","Mumbai"],\
              ["Abhijit","Solapur"],\
              ["Rohan","Satara"],\
              ["Soham","Jabalpur"],\
              ["Pratik","Satara"],\
              ["Manoj","Satara"],\
              ["Sanket","Pune"],\
              ["Harshal","Pune"],\
              ["Siddhi","Satara"]
              ]
numOfFriends = len(friendList)
print("TOTAL - ",numOfFriends," are there in my friend list")
print("Complete FriendList::: ",friendList)
print("**************************************")
for friend,city in friendList:
    if(city == "Satara"):
        print("Hi ",friend," please come to my Birthday!!!")