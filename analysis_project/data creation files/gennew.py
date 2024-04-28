import schedule
import time
import os
from datetime import datetime
import pandas as pd
import mysql.connector
import csv


def mockCurrentDates():
    from datetime import datetime as dt
    from random import randint
    import pandas as pd
    import productAmt as pa

    today = datetime.now().date()
    tranIdList = []
    storeIdList = []
    member_idList = []
    productIdList = []
    startDateList = []
    qtyList = []
    amtList = []

    def mockCurrentDates():
        for itr in range(1):
            no = random.randint(20, 40)
            memberlist = []
            for i in range(1, no + 1):
                id = random.randint(1001, 1100)
                if id not in memberlist:
                    memberlist.append(id)  # memberList
                    storeId = random.randint(1, 3)
                    storeList = []
                    if storeId not in storeList:
                        storeList.append(storeId)  # StoreList
                        numProduct = random.randint(1, 10)
                        productList = []
                        for j in range(1, numProduct + 1):
                            productId = random.randint(1, 100)
                            if productId not in productList:
                                productList.append(productId)  # productList
                                if (id <= 1020):
                                    qty = random.randint(1600, 2000)
                                elif id <= 1025:
                                    qty = random.randint(500, 600)
                                elif id <= 1030:
                                    qty = random.randint(150, 200)
                                elif id <= 1035:
                                    qty = random.randint(210, 240)
                                elif id <= 1035:
                                    qty = random.randint(15, 18)
                                elif id <= 1040:
                                    qty = random.randint(15, 80)
                                elif id <= 1050:
                                    qty = random.randint(110, 150)
                                elif id <= 1060:
                                    qty = random.randint(30, 140)
                                elif id <= 1070:
                                    qty = random.randint(10, 14)
                                elif id <= 1075:
                                    qty = random.randint(185, 200)
                                elif id <= 1078:
                                    qty = random.randint(210, 240)
                                elif id <= 1080:
                                    qty = random.randint(1, 5)
                                else:
                                    qty = random.randint(1, 10)
                                productId = str(productId)
                                price = pa.productAmt.get(productId)
                                price = float(price)
                                amt = qty * price  # amt  qty*price
                                amt = round(amt, 2)
                                currentDateTime = datetime.now()
                                tranId = currentDateTime.strftime('%Y-%m-%dT') + currentDateTime.strftime(
                                    '%H-%M-%S-%f') + '_' + str(i)
                                tranIdList.append(tranId)  # tran_id and its format
                                member_idList.append(id)  # memberList
                                storeIdList.append(storeId)
                                productIdList.append(productId)  # productIdList
                                qtyList.append(qty)  # qtyList
                                amtList.append(amt)

        print("tran_dtl..#############")
        print(today)
        df1 = {'tran_id': tranIdList, 'product_id': productIdList, 'qty': qtyList, 'amt': amtList, 'tran_dt': today}
        tran_dtl = pd.DataFrame(df1)
        print(tran_dtl)
        # tran_dtl.to_csv(
            fr"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_dtl_daily.csv",
            index=False)
        tran_dtl.to_csv(
            fr"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_dtl_{today}.csv",
            index=False)

        print("tran_hdr..#############")
        df2 = {'tran_id': tranIdList, 'store_id': storeIdList, 'member_id': member_idList, 'tran_dt': today}
        # print(len(tranIdList))
        # print(len(storeIdList))
        # print(len(member_idList))
        tran_hdr = pd.DataFrame(df2)
        tran_hdr = tran_hdr.drop_duplicates()
        print(tran_hdr)
        # tran_hdr.to_csv(fr"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_hdr_daily.csv",index=False)
        tran_hdr.to_csv(
            fr"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_hdr_{today}.csv",
            index=False)
    return


def append():
    import pandas as pd
    import mysql.connector
    import csv

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='0777',
        database='retail'
    )

    cursor = conn.cursor()
    path1 = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_dtl_daily.csv"
    path2 = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_hdr_daily.csv"

    with open(path1, 'r') as file:
        data = csv.reader(file)
        for line in data:
            query = f"INSERT INTO {'tran_dtl'} VALUES {tuple(line)}"
            # for itr in range(len(data))
            cursor.execute(query)

    with open(path2, 'r') as file:
        data = csv.reader(file)
        for line in data:
            query = f"INSERT INTO {'tran_hdr'} VALUES {tuple(line)}"
            # for itr in range(len(data))
            cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()


def daily_task():
    mockCurrentDates()
    append()
    print("Task executed at:", datetime.now())


# Schedule the daily task to run every day at a specific time (adjust time as needed)
# schedule.every().day.at('15:10').do(daily_task)
schedule.every(5).seconds.do(daily_task)

while True:
    schedule.run_pending()
    time.sleep(1)