from pymongo import MongoClient
import csv
import pandas as pd

# Connect to MongoDB locally
client = MongoClient("mongodb://localhost:27017/")
# Get the reckoning database
db = client["reckoning"]


# File paths
file_paths = [
    "/Users/amatamuadthong/Desktop/467_multi_media/Project/Reckoning/weekly_csv/week_4.csv",
    "/Users/amatamuadthong/Desktop/467_multi_media/Project/Reckoning/weekly_csv/week_5.csv",
    "/Users/amatamuadthong/Desktop/467_multi_media/Project/Reckoning/weekly_csv/week_6.csv",
    "/Users/amatamuadthong/Desktop/467_multi_media/Project/Reckoning/weekly_csv/week_7.csv",
    "/Users/amatamuadthong/Desktop/467_multi_media/Project/Reckoning/EG4-DBDump.csv"
]

# Read each CSV file into a DataFrame and print it
def print_files():
    for file_path in file_paths:
        print(f"File: {file_path}")
        try:
            df = pd.read_csv(file_path, encoding='ISO-8859-1')
            print(df.to_string())
            print("\n")
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.\n")
        except Exception as e:
            print(f"Error reading file {file_path}: {e}\n")

# check if collections exist
def print_collections():
    # List all collections in the reckoning database
    collections = db.list_collection_names()
    print(collections)

def print_collection_1():
    collections = db["collection 1"]
    for x in collections.find():
        print(x)

def print_collection_2():
    collections = db["collection 2"]
    for x in collections.find():
        print(x)

# print_files()
# print_collections()
# print_collection_1()
# print_collection_2()
    