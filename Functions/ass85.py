"""
ask user to enter a sentence and write a function to count number of words in the sentence

"""
wordList=[]
line=input("enter the line : ")
line=line+" "
def count_lines(l):
    count=0
    for i in line:

        if(i==" "):
         wordList.append(i)
         count+=1
    print("count of word= ",count)


count_lines(line)