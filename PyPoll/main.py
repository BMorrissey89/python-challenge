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
        index = candidates.index(row[2])

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

#Winning candidate
winning_candidate = max(total_votes)
index = total_votes.index(winning_candidate)
winner = candidates[index]

print("Election Results")
print("--------------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------------")
print(f"Charles Casper Stockham: {Charles_votes_percent}% ({len(Charles_votes)})")
print(f"Diana DeGette: {Diana_votes_percent}% ({len(Diana_votes)})")
print(f"Raymon Anthony Doane: {Raymon_votes_percent}% ({len(Raymon_votes)})")
print("--------------------------------")
print(f"Winner: {winner})")

