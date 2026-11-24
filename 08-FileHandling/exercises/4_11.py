###
# Calculates and saves numbers and their powers
#

# file name
file_name = '08-FileHandling\powers.txt'

# open file to write data
with open(file_name, 'w') as file:

    for i in range(1, 101):
        result = f'{i},{i**2},{i**3}'

        print(result)
        file.write(result + '\n')