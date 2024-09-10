number=input("enter the number..")

length=len(number)
print("length is ",length)
word=""
cnt=0
numDict={
    0:"zero",
    1:"one",
2:"two",
3:"three",
4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
}



if(length==1):
   for k,v in numDict.items():
       number=int(number)
       if number == k:
           print(v)

elif(length==2):
    for i in number:
        for k, v in numDict.items():
           i = int(i)
           if i == k:
             word += v
             if cnt==0:
                 word = v+"ty"
                 cnt+=1
             else:
                 word+=v


    print(word)