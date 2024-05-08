
path=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\item_descr.csv"
pathOut=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\cleanedData.csv"
wordList=[]
wordCnt=0
with open(path, 'r') as file:
    next(file)
    for line in file:
        # print(line)
        # if cnt == 100:
        #     break
        # else:
            desc = line.strip().split(",", 2)
            if len(desc) > 1:
                words = desc[1].strip().split(" ")
                # print(words)
                for word in words:
                    wordCnt += 1
                    if "/" in word:
                        new=word.split("/")
                    elif "-" in word:
                        new = word.split("-")
                    elif "%" in word:
                        new = word.split("%")
                    elif '"' in word:
                        new = word.split('"')
                    elif "." in word:
                        new = word.split(".")
                    elif " " in word:
                        new = word.split(" ")
                    elif "&" in word:
                        new = word.split("&")
                        for i in new:
                             wordList.append(i)
                    else:
                        # print(word)
                        wordList.append(word)

f=open(pathOut,"w")
for word in wordList:
    f.write(word+",")
    # print(word)

f.close()

print("###########################\n")
print("TOTAL WORDS ARE ::::")
print(wordCnt)

print("TOTAL WORDS AFTER CLEANING::::")
print(len(wordList))


