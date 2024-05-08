from pymongo import MongoClient
import csv
import pandas as pd

# Connect to MongoDB locally
client = MongoClient("mongodb://localhost:27017/")
# Get the reckoning database
db = client["reckoning"]
collection1 = db["collection 1"]
collection2 = db["collection 2"]


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
    for x in collection1.find():
        print(x)

def print_collection_2():
    for x in collection2.find():
        print(x)

from pymongo import MongoClient

# Connect to MongoDB locally
client = MongoClient("mongodb://localhost:27017/")
# Get the reckoning database
db = client["reckoning"]
collection1 = db["collection 1"]
collection2 = db["collection 2"]

def print_my_work():
    query = {"Test Owner": "Rmata Muadthong"}
    count = 0
    printed_ids = set()
    for collection in [collection1, collection2]:
        my_work = collection.find(query)
        for x in my_work:
            if x['_id'] not in printed_ids:
                # print(x)
                printed_ids.add(x['_id'])
                count += 1
    print("\nTotal: ", count)
    print(printed_ids)

# -------------------------------------
# print_files()
# print_collections()
# print_collection_1()
# print_collection_2()
print_my_work()
    