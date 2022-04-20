from email import header
import os
import csv

# The data we need to retrieve

# Assign a name for the path to the file to load
file_to_load = os.path.join('resources', 'election_results.csv')

# Open the election results, and read the file
# # election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
    
    # Read the file object
    file_reader = csv.reader(election_data)
    
    # Print the header row
    headers = next(file_reader)
    print(headers)
    
    # for row in file_reader:
    #     print(row)

# 1. The total number of votes cast

# 2. Complete list of candidates who received votes

# 3. Total number of votes won by each candidate  # NOTE: #3 and #4 were reversed in the Module, but since percentage is dependant on total…

# 4. Percentage of votes won by each candidate

# 5. Winner of election based on popular vote

# Create a filename name to a direct or indirect path to the file.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Open the analysis file in 'write' mode
with open(file_to_save, 'w') as txt_file:
    
    # Write some data to outfile
    txt_file.write('Counties in Election\n---------------------\nArapahoe\nDenver\nJefferson')

# Close the files
# election_data.close()
# outfile.close()
