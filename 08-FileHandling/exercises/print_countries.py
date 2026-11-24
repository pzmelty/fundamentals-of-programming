###
# Reads from file, line by line
#
with open('08-FileHandling/countries.txt', 'r') as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line}", end="")