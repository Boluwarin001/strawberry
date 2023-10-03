import csv
import random

# Function to generate and export data to CSV
def generate_and_export_data(filename, farm_name):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
            'Day', 'Farm', 'Farm Temperature (°C)', 'Humidity (%)', 'Average Light Intensity (lux)',
            'Atmospheric Pressure (kPa)', 'Rainfall (mm)', 'pH', 'Soil Moisture (%)',
            'Soil Compaction (%)', 'Soil Temperature (°C)', 'Pest Count', 'Irrigation Duration (minutes)'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Generate and insert data for each day for the specified farm
        for day in range(1, 91):
            data = {
                'Day': day,
                'Farm': farm_name,
                'Farm Temperature (°C)': round(random.uniform(24, 28), 1),
                'Humidity (%)': random.randint(65, 75),
                'Average Light Intensity (lux)': random.randint(5000, 6500),
                'Atmospheric Pressure (kPa)': round(random.uniform(100.8, 101.5), 1),
                'Rainfall (mm)': round(random.uniform(0, 2), 1),
                'pH': round(random.uniform(6.3, 6.8), 1),
                'Soil Moisture (%)': random.randint(40, 50),
                'Soil Compaction (%)': random.randint(18, 23),
                'Soil Temperature (°C)': round(random.uniform(20.0, 21.5), 1),
                'Pest Count': random.randint(4, 9),
                'Irrigation Duration (minutes)': random.randint(15, 20),
            }

            # Write the data for the day
            writer.writerow(data)

        print(f"Data export to {filename} for {farm_name} completed.")

# Generate and export data for Farm A
generate_and_export_data('farm_a_data.csv', 'farm_a')

# Generate and export data for Farm B
generate_and_export_data('farm_b_data.csv', 'farm_b')

# Generate and export data for Farm C
generate_and_export_data('farm_c_data.csv', 'farm_c')
