import os
import csv
#csvpath = os.path.join('/Users/ikran/OneDrive/Documents/Desktop/Python_challenge/PyBank/Resources/budget_data.csv')
cvspath = (f"../Resources/budget_data.csv")

csvpath = os.path.join("..", "Resources", "budget_data.csv")
#print (budget_data.csv)
print(f"current dir: {os.getcwd()}")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    print(csvreader)

    header = next(csvreader) # starts data on the next row
    total_month_count = 0 # store the count of all rows which provides month count
    budget_1 = [] # store budget values in this list
    total_budget = 0 # used to get the total sum of budget
    month_1 = [] # store month in this list

    for row in csvreader:
        total_month_count+=1
        budget_1.append(row[1])
        month_1.append(row[0])


    for x in budget_1:
         total_budget+=  float(x) # sums all data and gets the total
            
    budget_t = round(total_budget,) # store the total budget to output into text file
    profit_change = round((float(budget_1[len(budget_1) -1]) - float(budget_1[0]))/float(len(budget_1)-1),2) # used to get the average change
            

    first_number = 0 # looks the first number
    second_number = 0 # looks at second number
    profits_review = [] # used to append data to review max and min
    for i in budget_1:
        second_number = second_number + 1 # get the next second number
        if(second_number < len(budget_1)): # second number is less than the total number
            first_1 = budget_1[first_number] # assign first number 
            second_1 = budget_1[second_number] # assign second number
            profits_sub= float(second_1)-float(first_1) # second num - first num to get the gains and losses
            profits_review.append(profits_sub) # put the gains and losses in a list
            first_number = first_number + 1 # got to the next first number
        else:
            0

    max_number = round(max(profits_review),) # get the max number in the list of gains and losses   
    min_number = round(min(profits_review),) # get the min number in the list of gains and losses
    month_min = profits_review.index(min_number) +1 # find the index of the biggest loss within the list of gains and losses
    month_max = profits_review.index(max_number) +1 # find the index of the highest gains within the list of gains and losses
    m1 = month_1[month_max] # get the month that had the highest gains
    m2 = month_1[month_min] #get the month that had the biggest loss

print("Financial Analysis")
print('--------------------')
print(f"Total Months: {total}")
print(f"Total: ${round(count)}")
print(f"Average Change: {round(sum(monthly_profit)/len(monthly_profit),2)}")
print(f"Greatest Increase in Profits: (${max_increase_value})")
print(f"Greatest Decrease in Profits: (${min_increase_value})")

output_file = Path ("..", "Resources", "Analysis.txt")
with open(output_file, "w") as File:
# filepath = os.path.join('.', 'Resources', 'Analysis.txt')
# with open(filepath, "w") as text_file