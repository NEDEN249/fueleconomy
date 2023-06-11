from openpyxl import Workbook, load_workbook
from datetime import date
import matplotlib.pyplot as plt

#Current Date in DD/MM/YYYY format
today = date.today()
today1 = today.strftime("%d/%m/%Y")

def calculate_fuel_economy(kilometresDriven, litresUsed): # Function to calculate fuel economy by litres per 100km
    fuelEconomy =  (litresUsed / kilometresDriven) * 100
    return fuelEconomy

def insert_new_data(d,f): #Function to insert new data into spreadsheet
    book = load_workbook('testDocument.xlsx') # Load workbook
    sheet = book.active # Load active sheet
    new_data = (today1, int(d), int(f))
    sheet.append(new_data)
    book.save('testDocument.xlsx')
    print("Data successfully added to spreadsheet")

def printFuelEconomy(fuelEconomy):
    print("\nYour fuel economy is {:0.2f} litres per 100kms\n".format(fuelEconomy)) # Print fuel economy to 2 decimal places

def returnFuelEconomy():
    kilometresDriven = input("Please enter the number of kilometres driven: ") # User input for kilometres driven
    litresUsed = input("Please enter the number of litres used: ") # User input for litres used
    fuelEconomy = calculate_fuel_economy(float(kilometresDriven), float(litresUsed)) # Calling the function to calculate fuel economy
    printFuelEconomy(fuelEconomy)
    print("would you like to add this data to a spreadsheet?")
    answer = input("Please enter yes or no: ") # User input to choose between yes or no
    if answer == "yes":
        insert_new_data(kilometresDriven, litresUsed)
    #elif answer == "no": -> ask if want to see summary data 
    
def generateSummaryData():
    book = load_workbook('testDocument.xlsx') # Load workbook
    sheet = book.active # Load active sheet
    dict = {}
    for row in sheet.iter_rows():
        if row[0].value == "Date":
            continue # Skip
        if row[0].value not in dict.keys():
            temp = {str(row[0].value): [row[1].value, row[2].value]}
            dict.update(temp)
        else:
            dict[row[0].value].append("split")
            dict[row[0].value].append(row[1].value)
            dict[row[0].value].append(row[2].value)
    #for key, value in dict.items():
        #print(key, value)
    averages = []
    for key, value in dict.items():
        #print(key)
        if key == "Date":
            continue # Skip the first row
        #print(value[0])
        #print(value[1])
        averages.append(calculate_fuel_economy(int(value[0]), int(value[1])))
    fig,ax = plt.subplots()
    ax.bar(dict.keys(), averages)
    plt.show()