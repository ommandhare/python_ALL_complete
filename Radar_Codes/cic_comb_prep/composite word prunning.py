from utility import combUtility as c
import pandas as pd
path= r"/Radar_Codes/composite word.csv"
cmbList=[]
cmbDict={}
for data in open(path):
    cmbStr,cmbFreq,cmbSize,comb_detail_str,conf_detail_str,composite_flag=data.split(",")
    # print(cmbStr)
    cmbDict[cmbStr] = (int(cmbFreq), int(cmbSize))
    cmbList.append(cmbStr)


    for cmbStr in list(cmbDict.keys()):

        if cmbStr not in cmbDict:
            continue

        cmbFreq, cmbSize = cmbDict[cmbStr]

        subCmbStrs = c.subCompositStr(cmbStr, '#')

        for subStr in subCmbStrs:
            if subStr in cmbDict and cmbDict[subStr][0] == cmbFreq:
               print(subStr)
               cmbDict.pop(subStr)


    allData = []
    for cmbStr, (freq, size) in cmbDict.items():
        allData.append([cmbStr, freq, size])
        # print(allData)
        df = pd.DataFrame(allData,columns=["comb_str", "comb_freq","comb_size"])
df.to_csv("prunned.csv", index=False, mode='a', header=False)
    # print(df)

print("Done")