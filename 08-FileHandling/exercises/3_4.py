###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = '08-FileHandling/report.txt'

# read the content of email
with open(email_file, 'r', encoding='utf-8') as file:
    email_content = file.read()


email = str(email_content)
# regular expression pattern
# for amounts
pattern = r'€(\d+)'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0
for amount in amounts:
   total += float(amount.replace(',', '.'))

# print result
print('Total spent:', round(total, 2), '€')
