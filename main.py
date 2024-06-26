from pymongo import MongoClient
import csv
import pandas as pd
# pd.options.display.max_columns = None
# pd.options.display.max_rows = None

# Connect to MongoDB locally
client = MongoClient("mongodb://localhost:27017/")

# File paths
file_paths = [
    "/Users/amatamuadthong/Desktop/467_multi_media/Project/Reckoning/weekly_csv/week_4.csv",
    "/Users/amatamuadthong/Desktop/467_multi_media/Project/Reckoning/weekly_csv/week_5.csv",
    "/Users/amatamuadthong/Desktop/467_multi_media/Project/Reckoning/weekly_csv/week_6.csv",
    "/Users/amatamuadthong/Desktop/467_multi_media/Project/Reckoning/weekly_csv/week_7.csv",
    "EG4-DBDump.csv"
]

# Read each CSV file into a DataFrame and print it
for file_path in file_paths:
    print(f"File: {file_path}")
    # try:
    #     df = pd.read_csv(file_path, encoding='ISO-8859-1')
    #     print(df.to_string())
    #     print("\n")
    # except FileNotFoundError:
    #     print(f"Error: File {file_path} not found.\n")
    # except Exception as e:
    #     print(f"Error reading file {file_path}: {e}\n")
