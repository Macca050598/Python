import pandas as pd
import csv 
from datetime import datetime
#import the functions we made in data_entry
from data_entry import get_amount, get_category, get_date, get_desciption
import matplotlib.pyplot as plt

class CSV:
    CSV_File = "finance_data.csv"
    #df = dataframe
    #pd is the pandas we imported
    date_format = "%d-%m-%Y"
    COLUMNS = ["date", "amount", "category", "description"]
    @classmethod
    def initialise_csv(cls):
        try:
            pd.read_csv(cls.CSV_File)
        except FileNotFoundError:
            #declare the dataframe and declare necessary columns inside your csv
            df = pd.DataFrame(columns = cls.COLUMNS)
            #index false, means we won't be indexing
            df.to_csv(cls.CSV_File, index=False)
    #Initalising the csv file creates the file for 


    @classmethod
        #Create new dictionary that contains all the new data we wanted to add
    def add_entry(cls, date, amount, category, description):
        new_entry = {
                "date": date,
                "amount": amount,
                "category": category,
                "description": description,
        }
            #Then open the csv file
        with open(cls.CSV_File, "a", newline="") as csvfile: #This is known as the context manager
                writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS) #create a new writer
                writer.writerow(new_entry)
        print("Entry added successfully")
        
        
    @classmethod
    def get_transactions(cls, start_date, end_date):
        #df = dataframe
        df = pd.read_csv(cls.CSV_File)
        #By doing df[Date] you access all the columns in the date row of the csv
        df["date"] = pd.to_datetime(df["date"], format=CSV.date_format)
        #Make the start and end date time into date time objects
        start_date = datetime.strptime(start_date, CSV.date_format)
        end_date = datetime.strptime(end_date, CSV.date_format)

        #Checks if the date in the current row is greater than the start date and less than the end date
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]
        
        if filtered_df.empty:
            print("No transactions found in the given date range.")
        else:
            print(f"Transactions from {start_date.strftime(CSV.date_format)} to {end_date.strftime(CSV.date_format)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.date_format)}))
            
        total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
        total_expense = filtered_df[filtered_df["category"] == "Expenses"]["amount"].sum()
        print("\nSummary:")
        print(f"Total Income: £{total_income:.2f}")
        print(f"Total Expenses: £{total_expense:.2f}")
        print(f"Net Savings: £{(total_income - total_expense):.2f}")
        
        return filtered_df
        
def add():
    CSV.initialise_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date:", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_desciption()
    CSV.add_entry(date, amount, category, description)  
        
def plot_transactions(df):
    df.set_index('date', inplace = True)
    
    income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value =0)
    expense_df = df[df["category"] == "Expenses"].resample("D").sum().reindex(df.index, fill_value =0)
    
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transaction and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot ? (y/n)").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")
            
#Doesnt run the main function unless we choose an option 
if __name__ == "__main__":
    main()