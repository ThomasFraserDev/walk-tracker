import json
from pathlib import Path

DATAPATH = Path("data/walks.json")

def load_data(): # Function for reading data from walks.json
    if not DATAPATH.exists(): # If walks.json doesn't exist, ask to create it
        create = input("No walking data file detected. Would you like to create one? [Y/N] ").strip().lower()
        
        if create == "y":
            DATAPATH.parent.mkdir(parents = True, exist_ok = True) # Create walks.json
            with open(DATAPATH, "w") as file:
                json.dump([], file, indent = 2)
            print("File created successfully!")
            return []
        else:
            return []
        
    if DATAPATH.stat().st_size == 0: # Handle empty file
        return []
        
    with open(DATAPATH, "r") as file:
        return json.load(file) # Return the read data
    
def save_data(data): # Function for writing data to walks.json
    with open(DATAPATH, "w") as file:
        json.dump(data, file, indent = 2) # Writing the data, with an indent of 2 for readability