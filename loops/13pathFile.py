# browse over a file using for loop.
path = 'H:\countrydataSample.csv'
# open() function reads file and converts it into list of lines
for line in open(path):
    print(line)



