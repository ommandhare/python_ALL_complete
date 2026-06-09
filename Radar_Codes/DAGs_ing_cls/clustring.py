import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'ing_cls_code'))

from simUtility import wgtLevenstine,onlyWords
from google.cloud import bigquery  # pip install google-cloud-bigquery
import config as cfg
import pandas as pd



def clustringPrg(**kwarg):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # ------------------------- input table --------------------------------#
    ingNewDscTable_Q = cfg.recipeNewDscTableQuery.replace('PROJECTID',cfg.projectId).replace('DATASETID',cfg.dataSetId)\
        .replace('TABLEID',cfg.recipeNewDscId).replace("{{ params.env }}",kwarg['params']["env"])
    clusterTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.clusterId}'.replace("{{ params.env }}",kwarg['params']["env"])

    ingNewDscTable = client.query(ingNewDscTable_Q).result()
    # --------------------------- ing clustring program -------------------- #

    itemData = []
    for ingTuple in ingNewDscTable:
        ingId = ingTuple["ing_id"]
        oldDsc = ingTuple["old_ing_dsc"]
        newDsc = ingTuple["new_ing_dsc"]
        itemTuple = (ingId, newDsc) if len(newDsc) > 2 else (ingId, " ".join(onlyWords(oldDsc.upper())))
        itemData.append(itemTuple)

    # print(len(itemSetList))
    sortedList = sorted(itemData, key=lambda x: len(x[1]), reverse=True)

    # for item in sortedList:
    #    print("ID: ",item.id, " DES: ",item.name, " LEN: ",item.freq)
    print("clustring .../")
    itemDict = {}
    size = len(sortedList)
    for i in range(size - 1):
        # check if i is present in itemDict
        if (sortedList[i][0] in itemDict):
            continue
        for j in range(i + 1, size):
            if (wgtLevenstine(sortedList[i][1], sortedList[j][1]) > 0.75):
                # cluster formed
                # i is cluster center
                # j belongs to i
                if (sortedList[i][0] not in itemDict):
                    itemDict[sortedList[i][0]] = sortedList[i][0]
                if (sortedList[j][0] not in itemDict):
                    itemDict[sortedList[j][0]] = sortedList[i][0]

        if (sortedList[i][0] not in itemDict):
            itemDict[sortedList[i][0]] = sortedList[i][0]

    # --------------------------- load data to table ------------------------ #
    df = pd.DataFrame(itemDict.items(), columns=["ing_id", "cls_rep_id"])
    jobConf = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("ing_id", 'STRING'),
            bigquery.SchemaField("cls_rep_id", "STRING"),
        ],
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    job = client.load_table_from_dataframe(df,clusterTable, job_config=jobConf)
    print(f"step 5 : cluster table created     {job.result().state}")
