import pandas as pd
import matplotlib.pyplot as plt
from utils import load_data

def plot_trend():
    data = load_data()
    if not data:
        print("No data available.")
        return
    
    valid_stats = ['steps', 'distanceKm', 'timeMins', 'elevGain', 'heartRate', 'paceKm', 'stepLenM']
    stat = input("Enter the stat to plot (steps, distanceKm, timeMins, elevGain, heartRate, paceKm, stepLenM): ").strip()
    
    if stat not in valid_stats: # If entered stat isn't valid
        print(f"Invalid stat. Choose from {valid_stats}")
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