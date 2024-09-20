# Retail Data
#  transaction tran_dtl,tran_hdr  DAILY


from datetime import (
    datetime as dt,
    date,
    timedelta)
from random import randint
import pandas as pd
import productAmt as pa
from sqlalchemy import create_engine

pd.set_option('display.max_rows', None)

DATABASE_URI = 'mysql+pymysql://root:0777@localhost:3306/retail_project'
engine = create_engine(DATABASE_URI)

max_date = pd.read_sql_query("Select max(tran_dt) from tran_dtl", engine)
max_date = max_date['max(tran_dt)'].iloc[0]
last_date = max_date+timedelta(days=1)
print(last_date, type(last_date))
today = dt.today().date()
print(today, type(today))


def mockCurrentDates(last_date, today):
    tranIdLst = []
    startDateLst = []
    idLst = []
    storeIdLst = []
    productIdLst = []
    qtyLst = []
    amtLst = []

    while last_date <= today:
        for itr in range(1):
            trans = randint(10, 15)  # no of transactions done in a day
            # print(no)
            memberlst = []
            for i in range(1, trans + 1):
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
                                if (id <= 1020):
                                    qty = randint(1600, 2000)
                                elif id <= 1025:
                                    qty = randint(500, 600)
                                elif id <= 1030:
                                    qty = randint(150, 200)
                                elif id <= 1035:
                                    qty = randint(210, 240)
                                elif id <= 1035:
                                    qty = randint(15, 18)
                                elif id <= 1040:
                                    qty = randint(15, 80)
                                elif id <= 1050:
                                    qty = randint(110, 150)
                                elif id <= 1060:
                                    qty = randint(30, 140)
                                elif id <= 1070:
                                    qty = randint(10, 14)
                                elif id <= 1075:
                                    qty = randint(185, 200)
                                elif id <= 1078:
                                    qty = randint(210, 240)
                                elif id <= 1080:
                                    qty = randint(1, 5)
                                else:
                                    qty = randint(1, 10)  # qty for each product id
                                productId = str(productId)
                                price = pa.productAmt.get(productId)  # retrieve value from productAmt dictionary
                                price = float(price)
                                amt = qty * price  # calculating total amt
                                amt = round(amt, 2)
                                currentDateTime = last_date
                                tranId = currentDateTime.strftime('%Y-%m-%dT') + today.strftime(
                                    '%H-%M-%S-%f') + '_' + str(i)
                                # print(tranId)
                                tranIdLst.append(tranId)
                                startDateLst.append(currentDateTime.strftime('%Y-%m-%d'))
                                idLst.append(id)
                                storeIdLst.append(storeId)
                                productIdLst.append(productId)
                                qtyLst.append(qty)
                                amtLst.append(amt)

        last_date = last_date + timedelta(days=1)
    df1 = {'tran_id': tranIdLst, 'product_id': productIdLst, 'qty': qtyLst, 'amt': amtLst, 'tran_dt': startDateLst}
    tran_dtl = pd.DataFrame(df1)
    tran_dtl['tran_dt'] = pd.to_datetime(tran_dtl['tran_dt'])
    print(tran_dtl)

    # it will append to SQL DB and make CSV
    tran_dtl.to_sql('tran_dtl', engine, if_exists='append', index=False)
    print("tran_dtl to SQL......")

    df2 = {'tran_id': tranIdLst, 'store_id': storeIdLst, 'member_id': idLst, 'tran_dt': startDateLst}
    tran_hdr = pd.DataFrame(df2)
    tran_hdr = tran_hdr.drop_duplicates()
    tran_hdr['tran_dt'] = pd.to_datetime(tran_hdr['tran_dt'])
    print(tran_hdr)

    # it will append to SQL DB and make CSV
    tran_hdr.to_sql('tran_hdr', engine, if_exists='append', index=False)
    print("tran_hdr to SQL......")

    return


mockCurrentDates(last_date, today)
