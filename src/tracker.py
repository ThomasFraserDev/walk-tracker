from utils import load_data, save_data

def add_entry():
    try:
        date = input("Enter the date of the walk [YYYY-MM-DD]:").strip()
        steps = int(input("Enter your number of steps:"))
        distance = float(input("Enter the distance you walked (in km):"))
        time = float(input("Enter the length of your walk (in minutes): "))
        elevGain = float(input("Enter the elevation gain of your walk (in meters):"))
        heartRate = float(input("Enter your average heart rate for the walk (in bpm):"))
        
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