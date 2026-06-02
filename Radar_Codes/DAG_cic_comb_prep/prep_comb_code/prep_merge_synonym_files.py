import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'prep_comb_code'))

from google.cloud import bigquery  # pip install google-cloud-bigquery
import config as cfg
import pandas as pd



def merge_synonym_prg(**kwarg):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # ------------------------- input table --------------------------------#
    globalSynonymTable_Q = cfg.synonymTableQuery.replace('PROJECTID',cfg.projectId).replace('DATASETID',cfg.dataSetId)\
        .replace('TABLEID',cfg.globalSynonymId).replace("{{ params.env }}",kwarg['params']["env"])
    prepSynonymTable_Q = cfg.synonymTableQuery.replace('PROJECTID',cfg.projectId).replace('DATASETID',cfg.dataSetId)\
        .replace('TABLEID',cfg.prepSynonymId).replace("{{ params.env }}",kwarg['params']["env"])
    mergedSynonymTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.mergedSynonymId}'.replace("{{ params.env }}",kwarg['params']["env"])

    globalSynonymTable = client.query(globalSynonymTable_Q).result()
    prepSynonymTable   = client.query(prepSynonymTable_Q).result()
    # -------------------------- prep merge synonym prg ----------------------------- #
    synonyDict = {}
    for dataTuple in globalSynonymTable:
        word = dataTuple["word"]
        synonym = dataTuple["synonym"]
        synonyDict[word] = synonym

    for dataTuple in prepSynonymTable:
        word = dataTuple["word"]
        synonym = dataTuple["synonym"]
        if word not in synonyDict:
            synonyDict[word]= synonym

    allData = []
    for word,synonym in synonyDict.items():
        allData.append([word,synonym])

    # --------------------------- load data to table ------------------------ #
    df = pd.DataFrame(allData, columns=["word", "synonym"])
    jobConf = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("word", 'STRING'),
            bigquery.SchemaField("synonym", "STRING"),
        ],
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    # ------------------------ upload data to gcp ------------------------------- #
    job = client.load_table_from_dataframe(df,mergedSynonymTable, job_config=jobConf)
    # ------------------ special case step 4 clean up -------------------------   #
    print(f"step 3 : merge synonyms   {job.result().state}")
