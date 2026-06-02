import sys
import os
 
# Add the ing_cls_code directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'DAG_cic_comb'))
from google.cloud import bigquery  # pip install google-cloud-bigquery
import itemSet as itm
import wrdClenUtility as ut
import combUtility as cmb
import config as cfg
import pandas as pd


def generateCombinations(rIn):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # ----------------- Path In -------------------------------------#
    prepCicAttrib_Q = cfg.prepCicAttribQuery.replace("PROJECTID", cfg.projectId).replace("DATASETID", cfg.dataSetId) \
        .replace("TABLEID", cfg.prepCicAttribTableId)
    impWord_Q = cfg.wordAttribQuery.replace("PROJECTID",cfg.projectId).replace("DATASETID",cfg.dataSetId)\
        .replace("TABLEID",cfg.wordAttribTableId).replace("FLAG",'imp_fg')
    ignoreWords_Q = cfg.ignoreWordsQuery.replace("PROJECTID",cfg.projectId).replace("DATASETID",cfg.dataSetId)\
        .replace("TABLEID",cfg.ignoreWordsTableId)
    cicDesWordCnt_Q = cfg.prepCicWordCntQuery.replace("PROJECTID",cfg.projectId).replace("DATASETID",cfg.dataSetId)\
        .replace("TABLEID",cfg.prepCicWordCntTableId)
    cicwordCombTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.wordDesCombTableId}'

    prepCicAttribTable = client.query(prepCicAttrib_Q)
    impWordTable = client.query(impWord_Q)
    ignoreWordsTable = client.query(ignoreWords_Q)
    wordCntTable = client.query(cicDesWordCnt_Q)
    # ----------------- code -------------------------------------- #

    # create empty dictionaries
    wordDict = {}
    wordIdDict = {}
    combDict = {}
    ignoreDict = {}
    impDict = {}
    # read word file to create impDict
    for dataTuple in impWordTable:
        word = dataTuple["word"]
        impDict[word] = 1
    # read ignore word file and build ignore dict
    for dataTuple in ignoreWordsTable:
        word = dataTuple["word"]
        ignoreDict[word] = 1
    #----------------------- word freq code ----------------- #
    # read frequent itemset file and create itemset class obj
    cnt = -1
    for dataTuple in wordCntTable:
        cnt += 1
        wrd, freq = dataTuple
        if (len(wrd) < 3):
            continue
        if (int(freq) < 2):
            continue
        tempItemSet = itm.ItemSet(cnt, wrd, freq)
        #print(tempItemSet.word, tempItemSet.freq)
        wordDict[wrd] = tempItemSet
        wordIdDict[int(cnt)] = tempItemSet
    # --------------------- end of word freq code ------------ #

    ctt=0
    for dataTuple in prepCicAttribTable:
        ctt +=1
        combList = []
        cic, newDsc, oldDsc, dept, nvFlag, lqFlag, impFlag, effFlag = dataTuple

        if(len(newDsc)< 2):
            continue
        wList = []
        ut.getWordList(newDsc,wList) # create word list

        desWords = []
        for word in wList:
            if (word in wordDict):
                desWords.append(wordDict[word]) # create list of wordObj
        size = len(desWords)
        cmb.sortList(desWords, size) # sort by freq

        itemList = []
        for wordObj in desWords:
            itemList.append(wordObj.id) # add id's to itemList of word
        n = len(itemList)
        r = rIn #cfg.nCr
        comb = []
        for i in range(r):
            comb.append(0) # create stack of size r
        cmb.combinGen(n, r, itemList, 0, 0, comb, combList)
        # -------------- end of combination ----------------------- #

        cmbStr = []
        for c in combList:
            res = cmb.checkIgnoreComb(c,wordIdDict,ignoreDict)
            if(res==1):
                continue
            cStr = ""
            sortedC = sorted(c,key = lambda x:wordIdDict[x].word) # sort id's alphabeticaly
            for id in sortedC:
                if (cStr == ""):
                    cStr = wordIdDict[id].word
                else:
                    cStr = cStr + "_" + wordIdDict[id].word
            cmbStr.append(cStr)
        # --------- end of filtered and sorted and generated cmbStr ----------- #
        for cStr in cmbStr:
            if (cStr in combDict):
                freq = combDict[cStr]
                combDict[cStr] = freq + 1
            else:
                combDict[cStr] = 1
        # --------- end of freq of cmbStr ------------------------------------- #
    if len(combDict) < 1:
        return 0
    # ------------------------ write to file --------------------------------- #
    allData = []
    # code below is to write combinations to the file
    for key, val in combDict.items():
        if(val<2):
            continue
        items = key.split("_")
        iStr=""
        #confStr = ""
        confList = []
        ct=0
        freqList = []
        impWdCnt=0
        ## freq Bucket List:
        # index 0 - freq less than eq 10
        # index 1 - freq less than eq 20
        # index 2 - freq less than eq 50
        # index 3 - freq less than eq 100
        # index 4 - freq greater than 100
        freqBktList = [0,0,0,0,0]
        # --------------- fill freqBktList and confList ---------------- #
        for item in items:
            if(item in impDict):
                impWdCnt +=1
            #impWdCnt = cmb.getImportantWordCount(c, wordIdDict, impDict)
            frq = wordDict[item].freq
            bktIdx = cmb.get_bkt_index(frq)
            #freqBktList[bktIdx] = str(int(freqBktList[bktIdx]) + 1) # my cnage
            freqBktList[bktIdx] = freqBktList[bktIdx] + 1
            iL = [item,frq]
            freqList.append(iL)
            iConf = round(float(val/frq),2)
            confList.append(str(iConf))
            if(ct==0):
                iStr = item + "~" + str(frq)
                ct +=1
            else:
                iStr= iStr + "#:#" + item + "~" + str(frq)
        # my back tab
        # ------------------------ conflag,min-max conf -------------------- #
        #check if conf for all is > 0.75
        minConf = 100.0
        maxConf = 0.0
        for cff in confList:
            cff = float(cff)
            if(minConf > cff):
                minConf = cff
            if(maxConf < cff):
                maxConf = cff

        comWFlag = 1
        for cf in confList:
            if(float(cf)< 0.75):
                comWFlag = 0
                break
        # --- k: in ctrix create list here ----- #
        #freqBktStr = ""
        #freqBktStr = ",".join(freqBktList) # keep integer
        #confStr = ""
        #confStr = "#:#".join(confList) + ","+str(maxConf) + "," + str(minConf) + ","+ str(comWFlag) # keep split
        #strW = key + "," + str(val)+","+str(r)+","+str(impWdCnt) + ","+freqBktStr+"," + iStr + "," + confStr + "\n"
        currData = [key,val,r,impWdCnt,freqBktList[0],freqBktList[1],freqBktList[2],freqBktList[3],freqBktList[4],
                    iStr,"#:#".join(confList),maxConf,minConf,comWFlag]
        # sample line metadata as given below
        # combination,comb_freq,comb_size,impWdCnt,freqBktStr,item1,freq1,item2,freq2,..,itemN,freqN, conf1,conf2,conf3..confN,compFlag
        allData.append(currData)
    # --------------------------- load data to table ------------------------ #
    df = pd.DataFrame(allData,
                      columns=["comb_str", "comb_freq", "comb_size","imp_flag",
                               "bkt_below_10_cnt","bkt_10_20_cnt","bkt_20_50_cnt","bkt_50_100_cnt","bkt_100_above",
                               "comb_detail_str", "conf_detail_str","conf_max","conf_min","conf_flag"])
    schema = [
        bigquery.SchemaField("comb_str", 'STRING'),
        bigquery.SchemaField("comb_freq", "INT64"),
        bigquery.SchemaField("comb_size", "INT64"),
        bigquery.SchemaField("imp_flag", 'INT64'),
        bigquery.SchemaField("bkt_below_10_cnt", 'INT64'),
        bigquery.SchemaField("bkt_10_20_cnt", 'INT64'),
        bigquery.SchemaField("bkt_20_50_cnt", 'INT64'),
        bigquery.SchemaField("bkt_50_100_cnt", 'INT64'),
        bigquery.SchemaField("bkt_100_above", 'INT64'),
        bigquery.SchemaField("comb_detail_str", 'STRING'),
        bigquery.SchemaField("conf_detail_str", 'STRING'),
        bigquery.SchemaField("conf_max", "FLOAT"),
        bigquery.SchemaField("conf_min", "FLOAT"),
        bigquery.SchemaField("conf_flag", "INT64"),
    ]
    # ------------------ truncate first time ------------------------ #
    if (r == 1):
        jobConf = bigquery.LoadJobConfig(
            schema=schema,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
        )
    else:
        jobConf = bigquery.LoadJobConfig(
            schema=schema,
        )
    # ------------------------ upload data to gcp ------------------------------- #
    job = client.load_table_from_dataframe(df,cicwordCombTable, job_config=jobConf)
    print(f"step 2 : word combination size {r}  {job.result().state}")


