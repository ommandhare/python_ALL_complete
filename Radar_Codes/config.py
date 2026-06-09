"""
Name: config.py
"""

# -------------------------- MYSQL CONFIG ----------------------- #
host = "localhost"
user = "root"
password = "0777"
database = "mockproject"

# -------------------------- TABLE CONFIG ----------------------- #
input_Table1 = r'csc_classification_tmp'
input_Table2 = r'prep_item_attrib'

outputTableId = r'csc_item_score'

# ----------------------------- MYSQL QUERY ----------------------- #
input_query = r"""
SELECT DISTINCT
    consumer_selling_cd,
    COALESCE(att.cic, CAST(cis.corporate_item_cd AS SIGNED)) AS corporate_item_cd,
    COALESCE(att.new_cic_dsc, REPLACE(cis.internet_item_dsc, ',', ' ')) AS internet_item_dsc
FROM csc_classification_tmp AS cis
LEFT JOIN prep_item_attrib AS att
ON CAST(cis.corporate_item_cd AS SIGNED) = att.cic
WHERE internet_item_dsc IS NOT NULL
ORDER BY consumer_selling_cd;
"""