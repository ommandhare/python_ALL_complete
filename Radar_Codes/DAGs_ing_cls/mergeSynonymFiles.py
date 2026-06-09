import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'ing_cls_code'))

from google.cloud import bigquery  # pip install google-cloud-bigquery
import config as cfg
import pandas as pd


def mergeSynonymPrg(**kwarg):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # ------------------------- input table --------------------------------#
    globalSysTable_Q = cfg.globalSynynomTableQuery.replace('PROJECTID',cfg.projectId).replace('DATASETID',cfg.dataSetId)\
        .replace('TABLEID',cfg.globalSynonymTableId).replace("{{ params.env }}",kwarg['params']["env"])
    currSynTable_Q = cfg.currSynonymTableQuery.replace('PROJECTID', cfg.projectId).replace('DATASETID', cfg.dataSetId)\
        .replace('TABLEID', cfg.currSynonymTableId).replace("{{ params.env }}",kwarg['params']["env"])
    mergeSysTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.mergeSynonymTableId}'.replace("{{ params.env }}",kwarg['params']["env"])

    globalSynTable = client.query(globalSysTable_Q).result()
    currSynTable = client.query(currSynTable_Q).result()
    # -------------------------- merge program ---------------------------- #

    synonymDict = {}
    for wordTuple in globalSynTable:
        word = wordTuple["word"]
        synonym = wordTuple["synonym"]
        synonymDict[word] = synonym

    for wordTuple in currSynTable:
        word,  synonym = wordTuple
        if word in synonymDict:
            synonymDict[word] = synonymDict[word]
        else:
            synonymDict[word] = synonym

    mergedSynonyms = []
    for word,synonym in synonymDict.items():
        mergedSynonyms.append([word,synonym])

    # --------------------------- load data to table ------------------------ #
    df = pd.DataFrame(mergedSynonyms, columns=["word", "synonym"])
    jobConf = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("word", 'STRING'),
            bigquery.SchemaField("synonym", 'STRING'),
        ],
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE

    )
    job = client.load_table_from_dataframe(df,mergeSysTable, job_config=jobConf)
    print(f"step 3 : merge synonyms    {job.result().state}")

