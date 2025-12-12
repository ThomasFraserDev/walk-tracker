from utils import load_data, save_data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

TEMP_CHOICES = {"hot", "warm", "cold"}
WEATHER_CHOICES = {"sunny", "raining", "snowing", "cloudy", "windy"}
TIME_CHOICES = {"morning", "afternoon", "evening", "night"}

def add_entry():
    data = load_data()
    try:
        id = max([entry.get("id", 0) for entry in data], default=0) + 1 # Set a walk's id to be the current highest id + 1
        date = input("Enter the date of the walk [YYYY-MM-DD]: ").strip()
        steps = int(input("Enter your number of steps: "))
        distance = float(input("Enter the distance you walked (in km): "))
        time = float(input("Enter the length of your walk (in minutes): "))
        elevGain = float(input("Enter the elevation gain of your walk (in meters): "))
        temp = str(input("What was the temperature like on your walk? [ hot | warm | cold ]: ")).strip()
        weather = str(input("What was the weather like on your walk? [ sunny | raining | snowing | cloudy | windy ]: ")).strip()
        timeOfDay = str(input("What time of day was your walk at? [ morning | afternoon | evening | night ]: ")).strip()
        
        if temp not in TEMP_CHOICES:
            print("Invalid temperature. Choose one of: hot, warm, cold.")
            return
        if weather not in WEATHER_CHOICES:
            print("Invalid weather. Choose one of: sunny, raining, snowing, cloudy, windy.")
            return
        if timeOfDay not in TIME_CHOICES:
            print("Invalid time of day. Choose one of: morning, afternoon, evening, night.")
            return
       
        hr_choice = input("Do you know your average heart rate? (y/n): ").lower()
        
        if hr_choice == 'y':
            heartRate = float(input("Enter your average heart rate for the walk (in bpm):"))
        else:
            heartRate = estimate_heartRate(steps, distance, time, elevGain, temp, weather, timeOfDay)
            if heartRate is None:
                print("Cannot estimate heart rate. Please enter it manually.")
                heartRate = float(input("Enter your average heart rate for the walk (in bpm):"))
            else:
                print(f"Estimated heart rate: {heartRate:.1f} bpm")
        
        if distance <= 0 or time <= 0 or steps <= 0: # Validate distance, time and step input
            print("Error: Distance, time, and steps must be positive.")
            return
        
        pace = round((time / distance), 2) # Calculate pace
        stepLen = round((distance * 1000 / steps), 2) # Calculate average step length
        
        data = load_data()
        data.append({ # Add the entries to the dataset
            "id": id,
            "date": date,
            "steps": steps,
            "distanceKm": distance,
            "timeMins": time,
            "elevGain": elevGain,
            "temperature": temp,
            "weather": weather,
            "timeOfDay": timeOfDay,
            "heartRate": heartRate,
            "paceKm": pace,
            "stepLenM": stepLen
        })
        
        save_data(data)
        print("Your entry has been saved.")
        
    except ValueError:
        print("Please enter valid numeric or textual values.")
        
def delete_entry():
    data = load_data()
    removal_id = int(input("Enter the ID of the walk you wish to be deleted: "))
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
    edit_entry = None
    
    for entry in data:
        if entry.get("id") == edit_id: # Find the walk with the inputted ID
            edit_entry = entry
            break
        
    if edit_entry is None:
        print("A walk with the entered ID doesn't exist.")
        return
    
    valid_stats = ['steps', 'distanceKm', 'timeMins', 'elevGain', 'heartRate', 'temperature', 'weather', 'timeOfDay']
    edit_stat = input("Enter the stat you wish to edit [steps, distanceKM, timeMins, heartRate, temperature, weather, timeOfDay]: ")
    
    if edit_stat not in valid_stats:
        print(f"Invalid stat. Choose from {valid_stats}")
        return
    
    new_value = input(f"Enter the new value for {edit_stat}: ").strip()

    # Validate the entered new value
    if edit_stat == 'temperature':
        if new_value not in TEMP_CHOICES:
            print(f"Invalid temperature. Choose from {TEMP_CHOICES}")
            return
    elif edit_stat == 'weather':
        if new_value not in WEATHER_CHOICES:
            print(f"Invalid weather. Choose from {WEATHER_CHOICES}")
            return
    elif edit_stat == 'timeOfDay':
        if new_value not in TIME_CHOICES:
            print(f"Invalid time of day. Choose from {TIME_CHOICES}")
            return
    else:
        try:
            new_value = float(new_value) if edit_stat != 'steps' else int(new_value)
        except ValueError:
            print(f"Invalid value for {edit_stat}.")
            return
        
    edit_entry[edit_stat] = new_value # Edit the value
    save_data(data)
    print(f"Walk ID {edit_id} has been updated.")
    
def walk_by_id():
    data = load_data()
    walk_id = int(input("Enter the ID of the walk you wish to show: "))
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
    print(f"Distance (km): {walk.get('distanceKm', 0):.2f}")
    print(f"Time (mins): {walk.get('timeMins', 0):.2f}")
    print(f"Elevation Gain (m): {walk.get('elevGain', 0):.2f}")
    print(f"Temperature: {walk.get('temperature', '-')}")
    print(f"Weather: {walk.get('weather', '-')}")
    print(f"Time of Day: {walk.get('timeOfDay', '-')}")
    print(f"Heart Rate (bpm): {walk.get('heartRate', 0):.1f}")
    print(f"Pace (min/km): {walk.get('paceKm', 0):.2f}")
    print(f"Step Length (m): {walk.get('stepLenM', 0):.2f}")
    
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
        distance = entry.get("distanceKm", 0)
        print(f"{walk_id:<6} {date:<12} {distance:>14.2f}")

def estimate_heartRate(steps, distance, time, elevGain, temp, weather, timeOfDay):
    data = load_data()
    
    if not data or len(data) < 5:
        return None
    
    df = pd.DataFrame(data)
    calc_cols = ["steps", "distanceKm", "timeMins", "elevGain", "temperature", "weather", "timeOfDay"]
    X = df[calc_cols] # Drop the heart rate column
    y = df["heartRate"]
    X = pd.get_dummies(X, columns=["temperature", "weather", "timeOfDay"])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 100) ## Split data into training and testing sets, with test sets being 20% of the data and the training sets 80%
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    
    input_df = pd.DataFrame([[steps, distance, time, elevGain, temp, weather, timeOfDay]], columns=["steps", "distanceKm", "timeMins", "elevGain", "temperature", "weather", "timeOfDay"])
    input_df = pd.get_dummies(input_df, columns=["temperature", "weather", "timeOfDay"])
    input_df = input_df.reindex(columns=X.columns, fill_value=0)
    
    predicted_hr = lr.predict(input_df)[0]
        
    return round(predicted_hr, 1)