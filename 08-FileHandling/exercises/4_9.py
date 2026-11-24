###
# Prints Graphic Designers from a CSV file
#

import csv


# file name
file_name = '08-FileHandling/it_company.csv'

# read employee data
with open(file_name, 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)

    print('GRAPHIC DESIGNERS')
    print('=================')

    for row in reader:
        if row['Job Title'] == 'Graphic Designer':
            print(row['First Name'] + ' ' + row['Last Name'] + ',' + row['Email'])
