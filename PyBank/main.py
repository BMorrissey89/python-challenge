import os
import csv

budget_data = os.path.join("Resources","budget_data.csv")

total_months = 0
net_total = 0
previous_profit = 0
profit_change = 0

date = []
profit = []
change = []

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])

        #The total number of months included in the dataset
        total_months = len(date)

        #The net total amount of "Profit/Losses" over the entire period
        net_total += int(row[1])

        #The changes in "Profit/Losses" over the entire period, and then the average of those changes
        profit_loss = int(row[1])
        monthly_profit_change = profit_loss - previous_profit
        change.append(monthly_profit_change)
        profit_change = profit_change + monthly_profit_change
        previous_profit = profit_loss
        average_profit_change = (profit_change/total_months)
        
        #The greatest increase in profits (date and amount) over the entire period
        greatest_increase = max(change)
        greatest_decrease = min(change)

        greatest_increase_month = date[change.index(greatest_increase)]
        greatest_decrease_month = date[change.index(greatest_decrease)]

print("Financial Analysis")
print("--------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: Could not get this right')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

output = os.path.join("Analysis", "PyBank_Analysis.txt")

with open(output, "w") as datafile:
    datafile.write(f'Financial Analysis\n')
    datafile.write(f'----------------------------\n')
    datafile.write(f'Total Months: {total_months}\n')
    datafile.write(f'Total: ${net_total}\n')
    datafile.write(f'Average Change: Could not get this right\n')
    datafile.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    datafile.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')


