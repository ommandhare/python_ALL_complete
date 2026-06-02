import re


def findInList(w, l):
    for wd in l:
        if (w == wd):
            return 1
    return 0

def cleanString(s):
    sr=s
    if (s[-1] == "."):
        s = s[:-1]
        sr = s
    #if(s[-1]=="~"):
     #  sr = s.replace("~~", "")
    return sr

def getWordList(wrd,wl):
    pattern = r'[A-Z#]+' # find only capital character and # for composite words.
    tmpWdLst = re.findall(pattern,wrd)
    for word in tmpWdLst:
        wl.append(word)
