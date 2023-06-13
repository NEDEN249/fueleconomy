# import functions # Import functions.py file

# def main():
#     print("Welcome to the Fuel Economy Calculator") # Welcome message
#     print("=======================================")
#     print("What would you like to do?")
#     print("1. Calculate fuel economy")
#     print("2. Get Summary Data From Spreadsheet")
#     type = input("\nPlease enter 1 or 2: ") # User input to choose between 1 or 2
#     if type == "1":
#         functions.returnFuelEconomy()
#     elif type == "2": #summary data 
#         functions.generateSummaryData()

# if __name__ == "__main__":
#     main()
import functions # Import functions.py file

def main():
    while True:  # Run the loop indefinitely until the user chooses to exit
        print("What would you like to do?")
        print("1. Calculate fuel economy")
        print("2. Get Summary Data From Spreadsheet")
        print("3. Exit")
        choice = input("\nPlease enter your choice (1, 2, or 3): ")  # User input for choice

        if choice == "1":
            functions.returnFuelEconomy()
            while True:  # Nested loop for asking if the user wants to input more data
                more_data = input("Do you have more data you wish to input? (yes/no): ")
                if more_data.lower() == "no":
                    break  # Break the nested loop if the user doesn't want to input more data
                elif more_data.lower() == "yes":
                    functions.returnFuelEconomy()  # Run the function again for more data
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        elif choice == "2":
            functions.generateSummaryData()
        elif choice == "3":
            break  # Exit the loop if the user chooses option 3
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()     
