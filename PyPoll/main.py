# -*- coding: UTF-8 -*-
"""PyPoll Homework main File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
win_candidate = ""
win_count = 0
vote_percentage = 0
election_results = ""

# Process each row of csv and add candidates to dictionary
def count_votes(data):
    global total_votes, candidate_votes

    for row in data:
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1


# Loop through the candidates to determine vote percentages and identify the winner
def calculate_results(data):
    global win_candidate, win_count, vote_percentage, election_results
    
    for candidate in data:
        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate]

        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > win_count:
            win_count = votes
            win_candidate = candidate

        # Print and save each candidate's vote count and percentage
        candidate_votes[candidate] = (vote_percentage, votes)

        election_results += (
            f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        )

    # Generate and print the winning candidate summary
    election_results += (
        f"-------------------------\n"
        f"Winner: {win_candidate}\n"
        f"-------------------------\n"
    )
    

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    count_votes(reader)

    # Print new line for better results formatting in terminal
    print("\n")                

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Write the total vote count to the text file
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )

    # Obtain candidate values and identify winner
    calculate_results(candidate_votes)

    print(election_results)

    # Save the winning candidate summary to the text file
    txt_file.write(election_results)
