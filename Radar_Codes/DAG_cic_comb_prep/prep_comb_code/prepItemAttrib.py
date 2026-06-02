import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'prep_comb_code'))

from google.cloud import bigquery 
import config as cfg
import pandas as pd



def prepItemAttribPrg(**kwarg):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # ------------------------- input table --------------------------------#
    sysWordRepTable_Q = cfg.sysWordRepTableQuery.replace("PROJECTID",cfg.projectId).replace("DATASETID",cfg.dataSetId)\
        .replace("TABLEID",cfg.sysWordRepId).replace("{{ params.env }}",kwarg['params']["env"])
    impWordTable_Q = cfg.wordAttribTableQuery.replace('PROJECTID', cfg.projectId).replace('DATASETID',cfg.dataSetId)\
        .replace('TABLEID', cfg.wordAttribId).replace('FLAG', 'imp_fg').replace("{{ params.env }}",kwarg['params']["env"])
    nonVegWordTable_Q = cfg.wordAttribTableQuery.replace('PROJECTID', cfg.projectId).replace('DATASETID',cfg.dataSetId)\
        .replace('TABLEID', cfg.wordAttribId).replace('FLAG', 'nv_fg').replace("{{ params.env }}",kwarg['params']["env"])
    liquidWordTable_Q = cfg.wordAttribTableQuery.replace('PROJECTID', cfg.projectId).replace('DATASETID',cfg.dataSetId)\
        .replace('TABLEID', cfg.wordAttribId).replace('FLAG', 'lq_fg').replace("{{ params.env }}",kwarg['params']["env"])
    stopWordTable_Q = cfg.stopWordsTableQuery.replace('PROJECTID', cfg.projectId).replace('DATASETID',cfg.dataSetId)\
        .replace('TABLEID', cfg.stopWordsId).replace("{{ params.env }}",kwarg['params']["env"])
    prepIngDscTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.prepIngDscDeptId}'.replace("{{ params.env }}",kwarg['params']["env"])
    
    sysWordRepTable = client.query(sysWordRepTable_Q).result()
    impWordTable = client.query(impWordTable_Q).result()
    nonVegWordTable = client.query(nonVegWordTable_Q).result()
    liquidWordTable = client.query(liquidWordTable_Q).result()
    stopWordTable = client.query(stopWordTable_Q).result()
    # -------------------------- prep synonym word replace prg ----------------------------- #

    prepDscData = []
    impWordsDict = set()
    nonVegWordsDict = set()
    liqWordsDict = set()
    stopWords = set()
    # ------------------- extract data ----------------- #
    for dataTuple in sysWordRepTable:
        cic, newDsc, oldDsc,dept =  dataTuple
        prepDscData.append([cic, newDsc, oldDsc,dept])
    for  dataTuple in impWordTable:  # important word load
        word =  dataTuple["word"]
        impWordsDict.add(word)
    for dataTuple in  nonVegWordTable:  # non-veg word load
        word = dataTuple["word"]
        nonVegWordsDict.add(word)
    for dataTuple in liquidWordTable :  # liq word load
        word = dataTuple["word"]
        liqWordsDict.add(word)
    for dataTuple in stopWordTable: # stop word file
        word = dataTuple["word"]
        stopWords.add(word)
    # ------------------ prepItem attrib program ------------- #
    # ------------------- get word freq -------------------- #
    wordCnt = {}
    for dataTuple in prepDscData:
        newDsc = dataTuple[1]
        for wd in newDsc.split():
            if len(wd) > 2:
                if wd not in wordCnt:
                    wordCnt[wd] = 1
                else:
                    wordCnt[wd] += 1
    print('word count completed.')
    #   ---------------------- adding flags ------------------- #
    allData = []
    for dataTuple in prepDscData:
        cic,newDsc, oldDsc,dept = dataTuple
        tmpDsc = []
        dupWdDict = set() # updated
        nonVegFlag = 0
        liqFlag = 0
        impWdCnt = 0
        effWdCnt = 0
        for word in newDsc.split():
            if word in stopWords:
                continue
            if word not in dupWdDict: # updated
                tmpDsc.append(word)
                dupWdDict.add(word) #updated
            if word in nonVegWordsDict:
                nonVegFlag = 1
            if word in liqWordsDict:
                liqFlag = 1
            if word in impWordsDict:
                impWdCnt += 1
            if word in wordCnt and wordCnt[word] > 1 and len(word) > 2:
                effWdCnt += 1
        allData.append([cic," ".join(tmpDsc), oldDsc,dept, impWdCnt, nonVegFlag, liqFlag, effWdCnt])
    print('flaging dsc completed.')
    # ---------------------- load data ---------------------------- #
    df = pd.DataFrame(allData, columns=["cic", "new_cic_dsc", "old_cic_dsc","dept","imp_flag","nv_flag","lq_flag","effective_wrd_cnt"])
    jobConf = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("cic", 'INT64'),
            bigquery.SchemaField("new_cic_dsc", 'STRING'),
            bigquery.SchemaField("old_cic_dsc", 'STRING'),
            bigquery.SchemaField("dept", 'STRING'),
            bigquery.SchemaField("imp_flag", 'INT64'),
            bigquery.SchemaField("nv_flag", 'INT64'),
            bigquery.SchemaField("lq_flag", 'INT64'),
            bigquery.SchemaField("effective_wrd_cnt", 'INT64'),
        ],
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    # ------------------------ upload data to gcp ------------------------------- #
    job = client.load_table_from_dataframe(df,prepIngDscTable, job_config=jobConf)
    print(f"step 8 : adding attributes to dsc  {job.result().state}")
