import pandas as pd
from data import load_data
from rich.console import Console
from rich.table import Table

console = Console()

def show_totals(): # Function that shows total stats, formatted in a Rich table
    data = load_data()
    if not data:
        print("No data available.")
        return
    df = pd.DataFrame(data)
    
    table = Table(title="Total Stats", show_lines=True)
    table.add_column("Metric", style="bright_magenta")
    table.add_column("Value", justify="right", style="bright_yellow")

    table.add_row("Total walks", f"{len(df)}")
    table.add_row("Total steps", f"{df['steps'].sum():.0f}")
    table.add_row("Total distance (km)", f"{df['distance'].sum():.2f}")
    table.add_row("Total time (mins)", f"{df['time'].sum():.2f}")
    table.add_row("Total elevation gain (m)", f"{df['elev_gain'].sum():.2f}")

    temp_counts = df['temperature'].value_counts() # Count the amount of times each temperature appears
    weather_counts = df['weather'].value_counts() # Count the amount of times each weather appears
    time_counts = df['time_of_day'].value_counts() # Count the amount of times each time of day appears

    table.add_row("Total hot walks", f"{temp_counts.get('hot', 0)}")
    table.add_row("Total warm walks", f"{temp_counts.get('warm', 0)}")
    table.add_row("Total cold walks", f"{temp_counts.get('cold', 0)}")
    table.add_row("Total sunny walks", f"{weather_counts.get('sunny', 0)}")
    table.add_row("Total rainy walks", f"{weather_counts.get('raining', 0)}")
    table.add_row("Total snowy walks", f"{weather_counts.get('snowing', 0)}")
    table.add_row("Total cloudy walks", f"{weather_counts.get('cloudy', 0)}")
    table.add_row("Total windy walks", f"{weather_counts.get('windy', 0)}")
    table.add_row("Total morning walks", f"{time_counts.get('morning', 0)}")
    table.add_row("Total afternoon walks", f"{time_counts.get('afternoon', 0)}")
    table.add_row("Total evening walks", f"{time_counts.get('evening', 0)}")
    table.add_row("Total night walks", f"{time_counts.get('night', 0)}")

    console.print(table)

def show_stats(): # Function that shows stats for a specified date, formatted in a Rich table
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
        for i, row in day_stats.iterrows():
            table = Table(title=f"Stats for {date} - Walk #{i + 1}", show_lines=True)
            table.add_column("Metric", style="bright_magenta")
            table.add_column("Value", justify="right", style="bright_yellow")

            table.add_row("Steps", f"{row['steps']:.0f}")
            table.add_row("Distance (km)", f"{row['distance']:.2f}")
            table.add_row("Time (mins)", f"{row['time']:.2f}")
            table.add_row("Elevation gain (m)", f"{row['elev_gain']:.2f}")
            table.add_row("Temperature", f"{row['temperature']}")
            table.add_row("Weather", f"{row['weather']}")
            table.add_row("Time of day", f"{row['time_of_day']}")
            table.add_row("Average heart rate (bpm)", f"{row['heart_rate']:.2f}")
            table.add_row("Pace (min/km)", f"{row['pace']:.2f}")
            table.add_row("Step length (m)", f"{row['step_len']:.2f}")

            console.print(table)

def show_averages(): # Function that shows the average stats across a date range or all time, formatted in a Rich table
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
        df = df[df['date'] >= pd.to_datetime(start)] # Filter the data to start from the entered start date
    if end:
        df = df[df['date'] <= pd.to_datetime(end)] # Filter the data to end at the entered end date

    if df.empty:
        print("No data in the specified date range.")
        return

    table = Table(title="Averages", show_lines=True)
    table.add_column("Metric", style="bright_magenta")
    table.add_column("Value", justify="right", style="bright_yellow")

    table.add_row("Average steps", f"{df['steps'].mean():.2f}")
    table.add_row("Average distance (km)", f"{df['distance'].mean():.2f}")
    table.add_row("Average time (mins)", f"{df['time'].mean():.2f}")
    table.add_row("Average elevation gain (m)", f"{df['elev_gain'].mean():.2f}")
    table.add_row("Average heart rate (bpm)", f"{df['heart_rate'].mean():.2f}")
    table.add_row("Average pace (min/km)", f"{df['pace'].mean():.2f}")
    table.add_row("Average step length (m)", f"{df['step_len'].mean():.2f}")
    table.add_row("Most common temperature", f"{df['temperature'].mode()[0] if not df['temperature'].mode().empty else 'N/A'}")
    table.add_row("Most common weather", f"{df['weather'].mode()[0] if not df['weather'].mode().empty else 'N/A'}")
    table.add_row("Most common time of day", f"{df['time_of_day'].mode()[0] if not df['time_of_day'].mode().empty else 'N/A'}")

    console.print(table)

def show_comparison(): # Function that compares walk data across two date ranges, formatted in Rich tables
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
        df1 = df1[df1['date'] >= pd.to_datetime(start1)] # Filter the first dataset to start from the entered start date
    if end1:
        df1 = df1[df1['date'] <= pd.to_datetime(end1)] # Filter the first dataset to end at the entered end date

    df2 = df.copy()
    if start2:
        df2 = df2[df2['date'] >= pd.to_datetime(start2)] # Filter the second dataset to start from the entered start date
    if end2:
        df2 = df2[df2['date'] <= pd.to_datetime(end2)] # Filter the second dataset to end at the entered end date

    if df1.empty or df2.empty:
        print("No data in one or both ranges.")
        return

    stats = ['steps', 'distance', 'time', 'elev_gain', 'heart_rate', 'pace', 'step_len']

    table = Table(title="Comparison (Totals)", show_lines=True)
    table.add_column("Stat", style="bright_magenta")
    table.add_column("Range 1", justify="right", style="bright_yellow")
    table.add_column("Range 2", justify="right", style="bright_green")
    table.add_column("Diff (R1 - R2)", justify="right", style="bright_cyan")

    for stat in stats:
        t1 = df1[stat].sum()
        t2 = df2[stat].sum()
        diff = t1 - t2
        table.add_row(stat, f"{t1:.2f}", f"{t2:.2f}", f"{diff:.2f}")

    console.print(table)

    table2 = Table(title="Comparison (Categorical Modes)", show_lines=True)
    table2.add_column("Category", style="bright_magenta")
    table2.add_column("Range 1", style="bright_yellow")
    table2.add_column("Range 2", style="bright_green")

    table2.add_row("Temperature",
                      f"{df1['temperature'].mode()[0] if not df1['temperature'].mode().empty else 'N/A'}",
                      f"{df2['temperature'].mode()[0] if not df2['temperature'].mode().empty else 'N/A'}")
    table2.add_row("Weather",
                      f"{df1['weather'].mode()[0] if not df1['weather'].mode().empty else 'N/A'}",
                      f"{df2['weather'].mode()[0] if not df2['weather'].mode().empty else 'N/A'}")
    table2.add_row("Time of day",
                      f"{df1['time_of_day'].mode()[0] if not df1['time_of_day'].mode().empty else 'N/A'}",
                      f"{df2['time_of_day'].mode()[0] if not df2['time_of_day'].mode().empty else 'N/A'}")

    console.print(table2)

def show_maxes(): # Function that prints the highest values for eligible stats, formatted in a Rich table
    data = load_data()
    if not data:
        print("No data available.")
        return
    df = pd.DataFrame(data)

    table = Table(title="Max Stats", show_lines=True)
    table.add_column("Metric", style="bright_magenta")
    table.add_column("Value", justify="right", style="bright_yellow")

    table.add_row("Most steps on a walk", f"{df['steps'].max():.0f}")
    table.add_row("Longest walk (km)", f"{df['distance'].max():.2f}")
    table.add_row("Longest walk (minutes)", f"{df['time'].max():.2f}")
    table.add_row("Highest elevation gain (m)", f"{df['elev_gain'].max():.2f}")
    table.add_row("Highest average heart rate (bpm)", f"{df['heart_rate'].max():.2f}")
    table.add_row("Fastest pace (min/km)", f"{df['pace'].min():.2f}")

    console.print(table)