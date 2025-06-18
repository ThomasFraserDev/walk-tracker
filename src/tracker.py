from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from utils import load_data, save_data

def add_entry():
    date = input("Enter the date of the walk [YYYY-MM-DD]:")
    steps = int(input("Enter your number of steps:"))
    distance = float(input("Enter the distance you walked (in km):"))
    time = float(input("Enter the length of your walk (in minutes): "))
    elevGain = float(input("Enter the elevation gain of your walk (in meters):"))
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
    data = load_data()
    if not data:
        print("No data available.")
        return
    df = pd.DataFrame(data)
    print("\n---------- Total Stats ----------")
    print(f"Total walks: {len(df)}")
    print(f"Total steps: {df['steps'].sum()}")
    print(f"Total distance (in km): {df['distanceKm'].sum()}")
    print(f"Total time (in minutes): {df['timeMins'].sum()}")
    print(f"Total elevation gain (in meters): {df['elevGain'].sum()}")

def show_stats():
    data = load_data()
    if not data:
        print("No data available.")
        return
    date = input("Enter the date to view stats for [YYYY-MM-DD]: ").strip()
    df = pd.DataFrame(data)
    day_stats = df[df['date'] == date]
    if day_stats.empty:
        print(f"No data found for {date}.")
    else:
        print(f"\n---------- Stats for {date}: ----------")
        print(day_stats.to_string(index=False))
    
def show_averages():
    pass

def show_comparison():
    pass

def plot_trend():
    pass
    
def main():
    while True:
        print("Choose an option:\n[1] Add an entry\n[2] Show your total stats\n[3] Show your stats from a specific day\n[4] Show your averages across a timeframe\n[5] Show a comparison between stats\n[6] Plot a trend of a specified stat\n[7] Quit")
        choice = input()
        if choice == "1":
            add_entry()
        elif choice == "2":
            show_totals()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            show_averages()
        elif choice == "5":
            show_comparison()
        elif choice == "6":
            plot_trend()
        elif choice == "7":
            break
            
    
if __name__ == "__main__":
    main()