import sys
import os
 
# Add the ing_cls_code directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'DAG_cic_comb'))
from google.cloud import bigquery  # pip install google-cloud-bigquery
import config as cfg
import pandas as pd


def wordCntPrg():
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # ---------------- In paths -------------- #
    prepCicAttrib_Q = cfg.prepCicAttribQuery.replace("PROJECTID",cfg.projectId).replace("DATASETID",cfg.dataSetId)\
        .replace("TABLEID",cfg.prepCicAttribTableId)
    outputTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.prepCicWordCntTableId}'
    prepCicAttribTable = client.query(prepCicAttrib_Q)
    # ---------------- word Cnt prg ---------- #
    wordDict = {}
    for dataTuple in prepCicAttribTable:
        cic,newDsc,oldDsc,dept,nvFlag,lqFlag,impFlag,effFlag =dataTuple
        wordLst = newDsc.split()
        for word in wordLst:
            if word in wordDict:
                cnt = wordDict[word]
                wordDict[word] = cnt+1
            else:
                wordDict[word] = 1

    allData = []
    for word,cnt in wordDict.items():
        allData.append([word,cnt])
    # ------------load data into table--------------------- #
    df = pd.DataFrame(allData,columns=["word","freq"])
    jobConf = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("word", 'STRING'),
            bigquery.SchemaField("freq", "INT64"),
        ],
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    # ------------------------ upload data to gcp ------------------------------- #
    job = client.load_table_from_dataframe(df, outputTable, job_config=jobConf)
    print(f"step 1 : prep word count   {job.result().state}")

