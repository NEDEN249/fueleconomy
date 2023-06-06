import xlrd
import xlwt
import openpyxl as xl

def calculate_fuel_economy(kilometresDriven, litresUsed): # Function to calculate fuel economy by litres per 100km
    fuelEconomy =  (litresUsed / kilometresDriven) * 100
    return fuelEconomy

print("Welcome to the Fuel Economy Calculator") # Welcome message
print("=======================================")
print("what would you like to do?")
print("1. Calculate fuel economy")
print("2. Get Summary Data From Spreadsheet")
type = input("Please enter 1 or 2: ") # User input to choose between 1 or 2
if type == "1":
    kilometresDriven = input("Please enter the number of kilometres driven: ") # User input for kilometres driven
    litresUsed = input("Please enter the number of litres used: ") # User input for litres used
    fuelEconomy = calculate_fuel_economy(int(kilometresDriven), int(litresUsed)) # Calling the function to calculate fuel economy
    print("Your fuel economy is: " + str(fuelEconomy) + " litres per 100km") # Print fuel economy
    print("would you like to add this data to a spreadsheet?")
    answer = input("Please enter yes or no: ") # User input to choose between yes or no
    if answer == "yes":
        print("Data added to spreadsheet")
elif type == "2":
    print("Summary Data") # Print summary data