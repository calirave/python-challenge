#PyBank
#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

#source file to use is budget_data.csv

#import os and csv modules
import os
import csv

#set the source file path
mypath = os.path.join('Resources', 'budget_data.csv')

#open the file
with open(mypath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #store the header
    csvheader = next(csvreader)
    
    #initialize some variables for value storage
    months = 0
    profitnloss = 0
    avg_pnl_change = 0
    pnl_list = []
    

    #loop through the rows to find values
    for row in csvreader:
        months = months +1 #gets the number of months
        #add to profit and loss the value from the second column in the file
        profitnloss = profitnloss + float(row[1])
        #populate the list with values for profit and loss
        pnl_list.append(float(row[1]))

#create a list to hold differences in PNL from month to month
pnl_differences = []
#use a for loop to populate the above list with PNL changes
for i in range(len(pnl_list)):
    if i > 0: #ignore the first row because there is no previous value to compare to
        pnldiff = pnl_list[i] - pnl_list[i-1] 
        pnl_differences.append(pnldiff)
        #print(pnl_list[i], i, pnldiff)

#find average of the PNL changes
def average(numbers):
    length = len(numbers)
    total = 0.00
    for number in numbers:
        total += number
    return round(total/length,2)

#greatest increase
grtincrease = max(pnl_differences)

#greatest decrease
grtdecrease = min(pnl_differences)

#print results to terminal
print("Financial Analysis")
print("--------------------")    
print(f"Total months: {months}")
print(f"Total: {profitnloss}")
print(f"Average Change: ", average(pnl_differences))
print(f"Greatest Increase in Profits: {grtincrease}")
print(f"Greatest Decrease in Profits: {grtdecrease}")

#export results to a file

#output path and file to write to
export_path = os.path.join("Analysis", "results.txt")

#Open the file in write mode
with open(export_path, 'w', newline='') as datafile:
    datafile.write("Financial Analysis")
    datafile.write("\n--------------------")    
    datafile.write(f"\nTotal months: {months}")
    datafile.write(f"\nTotal: {profitnloss}")
    #datafile.write(f"Average Change: ", average(pnl_differences))
    datafile.write(f"\nGreatest Increase in Profits: {grtincrease}")
    datafile.write(f"\nGreatest Decrease in Profits: {grtdecrease}")







