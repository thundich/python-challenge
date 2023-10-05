# Import the necessary system modules/libraries
import os
import csv

# Set the file location
election_data = os.path.join('.', 'Resources', 'election_data.csv')

# Define the Candidates Array
Candidates = []

# Define the number of votes received for each candidate array
CandidateVotes = []

# Define the percentage of total votes each candidate receives 
CandidatePercent = []
# Define total counter to hold total number of votes 
TotalVotesCast = 0

# Open the election data file
with open(election_data, "r", newline = "") as VoteFile:
    VoteReader = csv.reader(VoteFile, delimiter = ",")
    # Get the column header row
    ColumnHeaders = next(VoteReader)
    # Save the Column Numbers
    ColumnNumbers = range(len(ColumnHeaders))
    
    # Set loop to read each row of the election data file
    for row in VoteReader:
        
        # Move row to fields
        IDNumber = row[0]
        County = row[1]
        Candidate = row[2]
                
        # Increment the total counter 
        TotalVotesCast += 1 

        # Check if candidate is in the candidate array
        # if candidate is not in the array, add the candiate  
        if Candidate not in Candidates:
            # Add candidate to candidate array
            Candidates.append(Candidate)
            # Get the candidate position in the array
            CandidateIndex = Candidates.index(Candidate)
            # Reset Candidate Vote Count to 0
            CandidateVotes.append(0)
            
        # if candiate is in the table then get the candidate position in array
        else:
            # Get the canidate index from candidate array
            CandidateIndex = Candidates.index(Candidate)
            
        # Increment the vote count for the candidate
        CandidateVotes[CandidateIndex] += 1
    
    # Calculate the percentage of votes each candiate received 
    for Votes in CandidateVotes:
        WorkPercent = (Votes/TotalVotesCast) * 100
        WorkPercent = "%.3f%%" % WorkPercent
        CandidatePercent.append(WorkPercent)
    
    # Find the winning candidate
    VoteWinner = max(CandidateVotes)
    VoteWinnerIndex = CandidateVotes.index(VoteWinner)
    Winner = Candidates[VoteWinnerIndex]

# Display the results to screen
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(TotalVotesCast)}")
print("--------------------------")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(CandidatePercent[i])} ({str(CandidateVotes[i])})")
print("--------------------------")
print(f"Winner: {Winner}")
print("--------------------------")

# Write the results to output file (text based)
outputpath = os.path.join(".", "analysis", "results.txt")
output = open(outputpath, "w")
output.write("--------------------------\n")
output.write(str(f"Total Votes: {str(TotalVotesCast)}\n"))
for i in range(len(Candidates)):
    line = str(f"{Candidates[i]}: {str(CandidatePercent[i])} ({str(CandidateVotes[i])})\n")
    output.write(line)
output.write("--------------------------\n")
output.write(str(f"Winner: {Winner}\n"))
output.write("--------------------------\n")

output.close()