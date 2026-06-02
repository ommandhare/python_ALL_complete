import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'ing_cls_code'))

from google.cloud import bigquery  # pip install google-cloud-bigquery
import config as cfg
import pandas as pd
import re


# ---------------------------- required functions --------------------------- #
def baseWordReplacing(baseWordDict, snt):
    sntLst = snt.split()
    for idx in range(len(sntLst)):
        if sntLst[idx] in baseWordDict:
            sntLst[idx] = baseWordDict[sntLst[idx]]
    return " ".join(sntLst)


def cleanDes(stn, wordCnt, stopWords):
    stnLst = stn.split()
    cleanStnLst = set()
    for idx in range(len(stnLst)):
        word = stnLst[idx]
        if word in stopWords:
            continue
        if word in wordCnt:
            if wordCnt[word] > 1 and len(word) > 1:
                cleanStnLst.add(word)
        elif len(word) > 2:
            cleanStnLst.add(word)
    return " ".join(cleanStnLst)
# ------------------------ End of required functions ------------------------ #
def ingDscReplacing(**kwarg):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # ------------------------- input table --------------------------------#
    ingDscTable_Q = cfg.recipeDscTableQuery.replace('PROJECTID',cfg.projectId).replace('DATASETID',cfg.dataSetId)\
        .replace('TABLEID',cfg.recipeTableId).replace("{{ params.env }}",kwarg['params']["env"])
    mergeSynTable_Q = cfg.mergeSynonymTableQuery.replace('PROJECTID',cfg.projectId).replace('DATASETID',cfg.dataSetId)\
        .replace('TABLEID',cfg.mergeSynonymTableId).replace("{{ params.env }}",kwarg['params']["env"])
    newDscTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.recipeNewDscId}'.replace("{{ params.env }}",kwarg['params']["env"])

    ingDscTable = client.query(ingDscTable_Q).result()
    mergeSynTable = client.query(mergeSynTable_Q).result()
    # --------------------------- word replacement program -------------------- #

    stopWords = {'OZ', 'IN', 'INCH', 'OZZ', 'KG', 'LB', 'FZ', 'BULK', 'BLK', 'EXTRA', 'SELECT', 'KB','DO'}  # TODO  make a .csv and read

    wordBaseWord = {}
    for wordTuple in mergeSynTable:
        word, synonym = wordTuple
        wordBaseWord[word] = synonym
    wordCntDict ={}
    ingData = []
    for ingTuple in ingDscTable:
        ingId, ingDsc = ingTuple
        ingDscLst = re.findall(r'[A-Z]+',ingDsc)
        ingDscWdOnly = " ".join(ingDscLst).upper()
        repDesc = baseWordReplacing(wordBaseWord,ingDscWdOnly)
        ingData.append([ingId,ingDsc.replace(',',' '),repDesc])
        for word in repDesc.split():
            if word not in wordCntDict:
                wordCntDict[word] = 1
            else:
                wordCntDict[word]+=1

    ingDataNew = []
    for ingDataTuple in ingData:
        ingId,oldDsc,currDsc = ingDataTuple
        clnDesc = cleanDes(currDsc, wordCntDict, stopWords)
        newDesc = " ".join(sorted(clnDesc.split()))
        ingDataNew.append([ingId, oldDsc.replace(",", " "), newDesc,])


    # --------------------------- load data to table ------------------------ #
    df = pd.DataFrame(ingDataNew, columns=["ing_id", "old_ing_dsc", "new_ing_dsc"])
    jobConf = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("ing_id", 'STRING'),
            bigquery.SchemaField("old_ing_dsc", "STRING"),
            bigquery.SchemaField("new_ing_dsc", 'STRING'),
        ],
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE

    )
    job = client.load_table_from_dataframe(df,newDscTable, job_config=jobConf)
    print(f"step 4 : new clean dsc created    {job.result().state}")
