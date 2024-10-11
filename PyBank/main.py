# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

#print(os.getcwd())

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
previous_net = 0
net_change_list = []
months = []
max_profit = ["", 0]
min_profit = ["", 0]

def convert_to_dict(budget):
    return {
        "date": budget[0],
        "profit": float(budget[1])
    }

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:

        budget_dict = convert_to_dict(row)
        month = budget_dict["date"]
        net = budget_dict["profit"]

        # Track the total
        total_months += 1
        total_net += net

        # Track the net change
        if previous_net != 0:
            net_change = net - previous_net
            net_change_list.append(net_change)
            months.append(month)

            # Calculate the greatest increase in profits (month and amount)
            if net_change > max_profit[1]:
                max_profit = [month, net_change]

            # Calculate the greatest decrease in losses (month and amount)
            if net_change < min_profit[1]:
                min_profit = [month, net_change]

        # Update the previous month's net
        previous_net = net


# Calculate the average net change across the months
average_changes = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (f"Financial Analysis\n"
          f"----------------------------\n"
          f"Total Months: {total_months}\n"
          f"Total: ${total_net}\n"
          f"Average Change: ${average_changes:0.2f}\n"
          f"Greatest Increase in Profits: {max_profit[0]} (${max_profit[1]})\n"
          f"Greatest Decrease in Profits: {min_profit[0]} (${min_profit[1]})\n")

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
