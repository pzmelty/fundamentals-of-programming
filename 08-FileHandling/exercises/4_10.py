###
# Prints products with price less than 60
# and stock less than 40
#

import csv

# file name
file_name = '08-FileHandling/clothing.csv'

# read product data
with open(file_name, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        if float(row['Price']) < 60 and int(row['Stock_Quantity']) < 40:
            print(row)