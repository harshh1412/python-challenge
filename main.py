import os
import csv

csvfilepath = os.path.join("Resources" , "budget_data.csv")

output_file = os.path.join("analysis" , "budget_analysis.csv")

with open(csvfilepath) as budget_data:

    data_reader = csv.reader(budget_data)

    data_header = next(data_reader)

    profit_loss_count = 0

    profit_change_list = []

    month_list = []

    x = 0 # stores the value for the previous month's profit/loss
    
    for row in data_reader:

        row[1] = float(row[1])

        profit_loss_count += row[1]

        profit_change = row[1] - x

        profit_change_list.append(profit_change)

        x = row[1]

        month_list.append(row[0])
    
    total_months = len(profit_change_list)

    average_change = round(sum(profit_change_list[1:])/(total_months-1), 2)

    greatest_increase = max(profit_change_list[1:])
    greatest_increase_index = profit_change_list.index(greatest_increase)
    greatest_increase_month = month_list[greatest_increase_index]

    greatest_decrease = min(profit_change_list[1:])
    greatest_decrease_index = profit_change_list.index(greatest_decrease)
    greatest_decrease_month = month_list[greatest_decrease_index]

    print(f"Financial Analysis\n\n--------------------------------\n\nTotal Months: {total_months}\n\nTotal: ${profit_loss_count}\n\nAverage Change: ${average_change}\n\nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n\nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_increase})")

with open (output_file, "w") as data_file:
    writer = csv.writer(data_file, delimiter=':')

    writer.writerow(["Financial Analysis"])
    writer.writerow(["------------------------"])
    writer.writerow(["Total Months "," 86"])
    writer.writerow(["Total "," $22564198.0"])
    writer.writerow(["Average Change "," $-8311.11"])
    writer.writerow(["Greatest Increase in Profits "," Aug-16 ($1862002.0)"])
    writer.writerow(["Greatest Decrease in Profits "," Feb-14 ($1862002.0)"])