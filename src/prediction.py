from data import load_data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def estimate_heartRate(steps, distance, time, elev_gain, temp, weather, time_of_day):
    data = load_data()
    
    if not data or len(data) < 5:
        return None
    
    df = pd.DataFrame(data)
    calc_cols = ["steps", "distance", "time", "elev_gain", "temperature", "weather", "time_of_day"]
    X = df[calc_cols] # Drop the heart rate column
    y = df["heart_rate"]
    X = pd.get_dummies(X, columns=["temperature", "weather", "time_of_day"])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 100) ## Split data into training and testing sets, with test sets being 20% of the data and the training sets 80%
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    
    input_df = pd.DataFrame([[steps, distance, time, elev_gain, temp, weather, time_of_day]], columns=["steps", "distance", "time", "elev_gain", "temperature", "weather", "time_of_day"])
    input_df = pd.get_dummies(input_df, columns=["temperature", "weather", "time_of_day"])
    input_df = input_df.reindex(columns=X.columns, fill_value=0)
    
    predicted_hr = lr.predict(input_df)[0]
        
    return round(predicted_hr, 1)