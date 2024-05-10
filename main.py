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

# my work collection 1
def print_my_work():
    query = {"Test Owner": "Rmata Muadthong"}
    count = 0
    # printed_names = set()
    for collection in [collection1]:
        my_work = collection.find(query)
        for x in my_work:
            # name = x.get("Test case")
            # if name not in printed_names:
                print(x)
                # printed_names.add(name)
                count += 1
    print("\nTotal: ", count)
    # sees test case stores in set: duplicate_test_case
    # print(printed_names)

def print_test_case():
    count = 0
    for collection in [collection1, collection2]:
        for test in collection.find({}, {"Test owner":1}):
            print(test.get("Test owner"))
            count += 1
    print("\nTotal: ", count)

def print_repeatable():
    query1 = {"Repeatable?": {"$regex": "^\s*Yes\s*$", "$options": "i"}}
    # "$regex": "^\s*Yes\s*$" means the value starts (^) and ends ($) with "Yes",
    # and there can be any amount of whitespace (\s*) before and after "Yes"
    # "$options": "i" makes the regex case-insensitive
    query2 = {
        "Repeatable?": {"$regex": "^\s*yes\s*$", "$options": "i"},
        "Test Owner": {"$not": {"$eq": "Rmata Muadthong"}}
    }
    count1 = 0
    count2 = 0
    for collection1_loop in [collection1]:
        repeatable = collection1_loop.find(query1)
        for x in repeatable:
            print(x)
            count1 += 1
    print("\n-----------------------\n")
    for collection2_loop in [collection2]:
        repeatable = collection2_loop.find(query1)
        for x in repeatable:
            print(x)
            count2 += 1
    total_count = count1 + count2
    print(f"\nTotal repeatable count: {total_count}\nRepeatable collection 1: {count1}\nRepeatable collection 2: {count2}")

def print_blocker():
    query1 = {"Blocker?": {"$regex": "^\s*Yes\s*$", "$options": "i"}}
    # "$regex": "^\s*Yes\s*$" means the value starts (^) and ends ($) with "Yes",
    # and there can be any amount of whitespace (\s*) before and after "Yes"
    # "$options": "i" makes the regex case-insensitive
    query2 = {
        "Blocker?": {"$regex": "^\s*yes\s*$", "$options": "i"},
        "Test Owner": {"$not": {"$eq": "Rmata Muadthong"}}
    }
    count1 = 0
    count2 = 0
    for collection1_loop in [collection1]:
        blocker = collection1_loop.find(query1)
        for x in blocker:
            print(x)
            count1 += 1
    print("\n-----------------------\n")
    for collection2_loop in [collection2]:
        blocker = collection2_loop.find(query1)
        for x in blocker:
            print(x)
            count2 += 1
    total_count = count1 + count2
    print(f"\nTotal Blocker Bugs count: {total_count}\nBlocker Bugs collection 1: {count1}\nBlocker Bugs collection 2: {count2}")

def print_3_19_24():
    query1 = {"Build #": {"$regex": ".*3\s*\/\s*19\s*\/\s*24.*", "$options": "i"}}
    # "$regex": "^\s*Yes\s*$" means the value starts (^) and ends ($) with "Yes",
    # and there can be any amount of whitespace (\s*) before and after "Yes"
    # "$options": "i" makes the regex case-insensitive
    query2 = {
        "Build #": {"$regex": ".*3\s*\/\s*19\s*\/\s*24.*", "$options": "i"},
        "Test Owner": {"$not": {"$eq": "Rmata Muadthong"}}
    }
    count1 = 0
    count2 = 0
    for collection1_loop in [collection1]:
        march = collection1_loop.find(query1)
        for x in march:
            print(x)
            count1 += 1
    print("\n-----------------------\n")
    for collection2_loop in [collection2]:
        march = collection2_loop.find(query1)
        for x in march:
            print(x)
            count2 += 1
    total_count = count1 + count2
    print(f"\nTotal 3/19/24 build count: {total_count}\n3/19/24 build collection 1: {count1}\n3/19/24 build collection 2: {count2}")

def print_3_case():
    # for collection in collection2:
    first_doc = collection2.find_one()
    total_count = collection2.count_documents({})
    middle_count = total_count // 2
    middle_doc = collection2.find().limit(1).skip(middle_count).next()
    last_doc = collection2.find().sort([("_id", -1)]).limit(1)
    print(f"\nFirst case:\n\n{first_doc}\n\nMiddle case: \n\n{middle_doc}\n\nFinal case:\n\n{next(last_doc)}\n")
# -------------------------------------
# print_files()
# print_collections()
# print_collection_1()
# print_collection_2()
# print_my_work()
# print_test_case()
# print_repeatable()
# print_blocker()
# print_3_19_24()
print_3_case()

    