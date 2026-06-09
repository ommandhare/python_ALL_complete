#service_account_key = r'C:\Users\KBIRA00\Downloads\sdra-biqquery.txt'
projectId = r'gcp-abs-sdra-{{ params.env }}-prj-01'
dataSetId = r'sdra_ds_radar'

# ------------------------confing ------------------------------------------ #
recipeTableId = r'recipe_flat'
# step 1 : ingWordCnt.py
wordCntTableId = r'ing_cls_word_cnt'
# step 2 : baseWordFinder.py
currSynonymTableId = r'ing_cls_latest_synonyms'
# step 3 : mergeSynonymFiles.py
globalSynonymTableId = r'global_synonyms'
mergeSynonymTableId = r'ing_cls_merge_synonyms'
# step 4 :ingDscReplaceSynonym.py
recipeNewDscId = r'ing_cls_recipe_new_dsc'
# step 5 : clustring.py
clusterId = r'recipe_ing_cls'

# -------------------------- SQl ------------------------------------------- #

# step 1 :
recipeDscTableQuery = r'''
SELECT CAST(ING_ID AS STRING) AS ING_ID,UPPER(REPLACE(ING_NAME,","," ")) AS ING_NAME
FROM `PROJECTID.DATASETID.TABLEID`
WHERE DW_LOGICAL_DELETE_IND=FALSE AND DW_CURRENT_VERSION_IND=TRUE
GROUP BY ING_ID,ING_NAME;
'''
# step 2 :
wordCntTableQuery = r'''SELECT * FROM `PROJECTID.DATASETID.TABLEID`'''
# step 3 :
globalSynynomTableQuery = r'''SELECT gs.word,gs.synonym FROM `PROJECTID.DATASETID.TABLEID` gs'''
currSynonymTableQuery = r'''SELECT * FROM `PROJECTID.DATASETID.TABLEID`'''
# step 4 :
mergeSynonymTableQuery = r'''SELECT * FROM `PROJECTID.DATASETID.TABLEID`'''
# step 5:
recipeNewDscTableQuery = r'''SELECT * FROM `PROJECTID.DATASETID.TABLEID`'''

truncateTableQuery = r'''TRUNCATE TABLE `CURRTABLEID`'''

