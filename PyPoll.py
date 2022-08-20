# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Assign a variable for the file to load and the path

# add dependencies
import csv
import os

# Assign variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# add total vote variable
total_votes = 0

# add list for candidate options
candidate_options = []

# Open the election results and read the file
with open(file_to_load) as election_data:
    # read and analyze the data here
    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)
    
    # iterate through each row in the file
    for row in file_reader:
        
        # add to total votes
        total_votes = total_votes + 1
        # or total_votes += 1

        # get candidate name from each row
        candidate_name = row[2]

        # add candidate names to candidate options list if not yet present
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

        

    # print the candidate list
    print(candidate_options)





        


# Open save file as text file with open statement. 
# with open(file_to_save, "w") as txt_file:

# Write some data to the file
    # txt_file.write("Counties in the election\n-------------------------\nArapahoe\nDenver\nJefferson")


