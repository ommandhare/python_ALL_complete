def ncr(lst:list[str], start:int , end:int, ret:list[list[str]], length:int, current:list[str]):
    """
    This function creates combination on given string as per mathematical nCr function.
    :param lst: input list of string
    :param start: starting idx in input list, should be 0 to select all data.
    :param end: ending idx in input list , should be len of input list to work on all data.
    :param ret: pointer to output list.
    :param length: number of combination to create (r) from nCr.
    :param current: temp list should be empty list , [].
    """
    if length == 0:
        ret.append(current[:])  # Append a copy of current to ret
        return
    for i in range(start, end):
        current.append(lst[i])
        ncr(lst, i + 1, end, ret, length - 1, current)
        current.pop()  # Backtrack

import re


def compReplace(compDict: dict[str:tuple[str, int]], snt: str):
    """
    This function takes composite word dict and description to operate on.
    It replaces all composite words from description and replace them with null,
    and add composite string.
    :param compDict: This dict consist of one of word from composite word str as key and (compStr,no. of words int compStr) as value.
    :param snt: this is cleaned description.
    :return: composite word replaced with null and compStr inserted in it with '#' as demiliter.
    """
    sntLst = re.findall('[A-Za-z]+', snt)
    currDict = {}
    for word in sntLst:
        if word in compDict:
            currCmb, size = compDict[word]
            if currCmb not in currDict:
                currDict[currCmb] = (size, 1)
            else:
                _, cSize = currDict[currCmb]
                currDict[currCmb] = (size, cSize + 1)
    tmpStr = snt
    for cmbStr, (size, cSize) in currDict.items():
        cmbLst = cmbStr.split('#')
        if size != cSize:
            continue
        for wd in cmbLst:
            tmpStr = tmpStr.replace(wd, '')
        tmpStr += ' ' + cmbStr
    return tmpStr


def subCompositStr(dscStr: str, splitChar: str):
    """
    This function creates sub string from given dsc string
    :param dscStr: description
    :param splitChar: char to split description e.g.'_'
    :return: list of sub-strings.
    """
    dscLst = dscStr.split(splitChar)
    tmpLst = []
    for idx in range(len(dscLst)):
        cStr = ""
        for cidx in range(len(dscLst)):
            if idx != cidx:
                if cStr == "":
                    cStr += dscLst[cidx]
                else:
                    cStr += splitChar + dscLst[cidx]
        tmpLst.append(cStr)
    return tmpLst

