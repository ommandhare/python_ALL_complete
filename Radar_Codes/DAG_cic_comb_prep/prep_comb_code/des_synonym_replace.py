import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'prep_comb_code'))

from google.cloud import bigquery  # pip install google-cloud-bigquery
import config as cfg
import pandas as pd


# --------------------------- required function ------------------------ #
def baseWordReplacing(baseWordDict, snt):
    sntLst = snt.split()
    for idx in range(len(sntLst)):
        if sntLst[idx] in baseWordDict:
            sntLst[idx] = baseWordDict[sntLst[idx]]
    return " ".join(sntLst)
# -------------------------- end of required function ------------------- #

def dscSynonymPrg(**kwarg):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # ------------------------- input table --------------------------------#
    compWordRepDscTable_Q = cfg.compWordRepTableQuery.replace('PROJECTID',cfg.projectId).replace('DATASETID',cfg.dataSetId)\
        .replace('TABLEID',cfg.compWordRepId).replace("{{ params.env }}",kwarg['params']["env"])
    mergedSynonymTable_Q = cfg.mergedSynonymTableQuery.replace('PROJECTID',cfg.projectId).replace("DATASETID",cfg.dataSetId)\
        .replace("TABLEID",cfg.mergedSynonymId).replace("{{ params.env }}",kwarg['params']["env"])
    synonyRepDscTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.sysWordRepId}'.replace("{{ params.env }}",kwarg['params']["env"])

    compWordRepDscTable = client.query(compWordRepDscTable_Q).result()
    mergedSynonymTable = client.query(mergedSynonymTable_Q).result()
    # -------------------------- prep synonym word replace prg ----------------------------- #

    # ---- read synonyms ------#
    synonyms = {}
    for dataTuple in mergedSynonymTable:
        word = dataTuple["word"]
        synonym = dataTuple["synonym"]
        if word not in synonyms:
            synonyms[word] = synonym

    allData = []
    for dataTuple in compWordRepDscTable:
        cic = dataTuple["cic"]
        newDsc = dataTuple["new_cic_dsc"]
        oldDsc = dataTuple["old_cic_dsc"]
        dept = dataTuple["dept"]
        newDsc = baseWordReplacing(synonyms, newDsc)  # replace word with synonym
        allData.append([cic, newDsc,oldDsc,dept])

    # --------------------------- load data to table ------------------------ #
    df = pd.DataFrame(allData, columns=["cic", "new_cic_dsc", "old_cic_dsc","dept"])
    jobConf = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("cic", 'INT64'),
            bigquery.SchemaField("new_cic_dsc", 'STRING'),
            bigquery.SchemaField("old_cic_dsc", 'STRING'),
            bigquery.SchemaField("dept", 'STRING'),
        ],
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    # ------------------------ upload data to gcp ------------------------------- #
    job = client.load_table_from_dataframe(df,synonyRepDscTable, job_config=jobConf)
    print(f"step 7 : synonym replaced dsc  {job.result().state}")

