import functions # Import functions.py file

def main():
    print("Welcome to the Fuel Economy Calculator") # Welcome message
    print("=======================================")
    print("What would you like to do?")
    print("1. Calculate fuel economy")
    print("2. Get Summary Data From Spreadsheet")
    type = input("\nPlease enter 1 or 2: ") # User input to choose between 1 or 2
    if type == "1":
        functions.returnFuelEconomy()
    elif type == "2": #summary data 
        functions.generateSummaryData()

if __name__ == "__main__":
    main()
        
