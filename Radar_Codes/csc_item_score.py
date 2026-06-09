"""
Name: cscItemScore.py
Description: This is script to calculate score of description in csc.
"""

import pandas as pd
import config as cfg
import mysql.connector
import re
# import pymysql
# from sqlalchemy import create_engine,text


# ----------- Required Routes -------------------- #
def nGram(s: str, n: int) -> list[str]:

    print(f"\nGenerating {n}-grams for word : {s}")

    lst = []

    for i in range(len(s) - n + 1):

        gram = s[i:i + n]

        print(f"Iteration {i} -> {gram}")

        lst.append(gram)

    print(f"Final nGram List : {lst}")

    return lst


def nGrams(s: str, t: str) -> float:

    print(f"\nComparing Words -> {s} VS {t}")

    if len(s) < len(t):
        s, t = t, s

    grams = nGram(s, 2) if len(s) > 2 else [s]

    print(f"Generated grams : {grams}")

    sml = 0

    for n in grams:

        print(f"Checking gram : {n}")

        if n in t:

            sml += 1

            print(f"Matched -> {n}")

    similarity = sml / len(grams)

    print(f"Similarity Score : {similarity}")

    return similarity


def simMrg(wordList, freqList):

    print("\nStarting simMrg Function")

    print(f"Input wordList : {wordList}")
    print(f"Input freqList : {freqList}")

    newDict = {}

    for i in range(0, len(wordList) - 1):

        print(f"\nOuter Loop i = {i}")

        for j in range(i + 1, len(wordList)):

            print(f"Comparing {wordList[i]} WITH {wordList[j]}")

            if freqList[i] > 0:
                break

            similarity = nGrams(wordList[i], wordList[j])

            print(f"Similarity : {similarity}")

            if similarity >= 0.66:

                print("Similarity Threshold Matched")

                if freqList[i] > freqList[j]:

                    freqList[i] += freqList[j]
                    freqList[j] = 0

                    print(f"Updated freqList : {freqList}")

                else:

                    freqList[j] += freqList[i]
                    freqList[i] = 0

                    print(f"Updated freqList : {freqList}")

    print("\nCreating Final Dictionary")

    for i in range(0, len(wordList)):

        if freqList[i] > 0:

            newDict[wordList[i]] = freqList[i]

            print(f"Added -> {wordList[i]} : {freqList[i]}")

    print(f"Final Dictionary : {newDict}")

    return newDict


# ----------- Actual Code ------------------------ #
def getItemScore():

    # ------- MySQL Connection ---------- #
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0777",
        database="mockproject"
    )

    cursor = conn.cursor()
    cursor.execute(cfg.input_query)

    data = cursor.fetchall()

    columns = [col[0] for col in cursor.description]

    inputTable = pd.DataFrame(data, columns=columns)

    print(cfg.input_Table1)
    print(cfg.input_Table2)

    print(cfg.input_query)

    outputTable = cfg.outputTableId

    cicCnt = {}
    cscDict = {}
    cscCentroids = {}

    prevCsc = ''

    # ---------------- Process Data ---------------- #
    print("\n================ PROCESSING INPUT DATA ================\n")

    for dataTuple in inputTable.itertuples(index=False):

        print("\n-------------------------------------")
        print(f"Current Row : {dataTuple}")

        csc, cic, desc = dataTuple

        print(f"CSC  : {csc}")
        print(f"CIC  : {cic}")
        print(f"DESC : {desc}")

        if prevCsc == '':
            prevCsc = csc

        if prevCsc != csc:

            print(f'\nBefore Merge : {cscDict[prevCsc]}\n')

            words_list = list(cscDict[prevCsc].keys())
            freq_list = list(cscDict[prevCsc].values())

            cscDict[prevCsc] = simMrg(words_list, freq_list)

            print(f'\nAfter Merge : {cscDict[prevCsc]}\n')

            prevCsc = csc

        if csc not in cscDict:
            cscDict[csc] = {}

        if csc not in cicCnt:
            cicCnt[csc] = 1
        else:
            cicCnt[csc] += 1

        print(f"Current CIC Count : {cicCnt[csc]}")

        words = set(re.findall(r'[a-zA-Z]+', str(desc))) # extracts words from description and ignore numbers and space and special characters

        print(f"Extracted Words : {words}")

        for word in words:

            print(f"\nProcessing Word : {word}")

            if word not in cscDict[csc]:

                cscDict[csc][word] = 1

            else:

                cscDict[csc][word] += 1

            print(f"Updated Word Count : {cscDict[csc]}")

    print("\nStep 4 : Word Frequency Dictionary Created")

    print("\n================ CENTROID CREATION ================\n")

    # ---------------- Find Centroids ---------------- #
    for csc, wordCntDict in cscDict.items():

        print(f"\nProcessing CSC : {csc}")

        itemCnt = cicCnt[csc]

        centroid_50 = set()
        centroid_60 = set()
        centroid_70 = set()

        for word, cnt in wordCntDict.items():

            print("\n-------------------------")
            print(f"CSC : {csc}")
            print(f"Word : {word}")
            print(f"Count : {cnt}")
            print(f"Item Count : {itemCnt}")
            print(f"Ratio : {cnt/itemCnt}")

            if cnt / itemCnt >= 0.7:

                centroid_50.add(word)
                centroid_60.add(word)
                centroid_70.add(word)

                print(f"{word} Added To 50, 60, 70")

            elif cnt / itemCnt >= 0.6:

                centroid_50.add(word)
                centroid_60.add(word)

                print(f"{word} Added To 50, 60")

            elif cnt / itemCnt >= 0.5:

                centroid_50.add(word)

                print(f"{word} Added To 50")

        cscCentroids[csc] = (
            centroid_50,
            centroid_60,
            centroid_70
        )

        print(f"\nCentroid 50 : {centroid_50}")
        print(f"Centroid 60 : {centroid_60}")
        print(f"Centroid 70 : {centroid_70}")

    print("\nStep 5 : CSC Centroids Created")

    print("\n================ SCORE CALCULATION ================\n")

    # ---------------- Calculate Score ---------------- #
    outPutData = []

    for dataTuple in inputTable.itertuples(index=False):

        print("\n===================================")
        print(f"Scoring Row : {dataTuple}")

        csc, cic, desc = dataTuple

        score_50 = 0
        score_60 = 0
        score_70 = 0

        centroid_50_score = 5 * len(cscCentroids[csc][0])
        centroid_60_score = 5 * len(cscCentroids[csc][1])
        centroid_70_score = 5 * len(cscCentroids[csc][2])

        print(f"Centroid 50 Total Score : {centroid_50_score}")
        print(f"Centroid 60 Total Score : {centroid_60_score}")
        print(f"Centroid 70 Total Score : {centroid_70_score}")

        words = set(re.findall(r'[a-zA-Z]+', str(desc)))

        print(f"Words Extracted : {words}")

        for word in words:

            print(f"\nChecking Word : {word}")

            if word in cscCentroids[csc][0]:

                score_50 += 5

                print(f"score_50 Updated : {score_50}")

            if word in cscCentroids[csc][1]:

                score_60 += 5

                print(f"score_60 Updated : {score_60}")

            if word in cscCentroids[csc][2]:

                score_70 += 5

                print(f"score_70 Updated : {score_70}")

        final_score_50 = (
            score_50 / centroid_50_score
            if centroid_50_score > 0 else 0
        )

        final_score_60 = (
            score_60 / centroid_60_score
            if centroid_60_score > 0 else 0
        )

        final_score_70 = (
            score_70 / centroid_70_score
            if centroid_70_score > 0 else 0
        )

        print(f"""
                Final Scores:
                score_50 : {final_score_50}
                score_60 : {final_score_60}
                score_70 : {final_score_70}
                """
            )

        outPutData.append([
            csc,
            cic,
            desc,
            final_score_50,
            final_score_60,
            final_score_70,
        ])

    print("\nStep 6 : Score Calculation Completed")

    # ---------------- Create DataFrame ---------------- #
    df = pd.DataFrame(
        outPutData,
        columns=[
            "consumer_selling_cd",
            "corporate_item_cd",
            "internet_item_dsc",
            "score_50",
            "score_60",
            "score_70"
        ]
    )

    print("\nStep 7 : Output DataFrame Created")

    print("\n================ FINAL OUTPUT DATAFRAME ================\n")

    print(df.head(50))

    # ---------------- Save CSV ---------------- #
    csv_output_path = "csc_item_score.csv"

    df.to_csv(csv_output_path, index=False)

    print(f"\nStep 8 : CSV Generated Successfully -> {csv_output_path}")

    # ---------------- Load Data Into MySQL ---------------- #
    # Uncomment if needed

    print(f"\nStep 9 : Data Loaded Successfully Into Table -> {outputTable}")

    # ---------------- Close Connection ---------------- #
    cursor.close()
    conn.close()

    print("\nStep 10 : MySQL Connection Closed")


# ---------------- Run Function ---------------- #
getItemScore()