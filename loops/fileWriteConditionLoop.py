# write a program to read countryDataSample.csv file
# print Line
# write all alternate lines to another file alternateCountry.csv
# r-- tell python to look at string as raw string
# without analysing special characters
path = r'H:\countrydataSample.csv'
print(path)
pathW = r'H:\alternateCountry.csv'
f = open(pathW,'a')
lineCnt=-1

for line in open(path):
    lineCnt +=1
    if(lineCnt==0):
        continue
    print(line,end="")
    if(lineCnt%2==0):
      f.write(line)

f.close()
