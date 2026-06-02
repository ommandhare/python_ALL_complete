
projectId__ = r'gcp-abs-sdra-dev-prj-01'
projectId_ = r'gcp-abs-sdra-qa-prj-01'
projectId = r'gcp-abs-sdra-prod-prj-01'
dataSetId = r'sdra_ds_radar'
# -------------------------- table names ----------------------------------- #
# step 1 : wordCnt.py
prepCicAttribTableId = r'prep_cic_dsc_item_attribute'
prepCicWordCntTableId = r'cic_wordcnt'
# step 2: wordCombination.py
ignoreWordsTableId = r'ignore_words'
wordAttribTableId = r'word_attrib'
wordDesCombTableId = r'cic_word_comb'
# step 3: pruneCombination.py
pruneCombTableId = r'cic_word_pruned'
# step 4: cicDscCombination.py
cicDscCombTableId = r'cic_des_comb_all_dept_final'

# -------------------------- SQL queries ---------------------------------- #
# step 1 : wordCnt.py
prepCicAttribQuery = r'SELECT * FROM `PROJECTID.DATASETID.TABLEID`'
# step 2 : wordCombination.p
wordAttribQuery = r'SELECT word FROM `PROJECTID.DATASETID.TABLEID` WHERE FLAG = 1'
ignoreWordsQuery = 'SELECT word FROM `PROJECTID.DATASETID.TABLEID`'
prepCicWordCntQuery = r'SELECT word,freq FROM `PROJECTID.DATASETID.TABLEID`'
# step 3 : pruneComnination.py
prepWordDesCombQuery = r'SELECT * FROM `PROJECTID.DATASETID.TABLEID` WHERE comb_size = {R}'
prepWordDesCombMaxSizeQuery = r'SELECT MAX(comb_size) AS m_size FROM `PROJECTID.DATASETID.TABLEID`'
# step 4 : cicDscCombination.py
prepWordPrunDesCombQuery = r'SELECT * FROM `PROJECTID.DATASETID.TABLEID` WHERE comb_size = {R}'
prepWordPrunDesCombMaxSizeQuery = r'SELECT MAX(comb_size) AS m_size FROM `PROJECTID.DATASETID.TABLEID`'

