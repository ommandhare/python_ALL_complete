path = r"C:\Users\om\PycharmProjects\python_All\RADAR\seperated(alphanumneric)"

wordDict = {}
for line in open(path):
    # print(line)
    words = line.strip().split(" ")
    # print(word)
    for word in words:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

print(wordDict)



sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)