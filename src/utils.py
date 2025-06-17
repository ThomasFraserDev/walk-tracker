import json
from pathlib import Path

DATAPATH = Path("data/walks.json")

def load_data(): # function for reading data from walks.json
    if not DATAPATH.exists(): # if the file doesn't exist
        create = input("No walking data file detected. Would you like to create one? [Y/N] ").strip().lower()
        if create == "y":
            DATAPATH.parent.mkdir(parents=True, exist_ok=True) # create the file
            with open(DATAPATH, "w") as file:
                json.dump([], file)
            print("File created successfully")
            return []
        else:
            return []
    with open(DATAPATH, "r") as file:
        return json.load(file) # return the read data
    
def save_data(data): # function for writing data to the walks.json file
    with open(DATAPATH, "w") as file:
        json.dump(data, file, indent=2) # writing the data, with an indent of 2 for readability