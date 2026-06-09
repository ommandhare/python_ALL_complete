import re
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'ing_cls_code'))

from google.cloud import bigquery  # pip install google-cloud-bigquery
import config as cfg
import pandas as pd



def wordCntPrg(**kwarg):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    #print(kwarg)
    # ------------------------- input table --------------------------------#
    recipeDscTable_Q = cfg.recipeDscTableQuery.replace('PROJECTID',cfg.projectId).replace('DATASETID',cfg.dataSetId)\
        .replace('TABLEID',cfg.recipeTableId).replace("{{ params.env }}",kwarg['params']["env"])
    wordCntTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.wordCntTableId}'.replace("{{ params.env }}",kwarg['params']["env"])
    recipeDscTable = client.query(recipeDscTable_Q).result()
    # -------------------------- wordCount prg ----------------------------- #
    wordCntDict = {}
    for dataTuple in recipeDscTable:
        ingId,dsc = dataTuple
        dscLst = re.findall(r'[A-Z]+',dsc)
        for wd in dscLst:
            if wd not in wordCntDict:
                wordCntDict[wd] = 1
            else:
                wordCntDict[wd] += 1

    allData = []
    for wd, freq in wordCntDict.items():
        allData.append([wd, freq])
    # --------------------------- load data to table ------------------------ #

    df = pd.DataFrame(allData, columns=["word", "freq"])
    jobConf = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("word", 'STRING'),
            bigquery.SchemaField("freq", "INT64"),
        ],
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    job = client.load_table_from_dataframe(df,wordCntTable, job_config=jobConf)
    print(f"step 1 : word count   {job.result().state}")
