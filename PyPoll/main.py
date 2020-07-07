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

print(total_votes)

for candidate_name, vote_count in candidates.items():
    percent = round((vote_count/total_votes)*100,3)
    print(f"{candidate_name}: {percent}% ({vote_count})")

