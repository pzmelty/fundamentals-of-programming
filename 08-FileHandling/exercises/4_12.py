
###
# Copies books of a selected genre to a file
#

import csv

# file name
file_name = '08-FileHandling/books.csv'


# Returns the name of the output file
def get_file_name(genre):
    filenames = {
        'Fantasy': 'books_fantasy.txt',
        'Historical': 'books_historical.txt',
        'Romance': 'books_romance.txt',
        'Classic': 'books_classic.txt'
    }

    return filenames.get(genre)


# Copies books of a selected genre
def copy_books(genre, file_name, target_file):
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        with open('08-FileHandling/' + target_file, 'w', encoding='utf-8', newline='') as output:
            writer = csv.DictWriter(output, fieldnames=reader.fieldnames)

            writer.writeheader()

            for row in reader:
                if row['Genre'] == genre:
                    writer.writerow(row)


# Main program
genre = input('Enter genre: ')

target_file = get_file_name(genre)

if target_file:
    copy_books(genre, file_name, target_file)
    print('Books saved to:', target_file)
else:
    print('Unknown genre!')
