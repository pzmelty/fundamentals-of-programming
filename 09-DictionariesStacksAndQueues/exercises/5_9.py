
import csv

# Dictionary with province letters and names
provinces = {}

with open('09-DictionariesStacksAndQueues/province.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        provinces[row['Letter']] = row['Name']

# Dictionary with the number of vehicles
vehicle_count = {}

for letter in provinces:
    vehicle_count[letter] = 0

# Read vehicle registration numbers
with open('09-DictionariesStacksAndQueues/vehicle.txt', 'r', encoding='utf-8') as file:
    for line in file:
        registration = line.strip()

        if registration:
            letter = registration[0]

            if letter in vehicle_count:
                vehicle_count[letter] += 1

# Print the results
for letter, name in provinces.items():
    print(name, ':', vehicle_count[letter])
