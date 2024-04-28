path = 'H:\countrydataSample.csv'
# open() function reads file and converts it into list of lines
count = 0
lineCnt = -1
lineList = []
continentList = ["Asia","Europe","Africa"]
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
    lst = [id,countryName,continent,population]
    lineList.append(lst)

print(lineList)

for cont in continentList:
    totalPopulation = 0
    for rec in lineList:
        if(cont == rec[2]):
            totalPopulation=totalPopulation+rec[3]
    print("CONTINENT: ",cont," TOTAL POPULATION: ",totalPopulation)
