###
# Prints file names with extensions consisting of four characters
#

import re
from pathlib import Path

# file name
file_name = Path(__file__).resolve().parent.parent / 'files.txt'

# read file
with open(file_name, 'r') as file:
    for line in file:
        line = line.strip()

        if re.search(r'\.[a-zA-Z0-9]{4}$', line):
            print(line)