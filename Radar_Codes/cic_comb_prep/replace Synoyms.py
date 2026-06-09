import csv
import pandas as pd
merged_syn=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\Merged_Synoyms.csv"

replaced_comb=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\composite comb replaced.csv"

def baseWordReplacing(baseWordDict, snt):
    sntLst = snt.split()
    for idx in range(len(sntLst)):
        if sntLst[idx] in baseWordDict:
            sntLst[idx] = baseWordDict[sntLst[idx]]
    return " ".join(sntLst)
# -------------------------- e
synonyms = {}
with open(merged_syn, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)


    for dataTuple in reader:
        word = dataTuple["word"]
        synonym = dataTuple["synonym"]
        # print(word)
        if word not in synonyms:
            synonyms[word] = synonym

    allData = []
with open(replaced_comb, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for dataTuple in reader:
        cic = dataTuple["product_id"]
        newDsc = dataTuple["new_product_dsc"]
        oldDsc = dataTuple["product_dsc"]
        dept = dataTuple["dept_nm"]
        newDsc = baseWordReplacing(synonyms, newDsc)  # replace word with synonym
        allData.append([cic, newDsc, oldDsc, dept])
        df = pd.DataFrame(allData, columns=["cic", "new_cic_dsc", "old_cic_dsc", "dept"])
df.to_csv("Synonym_Replaces.csv")