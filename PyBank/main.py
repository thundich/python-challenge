#Importing the necessary modules/libraries
import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('.', 'Resources', 'budget_data.csv')

# Define total months field
TotalMonths = 0
# Define total profit/loss field
TotalProfitLoss = 0

# Define dollar amount to store dollars from data
DollarAmount = 0

# Define Dates list
Dates = []
# Define ProfilLoss list
ProfitLoss = []

# Read the CSV file
with open(budget_data, "r") as BudgetFile:
    BudgetReader = csv.reader(BudgetFile, delimiter = ",")

    #Read header row
    ColumnHeaders = next(BudgetReader)
    # Save the Column Numbers
    ColumnNumbers = range(len(ColumnHeaders))

    # Read first row to set defaults
    FirstDataRow = next(BudgetReader)
    Date = FirstDataRow[0]
    RowAmount = int(FirstDataRow[1])

    TotalMonths +=1
    TotalProfitLoss += RowAmount
    PreviousDollarAmount = RowAmount
    Dates.append(Date)
   # ProfitLoss.append(0)

    # Set up loop to read the rest of data rows
    for row in BudgetReader: 
      # Move row to fields
        Date = row[0]
        RowAmount = int(row[1])

        #Store the Date
        Dates.append(Date)

        # Calculate the change, then add it to list of changes
        DollarChange = RowAmount-PreviousDollarAmount
        ProfitLoss.append(DollarChange)
        PreviousDollarAmount = RowAmount

        # Increment total number of months
        TotalMonths +=1 

        # Total net amount of "Profit/Losses over entire period"
        TotalProfitLoss = TotalProfitLoss + RowAmount

    # Find the greatest increase in profits 
    GreatestProfitLossIncrease = max(ProfitLoss)
    GreatestProfitLossIncreasef = "${:,.2f}".format(GreatestProfitLossIncrease)
    GreatestProfitLossIndex = ProfitLoss.index(GreatestProfitLossIncrease)
    GreatestProfitLossDate = Dates[GreatestProfitLossIndex]

# Find the greatest decrease in profits 
    GreatestProfitLossDecrease = min(ProfitLoss)
    GreatestProfitLossDecreaseIndex = ProfitLoss.index(GreatestProfitLossDecrease)
    GreatestProfitLossDecreaseDate = Dates[GreatestProfitLossDecreaseIndex]

# Average change in "Profit/Losses between months over entire period"
    AverageChange = sum(ProfitLoss)/len(ProfitLoss)
    AverageChangef = "${:,.2f}".format(AverageChange)
    #AverageChange = "%.2f%%" % AverageChange

# Display Analysis information on screen
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(TotalMonths)}")
print(f"Total: ${str(TotalProfitLoss)}")

#print(f"Average Change: ${str(round(AverageChange,2))}")
print(f"Average Change: {AverageChangef}") 
print(f"Greatest Increase in Profits: {GreatestProfitLossDate} {GreatestProfitLossIncreasef}")
print(f"Greatest Decrease in Profits: {GreatestProfitLossDecreaseDate} (${str(GreatestProfitLossDecrease)})")

# Write Analysis information to file (text format)
outputpath = os.path.join(".", "analysis", "results.txt")
output = open(outputpath, "w") 
output.write("Financial Analysis\n")
output.write("---------------------\n")
output.write(str(f"Total Months: {str(TotalMonths)}\n"))
output.write(str(f"Total: ${str(TotalProfitLoss)}\n"))
#output.write(str(f"Average Change: ${str(round(AverageChange,2))}\n"))
output.write(str(f"Average Change: {AverageChangef}\n"))
output.write(str(f"Greatest Increase in Profits: {GreatestProfitLossDate} (${str(GreatestProfitLossIncrease)})\n"))
output.write(str(f"Greatest Decrease in Profits: {GreatestProfitLossDecreaseDate} (${str(GreatestProfitLossDecrease)})\n"))

output.close()