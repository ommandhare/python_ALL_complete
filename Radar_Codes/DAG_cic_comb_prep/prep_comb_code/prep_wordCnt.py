import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'prep_comb_code'))

from google.cloud import bigquery  # pip install google-cloud-bigquery
import config as cfg
import pandas as pd
import re


def wordCnt(**kwarg):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # ------------------------- input table --------------------------------#
    cicDscTable_Q = cfg.cicDscTableQuery.replace('PROJECTID',cfg.projectId).replace('DATASETID',cfg.dataSetId)\
        .replace('TABLEID',cfg.srcTableId).replace("{{ params.env }}",kwarg['params']["env"])
    wordCntTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.prepWordCntId}'.replace("{{ params.env }}",kwarg['params']["env"])

    cicDscTable = client.query(cicDscTable_Q).result()
    # -------------------------- prep wordCount prg ----------------------------- #
    wordDict = {}
    for dataTuple in cicDscTable:
        dsc = dataTuple["internet_item_dsc"]
        if dsc is None:# skip cic with no dsc
            continue
        for word in re.findall(r'[A-Z]+', dsc): # get array of words from dsc
            if word not in wordDict:
                wordDict[word] = 1
            else:
                wordDict[word] += 1

    allData = []
    for word,freq in wordDict.items():
        allData.append([word,freq])
    # --------------------------- load data to table ------------------------ #

    df = pd.DataFrame(allData, columns=["word", "freq"])
    jobConf = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("word", 'STRING'),
            bigquery.SchemaField("freq", "INT64"),
        ],
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

    # ------------------------ upload data to gcp ------------------------------- #
    job = client.load_table_from_dataframe(df, wordCntTable, job_config=jobConf)
    print(f"step 1 : prep word count   {job.result().state}")

