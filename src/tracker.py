from rich.console import Console
from rich.table import Table
from data import load_data, save_data
from prediction import estimate_heartRate
from constants import TEMP_CHOICES, WEATHER_CHOICES, TIME_CHOICES, EDITABLE_FIELDS
from validation import validate_date, parse_positive_int, parse_positive_float, validate_choice, parse_yes_no

console = Console()

def add_entry(): # Function that adds an entry to the user's walks
    data = load_data()
    try:
        id = max([entry.get("id", 0) for entry in data], default=0) + 1 # Set a walk's id to be the current highest id + 1
        
        date = input("Enter the date of the walk [YYYY-MM-DD]: ")
        date = validate_date(date) # Validate that the entered date is in the correct format
        if not date:
            print("Invalid date. Use YYYY-MM-DD.")
            return
        
        steps = int(input("Enter your number of steps: "))
        steps = parse_positive_int(steps) # Validate that the entered amount of steps is an integer
        if steps is None:
            print("Steps must be a positive whole number.")
            return
        
        distance = float(input("Enter the distance you walked (in km): "))
        distance = parse_positive_float(distance) # Validate that the entered distance is a positive float
        if distance is None:
            print("Distance must be a positive number.")
            return
        
        time = float(input("Enter the length of your walk (rounded to nearest minute): "))
        time = parse_positive_int(time) # Validate that the entered time is a positive integer 
        if time is None:
            print("Time must be a positive whole number.")
            return
        
        elev_gain = float(input("Enter the elevation gain of your walk (in meters): "))
        elev_gain = parse_positive_float(elev_gain) # Validate that the entered elevation gain is a positive float
        if elev_gain is None:
            print("Elevation gain must be a positive number.")
            return
        
        temp = str(input("What was the temperature like on your walk? [ hot | warm | cold ]: "))
        temp = validate_choice(temp, TEMP_CHOICES) # Validate that the entered temperature is valid
        if not temp:
            print("Invalid temperature. Choose one of: hot, warm, cold.")
            return
        
        weather = str(input("What was the weather like on your walk? [ sunny | raining | snowing | cloudy | windy ]: "))
        weather = validate_choice(weather, WEATHER_CHOICES) # Validate that the entered weather is valid
        if not weather:
            print("Invalid weather. Choose one of: sunny, raining, snowing, cloudy, windy.")
            return
      
        time_of_day = str(input("What time of day was your walk at? [ morning | afternoon | evening | night ]: "))
        time_of_day = validate_choice(time_of_day, TIME_CHOICES) # Validate that the entered time of day is valid
        if not time_of_day:
            print("Invalid time of day. Choose one of: morning, afternoon, evening, night.")
            return
       
        hr_choice = input("Do you know your average heart rate from the walk? (y/n): ").lower()
        hr_choice = parse_yes_no(hr_choice) # Validate that the entered choice choice for estimating heart rate is valid
        if hr_choice is None:
            print("Please answer with y/n.")
            return
        
        if hr_choice:
            heart_rate = input("Enter your average heart rate for the walk (in bpm): ")
            heart_rate = parse_positive_float(heart_rate) # Validate that the entered heart rate is a positive float
            if heart_rate is None:
                print("Heart rate must be a positive number.")
                return
        else:
            heart_rate = estimate_heartRate(steps, distance, time, elev_gain, temp, weather, time_of_day) # Estimate the heart rate in bpm for the walk
            print(f"Estimated heart rate: {heart_rate:.1f} bpm")
        
        pace = round((time / distance), 2) # Calculate pace
        step_len = round((distance * 1000 / steps), 2) # Calculate average step length
        
        data = load_data()
        data.append({ # Add the entries to the dataset
            "id": id,
            "date": date,
            "steps": steps,
            "distance": distance,
            "time": time,
            "elev_gain": elev_gain,
            "temperature": temp,
            "weather": weather,
            "time_of_day": time_of_day,
            "heart_rate": heart_rate,
            "pace": pace,
            "step_len": step_len
        })
        
        save_data(data)
        print("Your entry has been saved.")
        
    except ValueError:
        print("Please enter valid numeric or textual values.")
        
def delete_entry(): # Function that deletes an entry from the user's walks
    data = load_data()
    removal_id = int(input("Enter the ID of the walk you wish to be deleted: "))
    removal_id = parse_positive_int(removal_id) # Validate the entered id is a positive integer
    if removal_id is None:
        print("ID must be a positive whole ID.")
        return
    
    removal_entry = None
    for entry in data:
        if entry.get("id") == removal_id: # Find the walk with the inputted ID
            removal_entry = entry
            break
        
    if removal_entry is None:
        print("A walk with the entered ID doesn't exist.")
        return
    
    data.remove(removal_entry) # Delete the walk
    save_data(data)
    print(f"Walk with ID {removal_id} has been deleted.")
    
def edit_entry(): # Function that edits one of the entries from the user's walks
    data = load_data()
    edit_id = int(input("Enter the ID of the walk you wish to edit: "))
    edit_id = parse_positive_int(edit_id) # Validate the entered id is a positive integer
    if edit_id is None:
        print("ID must be a positive integer.")
        return
    
    edit_entry = None
    for entry in data:
        if entry.get("id") == edit_id: # Find the walk with the inputted ID
            edit_entry = entry
            break
        
    if edit_entry is None:
        print("A walk with the entered ID doesn't exist.")
        return
    
    edit_stat = input(f"Enter the stat you wish to edit {EDITABLE_FIELDS}: ").strip()
    
    if edit_stat not in EDITABLE_FIELDS: # Validate that the entered stat is editable
        print(f"Invalid stat. Choose from {EDITABLE_FIELDS}")
        return
    
    new_value = input(f"Enter the new value for {edit_stat}: ").strip()

    # Validate the entered new value
    if edit_stat == 'temperature':
        new_value = validate_choice(new_value, TEMP_CHOICES)
        if not new_value:
            print(f"Invalid temperature. Choose from {TEMP_CHOICES}")
            return
    elif edit_stat == 'weather':
        new_value = validate_choice(new_value, WEATHER_CHOICES)
        if not new_value:
            print(f"Invalid weather. Choose from {WEATHER_CHOICES}")
            return
    elif edit_stat == 'time_of_day':
        new_value = validate_choice(new_value, TIME_CHOICES)
        if not new_value:
            print(f"Invalid time of day. Choose from {TIME_CHOICES}")
            return
    elif edit_stat == "steps" or edit_stat == "time":
        new_value = parse_positive_int(new_value)
        if new_value is None:
            print(f"{edit_stat} value must be a positive whole number.")
            return
    else:
        new_value = parse_positive_float(new_value)
        if new_value is None:
            print(f"{edit_stat} value must be a positive number.")
            return
        
    edit_entry[edit_stat] = new_value # Edit the value
    save_data(data)
    print(f"Walk ID {edit_id} has been updated.")
    
def walk_by_id(): # Function that returns a walk by it's ID, formatted in a Rich table
    data = load_data()
    walk_id = int(input("Enter the ID of the walk you wish to show: "))
    walk_id = parse_positive_int(walk_id)
    if walk_id is None:
        print("ID must be a positive integer.")
        return
    
    walk = None
    for entry in data:
        if entry.get("id") == walk_id: # Find the walk with the inputted ID
            walk = entry
            break
        
    if walk is None:
        console.print("[red]A walk with the entered ID doesn't exist.[/red]")
        return
    
    table = Table(title="Walk Details", show_lines=True)
    table.add_column("Field", style="bright_magenta")
    table.add_column("Value", justify="right", style="bright_yellow")

    table.add_row("ID", str(walk.get("id", "-")))
    table.add_row("Date", str(walk.get("date", "-")))
    table.add_row("Steps", f"{walk.get('steps', 0):,}")
    table.add_row("Distance (km)", f"{walk.get('distance', 0):.2f}")
    table.add_row("Time (mins)", f"{walk.get('time', 0):.2f}")
    table.add_row("Elevation Gain (m)", f"{walk.get('elev_gain', 0):.2f}")
    table.add_row("Temperature", str(walk.get('temperature', '-')))
    table.add_row("Weather", str(walk.get('weather', '-')))
    table.add_row("Time of Day", str(walk.get('time_of_day', '-')))
    table.add_row("Heart Rate (bpm)", f"{walk.get('heart_rate', 0):.1f}")
    table.add_row("Pace (min/km)", f"{walk.get('pace', 0):.2f}")
    table.add_row("Step Length (m)", f"{walk.get('step_len', 0):.2f}")
    
    console.print(table)
    
def walks_by_id(): # Function that lists all the user's walks by their ID
    data = load_data()
    if not data:
        print("No walks to show.")
        return
        
    data_sorted = sorted(data, key=lambda x: x.get("id", 0)) # Sort walk data by ID

    table = Table(title="Walks", show_lines=True)
    table.add_column("ID", style="bright_cyan", justify="center")
    table.add_column("Date", style="bright_magenta")
    table.add_column("Distance (km)", justify="right", style="bright_green")
    table.add_column("Steps", justify="right", style="bright_yellow")
    
    for entry in data_sorted:
        table.add_row(
            str(entry.get("id", "-")),
            entry.get("date", "-"),
            f"{entry.get('distance', 0):.2f}",
            f"{entry.get('steps', 0):,}"
        )
    
    console.print(table)