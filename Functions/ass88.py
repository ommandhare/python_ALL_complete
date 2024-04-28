"""

"""
path = r"C:\Users\HP\Desktop\Philomath\python_codes\.venv\Assignments\countrydata.csv"

count = 0

continentDict={}
def find_total_population():
    lineCnt = -1
    for line in open(path):
        lineCnt += 1
        if (lineCnt == 0):
            continue

        id, countryName, continent, population, lifeE, gdp = line.strip().split(",")
        id = int(id)
        population = float(population)
        if(continent in continentDict):
            currentPop = continentDict[continent]
            continentDict[continent] = currentPop + population
        else:
            continentDict[continent] = population
    print("CONTINENT DICT: ",continentDict)


find_total_population()