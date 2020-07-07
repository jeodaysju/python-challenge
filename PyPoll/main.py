import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for rows in csvreader:
        # print(rows)
        # election_dict{}
        election_dict = {'voter_id': rows[0],
                    'county': rows[1],
                    'candidate': rows[2]
                    }
        print()
        # election_dict = dict(voter_id = rows[0],
        #             county = rows[1],
        #             candidate = rows[2])

        print(f'{election_dict['county'][20]}')