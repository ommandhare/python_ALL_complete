# Retail Data Report
#  transaction tran_dtl,tran_hdr

from datetime import(
    datetime as dt,
    date,
    timedelta)
from random import randint
import pandas as pd
import productAmt as pa
from sqlalchemy import create_engine

begin = date(2021,1,1)
end = date(2024,7,23)

DATABASE_URI = 'mysql+pymysql://root:0777@localhost:3306/retail_project'
engine = create_engine(DATABASE_URI)

def mockBetweenDates(startDate, endDate):
    difference = endDate-startDate # difference between start and end date
    # print(difference.days)
    tranIdLst = []
    startDateLst = []
    idLst = []
    storeIdLst = []
    productIdLst = []
    qtyLst = []
    amtLst = []

    for itr in range(difference.days + 1):
        trans = randint(1,50) #no of transactions done in a day
        # print(no)
        memberlst = []
        for i in range(1,trans+1):
            id = randint(1001,1100) # creating member id
            if id not in memberlst:
                memberlst.append(id)
                storeLst = []
                storeId = randint(1,3) # creating store id
                if storeId not in storeLst:
                    storeLst.append(storeId)
                    numProduct = randint(1,10) # no of products purchased in store
                    productLst = []
                    for j in range(1,numProduct+1):
                        productId = randint(1,100) # creating product id 
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
                                qty = randint(1, 10)# qty for each product id
                            productId = str(productId)
                            price = pa.productAmt.get(productId) #retrieve value from productAmt dictionary
                            price = float(price)
                            amt = qty * price # calculating total amt
                            amt = round(amt, 2)
                            currentDateTime = dt.now()
                            tranId = startDate.strftime('%Y-%m-%dT') + currentDateTime.strftime('%H-%M-%S-%f') + '_' + str(i)
                            tranIdLst.append(tranId)
                            startDateLst.append(startDate)
                            idLst.append(id)
                            storeIdLst.append(storeId)
                            productIdLst.append(productId)
                            qtyLst.append(qty)
                            amtLst.append(amt)
                            # print(tranId,'_',startDate,'_',id,'_',storeId,'_',productId,'_',qty,'_',amt)
        newDate = startDate + timedelta(days=1)
        startDate = newDate

    df1 = {'tran_id':tranIdLst, 'product_id':productIdLst, 'qty':qtyLst, 'amt':amtLst, 'tran_dt':startDateLst}
    tran_dtl = pd.DataFrame(df1)
    tran_dtl['tran_dt'] = pd.to_datetime(tran_dtl['tran_dt'])
    print(tran_dtl)
    tran_dtl.to_sql('tran_dtl', engine, if_exists='append', index=False)
    print("tran_dtl to SQL......")


    df2 = {'tran_id':tranIdLst, 'store_id':storeIdLst, 'member_id': idLst, 'tran_dt':startDateLst}
    tran_hdr = pd.DataFrame(df2)
    tran_hdr = tran_hdr.drop_duplicates()

    tran_hdr['tran_dt'] = pd.to_datetime(tran_hdr['tran_dt'])
    print(tran_hdr)
    tran_hdr.to_sql('tran_hdr', engine, if_exists='append', index=False)
    print("tran_hdr to SQL......")
    return







mockBetweenDates(begin, end)
