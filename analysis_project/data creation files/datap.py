from datetime import(
    datetime as dt,
    date as Date,
    timedelta)
import pandas as pd
from random import randint
import productAmt as pa



# creating two dates
startDate = Date(2021,1,1)
endDate= Date(2024,12,31)


# timedelta between two dates
diff=endDate-startDate



print(diff)

storeIdList=[]
member_idList=[]
productIdList=[]
tranIdList=[]
startDateList=[]
qtyList=[]
amtList=[]

for itr in range(diff.days + 1):
         no = randint(20,40)
         memberlst = []
         for i in range(1,no+1):
             id = randint(1001, 1100)
             if id not in memberlst:
              memberlst.append(id)         #memberList
             storeList=[]
             storeId= randint(1,3)
             if storeId not in storeList:
              storeList.append(storeId)     #StoreList
              qty = randint(1, 5)
              numProduct = randint(1, 10)
              productList = []
             for j in range(1, numProduct + 1):
                productId = randint(1, 100)
                if productId not in productList:
                    productList.append(productId) #productLists
                    if id <= 1010:
                        qty = randint(10, 15)
                    elif id <= 1025:
                        qty = randint(130, 150)
                    elif id <= 1030:
                        qty = randint(4, 9)
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
                        qty=randint(1, 10)
                    productId = str(productId)
                    price = pa.productAmt.get(productId)
                    price = float(price)
                    amt = qty * price               #amt  qty*price
                    amt = round(amt, 2)
                    currentDateTime = dt.now()
                    tranId = startDate.strftime('%Y-%m-%dT') + currentDateTime.strftime('%H-%M-%S-%f') + '_' + str(i)
                    tranIdList.append(tranId)                #tran_id and its format
                    startDateList.append(startDate)
                    member_idList.append(id)                        #memberList
                    storeIdList.append(storeId)
                    productIdList.append(productId)      #productIdList
                    qtyList.append(qty) #qtyList
                    amtList.append(amt)                   #amtlIST

newDate = startDate + timedelta(days=1)




df1 = {'tran_id':tranIdList, 'product_id':productIdList, 'qty':qtyList, 'amt':amtList, 'tran_dt':startDateList}
tran_dtl = pd.DataFrame(df1)
print(tran_dtl)      #LIST TO DATAFRAME

df2 = {'tran_id':tranIdList, 'store_id':storeIdList, 'member_id':member_idList, 'tran_dt':startDateList}
tran_hdr = pd.DataFrame(df2)
tran_hdr = tran_hdr.drop_duplicates()
print(tran_hdr)     #LIST TO DATAFRAME


tran_dtl.to_csv(r"C:\Users\om\PycharmProjects\python_All\analysis_project\data creation files\tran_dtl.csv",index=False)
#DATAFRAME TO csv THROUGH PANDAS
tran_hdr.to_csv(r"C:\Users\om\PycharmProjects\python_All\analysis_project\data creation files\tran_hdr.csv",index=False)

