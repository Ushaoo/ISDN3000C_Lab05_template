# --- TODO: Complete the tasks listed in tutorial. Run and verify your results before submission. --- #
import pandas as pd
import numpy as np

def part2_exercises():
    # Exercise 2.1: Initial Inspection & Cleaning
    print("=== Exercise 2.1 ===")
    df = pd.read_csv('plant_sensors.csv')
    
    print("First 5 rows:")
    print(df.head())
    print(f"\nDataFrame shape: {df.shape}")
    print("\nDataFrame info:")
    print(df.info())
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    df['temperature_f'] = (df['temperature_c'] * 9/5) + 32
    
    print("\nAfter conversion - timestamp methods available:")
    print([method for method in dir(df['timestamp'].dt) if not method.startswith('_')])
    
    # Exercise 2.2: Missing Data & Filtering
    print("\n=== Exercise 2.2 ===")
    print("Missing values per column:")
    print(df.isnull().sum())
    
    df['soil_moisture'] = df['soil_moisture'].interpolate(method='linear')
    
    df['temperature_c'] = df['temperature_c'].fillna(method='ffill')
    df['light_level'] = df['light_level'].fillna(method='ffill')
    
    df = df.dropna(subset=['sensor_id', 'timestamp'])
    
    print("\nAfter handling missing values:")
    print(df.isnull().sum())
    
    patio_high_light = df[(df['location'] == 'Patio') & (df['light_level'] > 1200)]
    print("\nPatio high light readings (first 5):")
    print(patio_high_light.head())
    
    # Exercise 2.3: Grouping and Aggregation
    print("\n=== Exercise 2.3 ===")
    avg_moisture_by_sensor = df.groupby('sensor_id')['soil_moisture'].mean()
    print("Average soil moisture by sensor:")
    print(avg_moisture_by_sensor)
    
    pump_activations = df.groupby('plant_type')['pump_active'].sum()
    print("\nPump activations by plant type:")
    print(pump_activations)
    
    max_temp_by_location = df.groupby('location')['temperature_c'].max()
    print("\nMax temperature by location:")
    print(max_temp_by_location)
    


if __name__ == "__main__":
    part2_exercises()
'''
Import necessary libraries here
'''



'''
Load the datasets
'''



'''
Exercise 2.1: Initial Inspection & Cleaning
'''



'''
Exercise 2.2: Missing Data & Filtering
'''



'''
Exercise 2.3: Grouping and Aggregation
'''