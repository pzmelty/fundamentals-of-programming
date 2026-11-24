###
# Counts vowels in text entered from the keyboard
#

import re

# read text from keyboard
text = input('Enter text: ')

# pattern for vowels
pattern = r'[aeiouyAEIOUY]'

# find vowels
vowels = re.findall(pattern, text)

# count vowels
number_of_vowels = len(vowels)

# print result
print('Number of vowels:', number_of_vowels)