import pandas as pd
from utils import load_data

def show_totals(): # Function that shows total stats
    data = load_data()
    if not data:
        print("No data available.")
        return
    df = pd.DataFrame(data)
    
    print("\n---------- Total Stats ----------")
    print(f"Total walks: {len(df)}")
    print(f"Total steps: {df['steps'].sum():.0f}")
    print(f"Total distance (in km): {df['distanceKm'].sum():.2f}")
    print(f"Total time (in minutes): {df['timeMins'].sum():.2f}")
    print(f"Total elevation gain (in meters): {df['elevGain'].sum():.2f}")

def show_stats(): # Function that shows stats for a specified date
    data = load_data()
    if not data:
        print("No data available.")
        return
    date = input("Enter the date to view stats for [YYYY-MM-DD]: ").strip() # Get date from user
    df = pd.DataFrame(data)
    day_stats = df[df['date'] == date] # Get the stats for the date
    
    if day_stats.empty:
        print(f"No data found for {date}.")
    else:
        for i, row in day_stats.iterrows(): # For each walk on the date
            print(f"\n---------- Stats for {date}: ----------")
            print(f"\nWalk #{i + 1}:")
            print(f"    Steps: {row['steps']:.0f}")
            print(f"    Distance (in km): {row['distanceKm']:.2f}")
            print(f"    Time (in minutes): {row['timeMins']:.2f}")
            print(f"    Elevation gain (in meters): {row['elevGain']:.2f}")
            print(f"    Temperature: {row['temperature']}")
            print(f"    Weather: {row['weather']}")
            print(f"    Time of day: {row['timeOfDay']}")
            print(f"    Average heart rate (bpm): {row['heartRate']:.2f}")
            print(f"    Pace (min/km): {row['paceKm']:.2f}")
            print(f"    Step length (m): {row['stepLenM']:.2f}")

def show_averages(): # Function that shows the average stats across a date range or all time
    data = load_data()
    if not data:
        print("No data available.")
        return

    print("Enter a date range for averages or leave blank for all time.") # Get start and end dates from user
    start = input("Start date [YYYY-MM-DD] (leave blank for earliest): ").strip()
    end = input("End date [YYYY-MM-DD] (leave blank for latest): ").strip()

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])

    if start:
        df = df[df['date'] >= pd.to_datetime(start)] # Set the dataframe to be each walk set after the start date
    if end:
        df = df[df['date'] <= pd.to_datetime(end)] # Set the dataframe to be each walk set before the end date

    if df.empty:
        print("No data in the specified date range.")
        return

    print("\n---------- Averages ----------")
    print(f"Average steps: {df['steps'].mean():.2f}")
    print(f"Average distance (in km): {df['distanceKm'].mean():.2f}")
    print(f"Average time (in minutes): {df['timeMins'].mean():.2f}")
    print(f"Average elevation gain (in meters): {df['elevGain'].mean():.2f}")
    print(f"Average heart rate (bpm): {df['heartRate'].mean():.2f}")
    print(f"Average pace (min/km): {df['paceKm'].mean():.2f}")
    print(f"Average step length (m): {df['stepLenM'].mean():.2f}")
    print(f"Most common temperature: {df['temperature'].mode()[0] if not df['temperature'].mode().empty else 'N/A'}")
    print(f"Most common weather: {df['weather'].mode()[0] if not df['weather'].mode().empty else 'N/A'}")
    print(f"Most common time of day: {df['timeOfDay'].mode()[0] if not df['timeOfDay'].mode().empty else 'N/A'}")

def show_comparison(): # Function that compares walk data across two date ranges
    data = load_data()
    if not data:
        print("No data available.")
        return

    print("Enter two date ranges to compare.") # Get date ranges from user
    start1 = input("First range start [YYYY-MM-DD] (blank for earliest): ").strip()
    end1 = input("First range end [YYYY-MM-DD] (blank for latest): ").strip()
    start2 = input("Second range start [YYYY-MM-DD] (blank for earliest): ").strip()
    end2 = input("Second range end [YYYY-MM-DD] (blank for latest): ").strip()

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])

    df1 = df.copy()
    if start1: # Set df1 to the data within the first date range
        df1 = df1[df1['date'] >= pd.to_datetime(start1)]
    if end1:
        df1 = df1[df1['date'] <= pd.to_datetime(end1)]

    df2 = df.copy()
    if start2: # Set df2 to the data within the second date range
        df2 = df2[df2['date'] >= pd.to_datetime(start2)]
    if end2:
        df2 = df2[df2['date'] <= pd.to_datetime(end2)]

    if df1.empty or df2.empty:
        print("No data in one or both ranges.")
        return

    stats = ['steps', 'distanceKm', 'timeMins', 'elevGain', 'heartRate', 'paceKm', 'stepLenM']
    print("\nStat              | Range 1   | Range 2   | Diff")
    print("-" * 45)
    for stat in stats:
        t1 = df1[stat].sum()
        t2 = df2[stat].sum()
        diff = t1 - t2
        print(f"{stat:<17} {t1:>9.2f} {t2:>9.2f} {diff:>9.2f}")
    
    print("\nCategorical Stats:")
    print(f"\nRange 1 - Most common temperature: {df1['temperature'].mode()[0] if not df1['temperature'].mode().empty else 'N/A'}")
    print(f"Range 1 - Most common weather: {df1['weather'].mode()[0] if not df1['weather'].mode().empty else 'N/A'}")
    print(f"Range 1 - Most common time of day: {df1['timeOfDay'].mode()[0] if not df1['timeOfDay'].mode().empty else 'N/A'}")
    print(f"\nRange 2 - Most common temperature: {df2['temperature'].mode()[0] if not df2['temperature'].mode().empty else 'N/A'}")
    print(f"Range 2 - Most common weather: {df2['weather'].mode()[0] if not df2['weather'].mode().empty else 'N/A'}")
    print(f"Range 2 - Most common time of day: {df2['timeOfDay'].mode()[0] if not df2['timeOfDay'].mode().empty else 'N/A'}")