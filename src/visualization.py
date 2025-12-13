import pandas as pd
import matplotlib.pyplot as plt
from data import load_data
from constants import NUMERIC_STATS

def plot_trend():
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