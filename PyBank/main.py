import os
import csv

mypath = os.path.join('Resources', 'budget_data.csv')

with open(mypath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #store the header
    csvheader = next(csvreader)
    
    #initialize some variables for value storage
    months = 0
    profitnloss = 0
    #create a list for profit and loss values
    pnl_list = list(csvreader)
    csvfile.close

#Number of months
months = len(pnl_list)

#Total of the profit/loss column
for row in range(len(pnl_list)):
    profitnloss += int(pnl_list[row][1]) #iterate through all rows and pull value from 2nd column

#create separate lists with change values
pnl_changes = []
pnl_months = []
current = 0
previous = 0
change = 0
for i in range(len(pnl_list)):
    if i > 0: #ignore the first row because there is no previous value to compare to
        current = int(pnl_list[i][1])
        previous = int(pnl_list[i-1][1])
        change = current - previous
        pnl_months.append(pnl_list[i][0])
        pnl_changes.append(change)

#create a dictionary of months and changes 
combined = dict(zip(pnl_changes, pnl_months))

#calculate average change in profit and loss
average = sum(pnl_changes)/len(pnl_changes)

#greatest increase
grtincrease = max(combined)
maxmonth = combined.get(grtincrease)
#greatest decrease
grtdecrease = min(combined)
minmonth = combined.get(grtdecrease)

#print results to terminal
print("Financial Analysis")
print("--------------------")    
print(f"Total months: {months}")
print(f"Total: ${profitnloss}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {maxmonth} ${grtincrease}")
print(f"Greatest Decrease in Profits: {minmonth} ${grtdecrease}")

#export results to a file

#output path and file to write to
export_path = os.path.join("Analysis", "results.txt")

#Open the file in write mode
with open(export_path, 'w', newline='') as datafile:
    datafile.write("Financial Analysis")
    datafile.write("\n--------------------")    
    datafile.write(f"\nTotal months: {months}")
    datafile.write(f"\nTotal: ${profitnloss}")
    datafile.write(f"\nAverage Change: ${average}")
    datafile.write(f"\nGreatest Increase in Profits: {maxmonth} ${grtincrease}")
    datafile.write(f"\nGreatest Decrease in Profits: {minmonth} ${grtdecrease}")