# Election Analysis

## Overview of Election Audit
A Colorado Board of Elections employee requests the following information for a recent congressional election:

## General information
1. The total number of votes cast

## Information about voter turnout
2. Voter turnout for each county
3. Each county's percentage of votes (out of the total count)
4. The county with the highest turnout

## Information about votes cast for candidates
5. The list of candidates who received votes
6. The total number of votes cast for each candidate
7. Each candidate's percentage of votes
8. The winner of the election based on popular vote

## Resources
- Software:
  - Python 3.10.4
  - Visual Studio Code Version: 1.66.2
- Data Source: election_results.csv

## Election-Audit Results
Election Analysis shows that:
- There were 369,711 votes cast in the election.

### Voter Turnout Results
The voter turnout results were:
- Arapahoe County: 24,801 votes, 6.7% of the total
- Denver County: 306,055 votes, 82.8% of the total
- Jefferson County: 38,855 votes, 10.5% of the total

**Denver County** had the highest voter turnout in the election with 306,055 votes, comprising 82.8% of the total votes cast.

### Candidates Results
The candidates' results were:
- Charles Casper Stockham: 85,213 votes, 23.0% of the total
- Diana DeGette: 272,892 votes, 73.8% of the total
- Raymon Anthony Doane: 11,606 votes, 3.1% of the total

The winner of the election was **Diana DeGette** with 272,892 votes, comprising 73.8% of the total votes cast.

## Election-Audit Summary
Results from this script are obtained simply by reading each line of the election data file and tallying a vote for each category that the row matches. (For this election, the categories were county and candidate.)

### Modifying the Code for Other Elections
Modifying the code for other elections is a fairly simple process (provided the results are stored in a comma-separated values—a.k.a. CSV—file).

---
#### What If Voters Are Only Allowed to Vote for Approved Candidates?
One restriction that might come up is that, in some elections, a candidate has to be "on the ballot" in order for a vote cast for a candidate to count. Changing the code to accommodate this circumstance is fairly simple.

Suppose, for example, that voters can only vote for Alice, Bob, or Clara.

We start by including the approved candidates in the candidates list right from the start. We're also going to include a "none of the above" option for voters who don't want to cast a vote for any of the approved candidates.

##### The Code
The current code initializes a candidate list on line 17 with the instruction `candidates = []`. We create an "approved" list of candidates by inserting a (quoted) list of the candidates names inside the brackets of that instruction, like so: `candidates = ["Alice","Bob","Clara","none of the above"]`.

We then have to change one other section of code to accommodate our new, approved-candidate requirement.

Currently, lines 49–57 of the code check to see if a ballot shows a candidate we haven't seen before. If so, it adds it to the candidates list, and then tallys a vote for the candidate:
```
        # If the candidate does not match any existing candidate
        # add it to the candidate list
        if candidate not in candidates:

            # Add the candidate name to the candidate list.
            candidates.append(candidate)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate] += 1
```
What we do next depends on how the votes come in:
1. If the CSV can contain *only* approved candidates (including 'none of the above'), then remove the entire `if` block, leaving only the `candidate_votes[candidate] += 1` instruction.

2. If the CSV can contain other candidate values, then we need to convert all non-approved votes into votes for 'none of the above', and the code should look like:
```
        if candidate not in candidates:
            # Convert the non-approved vote into one for 'none of the above'
            candidate = 'none of the above'
        # Add a vote to that candidate's count
        candidate_votes[candidate] += 1
```
The rest of the code should work without modification.

---
#### What If The Election Still Has Two Categories, but the Categories Are Different?
For this election, the source data in the `election_results.csv` file contained the following categories:
```
Ballot ID,County,Candidate
```
These appear in the header (the first line) of the file.

If another election has different categories, they should appear in the header for that elections `election_results.csv` file.

As far as the code is concerned, though, these categories are just "indexed values" in the CSV's row data. For this election, Ballot ID is at index 0, County is at index 1, and Candidate is at index 2.

Even if another election has different categories, though, it will still have its values indexed at 0, 1, and 2.

##### The Code
For this election's code, we first see the categories referenced in lines 16–28:
```
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
```
and then again in lines 44 and 47:
```
candidate = row[2]
…
county = row[1]
```
All the labels to the left of the equals signs in the code, above, are arbitrary variable names. They can either remain, as-is, or they can be globally replaced throughout the code with something that conforms to the new elections's categories. For example, you might replace `counties`, `county_votes`, `top_county`, and `county` with `precincts`, `precinct_votes`, `top_precinct`, and `precinct`, respectively. (You could do similarly for all the candidate-related labels.)

The only thing left to do, after that, is to change the output text to reflect the new categories.

The output text appears on lines 82–90:
```
    # Print the final vote count (to terminal)
    election_results = (
        f"Election Results"
        f"\n-------------------------"
        f"\nTotal Votes: {total_votes:,}"
        f"\n-------------------------"
        f"\n\nCounty Votes:"
        f"\n-------------------------"
    )
```
On lines 121–130:
```
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
```
And on lines 160–167:
```
    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"\n-------------------------"
        f"\nWinner: {winner['name']}"
        f"\nWinning Vote Count: {winner['votes']:,}"
        f"\nWinning Percentage: {winner['percentage']:.1f}%"
        f"\n-------------------------"
    )
```

How, exactly, the text changes will depend on what the specific categories are in this hypothetical election.

---
#### What if the Election Has More Than Two Categories?
##### Assigning the Indexed Categories to Variables
Suppose our election also includes a "Proposition" category whose value follows the votes for Candidate (at index 2) in our CSV. That means County is at index 1, Candidate is at index 2, and Proposition (the new category) is at index 3.

##### The Code
The current code references the first two categories by index on lines 44 and 47:
```
candidate = row[2]
…
county = row[1]
```
Proposition is at index 3, and so we would prepare to tally votes for the proposition by putting something like `prop_response = row[3]` into our code in the same section.

##### Preparing to Count
We need to be able to store the results for each of our categories. In the existing code, this occurs in lines 16–28, as seen below (with comments altered for this context):
```
candidates = []         # Will hold a list of candidates that received votes
candidate_votes = {}    # Will hold each candidate's vote count

counties = []           # Will hold a list of counties that received votes
county_votes = {}       # Will hold each county's vote count

# Hold relevant parameters for each winning category
winner = {'name':'nobody','votes':0,'percentage':float(0)}
top_county = {'name':'none','votes':0,'percentage':float(0)}
```
Adding another category (ex.: Proposition) is simply a matter of adding variables in the same manner as above. For example:
```
candidates = []         # Will hold a list of candidates that received votes
candidate_votes = {}    # Will hold each candidate's vote count

counties = []           # Will hold a list of counties that received votes
county_votes = {}       # Will hold each county's vote count

prop_values = []        # Will hold a list of responses to the proposition vote
prop_votes = {}         # Will hold each response's vote count

# Hold relevant parameters for each winning category
winner = {'name':'nobody','votes':0,'percentage':float(0)}
top_county = {'name':'none','votes':0,'percentage':float(0)}
top_prop_response = {'response':'abstain','votes':0,'percentage':float(0)}
```

We then need to prepare the code to count our additional category.

The code to count the County votes is on lines 95–119, and includes the calculation for the county with the most votes:
```
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
```
The code to count the Candidate votes is on lines 136–158, and is nearly-identical; only the variable names have been changed.

We can count a third category by using the same code, again. For our Proposition example, we could add:
```
    # Get the proposition responses from the list of proposition values.
    for prop_response in prop_values:

        # Retrieve the response's vote count.
        votes = prop_values.get(prop_response)

        # Calculate the percentage of votes for the response.
        vote_percentage = float(votes) / float(total_votes) * 100

        prop_response_results = (
            f"\n{prop_response}: {vote_percentage:.1f}% ({votes:,})")

        # Print the results to the terminal.
        print(prop_response_results,end="")

        # Save the results to a text file.
        txt_file.write(prop_response_results)

        # Determine the winning response and get its vote count.
        if (top_prop_response["votes"] < votes):
            top_prop_response["votes"] = votes
            top_prop_response["response"] = prop_response

    # Calculate the top county's vote percentage
    top_county["percentage"] = float(top_county["votes"]) / float(total_votes) * 100
```

Finally, we need to change the boilerplate text that appears before and after the individual results. This was addressed, above, in the section on *What If The Election Still Has Two Categories, but the Categories are Different?*. Changing the boilerplate text, here, is no different, except that we once again have replicate a code block at the end to summarize our new category's data (but, again, it's just re-using code with some of the labels changed).

---
### Conclusion
This vote-counting solution is fast, and its code should be flexible enough to account for different elections' formats with only minor adjustments.