f#rom msilib.schema import File
import os
import csv
csvpath = os.path.join("..", "Resources", "election_data.csv")
print (election_data.csv)

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    print(csvreader)

    total_votes = 0 
    Charles_votes = 0
    Diana_votes = 0
    Raymon_votes = 0
    candidates = 0
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)
    unique_name1 = []
# Each row is read as a row
    for row in csvreader:
        #print(row)

        #A complete list of candidates who received votes


        #the total number of votes cast
        total_votes +=1

        #The percentage of votes each candidate won
        if row[2] == "Charles":
            Charles_votes +=1
        elif row[2] == "Diana":
            Diana_votes +=1
        elif row[2] == "Raymon":
            Raymon_votes +=1


candidates = ["Charles", "Diana", "Raymon"]
votes = [Charles_votes, Diana_votes, Raymon_votes]

dict_candidatesvotes = dict(zip(candidates,votes))
key = max(dict(dict_candidatesvotes, key=dict_candidatesvotes.get))
candilist = list()
tally = list()
for i in range (0,row_count):
    candidate = data[i][2]
    tally.append(candidate)
if candidate not in candilist: 
    candilist.append(candidate)
    candicount = len(candilist)

  # The total number of votes each candidate won & the percentage of votes each candidate won
    votes = list()
    percentage = list()
    for j in range (0,candicount):
        name = candilist[j]
        votes.append(tally.count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct)

  # The winner of the election based on popular vote.
    winner = votes.index(max(votes))    

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
  # Print the results to terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,candicount): 
        print(f"{candilist[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candilist[winner]}")
    print("----------------------------")

output_file = Path ("..", "Resources", "Analysis.txt")
with open(output_file, "w") as File