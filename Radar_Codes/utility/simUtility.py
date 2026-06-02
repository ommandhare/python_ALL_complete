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
