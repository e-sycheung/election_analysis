# Import the data file - adding dependencies
import csv 
import os

# Assign variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize vote counter
total_votes = 0

# Candidate Options
candidate_options = []
# Declare a dictionary 
candidate_votes = {}

# Winning candidate and Winning candidate tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    # To do: Read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)
    
    #Print ea. row in CSV
    for row in file_reader:
        # Add to total count vote
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If candidate is unique then add
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin to track the candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count 
        candidate_votes[candidate_name] += 1

# Save results to txt file.
with open(file_to_save,"w") as txt_file:
# Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n")
    print(election_results)
    # Save the final vote count to the text file
    txt_file.write(election_results)
     
    for candidate_name in candidate_votes:
        # Get vote candidat for each candidate
        votes = candidate_votes[candidate_name]
        # Calculate percentage vote
        vote_percentage = float(votes) / float(total_votes) *100
        
        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
        # Print each candidate and their results
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Print out the winning candidate's result
    winning_candidate_summary = (
        f"------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Voting Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"------------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

    
