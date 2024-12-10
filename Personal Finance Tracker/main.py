import pandas as pd
import csv 
from datetime import datetime

class CSV:
    CSV_File = "finance_data.csv"
    #df = dataframe
    #pd is the pandas we imported
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
# CSV.initialise_csv()
CSV.add_entry("20-7-2024", 125.65, "Income", "Salary")