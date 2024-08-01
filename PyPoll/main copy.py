import os
import csv

election_data = os.path.join("Resources","election_data.csv")

total_votes = []
candidates = []
Charles_votes = []
Diana_votes = []
Raymon_votes = []

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

#Total Votes   
    for row in csvreader:
        total_votes.append(row[2])

#Charles Votes
    for votes in total_votes:
        if votes == "Charles Casper Stockham":
            Charles_votes.append(votes)

#Diana Votes
    for votes in total_votes:
        if votes == "Diana DeGette":
            Diana_votes.append(votes)           

#Raymon Votes
    for votes in total_votes:
        if votes == "Raymon Anthony Doane":
            Raymon_votes.append(votes)  

#The percentage of votes each candidate won
Charles_votes_percent = round((len(Charles_votes)/len(total_votes))*100 ,3)
Diana_votes_percent = round((len(Diana_votes)/len(total_votes))*100 ,3)
Raymon_votes_percent = round((len(Raymon_votes)/len(total_votes))*100 ,3)

print("Election Results")
print("--------------------------------")
print(f"Total Votes: {len(total_votes)}")
print("--------------------------------")
print(f"Charles Casper Stockham: {Charles_votes_percent}% ({len(Charles_votes)})")
print(f"Diana DeGette: {Diana_votes_percent}% ({len(Diana_votes)})")
print(f"Raymon Anthony Doane: {Raymon_votes_percent}% ({len(Raymon_votes)})")
print("--------------------------------")


output = os.path.join("Analysis", "PyPoll_Analysis.txt")

with open(output, "w") as datafile:
    datafile.write(f"Election Results\n")
    datafile.write(f"----------------------------\n")
    datafile.write(f"Total Votes: {len(total_votes)}\n")
    datafile.write(f"----------------------------\n")
    datafile.write(f"Charles Casper Stockham: {Charles_votes_percent}% ({len(Charles_votes)})\n")
    datafile.write(f"Diana DeGette: {Diana_votes_percent}% ({len(Diana_votes)})\n")
    datafile.write(f"Raymon Anthony Doane: {Raymon_votes_percent}% ({len(Raymon_votes)})\n")
    datafile.write(f"----------------------------\n")
