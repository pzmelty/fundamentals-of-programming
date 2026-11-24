###
# Reads the entire contents of a file
#

def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content


# reads the entire file
file_content = read_from_file('08-FileHandling/pets.txt')


# prints the text
print(file_content)


# counts the number of words
words = file_content.split()
print('Number of words:', len(words))