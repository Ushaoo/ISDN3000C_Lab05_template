# Script to generate plant_sensors.csv
import pandas as pd
import numpy as np

# --- SET THE SEED FOR REPRODUCIBILITY ---
np.random.seed(42)
# ----------------------------------------

# We create data hourly over a month
time_range = pd.to_datetime(pd.date_range(start='2023-07-01', end='2023-07-31', freq='H'))

# Properties: 5 plants, in 3 locations
sensors = {
    'A-1': {'plant_type': 'Fiddle Leaf Fig', 'location': 'Living Room'},
    'A-2': {'plant_type': 'Monstera', 'location': 'Living Room'},
    'B-1': {'plant_type': 'Snake Plant', 'location': 'Office'},
    'B-2': {'plant_type': 'Pothos', 'location': 'Office'},
    'C-1': {'plant_type': 'Tomato', 'location': 'Patio'},
}

num_records = len(time_range) * len(sensors)
data = []

for id, props in sensors.items():
    for ts in time_range:
        sensor_id = id
        # Simulate temperature and light
        hour_of_day = ts.hour
        base_temp = 20 + 5 * np.sin(np.pi * (hour_of_day-8)/12) # Temperature is highest in the afternoon
        temp_c = base_temp + np.random.randn() * 0.5
        
        light = 800 + 600 * np.sin(np.pi * (hour_of_day-6)/14) # Light peaks at noon
        light_level = max(0, light + np.random.randn() * 50)
        
        # Simulate soil moisture with drying and occasional watering
        # Naive model where the soil dries faster in higher temperatures/sunlight, and dires during the day with occasional rewatering at night
        moisture_decay = 1 + temp_c/20 + light_level/800
        base_moisture = 55 - 20 * np.sin(np.pi * (hour_of_day-2)/24) - moisture_decay
        soil_moisture = base_moisture + np.random.randn() * 3

        # Add some sensor errors and NaNs
        if np.random.rand() < 0.02: # 2% chance of a NaN reading
            soil_moisture = np.nan
        elif np.random.rand() < 0.005: # 0.5% chance of complete data corruption
            ts = np.nan
            sensor_id = np.nan
            temp_c = np.nan
            soil_moisture = np.nan
            light_level = np.nan
        elif sensor_id == 'B-1' and np.random.rand() < 0.1: # Sensor B-1 is faulty, 10% chances to have a very high value
             soil_moisture = 95.0 + np.random.randn() 
        
        pump_active = 1 if soil_moisture < 35 and not np.isnan(soil_moisture) else 0

        data.append({
            'timestamp': ts,
            'sensor_id': sensor_id,
            'plant_type': props['plant_type'],
            'location': props['location'],
            'temperature_c': round(temp_c, 2),
            'soil_moisture': round(soil_moisture, 2),
            'light_level': round(light_level, 2),
            'pump_active': pump_active
        })

df = pd.DataFrame(data)
df.to_csv('plant_sensors.csv', index=False)
print("plant_sensors.csv successfully created!")