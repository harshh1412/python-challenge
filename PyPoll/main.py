import os
import csv

csvfilepath = os.path.join("Resources" , "election_data.csv")

output_file = os.path.join("analysis" , "election_analysis.csv")

with open(csvfilepath) as election_data:

    data_reader = csv.reader(election_data)

    data_header = next(data_reader)

    candidates = {} #this dictionary will hold the candidate names as keys and count the votes in the values
    
    for row in data_reader:

        name = row[2]

        if name in candidates:
            candidates[name] += 1

        else:
            candidates[name] = 1


    print(f"Election Results\n------------------------------------")

    total_votes = sum(candidates.values())

    print(f"Total Votes: {total_votes}\n------------------------------------")

    for key in candidates.keys():
        print(f"{key}: {round(((candidates[key]/total_votes)*100), 3)}% ({candidates[key]})")

    max_votes = max(candidates.values())
        
    for key in candidates.keys():   
        if candidates[key] == max_votes:
            print(f"------------------------------------\nWinner: {key}\n------------------------------------")
    
    
with open (output_file, "w") as data_file:
    writer = csv.writer(data_file, delimiter=':')

    writer.writerow(["Election Results"])
    writer.writerow(["------------------------------------"])
    writer.writerow(["Total Votes"," 369711"])
    writer.writerow(["------------------------------------"])
    writer.writerow(["Charles Casper Stockham"," 23.049% (85213)"])
    writer.writerow(["Diana DeGette"," 73.812% (272892)"])
    writer.writerow(["Raymon Anthony Doane"," 3.139% (11606)"])
    writer.writerow(["------------------------------------"])
    writer.writerow(["Winner"," Diana DeGette"])
    writer.writerow(["------------------------------------"])