###
# Counts lines, characters and words in a text file
#
import os

file_name = input('File name: ')
file_name = os.path.join(os.path.dirname(__file__), '..', file_name)

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()

    number_of_lines = len(lines)
    number_of_characters = len(content)
    number_of_words = len(words)

    print('Number of lines:', number_of_lines)
    print('Number of characters:', number_of_characters)
    print('Number of words:', number_of_words)

except FileNotFoundError:
    print('File not found!')