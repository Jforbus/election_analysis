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
file_to_save = os.path.join("analysis", "election_analysis.txt")

# add total vote variable
total_votes = 0

# add list for candidate options
candidate_options = []

# create a dictionary for each candidates votes
candidate_votes = {}

# create variables for winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0


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

        # check if candidate name present in candidate list
        if candidate_name not in candidate_options:
            
            # add candidate name to candidate list
            candidate_options.append(candidate_name)

            # begin tracking candidates vote count
            candidate_votes[candidate_name] = 0

        # add votes to each candidate's count
        candidate_votes[candidate_name] += 1

# save results to our text file
with open(file_to_save, "w") as txt_file:

    election_results = (
        
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n")

    # print final vote count to terminal
    print(election_results, end="")

    # save final vote count to text file
    txt_file.write(election_results)


    # determnine percentage of votes for each candidate
    # loop through list of candidate votes
    for candidate_name in candidate_votes:
        
        # retreive vote count for each candidate
        votes = candidate_votes[candidate_name]

        #calculate percentage of votes for each candidate
        vote_percentage = (float(votes) / float(total_votes)) * 100

        # create each candidates name and vote count
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # print candidate results
        print(candidate_results)

        # save individual candidate results to text file
        txt_file.write(candidate_results)


        # establish winning candidate, vote count, and vote percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name

    # print winning candidate name, vote count, and vote percentage to terminal

    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")

    
    # print winning cadidate summary
    print(winning_candidate_summary)

    # save winning candidate summary to text file
    txt_file.write(winning_candidate_summary)

    


