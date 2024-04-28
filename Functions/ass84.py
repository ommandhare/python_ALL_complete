"""
ask user to enter a word, write a function to count number of vovels in the word

"""
consList=[]
vowelList=["a","e","i","o","u"]
word=input("enter the word: ")

def check_consonents(w):
    for i in word:
     if(i in vowelList):
        consList.append(i)

    print(word)
    print(consList)
    print(len(consList))

check_consonents(word)
