from utils import load_data, save_data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def add_entry():
    try:
        date = input("Enter the date of the walk [YYYY-MM-DD]:").strip()
        steps = int(input("Enter your number of steps:"))
        distance = float(input("Enter the distance you walked (in km):"))
        time = float(input("Enter the length of your walk (in minutes): "))
        elevGain = float(input("Enter the elevation gain of your walk (in meters):"))
       
        hr_choice = input("Do you know your average heart rate? (y/n): ").lower()
        
        if hr_choice == 'y':
            heartRate = float(input("Enter your average heart rate for the walk (in bpm):"))
        else:
            heartRate = estimate_heartRate(steps, distance, time, elevGain)
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
            "heartRate": heartRate,
            "paceKm": pace,
            "stepLenM": stepLen
        })
        
        save_data(data)
        print("Your entry has been saved.")
        
    except ValueError:
        print("Please enter valid numeric values.")
        
def estimate_heartRate(steps, distance, time, elevGain):
    data = load_data()
    
    if not data or len(data) < 5:
        return None
    
    df = pd.DataFrame(data)
    calc_cols = ["steps", "distanceKm", "timeMins", "elevGain"]
    X = df[calc_cols] # Drop the heart rate column
    y = df["heartRate"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 100) ## Split data into training and testing sets, with test sets being 20% of the data and the training sets 80%
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    predicted_hr = lr.predict([[steps, distance, time, elevGain]], columns=calc_cols)[0]
        
    return round(predicted_hr, 1)