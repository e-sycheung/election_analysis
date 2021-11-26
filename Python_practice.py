counties = ["Arapahoe","Denver","Jefferson"]
print (counties)
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the window.")

#What is the score?
score = int(input("What is your test score?"))

#Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is an B.')
elif score >= 70:
    print('Your grade is an C.')
elif score >= 60:
    print('Your grade is an D.')
else:
    print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list")

#voting data 
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
# printing the dictionaries
for county_dict in voting_data:
    print(county_dict)

# for loop over range to output counties
for i in range(len(voting_data)):
    print(voting_data[i]['county'])

# nested loop over list of dictionary 
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total numver of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes *100:.2f}% of the total votes.")
print(message_to_candidate)

for i in range(len(voting_data)):
    print(f"{(voting_data[i]['county'])} county has {(voting_data[i]['registered_voters']):,} registered voters. ")


