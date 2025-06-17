from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from utils import load_data, save_data

def add_entry():
    date = input("Enter the date of the walk[YYYY-MM-DD]:")
    steps = int(input("Enter your number of steps:"))
    distance = float(input("Enter the distance you walked (in km):"))
    time = float(input("Enter the length of your walk (in minutes): "))
    elevGain = float(input("Enter the elevation gain of your walk (in km):"))
    heartRate =  float(input("Enter your average heart rate for the walk (in bpm):"))
    
    pace = round((time / distance), 2)
    stepLen = round((distance * 1000 / steps), 2)
    
    data = load_data()
    data.append({
        "date": date,
        "steps": steps,
        "distanceKm": distance,
        "timeMins": time,
        "elevGain":  elevGain,
        "heartRate": heartRate,
        "paceKm": pace,
        "stepLenM": stepLen
    })
    save_data(data)
    print("Your entry has been saved.")
    
def show_totals():
    pass

def show_stats():
    pass
    
def show_averages():
    pass

def show_comparison():
    pass
    
def main():
    pass   
    
if __name__ == "__main__":
    main()