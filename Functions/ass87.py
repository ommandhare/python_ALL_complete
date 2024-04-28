"""
read the file country data and find total population for continent using list and function


"""

path = r"C:\Users\HP\Desktop\Philomath\python_codes\.venv\Assignments\countrydata.csv"
count = 0
lineCnt = -1
lineList = []
continentlist = []


def find_total():
    lineCnt = -1
    for line in open(path):
        lineCnt += 1
        if (lineCnt == 0):
            continue


        id, countryName, continent, population, lifeE, gdp = line.strip().split(",")
        id = int(id)
        population = float(population)
        lst = [id,countryName,continent,population]
        lineList.append(lst)

        if (continent in continentlist):
           continue
        else:
            continentlist.append(continent)


    for cont in continentlist:
        totalPopulation = 0
        for rec in lineList:
            if(cont == rec[2]):
                totalPopulation=totalPopulation+rec[3]
        print("CONTINENT: ",cont," TOTAL POPULATION: ",totalPopulation)


find_total()