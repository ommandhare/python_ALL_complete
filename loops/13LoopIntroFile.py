# browse over a file using for loop.
#itemList = ['banana','apple','orange','mango','sitaphal','fanas']

#for s in itemList:
 #   print("MOTHER ASKED TO BRING: ",s)




path = 'H:\countrydataSample.csv'
# open() function reads file and converts it into list of lines
count=0
lineCnt=-1

totalPopulation= 0
avgpopulation=0
for line in open(path):
    lineCnt +=1
    if(lineCnt==0):
        continue
    id,countryName,continent,population,lifeE,gdp = line.strip().split(",")
    population = float(population)
    totalPopulation=totalPopulation+population
    print("LINE:",lineCnt,"--",line,end="") # don't add \n at end


avgpopulation=totalPopulation/lineCnt
print("TOTAL COUNT OF LINES IN FILE IS: ",lineCnt)
print("TOTAL POPULATION: ",totalPopulation)
print("Average population: ",avgpopulation)

"""
  print("LINE: BEGIN:---------------------------------- ")
  if(count==0):
      print("LINE: HEADER LINE SKIPPED")
      print("LINE: END: ----------------------------")
      count +=1
      continue
  print("LINE: ",line)
  print("LINE: END: ----------------------------")
  """