# read file country data
# create separate file for each continent.
# each file should have only line related to that continent.

path = r"C:\PythonWork\Data\countrydata.csv"
count=0
continentDict = {}
for line in open(path):
    if(count == 0):
        count +=1
        continue
    print(line,end="")
    countryId, countryName, continent, population, lifeE, gdp = line.strip().split(",")
    if(continent in continentDict):
       lineList = continentDict[continent]
       lineList.append(line)
       continentDict[continent] = lineList
    else:
        lineList = []
        lineList.append(line)
        continentDict[continent] = lineList
print(continentDict)

pathCommon = r"C:\PythonWork\Data\countrydata_CONTINENT.csv"

for c,lineList in continentDict.items():
    pathContinent = pathCommon.replace("CONTINENT",c)
    fp = open(pathContinent,'a')
    for line in lineList:
        fp.write(line)
    fp.close()

print("I DID MY JOB -- GOOD BYE")