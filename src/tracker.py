from utils import load_data, save_data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

TEMP_CHOICES = {"hot", "warm", "cold"}
WEATHER_CHOICES = {"sunny", "raining", "snowing", "cloudy", "windy"}
TIME_CHOICES = {"morning", "afternoon", "evening", "night"}

def add_entry():
    try:
        date = input("Enter the date of the walk [YYYY-MM-DD]:").strip()
        steps = int(input("Enter your number of steps:"))
        distance = float(input("Enter the distance you walked (in km):"))
        time = float(input("Enter the length of your walk (in minutes): "))
        elevGain = float(input("Enter the elevation gain of your walk (in meters):"))
        temp = str(input("What was the temperature like on your walk? [ hot | warm | cold ]")).strip()
        weather = str(input("What was the weather like on your walk? [ sunny | raining | snowing | cloudy | windy ]")).strip()
        timeOfDay = str(input("What time of day was your walk at? [ morning | afternoon | evening | night ]")).strip()
        
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