import sys
import os
 
# Add the ing_cls_code directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'DAG_cic_comb'))
import itemSet as itm
import wrdClenUtility as ut
import combUtility as cmb
import config as cfg
from google.cloud import bigquery
import pandas as pd

def generateDesComb(rIn):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # -------------------- In Path ------------------- #
    prepCicAttrib_Q = cfg.prepCicAttribQuery.replace("PROJECTID", cfg.projectId).replace("DATASETID", cfg.dataSetId) \
        .replace("TABLEID", cfg.prepCicAttribTableId)
    prunWordDscComb_Q = cfg.prepWordDesCombQuery.replace("PROJECTID", cfg.projectId).replace("DATASETID", cfg.dataSetId) \
        .replace("TABLEID", cfg.pruneCombTableId).replace('{R}', str(rIn))
    cicDesWordCnt_Q = cfg.prepCicWordCntQuery.replace("PROJECTID", cfg.projectId).replace("DATASETID", cfg.dataSetId) \
        .replace("TABLEID", cfg.prepCicWordCntTableId)
    prunWordDscCombMaxSize_Q = cfg.prepWordPrunDesCombMaxSizeQuery.replace("PROJECTID", cfg.projectId).replace("DATASETID", cfg.dataSetId)\
        .replace("TABLEID", cfg.pruneCombTableId)
    cicDesCombTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.cicDscCombTableId}'

    prepCicAttribTable = client.query(prepCicAttrib_Q)
    prunWordDscCombTable = client.query(prunWordDscComb_Q)
    cicDesWordCntTable = client.query(cicDesWordCnt_Q)
    maxCombSize = 0
    for size in client.query(prunWordDscCombMaxSize_Q):
        maxCombSize = size['m_size']
    # ------------------- End in Path --------------------------- #
    if rIn > maxCombSize:
        return 0
    #print('max :',maxCombSize,'r : ',rIn)
    # ----------------------------------------------------------- #
    wordDict = {}
    wordIdDict = {}
    finCombDict = {}
    allData = []
    # read combination file and load in dict to create impDict and ignDict
    #print(pathComb)
    # -------------------- read pruned cmb -------------------------- #
    for pruDataTuple in prunWordDscCombTable:
        combStr, combFreq, combSize, impFg, bk1, bk2, bk3, bk4, bk5, combDtlStr, confDtlStr, maxConf, minConf, confFg = pruDataTuple
        finCombDict[combStr] = [combFreq, combSize, impFg, bk1, bk2, bk3, bk4, bk5, combDtlStr, confDtlStr, maxConf, minConf, confFg]
    # -------------------- End of pruned cmb ----------------------- #
    # read frequent itemset file and create itemset class obj
    cnt = -1
    for freqDataTuple in cicDesWordCntTable:
        cnt += 1
        wrd,freq = freqDataTuple
        if (len(wrd) < 3):
            continue
        if (int(freq) < 2):
            continue
        tempItemSet = itm.ItemSet(cnt, wrd, freq)
        wordDict[wrd] = tempItemSet
        wordIdDict[int(cnt)] = tempItemSet
    # ---------------------- End of word freq obj ------------------ #
    # ----------------- combination start here ---------------- #
    ctt=0
    for prepDataTuple in prepCicAttribTable:
        cic, newDsc, oldDsc, dept, nvFlag, lqFlag, impFlag, effFlag = prepDataTuple

        ctt +=1
        combList = []
        if (len(newDsc) < 2):
            continue
        #print(desc)
        wList = []
        ut.getWordList(newDsc,wList)
        desWords = []
        wl = []
        for word in wList:
            if (word in wordDict):
                desWords.append(wordDict[word])

        size = len(desWords)
        cmb.sortList(desWords, size)
        itemList = []
        for wordObj in desWords:
            itemList.append(wordObj.id)
        n = len(itemList)
        r = rIn #cfg.nCr
        comb = []
        for i in range(r):
            comb.append(0)
        cmb.combinGen(n, r, itemList, 0, 0, comb, combList)
        cmbStr = []
        for c in combList:
            cStr = ""
            sortedC = sorted(c,key = lambda x:wordIdDict[x].word)
            for id in sortedC:
                if (cStr == ""):
                    cStr = wordIdDict[id].word
                else:
                    cStr = cStr + "_" + wordIdDict[id].word
            if(cStr in finCombDict):
                combFreq, combSize, impFg, bk1, bk2, bk3, bk4, bk5, combDtlStr, confDtlStr, maxConf, minConf, confFg = finCombDict[cStr]
                allData.append([cic, newDsc, oldDsc, dept,cStr,combFreq, combSize, impFg,
                                bk1, bk2, bk3, bk4, bk5, combDtlStr, confDtlStr, maxConf, minConf, confFg])
                #finLine = strLn + "," + finCombDict[cStr] # changes
                #f.write(finLine)
    # --------------------- load data ------------------------------------- #
    df = pd.DataFrame(allData,
                      columns=["cic","new_cic_des","old_cic_des","dept","comb_des",
                               "comb_freq", "comb_size", "imp_flag","bkt_below_10_cnt", "bkt_10_20_cnt",
                               "bkt_20_50_cnt", "bkt_50_100_cnt","bkt_100_above","comb_detail_str", "conf_detail_str",
                               "conf_max", "conf_min", "composite_flag"])
    schema = [
        bigquery.SchemaField("cic", 'INT64'),
        bigquery.SchemaField("new_cic_des", 'STRING'),
        bigquery.SchemaField("old_cic_des", 'STRING'),
        bigquery.SchemaField("dept", 'STRING'),
        bigquery.SchemaField("comb_des", 'STRING'),
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
        bigquery.SchemaField("composite_flag", "INT64"),
    ]
    # ------------------ truncate first time ------------------------ #
    #jobConf = bigquery.LoadJobConfig()
    if (rIn == 1):
        jobConf = bigquery.LoadJobConfig(
            schema=schema,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
        )
    else:
        jobConf = bigquery.LoadJobConfig(
            schema=schema,
        )
    job = client.load_table_from_dataframe(df,cicDesCombTable, job_config=jobConf)
    print(f"step 5 : gen des comb size {r}  {job.result().state}")
    return 1
