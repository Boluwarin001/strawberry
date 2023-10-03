import sqlite3
import random

# Connect to an SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('strawberry_farm_data.db')
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS strawberry_farm (
        Day INTEGER PRIMARY KEY,
        Farm TEXT,
        Farm_Temperature REAL,
        Humidity INTEGER,
        Average_Light_Intensity INTEGER,
        Atmospheric_Pressure REAL,
        Rainfall REAL,
        pH REAL,
        Soil_Moisture INTEGER,
        Soil_Compaction INTEGER,
        Soil_Temperature REAL,
        Pest_Count INTEGER,
        Irrigation_Duration INTEGER
    )
''')

# Generate and insert data for each day for all farms
for farm_name in ['Farm A', 'Farm B', 'Farm C']:
    for day in range(1, 91):
        data = (
            day,
            farm_name,
            round(random.uniform(24, 28), 1),
            random.randint(65, 75),
            random.randint(5000, 6500),
            round(random.uniform(100.8, 101.5), 1),
            round(random.uniform(0, 2), 1),
            round(random.uniform(6.3, 6.8), 1),
            random.randint(40, 50),
            random.randint(18, 23),
            round(random.uniform(20.0, 21.5), 1),
            random.randint(4, 9),
            random.randint(15, 20)
        )

        cursor.execute('''
            INSERT INTO strawberry_farm
            (Day, Farm, Farm_Temperature, Humidity, Average_Light_Intensity, Atmospheric_Pressure, Rainfall, pH,
            Soil_Moisture, Soil_Compaction, Soil_Temperature, Pest_Count, Irrigation_Duration)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)

# Commit changes and close the database connection
conn.commit()
conn.close()

print("Data export to SQLite database (for MySQL) completed.")
