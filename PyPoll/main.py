#PyPoll

#import os and csv modules
import os
import csv

#set the source file path
mypath = os.path.join('Resources', 'election_data.csv')

#open the file
with open(mypath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #store the header
    csvheader = next(csvreader)
    
    #initialize some lists for value storage
    candidates = []
    totalvotes = 0
    #loop through the rows to find values
    for row in csvreader:
        totalvotes = totalvotes +1 #calculates total number of votes cast
        #populate candidate list
        candidates.append(row[2])

#create a dictionary and loop through candidates list to populate the dictionary
pollresults = {}
for candidate in candidates:
   if candidate in pollresults:
      pollresults[candidate] +=1
   else:
      pollresults[candidate] = 1

#create a list of percentages from the pollresults dictionary
perclist = []
for name, vote in pollresults.items():
    voteperc = 0.0
    voteperc = round((vote/totalvotes)*100,3) #round to 3 decimal places
    perclist.append(voteperc)

#create names and votes list from pollresults dictionary
nameslist = list(pollresults.keys())
voteslist = list(pollresults.values())
#pull winner name from sorted pollresults dictionary
winner = sorted(pollresults,reverse=True)[1]  

#create an export string list that combines the three lists and produces the string for the results file
exportlist = []
for i in range(len(nameslist)):
    myline = ""
    myperc = str(perclist[i])
    myname = str(nameslist[i])
    myvote = str(voteslist[i])
    myline += myname + ": " + myperc + "% " + "(" + myvote + ")"
    exportlist.append(myline)

#print results to terminal
print("Election Results")
print("--------------------")    
print(f"Total Votes: {totalvotes}")
print("--------------------")
for i in range(len(nameslist)):
    print(nameslist[i],": ", perclist[i],"% ", "(", voteslist[i], ")", sep='')  
print("--------------------")  
print(f"Winner: {winner}")
print("--------------------")  

#export results to a file

#output path and file to write to
export_path = os.path.join("Analysis", "poll_results.txt")

#Open the file in write mode
with open(export_path, 'w', newline='') as datafile:
    datafile.write("Election Results")
    datafile.write("\n--------------------")    
    datafile.write(f"\nTotal Votes: {totalvotes}")
    datafile.write("\n--------------------")
    for i in exportlist:
        datafile.write("\n" + i)    
    datafile.write("\n--------------------")  
    datafile.write(f"\nWinner: {winner}")
    datafile.write("\n--------------------")  
datafile.close()
