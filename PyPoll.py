# Import dependencies
import os
import csv

# Retrieve data

# Assign a name for the path to the file to load
file_to_load = os.path.join('resources', 'election_results.csv')

# Initialize vote counter, candidates list, and vote-count dictionary
total_votes = 0
candidate_options = []
candidate_votes = {'winner':{'name':'nobody','votes':0}}  # Include a 'winner' key whose value will hold the name and votes of the eventual winner

# Open the election results, and read the file
# # election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
    
    # Read the file object
    file_reader = csv.reader(election_data)
    
    # Read the header row
    headers = next(file_reader)
    
    # Loop through each row in the CSV file
    for row in file_reader:
    
        # 1. Count the total number of votes cast
        total_votes += 1

        # 2. Create list of candidates who received votes
        if row[2] not in candidate_options:     # If the candidate (candidates' names are at index 2) on the current row is new to the list, then
            candidate_options.append(row[2])    # add the candidate's name to the list,
            candidate_votes[row[2]] = 0         # and create a vote counter for the candidate
        
        # 3. Count the votes for the current row's candidate
        candidate_votes[row[2]] += 1

# Print the results
# print(f'\nTotal Votes Cast: {total_votes:,}')   # total number of votes
# candidate_options.sort()                        # Sort the candidate list
# print('\nCandidates:')
# for candidate in candidate_options:             # List each candidate, along with candidate's vote count and vote proportion (%)
#     print(f'{candidate}: {candidate_votes[candidate]:,} votes, {100 * candidate_votes[candidate] / total_votes:.1f}% of total')
#     if candidate_votes['winner']['votes'] < candidate_votes[candidate]: # If the candidate has more votes than the current 'winner', then
#         candidate_votes['winner']['name'] = candidate                   # set the potential winner's name to the current candidate's,
#         candidate_votes['winner']['votes'] = candidate_votes[candidate] # and record the candidate's vote count
# print(f"\nWinner: {candidate_votes['winner']['name']}!\n")

# Create a filename name to a direct or indirect path to the file.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Open the analysis file in 'write' mode
with open(file_to_save, 'w') as txt_file:
    
    # Collate the results
    election_results = (
        f"Election Results"
        f"\n-------------------------"
        f"\nTotal Votes Cast: {total_votes:,}"  # total number of votes
        f"\n-------------------------"
    )
    # print(election_results, end="")
    
    # Save the final vote count to output file
    txt_file.write(election_results)
    
    for candidate in candidate_options:             # List each candidate, along with candidate's vote count and vote proportion (%)
        candidate_results = f'\n{candidate}: {candidate_votes[candidate]:,} votes, {100 * candidate_votes[candidate] / total_votes:.1f}% of total'
        txt_file.write(candidate_results)
        if candidate_votes['winner']['votes'] < candidate_votes[candidate]: # If the candidate has more votes than the current 'winner', then
            candidate_votes['winner']['name'] = candidate                   # set the potential winner's name to the current candidate's,
            candidate_votes['winner']['votes'] = candidate_votes[candidate] # and record the candidate's vote count
    txt_file.write(f"\n-------------------------\nWinner: {candidate_votes['winner']['name']}!")

# Close the files
# election_data.close()
# outfile.close()
