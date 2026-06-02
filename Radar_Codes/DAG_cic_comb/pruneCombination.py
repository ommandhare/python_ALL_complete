import sys
import os
 
# Add the ing_cls_code directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'DAG_cic_comb'))
from google.cloud import bigquery  # pip install google-cloud-bigquery
import config as cfg
import pandas as pd

def getPrevComb(combDesc, cList):
    itemList = combDesc.split("_")
    size = len(itemList)
    for i in range(size):
        tempIL = itemList[:]
        tempIL.pop(i)
        cList.append("_".join(tempIL))


def getFinalCombin(rIn):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # --------------------- In path ----------------------- #
    wordDesCombMaxSize_Q = cfg.prepWordDesCombMaxSizeQuery.replace("PROJECTID",cfg.projectId).replace("DATASETID",cfg.dataSetId)\
        .replace("TABLEID",cfg.wordDesCombTableId)
    prevWordDesComb_Q = cfg.prepWordDesCombQuery.replace("PROJECTID",cfg.projectId).replace("DATASETID",cfg.dataSetId)\
        .replace("TABLEID",cfg.wordDesCombTableId).replace("{R}",str(rIn-1))
    currWordDesComb_Q = cfg.prepWordDesCombQuery.replace("PROJECTID",cfg.projectId).replace("DATASETID",cfg.dataSetId)\
        .replace("TABLEID",cfg.wordDesCombTableId).replace("{R}",str(rIn))
    prunWordDesCombTable = f"{cfg.projectId}.{cfg.dataSetId}.{cfg.pruneCombTableId}"

    prevWordDesCombTable = client.query(prevWordDesComb_Q)
    currWordDesCombTable = client.query(currWordDesComb_Q)
    maxCombSize = 0
    for size in client.query(wordDesCombMaxSize_Q):
        maxCombSize = size['m_size']
    # ---------------------- check for size -------------------------- #
    print('max : ',maxCombSize,"r :",rIn)
    if rIn > maxCombSize+1:
        return 0
    r = rIn
    # --------------------------- previous comb ---------------------------- #
    prevCombDict = {}
    for prevDataTuple in prevWordDesCombTable:
        combStr,combFreq,combSize,impFg,bk1,bk2,bk3,bk4,bk5,combDtlStr,confDtlStr,maxConf,minConf,confFg = prevDataTuple
        prevCombDict[combStr] = [combFreq,combSize,impFg,bk1,bk2,bk3,bk4,bk5,combDtlStr,confDtlStr,maxConf,minConf,confFg]

    #if os.path.isfile(combPath): # remove this in ctrix
    for currDataTuple in currWordDesCombTable:
        combStr,combFreq,combSize,impFg,bk1,bk2,bk3,bk4,bk5,combDtlStr,confDtlStr,maxConf,minConf,confFg = currDataTuple
        combination = combStr
        freq = combFreq
        pCombList = []
        getPrevComb(combination,pCombList)
        #print(pCombList)
        for subCmb in pCombList:
            if subCmb in prevCombDict and prevCombDict[subCmb][0] == freq:
                prevCombDict.pop(subCmb)

    allData = []
    for comb,dataTuple in prevCombDict.items():
        combFreq, combSize, impFg, bk1, bk2, bk3, bk4, bk5, combDtlStr, confDtlStr, maxConf, minConf, confFg = dataTuple
        allData.append([comb,combFreq, combSize, impFg, bk1, bk2, bk3, bk4, bk5, combDtlStr, confDtlStr, maxConf, minConf, confFg ])
    # --------------------- load data ------------------------------------- #
    df = pd.DataFrame(allData,
                      columns=["comb_str", "comb_freq", "comb_size", "imp_flag",
                               "bkt_below_10_cnt", "bkt_10_20_cnt", "bkt_20_50_cnt", "bkt_50_100_cnt", "bkt_100_above",
                               "comb_detail_str", "conf_detail_str", "conf_max", "conf_min", "conf_flag"])
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
    if (rIn-1 == 1):
        jobConf = bigquery.LoadJobConfig(
            schema=schema,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
        )
    else:
        jobConf = bigquery.LoadJobConfig(
            schema=schema,
        )
    job = client.load_table_from_dataframe(df,prunWordDesCombTable, job_config=jobConf)
    print(f"step 3 : word combination pruned size {r-1}  {job.result().state}")
    return 1

