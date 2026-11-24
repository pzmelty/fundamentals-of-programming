###
# Displays file contents in groups of five lines
#

file_name = '08-FileHandling/it_company.csv'

with open(file_name, 'r') as file:
    lines = file.readlines()

    for i in range(0, len(lines), 5):
        for line in lines[i:i+5]:
            print(line, end='')

        if i + 5 < len(lines):
            input('Press Enter key...')