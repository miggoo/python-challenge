#import os and csv tools
import os
import csv


#set data file path
tradeCSV = os.path.join('budget_data.csv')
#open data file in location below, read it, store data as csvfile

with open(tradeCSV, "r") as csvfile:
    c1 = []
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csv.reader(csvfile):

                c1.append(row[1])

    months = len(c1)
    print("Financial Analysis")
    print(".............")
    print("Total months: " + str(months))

    total = 0
    total = sum(int(r[1]) for r in csv.reader(csvfile))
     
    print("Total $: " + str(total))

with open(tradeCSV, "r") as csvfile:
 
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    c2 = []
    for x, y in zip(c1, c1[1:]):
        print (x, y)

        c2.append(int(x) - int(y))
        
    totalchange = sum(c2)
    average = totalchange / months
    print(average)
      #  print("Monthy Average = " + str(monthlyaverage))
   
