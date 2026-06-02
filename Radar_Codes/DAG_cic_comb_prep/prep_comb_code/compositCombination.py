import re
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'prep_comb_code'))
import combUtility as cu
from google.cloud import bigquery 
import config as cfg
import pandas as pd



def compositWordPrg(r,**kwarg):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    print("env : ",kwarg["params"]["env"])
    # ------------------------- input table --------------------------------#
    cicDscTable_Q = cfg.cicDscTableQuery.replace('PROJECTID', cfg.projectId).replace('DATASETID', cfg.dataSetId) \
        .replace('TABLEID', cfg.srcTableId).replace("{{ params.env }}",kwarg['params']["env"])
    compositeWordsTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.compositeWordId}'.replace("{{ params.env }}",kwarg['params']["env"])

    cicDscTable = client.query(cicDscTable_Q).result()
    # -------------------------- prep composit words prg ----------------------------- #
    dscCombDict = {}
    wordCnt = {}
    for dataTuple in cicDscTable:
        ingDsc = dataTuple["internet_item_dsc"]
        if ingDsc is None: # skip cic with no dsc
            continue
        ingDscLst = re.findall(r'[A-Z]+',ingDsc) # get words from dsc
        words = sorted(ingDscLst)  # is sorted alphabetically.
        # -------- get word freq ------------------------------#
        for word in words:
            if word not in wordCnt:
                wordCnt[word] = 1
            else:
                wordCnt[word] += 1
        # --------------- gen combination ------------------- #
        wordCombs = []
        cu.ncr(words, 0, len(words), wordCombs, r, [])
        if len(wordCombs) == 0:  # skip dsc if r size combi cannot be created.
            continue
        # --------------   cmb freq  ------------------------ #
        for cmbLst in wordCombs:
            cmbStr = "#".join(cmbLst)
            if cmbStr not in dscCombDict:
                dscCombDict[cmbStr] = 1
            else:
                dscCombDict[cmbStr] += 1

    allData = []
    for cmbStr, cmbFreq in dscCombDict.items():
        if cmbFreq < 2 :
            continue
        # ------- gen conf str -------------------- #
        confLst = []
        confFlag = 1
        for word in cmbStr.split('#'):
            currConf = cmbFreq / wordCnt[word]
            if currConf < 0.75 or wordCnt[word] <= 1:
                confFlag = 0
            confLst.append(f'{word}~{round(currConf, 2)}')
        confStr = "#:#".join(confLst)

        if confFlag == 0:
            continue
        # -------- gen wordFreqStr ---------------- #
        wordFreqLst = []
        for wd in cmbStr.split('#'):
            wordFreqLst.append(f'{wd}~{wordCnt[wd]}')
        wordFreqStr = "#:#".join(wordFreqLst)
        allData.append([cmbStr, cmbFreq, r, wordFreqStr, confStr, confFlag])

    # --------------------------- load data to table ------------------------ #
    df = pd.DataFrame(allData, columns=["comb_str","comb_freq","comb_size","comb_detail_str","conf_detail_str","composite_flag"])
    schema = [
                bigquery.SchemaField("comb_str", 'STRING'),
                bigquery.SchemaField("comb_freq", "INT64"),
                bigquery.SchemaField("comb_size", "INT64"),
                bigquery.SchemaField("comb_detail_str", 'STRING'),
                bigquery.SchemaField("conf_detail_str", 'STRING'),
                bigquery.SchemaField("composite_flag", "INT64"),
            ]
    if(r == 2):
        jobConf = bigquery.LoadJobConfig(
            schema=schema,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
        )
    else:
        jobConf = bigquery.LoadJobConfig(
            schema=schema,
        )
    # ------------------------ upload data to gcp ------------------------------- #
    job = client.load_table_from_dataframe(df, compositeWordsTable, job_config=jobConf)

    print(f"step 4 : composit words gen of size {r}  {job.result().state}")

