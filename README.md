# Election_Analysis

## Project Overview
Complete an election audit for a recent local Congressional Election in Colorado assigned by Colorado Board of Elections.

1. Calculate the total number of votes casted in the election.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner based on the popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, VS Code 1.62

## Summary
The analysis of the elections showed:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the votes, which is 84,213 votes.
    - Diana DeGette received 73.8% of the votes, which is 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the votes, which is 11,606 votes.
- The winner of the election was:
    - Diana Degette who recevied 73.8% of the votes, which is 272,892 votes. 

## Challenge Overview
Overview of Election-Audit:

In addition to the previously performed audit, the Colorado Board of Elections would like to see more result analysis. 
1. The number of the voter turnout by county. 
2. The percentage of the voter turnout by county.
3. The county that had the highest turnout.

Approach:
1. Read the data files.
2. Iterate through rows of csv (for loop)
3. Place conditionals (if statements)
4. Filter out the candidates and votes
5. Perform Mathematical Calculations to needed outputs 
6. Export to .txt file for a clean presentation of results

## Challenge Summary

<img src="https://github.com/e-sycheung/election_analysis/blob/main/Practice_Code_%26Img/county_result.png" style=" width: 385px ; height: 250px">

Election-Audit Results: 
- The total number of votes casted in the precinct for this congressional election: 
    - 369,711 votes.
- The total number of total votes in each county:
    - Jefferson County had 38,855 votes, 10.51% of the total votes.
    - Denver County had 306,055 votes, 82.78% of the total votes.
    - Arapahoe County had 24,801 votes, 6.71% of the total votes. 
- The county with the largest number of votes:
    - Denver County with 306,055 votes.
- The election results by candidate:
    - Charles Casper Stockham received 85,213 votes, 23% of the total votes
    - Diana DeGette received 272,892 votes, 73.8% of the total votes.
    - Raymon Anthony Doane received 11,606 votes, 3.1% of the total votes.
- The winning candidate of this election:
    - Diana DeGette won the election with 272,892 votes, 73.8% of the total votes.

Election-Audit Summary:

Since the project was commissioned by the Colorado Board of Elections, the Python program could easily be applied to other precincts in this Congressional elections as well as local elections within the state.

By uploaded different voting data files we can run the same calculations in the program to compute the result in the other districts. We would change the (file_to_load). If the format and the header of the file remain the same, we wouldn’t have to change the code except the .txt file we would save the result to.


<img src="https://github.com/e-sycheung/election_analysis/blob/main/Practice_Code_%26Img/file_to_load.png" style=" width: 480px ; height: 130px">


In closer electoral races, the number of eligible voters who didn’t vote is a vital piece of information sought out by different parties. If that total number could be calculated, we can apply the same equation to see the percentage of the population who voted and those who did not. This information could changes the political parties’ efforts and planning during election years as well as an incumbants time in office . We see this in major swing states  as well as in smaller local elections that effect redistricting. In this situation our total would be the total eligible votes in the region. A comparative analysis of voters and nonvoters could be analyzed. With the new total variable we could run the same calcuation for the percentages. 


<img src="https://github.com/e-sycheung/election_analysis/blob/main/Practice_Code_%26Img/vote_percentage.png" style=" width: 480px ; height: 130px">



