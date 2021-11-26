import datetime as dt
now = dt.datetime.now()

print("The time right now is", now)


# Import the data file
import csv 
import os
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    # To do: Read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
    print(headers)
    #Print each row in the CSV file.
    for row in file_reader:
        print(row)

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:

    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
    

#1. The total number of votes case


#2. A complete list of canidadates who received votes


#3. The percentage of votes each candidate won 


#4. The total number of votes each candidate won 


#5. THe winner of the election based on the popular vote.



