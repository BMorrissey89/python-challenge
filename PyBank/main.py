import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

date = []
profit_losses = []
changes = []

with open(budget_csv) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=",")

  csv_header = next(csv_reader)

  for row in csv_reader:

    date.append(row[0])
    profit_losses.append(row[1])

      #The total number of months included in the dataset
      total_months = len(date)

      #The net total amount of "Profit/Losses" over the entire period
      net_total = sum(profit_losses)
    
      #The changes in "Profit/Losses" over the entire period, and then the average of those changes
      
    

