import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

# files to load and output
file_to_output = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidates = {}

# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    for row in csvreader:
        # calc total votes
        total_votes = total_votes + 1

        name = row[2]

        if name not in candidates:
            candidates[name] = 1
        else:
            candidates[name] = candidates[name] + 1

# print(total_votes)
output_str=''
winner = 0
for candidate_name, vote_count in candidates.items():
    if vote_count > winner:
        winner = vote_count
        can_winner = candidate_name
        # print(f"Winner: {can_winner}")
    percent = round((vote_count/total_votes)*100,3)
    output_str += f"{candidate_name}: {percent}% ({vote_count})\n"
output_str = f'Election Results\n----------------------\nTotal Votes: {total_votes}\n---------------------- \n'+ output_str + f'---------------------- \nWinner: {can_winner} \n'
print(output_str)

file1 = open(file_to_output,"w") 

file1.writelines(output_str) 
file1.close() #to change file access modes 