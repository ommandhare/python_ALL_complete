# Clustering Algorithm

## Loading Data in sql:
### sqlLoading.py
 This is so it can help in viewing data and sometime
extracting specific data to do operation.

    step 1: Extract only intern descpriction to clean description.
#### desc_data_raw.csv

## Clean Describtion :
### cleanDesc.py
 This is so that we can seprate alpha-numeric words .
It will help when finding similer data and also decrease
size of data extarxted from next step

    step 2: Clean Description data.
#### cleanDesc.csv

## Category Data from sql:
### manual extraction
 Here we extract all the remaining data of category 
from sql.

    step 3: Extract category data from sql.
#### category_raw.csv

## Joining Data
### cleanData.py
 Here we join cleaned Description and 
extracted categories to create cleaned 
data.

    step 4: Join cleaned desc and category .
#### cleanData.csv

## Generating word Id's
### genId.py
 Here we count repeation of word in file and 
assigne a numeric id to word based of occurance 
of word in file. (word,word Id,Count)

    step 5: Generate Id's for words.
#### wordId.csv







