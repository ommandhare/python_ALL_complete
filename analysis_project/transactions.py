# Retail Data Report
#  transaction

from datetime import(
    datetime as dt,
    date,
    time,
    timedelta)
from random import randint
import productAmt as pa
import pandas as pd

startDate = date(2021,3,20)
endDate = date(2024,3,20)
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
    no = randint(1,50) #no of transactions done in a day
    # print(no)
    memberlst = []
    for i in range(1,no+1):
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
                        if id <= 1010:
                            qty = randint(1,5)
                        elif id <= 1025:
                            qty = randint(250,300)
                        elif id <= 1030:
                            qty = randint(4,9)
                        elif id <= 1035:
                            qty = randint(1,20)
                        elif id <= 1035:
                            qty = randint(15,18)
                        elif id <= 1040:
                            qty = randint(15,80)
                        elif id <= 1050:
                            qty = randint(11,20)
                        elif id <= 1060:
                            qty = randint(1,4)
                        elif id <= 1065:
                            qty = randint(150,200)
                        elif id <= 1070:
                            qty = randint(1,5)
                        elif id <= 1075:
                            qty = randint(1,10)
                        elif id <= 1078:
                            qty = randint(200,350)
                        elif id <= 1080:
                            qty = randint(1,5)
                        elif id <= 1090:
                            qty = randint(1,100)
                        elif id <= 1095:
                            qty = randint(150,250)
                        else:
                            qty = randint(1,3) # qty for each product id
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
tran_dtl.to_csv(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_dtl.csv",index=False)

df2 = {'tran_id':tranIdLst, 'store_id':storeIdLst, 'member_id': idLst, 'tran_dt':startDateLst}
tran_hdr = pd.DataFrame(df2)
tran_hdr = tran_hdr.drop_duplicates()
tran_hdr['tran_dt'] = pd.to_datetime(tran_hdr['tran_dt'])
print(tran_hdr)

tran_hdr.to_csv(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_hdr.csv",index=False)
