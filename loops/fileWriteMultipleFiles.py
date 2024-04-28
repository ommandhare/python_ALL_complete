# write a program to read countryDataSample.csv file
# print Line
# write all alternate lines to another file alternateCountry.csv
# r-- tell python to look at string as raw string
# without analysing special characters

path = r'H:\countrydataSample.csv'
print(path)
pathW_l5 = r'H:\l5_data.csv'
pathW_g5 = r'H:\g5_data.csv'

fl = open(pathW_l5,'a')
fg = open(pathW_g5,'a')

lineCnt=-1
for line in open(path):
    lineCnt +=1
    if(lineCnt==0):
        continue
    print(line,end="")
    if(lineCnt<=5):
        #name = '5l_data.csv'
        fl.write(line)
    else:
        fg.write(line)


fl.close()
fg.close()