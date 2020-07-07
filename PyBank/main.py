# import dependencies
import os
import csv
import numpy as np

# need to set the path for the csv file
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Initiate lists
dates = []
pnl = []

def average(list_chng_pnl):
        return sum(list_chng_pnl) / len(list_chng_pnl)

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    next(csvreader)

    for row in csvreader:
        # append to list for date_list
        dates.append(row[0])
        #append to list for profit and loss
        pnl.append(int(row[1]))

# total months calc
total_months = len(dates)   

#net profit calc
net_profit = sum(pnl)

# calculate the changes in each month using the numpy diff     
prof_array = np.array(pnl)
change_pnl = np.diff(prof_array)

# change from array to a list
list_chng_pnl = change_pnl.tolist()

avg_chnge = round(average(list_chng_pnl),2)

# print(dates)
# print(pnl)
# print(prof_array)
# print(change_pnl)
# print(list_chng_pnl)
# print(avg_chnge)
# print("Average of the list =", avg_chnge)

# use numpy to get the min and the max for change in pnl
maxchange = np.amax(change_pnl)
minchange = np.amin(change_pnl)

# verify that the max is calculated properly
# print('Max from Numpy Array : ', maxchange)
# print('Min from Numpy Array : ', minchange)

# find the index of where the max and min are located
max_ind = np.where(change_pnl == np.amax(change_pnl))
min_ind = np.where(change_pnl == np.amin(change_pnl))

# print('Indices of max :', max_ind[0])
# print('Indices of min :', min_ind[0])

# because the change data is one less due to the first value having no change we have to add one to get to the index for the date
max_date_ind = max_ind[0] +1
min_date_ind = min_ind[0] +1
# print('max date index is :', max_date_ind)
# print('min date index is :', min_date_ind)

min_date = dates[min_date_ind[0]]
max_date = dates[max_date_ind[0]]

# print(min_date)
# print(max_date)

print("Financial Analysis \n", f"---------------------- \n", f"Total Months: {total_months} \n",f"Total: ${net_profit} \n",f"Average Change: ${avg_chnge} \n",
f"Greatest Increase in Profits: {max_date} (${maxchange}) \n", f"Greatest Decrease in Profits: {min_date} (${minchange}) \n")

# Program to show various ways to read and 
# write data in a file. 
output_data = os.path.join('analysis', 'py_analysis.txt')
file1 = open(output_data,"w") 
L = [f"---------------------- \n", f"Total Months: {total_months} \n",f"Total: ${net_profit} \n",f"Average Change: ${avg_chnge} \n",
f"Greatest Increase in Profits: {max_date} (${maxchange}) \n", f"Greatest Decrease in Profits: {min_date} (${minchange}) \n"]
  
# \n is placed to indicate EOL (End of Line) 
file1.write("Financial Analysis \n") 
file1.writelines(L) 
file1.close() #to change file access modes 


