path=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\item_descr.csv"

def count_occurance(path):
    wordList = []
    wordDict = {}
    cnt = 0
    with open(path, 'r') as file:
        next(file)
        for line in file:
                cnt+=1
                desc=line.strip().split(",")
                # print(desc)
                wordList.append(desc)
                # print(wordList)
                for line in wordList:
                    # print(line[1])
                    word=line[1].strip().split(" ")
                    # print(word)
                    for w in word:
                        # print(w)
                        if w not in wordDict:
                            wordDict[w] = 1
                        else:
                            wordDict[w] += 1
        return wordDict


wordDict=count_occurance(path)


print(wordDict)