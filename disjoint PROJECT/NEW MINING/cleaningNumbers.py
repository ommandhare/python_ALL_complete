path=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\item_descr.csv"

nDict={}
newClean=[]
cnt=0
c=0
for line in open(path):
        # print(line)
        desc = line.strip().split(",", 2)
        if len(desc) > 1:  # Check if there are at least two fields
            words = desc[1].strip().split(" ")
            for word in words:
                # print(word)
                if word.isdigit():
                   cnt+=1
                   print("FOUND:::")
                   print(desc,"--------",word)
                for w in word:
                    size=len(word)
                    if w.isdigit():
                        print("ALPHA NUMERIC::",word)


# print("Total count:: ",cnt)