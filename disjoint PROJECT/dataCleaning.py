
path=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\item_descr.csv"
def cleaner(str,word):
    flag=0
    first=''
    sec=''
    new=''
    if str  in word:
        print(word)
        for w in word:
          if w == str:
              flag=1
              continue
          elif flag==1:
             sec=sec+w
          else:
              new=new+w
    print(new)
    print(sec)
    # return new
    # return sec


# word="omman?dhare"
# str="?"
# cleaner(str,word)
wordList=[]
with open(path, 'r') as file:
    next(file)
    for line in file:
        # print(line)
        # if cnt == 100:
        #     break
        # else:
            desc = line.strip().split(",", 2)
            if len(desc) > 1:  # Check if there are at least two fields
                words = desc[1].strip().split(" ")
                # print(words)
                for word in words:
                    if "/" in word:
                        new=word.split("/")
                    elif "-" in word:
                        new = word.split("-")
                    elif "%" in word:
                        new = word.split("%")
                    elif '"' in word:
                        new = word.split('"')
                        for i in new:
                         wordList.append(i)
                    else:
                        # print(word)
                        wordList.append(word)

for word in wordList:
    print(word)