import pandas as pd

import item_set as itm
from utility import combUtility as cmb ,simUtility as sim ,wrdClenUtility as ut


imp_word=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\word_attrib 1.csv"
word_count=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\cic_comb\Word_Count.csv"
item_attrib=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\Item_Attribut_table.csv"
wordDict = {}
wordIdDict = {}
combDict = {}
ignoreDict = {}
impDict = {}
# read word file to create impDict
def generate_combinations(r):
    for dataTuple in open(imp_word):
        word,imp_flg=dataTuple.strip().split(",")
        impDict[word] = 1

    # read ignore word file and build ignore dict
    # for dataTuple in ignoreWordsTable:
    #     word = dataTuple["word"]
    #     ignoreDict[word] = 1
    # # ----------------------- word freq code ----------------- #
    # # read frequent itemset file and create itemset class obj
    cnt = -1
    for dataTuple in open(word_count):
        cnt += 1
        sr, wrd, freq = dataTuple.strip().split(",")
        if (len(wrd) < 3):
            continue
        if len(freq) < 2:
            continue
        tempItemSet = itm.ItemSet(cnt, wrd, freq)
        # print(tempItemSet.word, tempItemSet.freq)
        wordDict[wrd] = tempItemSet
        wordIdDict[int(cnt)] = tempItemSet
    # # --------------------- end of word freq code ------------ #
    # print(wordIdDict)
    ctt = 0
    for dataTuple in open(item_attrib,encoding="utf-8"):
        ctt += 1
        combList = []
        sr,cic,new_cic_dsc,old_cic_dsc,dept,imp_flag,effective_wrd_cnt = dataTuple.strip().split(",")
    #
        if (len(new_cic_dsc) < 2):
            continue
        wList = []
        ut.getWordList(new_cic_dsc, wList)  # create word list
    #
        desWords = []
        for word in wList:
            if (word in wordDict):
                desWords.append(wordDict[word])  # create list of wordObj
        size = len(desWords)
        cmb.sortList(desWords, size)  # sort by freq
    #
        itemList = []
        for wordObj in desWords:
            itemList.append(wordObj.id)  # add id's to itemList of word
        n = len(itemList)
        # r = 2  # cfg.nCr
        comb = []
        for i in range(r):
            comb.append(0)  # create stack of size r
        cmb.combinGen(n, r, itemList, 0, 0, comb, combList)
    #     # -------------- end of combination ----------------------- #
    #
        cmbStr = []
        for c in combList:
            # print(c)
            res = cmb.checkIgnoreComb(c, wordIdDict, ignoreDict)
            if (res == 1):
                continue
            cStr = ""
            sortedC = sorted(c, key=lambda x: wordIdDict[x].word)  # sort id's alphabeticaly
            for id in sortedC:
                if (cStr == ""):
                    cStr = wordIdDict[id].word
                else:
                    cStr = cStr + "_" + wordIdDict[id].word
            cmbStr.append(cStr)
            # print(cmbStr)
    #     # --------- end of filtered and sorted and generated cmbStr ----------- #
        for cStr in cmbStr:
            if (cStr in combDict):
                freq = combDict[cStr]
                combDict[cStr] = freq + 1
            else:
                combDict[cStr] = 1
        # --------- end of freq of cmbStr ------------------------------------- #
    # if len(combDict) < 1:
        # print(0)
    # # ------------------------ write to file --------------------------------- #
    allData = []
    # # code below is to write combinations to the file
    for key, val in combDict.items():
        if (val < 2):
            continue
        items = key.split("_")
        iStr = ""
        confStr = ""
        confList = []
        ct = 0
        freqList = []
        impWdCnt = 0
        ## freq Bucket List:
        # index 0 - freq less than eq 10
        # index 1 - freq less than eq 20
        # index 2 - freq less than eq 50
        # index 3 - freq less than eq 100
        # index 4 - freq greater than 100
        freqBktList = [0, 0, 0, 0, 0]
    #     # --------------- fill freqBktList and confList ---------------- #
        for item in items:
            if (item in impDict):
                impWdCnt += 1
            # impWdCnt = cmb.getImportantWordCount(c, wordIdDict, impDict)
            frq = wordDict[item].freq
            bktIdx = cmb.get_bkt_index(frq)
            freqBktList[bktIdx] = str(int(freqBktList[bktIdx]) + 1) # my cnage
            freqBktList[bktIdx] = str(int(freqBktList[bktIdx]) + 1)
            iL = [item, frq]
            freqList.append(iL)
            iConf = round(float(val / frq), 2)
            confList.append(str(iConf))
            if (ct == 0):
                iStr = item + "~" + str(frq)
                ct += 1
            else:
                iStr = iStr + "#:#" + item + "~" + str(frq)
        # my back tab
        # ------------------------ conflag,min-max conf -------------------- #
        # check if conf for all is > 0.75
        minConf = 100.0
        maxConf = 0.0
        for cff in confList:
            cff = float(cff)
            if (minConf > cff):
                minConf = cff
            if (maxConf < cff):
                maxConf = cff

        comWFlag = 1
        for cf in confList:
            if (float(cf) < 0.75):
                comWFlag = 0
                break
        # --- k: in ctrix create list here ----- #
        # freqBktStr = ""
        # freqBktStr = ",".join(freqBktList) # keep integer
        # confStr = ""
        # confStr = "#:#".join(confList) + ","+str(maxConf) + "," + str(minConf) + ","+ str(comWFlag) # keep split
        # strW = key + "," + str(val)+","+str(r)+","+str(impWdCnt) + ","+freqBktStr+"," + iStr + "," + confStr + "\n"
        currData = [key, val, r, impWdCnt, freqBktList[0], freqBktList[1], freqBktList[2], freqBktList[3], freqBktList[4],
                    iStr, "#:#".join(confList), maxConf, minConf, comWFlag]
        # sample line metadata as given below
        # combination,comb_freq,comb_size,impWdCnt,freqBktStr,item1,freq1,item2,freq2,..,itemN,freqN, conf1,conf2,conf3..confN,compFlag
        allData.append(currData)
    # print(allData)
    # --------------------------- load data to table ------------------------ #
    df = pd.DataFrame(allData,
                      columns=["comb_str", "comb_freq", "comb_size", "imp_flag",
                               "bkt_below_10_cnt", "bkt_10_20_cnt", "bkt_20_50_cnt", "bkt_50_100_cnt", "bkt_100_above",
                               "comb_detail_str", "conf_detail_str", "conf_max", "conf_min", "conf_flag"])

    df.to_csv("word_Combination.csv",mode="a")


r = 1
while(True):
 res=generate_combinations(r)
 print(f"{r}_is_generated...")
 if res==0:
    break
 r+=1

