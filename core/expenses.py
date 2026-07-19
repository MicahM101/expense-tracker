import csv
import os
from datetime import datetime

# getting the name of the current directory
BASE_DIR = os.path.dirname(__file__)

# getting the path for the csv file for expenses
CSV_PATH = os.path.join(BASE_DIR, "..", "data", "expenses.csv")

# code to open the file, if there, and create it if not there

#List of headings for CSV file
headerList = ["ID", "Date", "Amount", "Category", "Description"]

def initialize_CSV():
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headerList)


# Code for adding a new expense to the CSV file    
def addExpense(amount, category, description):
    initialize_CSV()
    # initialize the date for the new entry
    currentDate = datetime.today().strftime("%Y-%m-%d")
    # initialize the id for the new entry
    with open(CSV_PATH, "r", newline='') as rfile:
        reader = csv.reader(rfile)
        lastRow = None
        for row in reader:
            lastRow = row

    currentID = lastRow[0]        
    if currentID == "ID":
        id = 1
    else:
        id = int(currentID) + 1

    # Code to create the new row and write it into the CSV file 
    with open(CSV_PATH, "a", newline='') as afile:
        writer = csv.writer(afile)
        newRow = [id, currentDate, amount, category, description]
        writer.writerow(newRow)
        

def loadExpense():
    initialize_CSV
    expenses = []
    with open(CSV_PATH, 'r', newline='') as loadFile:
        loadReader = csv.reader(loadFile)
        for row in loadReader:
            expenses.append(row)
    return expenses

def deleteExpense(id):
    initialize_CSV
    with open(CSV_PATH, 'r', newline='') as rfile:
        reader = csv.reader(rfile)
        buffer_list = list(reader)
    
    buffer_list = [row for row in buffer_list if row[0] != str(id)]

    with open(CSV_PATH, "w", newline = '') as wfile:
        writer = csv.writer(wfile)
        writer.writerows(buffer_list)


def summaryExpenses():

    # Code to create a new a dictionary holding the total spend of all categories identified in the CSV file
    summaryDict = {}
    with open(CSV_PATH, 'r', newline='') as rfile:
        summaryReader = csv.reader(rfile)
        next(summaryReader)
        for row in summaryReader:
            if row[3] in summaryDict:
                summaryDict[row[3]] += float(row[2])
            else:
                summaryDict[row[3]] = float(row[2])
    
    return summaryDict













