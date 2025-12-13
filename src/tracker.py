from data import load_data, save_data
from prediction import estimate_heartRate
from constants import TEMP_CHOICES, WEATHER_CHOICES, TIME_CHOICES, EDITABLE_FIELDS
from validation import validate_date, parse_positive_int, parse_positive_float, validate_choice, parse_yes_no

def add_entry():
    data = load_data()
    try:
        id = max([entry.get("id", 0) for entry in data], default=0) + 1 # Set a walk's id to be the current highest id + 1
        
        date = input("Enter the date of the walk [YYYY-MM-DD]: ")
        date = validate_date(date)
        if not date:
            print("Invalid date. Use YYYY-MM-DD.")
            return
        
        steps = int(input("Enter your number of steps: "))
        steps = parse_positive_int(steps)
        if steps is None:
            print("Steps must be a positive whole number.")
            return
        
        distance = float(input("Enter the distance you walked (in km): "))
        distance = parse_positive_float(distance)
        if distance is None:
            print("Distance must be a positive number.")
            return
        
        time = float(input("Enter the length of your walk (rounded to nearest minute): "))
        time = parse_positive_int(time)
        if time is None:
            print("Time must be a positive whole number.")
            return
        
        elev_gain = float(input("Enter the elevation gain of your walk (in meters): "))
        elev_gain = parse_positive_float(elev_gain)
        if elev_gain is None:
            print("Elevation gain must be a positive number.")
            return
        
        temp = str(input("What was the temperature like on your walk? [ hot | warm | cold ]: "))
        temp = validate_choice(temp, TEMP_CHOICES)
        if not temp:
            print("Invalid temperature. Choose one of: hot, warm, cold.")
            return
        
        weather = str(input("What was the weather like on your walk? [ sunny | raining | snowing | cloudy | windy ]: "))
        weather = validate_choice(weather, WEATHER_CHOICES)
        if not weather:
            print("Invalid weather. Choose one of: sunny, raining, snowing, cloudy, windy.")
            return
      
        time_of_day = str(input("What time of day was your walk at? [ morning | afternoon | evening | night ]: "))
        time_of_day = validate_choice(time_of_day, TIME_CHOICES)
        if not time_of_day:
            print("Invalid time of day. Choose one of: morning, afternoon, evening, night.")
            return
       
        hr_choice = input("Do you know your average heart rate from the walk? (y/n): ").lower()
        hr_choice = parse_yes_no(hr_choice)
        if hr_choice is None:
            print("Please answer with y/n.")
            return
        
        if hr_choice:
            heart_rate = input("Enter your average heart rate for the walk (in bpm): ")
            heart_rate = parse_positive_float(heart_rate)
            if heart_rate is None:
                print("Heart rate must be a positive number.")
                return
        else:
            heart_rate = estimate_heartRate(steps, distance, time, elev_gain, temp, weather, time_of_day)
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
        
def delete_entry():
    data = load_data()
    removal_id = int(input("Enter the ID of the walk you wish to be deleted: "))
    removal_id = parse_positive_int(removal_id)
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
    
def edit_entry():
    data = load_data()
    edit_id = int(input("Enter the ID of the walk you wish to edit: "))
    edit_id = parse_positive_int(edit_id)
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
    
    if edit_stat not in EDITABLE_FIELDS:
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
    
def walk_by_id():
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
        print("A walk with the entered ID doesn't exist.")
        return
    
    print("\n---------- Walk Details ----------")
    print(f"ID: {walk.get('id', '-')}")
    print(f"Date: {walk.get('date', '-')}")
    print(f"Steps: {walk.get('steps', 0)}")
    print(f"Distance (km): {walk.get('distance', 0):.2f}")
    print(f"Time (mins): {walk.get('time', 0):.2f}")
    print(f"Elevation Gain (m): {walk.get('elev_gain', 0):.2f}")
    print(f"Temperature: {walk.get('temperature', '-')}")
    print(f"Weather: {walk.get('weather', '-')}")
    print(f"Time of Day: {walk.get('time_of_day', '-')}")
    print(f"Heart Rate (bpm): {walk.get('heart_rate', 0):.1f}")
    print(f"Pace (min/km): {walk.get('pace', 0):.2f}")
    print(f"Step Length (m): {walk.get('step_len', 0):.2f}")
    
def walks_by_id():
    data = load_data()
    if not data:
        print("No walks to show.")
        return
        
    data_sorted = sorted(data, key=lambda x: x.get("id", 0))

    print("\n---------- Walks ----------")
    print(f"{'ID':<6} {'Date':<12} {'Distance (km)':>14}")
    print("-" * 34)
    for entry in data_sorted:
        walk_id = entry.get("id", "-")
        date = entry.get("date", "-")
        distance = entry.get("distance", 0)
        print(f"{walk_id:<6} {date:<12} {distance:>14.2f}")