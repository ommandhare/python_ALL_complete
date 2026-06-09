import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'ing_cls_code'))

from google.cloud import bigquery  # pip install google-cloud-bigquery
import config as cfg
import simUtility as su
import pandas as pd

# ------------------------- required functions ------------------- #
def loadSet(output,input):
    for wd in input:
        output.add(wd)
def genSynonymsData(word,wordLenDict,wordCntDict):
    baseWd = word
    wordSize = len(word)
    allDataSet = set()
    for i in range(wordSize-2,wordSize+4):
        if i in wordLenDict and word[0] in wordLenDict[i]:
            loadSet(allDataSet,wordLenDict[i][word[0]])

    simList = []
    for target in allDataSet:
        if su.nGrams(baseWd,target) >= 0.75: #or levenstine(baseWd,target) > 0.75:
            if wordCntDict[target] > wordCntDict[baseWd]:
                baseWd = target
            simList.append(target)
    return baseWd,simList
# ----------------- End of Required functions ---------------------------- #
def synonymPrg(**kwarg):
    # ------------------------- bigcloud setup ------------------------------#
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cfg.service_account_key
    client = bigquery.Client()
    # ------------------------- input table --------------------------------#
    wordCntTable_Q =cfg.wordCntTableQuery.replace("PROJECTID",cfg.projectId).replace("DATASETID",cfg.dataSetId)\
        .replace("TABLEID",cfg.wordCntTableId).replace("{{ params.env }}",kwarg['params']["env"])
    currSynonymTable = f'{cfg.projectId}.{cfg.dataSetId}.{cfg.currSynonymTableId}'.replace("{{ params.env }}",kwarg['params']["env"])

    wordCntTable = client.query(wordCntTable_Q).result()
    # -------------------------- base word program -------------------------#
    wordCntDict = {}
    wordLenDict = {}
    wordList = []
    for wdDataTuple in wordCntTable:
        word, cnt = wdDataTuple
        if len(word) < 3:
            continue
        wordCntDict[word] = int(cnt)
        wordList.append(word)
        if len(word) not in wordLenDict:  # if size is not in dict
            wordLenDict[len(word)] = {word[0]: {word}}
        else:
            if word[0] not in wordLenDict[len(word)]:  # if size is there but first character set is not
                wordLenDict[len(word)][word[0]] = {word}
            else:
                wordLenDict[len(word)][word[0]].add(word)  # just add word in right place
    print("data Loaded")
    wordList.sort(key=lambda x:wordCntDict[x],reverse=True) # sort word by freq des

    wordBaseWordDict = {}
    for word in wordList:
        if word in wordBaseWordDict:
            continue
        baseWd, simList = genSynonymsData(word, wordLenDict, wordCntDict)
        for wd in simList:
            wordBaseWordDict[wd] = baseWd
            wordLenDict[len(wd)][wd[0]].remove(wd)
    print("synonym finder done")
    allData = []
    for word, baseword in wordBaseWordDict.items():
        allData.append([word, baseword])

    # --------------------------- load data to table ------------------------ #

    df = pd.DataFrame(allData, columns=["word", "synonym"])
    jobConf = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("word", 'STRING'),
            bigquery.SchemaField("synonym", 'STRING'),
        ],
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    job = client.load_table_from_dataframe(df,currSynonymTable, job_config=jobConf)
    print(f"step 2 : synonym finder   {job.result().state}")
