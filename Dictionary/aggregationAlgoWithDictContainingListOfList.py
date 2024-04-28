path = 'H:\countrydataSample.csv'
# open() function reads file and converts it into list of lines
count = 0
lineCnt = -1
continentDict={}

# listOfLines = ["i am mandar kale","i live in satara","satara is my birthplace"]
for line in open(path):
    lineCnt += 1
    if (lineCnt == 0):
        continue
    print(line, end="")
    # a,b=b,a
    # [[11,"Afganistan","Asia",3188888],[23,"Albania","Europe",3600]]
    #lineLst = line.strip().split(",")
    # idx 0 - id

    id, countryName, continent, population, lifeE, gdp = line.strip().split(",")
    id = int(id)
    population = float(population)
    if(continent not in continentDict):
        countryList = []
        countryAttrib = [countryName,population]
        countryList.append(countryAttrib)
        continentDict[continent] = countryList
    else:
        countryList = continentDict[continent]
        countryAttrib = [countryName,population]
        countryList.append(countryAttrib)
        continentDict[continent] = countryList



print("CONTINENT DICT: ",continentDict)