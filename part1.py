import numpy as np
import pandas as pd

# --- TODO: Complete the tasks listed in tutorial. Run and verify your results before submission. --- #
def part1_exercises():
    print("Loading dataset...")
    df = pd.read_csv('plant_sensors.csv')
    moisture_readings = df['soil_moisture'].to_numpy()
    print("Dataset loaded successfully!")
    print("----------------------------------")
    #Exercise 1.1: Array Basics
    print("== Exercises 1.1: NumPy Basics ==")
    calibrated_moisture = moisture_readings - 0.5
    print("Calibrated Moisture Readings (first 5):", calibrated_moisture[:5])
    print("----------------------------------")
    #Exercise 1.2: Array Slicing and Stats
    print("== Exercises 1.2: Array Slicing and Stats ==")
    selected_readings = moisture_readings[50:60]
    print("Readings from index 50 to 59:")
    print(selected_readings)
    mean_moisture = np.nanmean(moisture_readings)
    median_moisture = np.nanmedian(moisture_readings)
    std_moisture = np.nanstd(moisture_readings)
    q25 = np.nanpercentile(moisture_readings, 25)
    q75 = np.nanpercentile(moisture_readings, 75)
    print(f"Summary Statistics (ignoring NaN):")
    print(f"Mean: {mean_moisture:.2f}")
    print(f"Median: {median_moisture:.2f}")
    print(f"Standard Deviation: {std_moisture:.2f}")
    print(f"25th Percentile: {q25:.2f}")
    print(f"75th Percentile: {q75:.2f}")
    print("----------------------------------")
    #Exercise 1.3: Boolean Indexing and Logic
    print("== Exercises 1.3: Boolean Indexing and Logic ==")
    moisture_status = np.where(
        calibrated_moisture < 35, 'Dry',
        np.where(calibrated_moisture > 70, 'Wet', 'OK')
    )
    
    print("Sample of 10 moisture_status values:")
    print(moisture_status[:10])
    print("----------------------------------")

if __name__ == "__main__":
    part1_exercises()