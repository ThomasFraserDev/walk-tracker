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
        row = day_stats.iloc[0]
        print(f"\n---------- Stats for {date}: ----------")
        print(f"Steps: {row['steps']}")
        print(f"Distance (in km): {row['distanceKm']}")
        print(f"Time (in minutes): {row['timeMins']}")
        print(f"Elevation gain (in meters): {row['elevGain']}")
        print(f"Average heart rate (bpm): {row['heartRate']}")
        print(f"Pace (min/km): {row['paceKm']}")
        print(f"Step length (m): {row['stepLenM']}")
    
def show_averages():
    data = load_data()
    if not data:
        print("No data available.")
        return

    print("Enter a date range for averages or leave blank for all time.")
    start = input("Start date [YYYY-MM-DD] (leave blank for earliest): ").strip()
    end = input("End date [YYYY-MM-DD] (leave blank for latest): ").strip()

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])

    if start:
        df = df[df['date'] >= pd.to_datetime(start)]
    if end:
        df = df[df['date'] <= pd.to_datetime(end)]

    if df.empty:
        print("No data in the specified range.")
        return

    print("\n---------- Averages ----------")
    print(f"Average steps: {df['steps'].mean():.2f}")
    print(f"Average distance (in km): {df['distanceKm'].mean():.2f}")
    print(f"Average time (in minutes): {df['timeMins'].mean():.2f}")
    print(f"Average elevation gain (in meters): {df['elevGain'].mean():.2f}")
    print(f"Average heart rate (bpm): {df['heartRate'].mean():.2f}")
    print(f"Average pace (min/km): {df['paceKm'].mean():.2f}")
    print(f"Average step length (m): {df['stepLenM'].mean():.2f}")
    
def show_comparison():
    data = load_data()
    if not data:
        print("No data available.")
        return

    print("Enter two date ranges to compare.")
    start1 = input("First range start [YYYY-MM-DD] (blank for earliest): ").strip()
    end1 = input("First range end [YYYY-MM-DD] (blank for latest): ").strip()
    start2 = input("Second range start [YYYY-MM-DD] (blank for earliest): ").strip()
    end2 = input("Second range end [YYYY-MM-DD] (blank for latest): ").strip()

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])

    df1 = df.copy()
    if start1:
        df1 = df1[df1['date'] >= pd.to_datetime(start1)]
    if end1:
        df1 = df1[df1['date'] <= pd.to_datetime(end1)]

    df2 = df.copy()
    if start2:
        df2 = df2[df2['date'] >= pd.to_datetime(start2)]
    if end2:
        df2 = df2[df2['date'] <= pd.to_datetime(end2)]

    if df1.empty or df2.empty:
        print("No data in one or both ranges.")
        return

    stats = ['steps', 'distanceKm', 'timeMins', 'elevGain', 'heartRate', 'paceKm', 'stepLenM']
    print("\nStat              | Range 1   | Range 2   | Diff")
    print("-" * 50)
    for stat in stats:
        if stat in ["heartRate", "paceKm", "stepLenM"]:
            t1 = round(df1[stat].mean(), 2)
            t2 = round(df2[stat].mean(), 2)
        else:
            t1 = df1[stat].sum()
            t2 = df2[stat].sum()
        diff = abs(t1 - t2)
        print(f"{stat:<17} {t1:>9.2f} {t2:>9.2f} {diff:>9.2f}")
    
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