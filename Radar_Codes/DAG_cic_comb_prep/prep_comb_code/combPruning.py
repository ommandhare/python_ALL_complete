import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'prep_comb_code'))

from combUtility import subCompositStr
from google.cloud import bigquery  # pip install google-cloud-bigquery
import config as cfg
import pandas as pd



def combPruningPrg(**kwarg):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # ------------------------- input table -------------------------------- #
    compositWordsTable_Q = cfg.compositeWordTableQuery.replace("PROJECTID",cfg.projectId).replace("DATASETID",cfg.dataSetId)\
        .replace("TABLEID",cfg.compositeWordId).replace("{{ params.env }}",kwarg['params']["env"])
    compositeWordPrTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.compositeWordPrId}'.replace("{{ params.env }}",kwarg['params']["env"])

    compositWordsTable = client.query(compositWordsTable_Q).result()
    # -------------------------- prep composit words pruning prg ----------------------------- #

    cmbDict = {}
    cmbList = []
    # ------------------- access data -------------- #
    for dataTuple in compositWordsTable:
        cmbStr = dataTuple["comb_str"]
        cmbFreq = dataTuple["comb_freq"]
        cmbSize = dataTuple["comb_size"]
        cmbDict[cmbStr] = (int(cmbFreq), int(cmbSize))
        cmbList.append(cmbStr)

    for cmbStr in cmbList:
        cmbFreq,cmbSize = cmbDict[cmbStr]
        subCmbStrs = subCompositStr(cmbStr,'#')
        for subStr in subCmbStrs:
            if subStr not in cmbDict:
                continue
            if cmbDict[subStr][0] == cmbFreq:
                cmbDict.pop(subStr)

    allData = []
    for cmbStr, (freq,size) in cmbDict.items():
        allData.append([cmbStr,freq,size])

# --------------------------- load data to table ------------------------ #
    df = pd.DataFrame(allData, columns=["comb_str", "comb_freq","comb_size"])
    jobConf = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("comb_str", 'STRING'),
            bigquery.SchemaField("comb_freq", "INT64"),
            bigquery.SchemaField("comb_size", "INT64"),
        ],
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    # ------------------------ upload data to gcp ------------------------------- #
    job = client.load_table_from_dataframe(df,compositeWordPrTable, job_config=jobConf)
    print(f"step 5 : prune composite words   {job.result().state}")


