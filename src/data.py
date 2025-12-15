import json
import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/walks.json")

def load_data(): # Function for reading data from walks.json
    if not DATA_PATH.exists(): # If walks.json doesn't exist, ask to create it
        create = input("No walking data file detected. Would you like to create one? [Y/N] ").strip().lower()
        
        if create == "y":
            DATA_PATH.parent.mkdir(parents = True, exist_ok = True) # Create walks.json
            with open(DATA_PATH, "w") as file:
                json.dump([], file, indent = 2)
            print("File created successfully!")
            return []
        else:
            return []
        
    if DATA_PATH.stat().st_size == 0: # Handle empty file
        return []
        
    with open(DATA_PATH, "r") as file:
        return json.load(file) # Return the read data
    
def save_data(data): # Function for writing data to walks.json
    with open(DATA_PATH, "w") as file:
        json.dump(data, file, indent = 2) # Writing the data, with an indent of 2 for readability
        
def export_csv(): # Function that exports walk data as a csv
    data = load_data
    df = pd.DataFrame(data)
    df.to_csv('walks.csv', encoding='utf-8', index=False)
    print("Data exported as walks.csv")