#import os and csv tools
import os
import csv


#set data file path
tradeCSV = os.path.join('election_data.csv')
#open data file in location below, read it, store data as csvfile

with open(tradeCSV, "r") as csvfile:
    votecount = 0
    candidates = []
    cand1count = 0
    cand2count = 0
    cand3count = 0
    cand4count = 0
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csv.reader(csvfile):
        votecount = votecount + 1
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == candidates[0]:
           cand1count = cand1count + 1
        elif row[2] == candidates[1]:
           cand2count = cand2count + 1
        elif row[2] == candidates[2]:
           cand3count = cand3count + 1
        elif row[2] == candidates[3]:
           cand4count = cand4count + 1
print("Total votes: " + str(votecount))
print(candidates)

