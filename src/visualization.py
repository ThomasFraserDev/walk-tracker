import pandas as pd
import matplotlib.pyplot as plt
from data import load_data
from constants import NUMERIC_STATS

def plot_trend(): # Function that plots a trend of an inputted stat
    data = load_data()
    if not data:
        print("No data available.")
        return
    
    stat = input(f"Enter the stat to plot {NUMERIC_STATS}: ").strip()
    
    if stat not in NUMERIC_STATS: # If entered stat isn't valid
        print(f"Invalid stat. Choose from {NUMERIC_STATS}")
        return
    
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date') # Sort all the walks by date
    
    # Plotting the graph
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df[stat], marker='o', linestyle='-', linewidth=2)
    plt.xlabel('Date')
    plt.ylabel(stat.capitalize())
    plt.title(f'{stat.capitalize()} Over Time')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def weekly_steps(): # Function that plots a bar chart of total steps walked weekly
    data = load_data()
    if not data:
        print("No data available.")
        return
    
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date') # Sort all the walks by date
    
    weekly = ( # Sort the data to into weeks, summing up the steps of each one
        df.set_index('date')
          .groupby(pd.Grouper(freq='W-MON'))['steps']
          .sum()
          .reset_index()
    )
    weekly['week_label'] = weekly['date'].dt.strftime('%Y-%m-%d')

    plt.figure(figsize=(10, 6))
    plt.bar(weekly['week_label'], weekly['steps'], color='skyblue')
    plt.xlabel('Week (beginning Monday)')
    plt.ylabel('Steps')
    plt.title('Weekly Steps')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
def monthly_steps(): # Function that plots a bar chart of total steps walked monthly
    data = load_data()
    if not data:
        print("No data available.")
        return
    
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date') # Sort all the walks by date
    
    monthly = ( # Sort the data to into months, summing up the steps of each one
        df.set_index('date')
          .groupby(pd.Grouper(freq='MS'))['steps']
          .sum()
          .reset_index()
    )
    monthly['month_label'] = monthly['date'].dt.strftime('%Y-%m-%d')

    plt.figure(figsize=(10, 6))
    plt.bar(monthly['month_label'], monthly['steps'], color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Steps')
    plt.title('Monthly Steps')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
def weekly_distance(): # Function that plots a bar chart of total distance walked weekly
    data = load_data()
    if not data:
        print("No data available.")
        return
    
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date') # Sort all the walks by date
    
    weekly = ( # Sort the data to into weeks, summing up the distance of each one
        df.set_index('date')
          .groupby(pd.Grouper(freq='W-MON'))['distance']
          .sum()
          .reset_index()
    )
    weekly['week_label'] = weekly['date'].dt.strftime('%Y-%m-%d')

    plt.figure(figsize=(10, 6))
    plt.bar(weekly['week_label'], weekly['steps'], color='skyblue')
    plt.xlabel('Week (beginning Monday)')
    plt.ylabel('Distance (km)')
    plt.title('Weekly Distance')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
def monthly_distance(): # Function that plots a bar chart of total distance walked monthly
    data = load_data()
    if not data:
        print("No data available.")
        return
    
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date') # Sort all the walks by date
    
    monthly = ( # Sort the data to into months, summing up the distance each one
        df.set_index('date')
          .groupby(pd.Grouper(freq='MS'))['distance']
          .sum()
          .reset_index()
    )
    monthly['month_label'] = monthly['date'].dt.strftime('%Y-%m')

    plt.figure(figsize=(10, 6))
    plt.bar(monthly['month_label'], monthly['distance'], color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Distance (km)')
    plt.title('Monthly Distance')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()