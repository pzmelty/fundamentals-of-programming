###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'

number = 1

with open('08-FileHandling/it_company.csv') as file:
   for line in file:
      if job_title in line:
        print(f"{number}. {line}", end="")
        number += 1