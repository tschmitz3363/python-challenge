import os
import csv


file_to_open="03-Python_HW_Instructions_PyBank_Resources_budget_data.csv"
#read csv file and print the headers of the two colums
#for must be nested in the with
with open (file_to_open, 'r') as this_csv_file:
    this_csv_reader=csv.reader(this_csv_file, delimiter=",")
    header=next(this_csv_reader)
    print(header)
    #print and go through each row
    for row in this_csv_reader:
        #row is now a list of the rows in the csv
        print(row)

#1
#print and count the total number of months 

#I know I need a with and an if statement
#if count of a certain month is more than 1 then dont count it
#the with statement would be for reading the rows of the first column of csv

with open (file_to_open, 'r') as this_csv_file:
    




#2
#calculate and print the net total for the entire period
#add function






    

