
#service_account_key = r'C:\Users\KBIRA00\Downloads\sdra-biqquery.txt'
projectId = r'gcp-abs-sdra-{{ params.env }}-prj-01'
projectId_ = r'gcp-abs-sdra-dev-prj-01'
dataSetId = r'sdra_ds_radar' # also change cicDscTableQuery sdim used
# --------------------------------------------- table config ----------------------------------------- #
# step 1: prep-word count.
srcTableId = r'item_dimension'
prepWordCntId = r'prep_cic_wordcnt'
# step 2: prep-synonym
prepSynonymId =r'prep_cic_latest_synonyms'
# step 3: merge synonym
globalSynonymId = r'global_synonyms'
mergedSynonymId = r'prep_cic_merged_synonyms'
# step 4: composit combination
compositeWordId =r'prep_cic_composite_words'
# step 5: comb pruning
compositeWordPrId = r'prep_cic_composite_words_pruned'
# step 6: replace composite word with words
compWordRepId = r'prep_cic_composite_words_replaced_dsc'
# step 7: replace synonym word with words
sysWordRepId = r'prep_cic_synonym_replaced_dsc'
# step 8: adding attrib flags to dsc
wordAttribId = r'word_attrib'
stopWordsId = r'stop_words'
prepIngDscDeptId = r'prep_cic_dsc_item_attribute'


# --------------------------------------------- SQL -------------------------------------------------- #
# step 1 : cic_cmb_wordCnt.py
cicDscTableQuery = r'''
    SELECT
    CAST(idim.corporate_item_cd AS INT64) AS cic,
    UPPER(REPLACE(idim.internet_item_dsc,","," ")) AS internet_item_dsc,
    idim.facility_department_nm
    FROM `gcp-abs-sdim-{{ params.env }}-prj-01.sdim_ds_data_analytics_{{ params.env }}_cts.TABLEID` idim
    GROUP BY idim.corporate_item_cd,
    idim.department_id,idim.facility_department_nm,idim.internet_item_dsc
'''
cicDscTableQuery_ = r'''
    SELECT
    CAST(idim.corporate_item_cd AS INT64) AS cic,
    UPPER(REPLACE(idim.internet_item_dsc,","," ")) AS internet_item_dsc,
    idim.facility_department_nm
    FROM `gcp-abs-sdim-dev-prj-01.sdim_ds_data_analytics_dev_cts.TABLEID` idim
    GROUP BY idim.corporate_item_cd,
    idim.department_id,idim.facility_department_nm,idim.internet_item_dsc
'''
truncateTableQuery = r'''
    TRUNCATE TABLE `TABLEURL` 
    '''
# step 2: prep_baseWordFinder.py
prepWordCntTableQuery = r'''
    SELECT word,freq FROM `PROJECTID.DATASETID.TABLEID`
    '''
# step 3: prep_merge_synonym_files.py
synonymTableQuery = r'''
    SELECT word,synonym FROM `PROJECTID.DATASETID.TABLEID`
    '''
# step 4: compositeCombination.py
# use  onlyDscSrcTableQuery

# step 5: combPruning.py
compositeWordTableQuery = '''
    SELECT * FROM `PROJECTID.DATASETID.TABLEID` cws
    ORDER BY cws.comb_size , cws.comb_freq DESC'''

#step 6: compositeWordReplace.py
compositeWordPrTableQuery = '''
SELECT comb_str FROM `PROJECTID.DATASETID.TABLEID`
'''
# step 7: des_synonym_replace.py
compWordRepTableQuery = '''
SELECT * FROM `PROJECTID.DATASETID.TABLEID`'''
mergedSynonymTableQuery = '''
SELECT word,synonym FROM `PROJECTID.DATASETID.TABLEID`'''

# step 8: prepItemAttrib.py
wordAttribTableQuery = '''
SELECT word FROM `PROJECTID.DATASETID.TABLEID`
WHERE FLAG = 1;
'''
stopWordsTableQuery = '''
SELECT word FROM `PROJECTID.DATASETID.TABLEID`'''
sysWordRepTableQuery = '''
SELECT * FROM `PROJECTID.DATASETID.TABLEID`'''

