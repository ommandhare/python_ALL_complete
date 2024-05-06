path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\disjoint PROJECT\item_desc.csv"

def count_occurance(path):
    wordList = []
    wordDict = {}
    count = 0
    for line in open(path):
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