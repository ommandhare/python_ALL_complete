"""
ask user to enter a sentence, store sentence as list of words. Enter another word from user
 and write a function to findout number of occurances of the word in the sentence

"""
wordList=[]


str=input("enter the line ")
word=input("enter the word to check occurences in line: ")
def check(s,w):
    count=0
    s=s+" "
    char=""
    for i in s:
      if(i==" "):
          # tempList.append()
          wordList.append(char)
          char=""
      else:
          char=char+i
    print(wordList)
    for ch in wordList:
        if(ch==w):
            count+=1
    print("occurence in list : ",count)

check(str,word)




