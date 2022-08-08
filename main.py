## Python Challenge
## By Nathan Skinner


import csv
import os

### PyBank ###

budget_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_csv, 'r') as csv_file:
    
    #read the file
    csvreader = csv.reader(csv_file, delimiter = ',')
    
    #get the header of the data and skip it
    header = next(csvreader)
    
    #Set variables to be added to
    nrow = 0
    profloss = 0
    maxv = 0
    minv = 0
    last_val = 0
    change_total = 0
    
    #Search each row for data
    for row in csvreader:
        row[1] = int(row[1])
        nrow = nrow + 1
        profloss = row[1] + profloss
        
        #Change in prof/loss
        if not last_val == 0:
            change = row[1] - last_val
            change_total = change_total + change
            if change > maxv:
                maxv = change
                max_name = row[0]
            if change < minv:
                minv = change
                min_name = row[0]
        
        #redefine the last value
        last_val = row[1]
        

    change_average = change_total / (nrow-1)
    
    #Print out all necessary information
    print('Financial Analysis')
    print('-------------------------------------------')
    print(f'Total Months: ${nrow}')
    print(f'Net Profit/Loss: ${profloss}')
    print(f'Average Change: ${round(change_average,2)}')
    print(f'Greatest Increase in Profits: {max_name} (${maxv})')
    print(f'Greatest Decrease in Profits: {min_name} (${minv})')
    
    
    with open('analysis/financial_analysis.txt', 'w') as f:
        f.write('Financial Analysis\n')
        f.write('-------------------------------------------\n')
        f.write(f'Total Months: ${nrow}\n')
        f.write(f'Net Profit/Loss: ${profloss}\n')
        f.write(f'Average Change: ${round(change_average,2)}\n')
        f.write(f'Greatest Increase in Profits: {max_name} (${maxv})\n')
        f.write(f'Greatest Decrease in Profits: {min_name} (${minv})\n')
    
    
print('\n')
print('\n')    
### PyPoll ###

election_csv = os.path.join('Resources', 'election_data.csv')

with open(election_csv, 'r') as csv_file:
    
    #read the file
    csvreader = csv.reader(csv_file, delimiter = ',')
    
    #get the header of the data and skip it
    header = next(csvreader)
    
    #define some variables
    nrow = 0
    votes = {}
    
    #Search each row for data
    for row in csvreader:
        #Count number of votes
        nrow = nrow + 1
        
        #create a dictionary of each unique candidate
        if row[2] not in votes:
            votes[row[2]] = 0
        #add a count to each candidate, for each row that matches
        votes[row[2]] = votes[row[2]] + 1


    # extract data from the dictionary into lists and run some calculations
    candidate = list(votes.keys())
    nvote = list(votes.values())
    percent_vote = [round((v/nrow) * 100,3) for v in nvote]
    
    #Get the winner
    winner = candidate[nvote.index(max(nvote))]

    
    #print the results
    print("Election Results")
    print("------------------------------------------")
    print(f"Total Votes: {nrow}")
    print("------------------------------------------")
    #zip up the results table and run a single print statement for each candidate
    for i in zip(candidate, nvote, percent_vote):
        print(f"{i[0]}: {i[2]} ({i[1]})")
    print("------------------------------------------")
    print(f"Winner: {winner}")
    
    #write a text file with the election analysis
    with open('analysis/election_analysis.txt', 'w') as f:
        f.write("Election Results\n")
        f.write("------------------------------------------\n")
        f.write(f"Total Votes: {nrow}\n")
        f.write("------------------------------------------\n")
        for i in zip(candidate, nvote, percent_vote):
            f.write(f"{i[0]}: {i[2]} ({i[1]})\n")
        f.write("------------------------------------------\n")
        f.write(f"Winner: {winner}\n")











