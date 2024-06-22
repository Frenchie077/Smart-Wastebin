import csv
import random
from datetime import datetime

# Define column names
columns = ['Timestamp', 'Filename', 'PredictedClass', 'FilllevelBio', 'FilllevelMetal', 'FilllevelNonmetal', 'GasBIo']

# Generate 15 rows of random data
data = []
for i in range(15):
    # Generate random date in YY/MM/DD format
    timestamp = datetime.now().strftime('%y/%m/%d')
    
    # Generate filename in the form 'image1', 'image2', 'image3', etc.
    filename = f'image{i+1}'

    # Generate random predicted class ('Biodegradable' or 'Non-Biodegradable')
    predicted_class = random.choice(['Biodegradable', 'Non-Biodegradable'])

    # Generate random fill levels (0-10) and gas level (0-15)
    filllevel_bio = random.randint(0, 10)
    filllevel_metal = random.randint(0, 10)
    filllevel_nonmetal = random.randint(0, 10)
    gas_bio = random.randint(0, 15)

    # Append row to data
    row = [timestamp, filename, predicted_class, filllevel_bio, filllevel_metal, filllevel_nonmetal, gas_bio]
    data.append(row)

# Write data to CSV file
with open('pro.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(columns)  # Write column headers
    writer.writerows(data)     # Write data rows

