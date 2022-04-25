# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Dependencies.
import os
import csv

# Add a name to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Add a name to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidates = []         # will contain `str candidate` elements
candidate_votes = {}    # will contain `str candidate`:`int votes` elements

# 1: Create a county list and county votes dictionary.
counties = []       # will contain `str county` elements
county_votes = {}   # will contain `str county`:`int votes` elements

# Track the winning candidate, vote count and percentage
winner = {'name':'nobody','votes':0,'percentage':float(0)}

# 2: Track the largest county and county voter turnout.
top_county = {'name':'none','votes':0,'percentage':float(0)}

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes += 1

        # Get the candidate name from each row.
        candidate = row[2]

        # 3: Extract the county name from each row.
        county = row[1]

        # If the candidate does not match any existing candidate
        # add it to the candidate list
        if candidate not in candidates:

            # Add the candidate name to the candidate list.
            candidates.append(candidate)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county not in counties:

            # 4b: Add the existing county to the list of counties.
            counties.append(county)

            # 4c: Begin tracking the county's vote count.
            county_votes[county] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county] += 1

# Sort the lists of candidates and counties
candidates.sort()
counties.sort()

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"Election Results"
        f"\n-------------------------"
        f"\nTotal Votes: {total_votes:,}"
        f"\n-------------------------"
        f"\n\nCounty Votes:"
        f"\n-------------------------"
    )
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in counties:

        # 6b: Retrieve the county vote count.
        votes = county_votes.get(county)

        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100

        county_results = (
            f"\n{county}: {vote_percentage:.1f}% ({votes:,})")

         # 6d: Print the county results to the terminal.
        print(county_results,end="")

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (top_county["votes"] < votes):
            top_county["votes"] = votes
            top_county["name"] = county

    # Calculate the top county's vote percentage
    top_county["percentage"] = float(top_county["votes"]) / float(total_votes) * 100

    # 7: Print the county with the largest turnout to the terminal.
    top_county_summary = (
        f"\n-------------------------"
        f"\nHighest County Turnout: {top_county['name']}"
        f"\nTurnout: {top_county['votes']:,}"
        f"\nTurnout Percentage: {top_county['percentage']:.1f}%"
        f"\n-------------------------"
        f"\n\nCandidate Votes:"
        f"\n-------------------------"
    )
    print(top_county_summary, end="")

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(top_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate in candidates:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"\n{candidate}: {vote_percentage:.1f}% ({votes:,})")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results, end = "")

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning candidate and vote count.
        if (winner["votes"] < votes): # and (winning_percentage < vote_percentage):
            winner["votes"] = votes
            winner["name"] = candidate

    # Calculate the winner's vote percentage
    winner["percentage"] = float(winner["votes"]) / float(total_votes) * 100

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"\n-------------------------"
        f"\nWinner: {winner['name']}"
        f"\nWinning Vote Count: {winner['votes']:,}"
        f"\nWinning Percentage: {winner['percentage']:.1f}%"
        f"\n-------------------------"
    )
    print(winning_candidate_summary, end = "")

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
