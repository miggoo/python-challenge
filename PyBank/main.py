import os
import csv

#open data file in location below, read it, store data as f
with open('budget_data.csv', "r") as reader:
# read f as csv file with delimiter , and store that data as reader
    reader = csv.reader(reader, delimiter=",")
#skip header

header = next(reader)
# create a list from that delimited file and store it as data. count rows
header = next(reader)

data = list(reader)

row_count = len(data)
    
#print output etc
print("Financial Analysis")
print(".......................")
print("Total Months: " + str(row_count))

with open('budget_data.csv', "r") as f:
    total = 0
for row in data:
    total += int(row[1])
   # possibly do other things with data/rows
print(total)


   
