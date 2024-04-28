def getWordList(path):
    wordList = []
    with open(path, 'r') as file:
        next(file)
        for line in file:
            desc = line.strip().split(",", 1)
            if len(desc) > 1:  # Check if there are at least two fields
                words = desc[1].strip().split(" ")
                for word in words:
                    wordList.append(word)
        return wordList


def getSameword(wordList, word):
    cnt = 0
    for idx in wordList:
        if idx == word:
            cnt += 1
            print(idx)

    print("result::::")
    if cnt > 1:
        print(f"{word} founded {cnt} times")
    elif (cnt == 1):
        print(f"{word} is single in list")
    else:
        print(f"{word} not found in list")


def getSubset(wordList, word):
    list = []
    for letter in word:
        list.append(letter)
    print(list)

    for key in wordList:
        print(key)

    # for key in wordList:
    #     # print(key)
    #     for idx in key :
    #         for letter in word:
    #             if (idx==letter):
    #                 print(word,"--",key)


path = r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\item_desc.csv"

sWord = "goa"

wordList = getWordList(path)
# print(wordList)

getSameword(wordList, sWord)

getSubset(wordList, sWord)