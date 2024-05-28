
string="ASSORTMENT REESES PIECES,KIT KAT,HERSHEY MINIATURE,REESE PEANUT BUTTER CUPS,C1~1,C2~4,C3~1,C4~2,C5~3,C6~5,C7~10"

def comma_sep(string:str):
    commaIdx=[]
    dataList=[]
    cnt=7
    for i in range(len(string)-1,-1,-1):
        if string[i]=="," and cnt>0:
         commaIdx.append(i)
         cnt-=1
    for idx in range(len(commaIdx)-1):
        print(string[commaIdx[idx+1]+1:commaIdx[idx]])



comma_sep(string)

