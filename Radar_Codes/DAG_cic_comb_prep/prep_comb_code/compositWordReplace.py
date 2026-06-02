import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'prep_comb_code'))

from combUtility import compReplace
from google.cloud import bigquery
import config as cfg
import pandas as pd
import re


def compositWdRepPrg(**kwarg):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # ------------------------- input table --------------------------------#
    compositWordsPrTable_Q = cfg.compositeWordPrTableQuery.replace("PROJECTID",cfg.projectId).replace("DATASETID",cfg.dataSetId)\
        .replace("TABLEID",cfg.compositeWordPrId).replace("{{ params.env }}",kwarg['params']["env"])
    cicDscTable_Q = cfg.cicDscTableQuery.replace('PROJECTID', cfg.projectId).replace('DATASETID', cfg.dataSetId) \
        .replace('TABLEID', cfg.srcTableId).replace("{{ params.env }}",kwarg['params']["env"])
    compositWordsRepDscTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.compWordRepId}'.replace("{{ params.env }}",kwarg['params']["env"])

    compositWordsPrTable = client.query(compositWordsPrTable_Q).result()
    cicDscTable = client.query(cicDscTable_Q).result()
    # -------------------------- prep composit word replace prg ----------------------------- #

    compWordDict = {}
    for dataTuple in compositWordsPrTable:
        cmbStr = dataTuple["comb_str"]
        cmbLst = cmbStr.split('#')
        for wd in cmbLst:
            compWordDict[wd] = (cmbStr,len(cmbLst))

    allData = []
    for dataTuple in cicDscTable:
        cic = dataTuple["cic"]
        dsc = dataTuple["internet_item_dsc"]
        dept = dataTuple["facility_department_nm"]
        if dsc is None:
            continue
        dscLst = re.findall(r'[A-Z]+',dsc)
        filterWords = " ".join(set(dscLst))
        sortedWords = " ".join(sorted(filterWords.split()))
        tmpDesc = str(compReplace(compWordDict,sortedWords))
        allData.append([cic,tmpDesc,dsc,dept])
    # --------------------------- load data to table ------------------------ #
    df = pd.DataFrame(allData, columns=["cic", "new_cic_dsc","old_cic_dsc","dept"])
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
    job = client.load_table_from_dataframe(df,compositWordsRepDscTable, job_config=jobConf)
    print(f"step 6 : composite words replaced in dsc  {job.result().state}")
