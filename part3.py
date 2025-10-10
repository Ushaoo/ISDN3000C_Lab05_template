import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

def create_output_directory():
    output_dir = 'plots'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def part3_exercises():
    output_dir = create_output_directory()
    
    df = pd.read_csv('plant_sensors.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    df['soil_moisture'] = df['soil_moisture'].interpolate(method='linear')
    df = df.dropna(subset=['sensor_id', 'timestamp'])
    
    # Exercise 3.1: Bar Chart
    print("=== Exercise 3.1: Bar Chart ===")
    avg_moisture_by_sensor = df.groupby('sensor_id')['soil_moisture'].mean()
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(avg_moisture_by_sensor.index, avg_moisture_by_sensor.values, 
                   color=['skyblue', 'lightcoral', 'lightgreen', 'gold', 'violet'])
    plt.title('Average Soil Moisture by Sensor', fontsize=14, fontweight='bold')
    plt.ylabel('Average Moisture (%)', fontsize=12)
    plt.xlabel('Sensor ID', fontsize=12)
    plt.xticks(rotation=45)
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%',
                ha='center', va='bottom', fontweight='bold')
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    plt.savefig(f'{output_dir}/exercise3_1_bar_chart.png', dpi=300, bbox_inches='tight')
    plt.savefig(f'{output_dir}/exercise3_1_bar_chart.pdf', bbox_inches='tight')  
    print(f"Bar chart saved as: {output_dir}/exercise3_1_bar_chart.png")
    plt.show()
    
    # Exercise 3.2: Line Plot
    print("\n=== Exercise 3.2: Line Plot ===")
    sensor_a1 = df[df['sensor_id'] == 'A-1'].copy()
    sensor_a1 = sensor_a1.set_index('timestamp')
    
    plt.figure(figsize=(12, 6))
    plt.plot(sensor_a1.index, sensor_a1['soil_moisture'], 
             linewidth=1.2, color='blue', alpha=0.8)
    plt.title('Moisture Level for Sensor A-1 Over Time', fontsize=14, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Soil Moisture (%)', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    plt.fill_between(sensor_a1.index, sensor_a1['soil_moisture'], 
                     alpha=0.3, color='blue')
    
    plt.tight_layout()
    
    plt.savefig(f'{output_dir}/exercise3_2_line_plot.png', dpi=300, bbox_inches='tight')
    plt.savefig(f'{output_dir}/exercise3_2_line_plot.pdf', bbox_inches='tight')
    print(f"Line plot saved as: {output_dir}/exercise3_2_line_plot.png")
    plt.show()
    
    # Exercise 3.3: Subplots and Anomaly Detection
    print("\n=== Exercise 3.3: Subplots and Anomaly Detection ===")
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Left subplot: Histogram of temperature
    axes[0].hist(df['temperature_c'], bins=40, color='lightcoral', 
                 alpha=0.7, edgecolor='black')
    axes[0].set_title('Distribution of All Temperature Readings', 
                     fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Temperature (°C)', fontsize=11)
    axes[0].set_ylabel('Frequency', fontsize=11)
    axes[0].grid(True, alpha=0.3)
    
    mean_temp = df['temperature_c'].mean()
    axes[0].axvline(mean_temp, color='red', linestyle='--', 
                   label=f'Mean: {mean_temp:.1f}°C')
    axes[0].legend()
    
    # Right subplot: Scatter plot
    scatter = axes[1].scatter(df['temperature_c'], df['soil_moisture'], 
                             alpha=0.1, color='green', s=10)
    axes[1].set_title('Temperature vs. Soil Moisture', 
                     fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Temperature (°C)', fontsize=11)
    axes[1].set_ylabel('Soil Moisture (%)', fontsize=11)
    axes[1].grid(True, alpha=0.3)
    
    z = np.polyfit(df['temperature_c'], df['soil_moisture'], 1)
    p = np.poly1d(z)
    axes[1].plot(df['temperature_c'], p(df['temperature_c']), 
                "r--", alpha=0.8, linewidth=2)
    
    plt.tight_layout()
    
    plt.savefig(f'{output_dir}/exercise3_3_subplots.png', dpi=300, bbox_inches='tight')
    plt.savefig(f'{output_dir}/exercise3_3_subplots.pdf', bbox_inches='tight')
    print(f"Subplots saved as: {output_dir}/exercise3_3_subplots.png")
    plt.show()
    
    
    print(f"\n=== Summary ===")
    print(f"All plots have been saved to the '{output_dir}/' directory")
    print(f"Generated files:")
    plot_files = [f for f in os.listdir(output_dir) if f.endswith(('.png', '.pdf'))]
    for file in sorted(plot_files):
        file_path = os.path.join(output_dir, file)
        file_size = os.path.getsize(file_path) / 1024  # KB
        print(f"  - {file} ({file_size:.1f} KB)")

if __name__ == "__main__":
    part3_exercises()