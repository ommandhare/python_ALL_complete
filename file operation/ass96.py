"""
read file country data and calculate average population by continent

"""
path = r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\data\countrydata.csv'

count = 0
lineCnt = -1
continentDict={}


for line in open(path):
    lineCnt += 1
    if (lineCnt == 0):
        continue
    # print(line, end="")


    id, countryName, continent, population, lifeE, gdp = line.strip().split(",")
    id = int(id)
    population = float(population)
    contCount=0
    if(continent not in continentDict):
        contCount=0
        continentDict[continent] = population
    else:
        totalPopulation= continentDict[continent]
        contCount+=1
        continentDict[continent] = totalPopulation + population
        continentDict[continent]= totalPopulation/contCount

print(continentDict)