import pymongo
import pandas as pd
import json


client = pymongo.MongoClient("mongodb+srv://Rohan:Rrohhan1@cluster0.pqfms1m.mongodb.net/?retryWrites=true&w=majority")
 


DATA_FILE_PATH="insurance.csv"

DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print("Rows and columns:", df.shape)

    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
