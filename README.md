# Election Analysis

## Project Overview
The Colorado Board of Elections has issued the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate the total number of votes cast in each county.
7. Calculate the percentage of votes cast in each county.
8. Determine which county had the largest turnout.

The purpose of the audit is to determine which candidates received what quantity of votes, and which candidate won the election, as well as how many votes were cast in each county, and which county had the largest number of votes cast. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code 1.70.2

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was:
    - Diana DeGette: 73.8% (272,892)
- The county results were:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
- The county with the largest voter turnout was:
    - Denver
    
## Challenge Overview
To accomplish the tasks necessary to complete the election audit a Python script was written in Visual Studio Code. First, code needed to be written that would access and read the election data sent from the Colorado Board of elections. This data is held in a CSV file titled `election_results.csv`.
To open and read this file dependencies that hold the necessary functions are imported. A variable is established to hold the path for the file. Then the necessary functions to open and read the file are called. The path to open the text file necessary for saving the final results is also established.

```
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
```

```
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
```

Lists, dictionaries, and variables are then established to hold the results as the data is analyzed.

```
# Initialize a total vote counter.
total_votes = 0

# Initialize candidate options list and candidate votes dict.
candidate_options = []
candidate_votes = {}

# 1: Initialize county options list and county votes dict.
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county, vote count and percentage.
winning_county = ""
winning_county_votes = 0
winning_county_percentage = 0
```

With the file open, a loop is created that reads each row of data in the file. As each row is read, the voting data is collected and a series of conditions is checked. At every row a vote is added to the tally of total votes. The first condition checked is whether the candidate name which received the current vote exists in a candidate list and if a count of votes for the candidate has been established. If this is the first occurence of the candidate's name, it is added to the list that holds the candidate names and a count is established for the candidate. 
```
    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
```
The next condition checked is if the county in which the vote was cast exists in the list of county names. If this is the first occurence of the county, it is added to the list of counties and a count of votes is established for the county. 
At each row the county in which the vote was cast as well as the candidate the vote is for recieve an additional vote in their corresponding counts. At the conclusion of this loop all the votes are counted and the results held in dictionaries titled `candidate_votes` and `county_votes`.

```
# Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: If the county does not match any existing county add it to
        # the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0


        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
```

Now, the file to save the results is opened,

```
# Save the results to the text file.
with open(file_to_save, "w") as txt_file:
```
and the final results of the election are calculated, formatted, sent to the terminal, and saved to the text file. First, the total votes in the election are printed and saved in a readable format. 
```
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)
```

Then a loop is created to pass through the `county_votes` dictionary and calculate the percentage of votes cast in each county, and determine which county received the largest number of votes. These results are then printed to the terminal and saved in the designated text file. 
```
# 6a: For loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        co_votes = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        co_percentage = float(co_votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {co_percentage:.1f}% ({co_votes:,})\n")
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: If statement to determine the winning county and get its vote count.
        if (co_votes > winning_county_votes) and (co_percentage > winning_county_percentage):

            winning_county = county_name
            winning_county_votes = co_votes
            winning_county_percentage = co_percentage
        
    # 7: Print the county with the largest turnout to the terminal.
    largest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n\n"
        f"Candidate Votes:\n")

    print(largest_county_summary)

    # 8: Save the county with the largest turnout to the text file.
    txt_file.write(largest_county_summary)
```
An additional loop is created to pass through the `candidate_votes` dictionary, calculate the percentage of votes each candidate received, and determine the winner of the election. These results are also printed to the terminal and saved in the designated text file.
After these steps are finished, the tasks required by the election board are complete and the audit is ready for submission. When the script is run, the results of the election are printed in the terminal and saved in a text file titled `election_analysis.txt` that can be sent to the Colorado Board of Elections.

![election_results](https://github.com/Jforbus/election_analysis/blob/main/Analysis/election_results.png)

## Challenge Summary
The Python script written to accomplish this task accurately determined all the necessary information and transmitted this data in an easily accessible format. With a few minor adjustments the Colorado Board of Elections could use this script to audit any election. This script could also be modified in certain ways to expand its uses. It could be modified to read and analyze election data from multiple sources instead of a single CSV file. This would allow the script to be more versatile in the types of elections it can audit as well as help the election board to aggregate data from multiple sources easily. The script could also be modified to provide a more in-depth look at the election data from any given election, such as providing a candidate vote count by county summarization, showing which counties voted for which candidates and in what amounts. Overall it is a well written script that would be a useful tool to the Colorado Board of Elections, or any election commission.
