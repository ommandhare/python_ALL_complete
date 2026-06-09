import re
def onlyWords(dsc):
    return re.findall(r'[A-Z]+',dsc)

def nGram(s:str, n:int)-> list[str]:
    """
    This function creates n grams from given string input.
    :param s: Source string.
    :param n: Number of char per nGram
    :return: list of nGrams
    """
    lst = []
    for i in range(len(s) - n + 1):
        lst.append(s[i:i + n])
    return lst


def nGrams(s:str, t:str)-> float:
    """
    This function return's word matching score using nGrams.
    0 is total unmatch.
    1 is absolute match.
    :param s: Source string.
    :param t: Target string.
    :return: score of word similarity.
    """
    if len(s) < len(t):
        s, t = t, s
    grams = nGram(s, 2) if len(s) > 2 else [s]
    sml = 0
    for n in grams:
        if n in t:
            sml += 1
    return sml / len(grams)

# levenstine
def levenstine(s:str, t:str)->float:
    """
    This function calculates word similarity score using levenstine.
    0 is total unmatch.
    1 is total match.
    :param s: Source string.
    :param t: Source string.
    :return: levestine matching score .
    """
    cache = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    for idx in range(len(s)):
        cache[idx][len(t)] = len(s) - idx
    for idx in range(len(t)):
        cache[len(s)][idx] = len(t) - idx
    for i in range(len(s) - 1, -1, -1):
        for j in range(len(t) - 1, -1, -1):
            if s[i] == t[j]:
                cache[i][j] = cache[i + 1][j + 1]
            else:
                cache[i][j] = 1 + min(cache[i][j + 1], cache[i + 1][j], cache[i + 1][j + 1])
    return (max(len(s), len(t)) - cache[0][0]) / max(len(s), len(t))


#weighted levenstine
def wgtLevenstine(s, t):
    if len(s) < len(t):
        s, t = t, s
    sLst = onlyWords(s)
    tLst = onlyWords(t)
    distances = 0
    div = 0
    for sWord in sLst:
        score = 0.00
        for tWord in tLst:
            if sWord[0] != tWord[0]:
                continue
            tmpScore = levenstine(sWord, tWord)
            if tmpScore > score:
                score = tmpScore
        distances += (score * len(sWord))
        div += len(sWord)
    return distances / div