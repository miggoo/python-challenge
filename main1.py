#import os and csv tools
import os
import csv
#create 2 lists to split data (date and profit/loss)for later
c1 = []
c2 = []
#and one for the combined data
c3 = []
#set column_sum variable (used to calculate total later as zero)
column_sum = 0
#set input_path as budget data file filepth
input_path = os.path.join('budget_data.csv')
#open data file in location below, read it, store data as f
with open(input_path, "r") as f:
# read f as csv file with delimiter , and store that data as reader
    reader = csv.reader(f, delimiter=",")
# skip headers

    next(f)
#populate lists c1 and c2 with headerless values from delimited csv file read by row 
    for row in f:
        c1.append(row[0])
        c2.append(row[1])
#store the number of values in c1 (should be same in c2) as a variable called months
        months = len(c1)
    
#print header
    print("Financial Analysis")
    print(".......................")
#print number of months
    print("Total Months: " + str(months))
    column_sum += float(row[1])
    print("Total $: " + str(column_sum))

