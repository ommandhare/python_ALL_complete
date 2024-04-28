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

    tranIdLst = []
    startDateLst = []
    idLst = []
    storeIdLst = []
    productIdLst = []
    qtyLst = []
    amtLst = []

    for itr in range(1):
        no = randint(1, 50)  # no of transactions done in a day
        # print(no)
        memberlst = []
        for i in range(1, no + 1):
            id = randint(1001, 1100)  # creating member id
            if id not in memberlst:
                memberlst.append(id)
                storeLst = []
                storeId = randint(1, 3)  # creating store id
                if storeId not in storeLst:
                    storeLst.append(storeId)
                    numProduct = randint(1, 10)  # no of products purchased in store
                    productLst = []
                    for j in range(1, numProduct + 1):
                        productId = randint(1, 100)  # creating product id
                        if productId not in productLst:
                            productLst.append(productId)
                            qty = randint(1, 5)  # qty for each product id
                            productId = str(productId)
                            price = pa.productAmt.get(productId)  # retrieve value from productAmt dictionary
                            price = float(price)
                            amt = qty * price  # calculating total amt
                            amt = round(amt, 2)
                            currentDateTime = dt.now()
                            tranId = currentDateTime.strftime('%Y-%m-%dT') + currentDateTime.strftime('%H-%M-%S-%f') + '_' + str(i)
                            tranIdLst.append(tranId)
                            startDateLst.append(currentDateTime.strftime('%Y-%m-%d'))
                            idLst.append(id)
                            storeIdLst.append(storeId)
                            productIdLst.append(productId)
                            qtyLst.append(qty)
                            amtLst.append(amt)
                            # print(tranId,'',startDate,'',id,'',storeId,'',productId,'',qty,'',amt)

    df1 = {'tran_id': tranIdLst, 'product_id': productIdLst, 'qty': qtyLst, 'amt': amtLst, 'tran_dt': startDateLst}
    tran_dtl = pd.DataFrame(df1)
    tran_dtl['tran_dt'] = pd.to_datetime(tran_dtl['tran_dt'])
    print(tran_dtl)
    tran_dtl.to_csv(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_dtl_daily.csv", index=False,
                    header=False)
    
    df2 = {'tran_id': tranIdLst, 'store_id': storeIdLst, 'member_id': idLst, 'tran_dt': startDateLst}
    tran_hdr = pd.DataFrame(df2)
    tran_hdr = tran_hdr.drop_duplicates()
    tran_hdr['tran_dt'] = pd.to_datetime(tran_hdr['tran_dt'])
    print(tran_hdr)
    tran_hdr.to_csv(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_hdr_daily.csv", index=False,
                    header=False)
    return


def append():
    import pandas as pd
    import mysql.connector
    import csv

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='0777',
        database='retail_project'
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



mockCurrentDates()
append()
print("Task executed at:", datetime.now())


# daily_task()

# Schedule the daily task to run every day at a specific time (adjust time as needed)
# schedule.every().day.at('12:00').do(daily_task)
# schedule.every(40).seconds.do(daily_task)
#
# while True:
#    schedule.run_pending()
#    time.sleep(1)