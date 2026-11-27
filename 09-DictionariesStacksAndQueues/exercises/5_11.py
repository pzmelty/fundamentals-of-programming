import json

# Read the contents of the json file
try:
    with open("voting.json", "r", encoding="utf-8") as file:
        voting = json.load(file)
except FileNotFoundError:
    voting = {}

# Vote for a person
person_name = input("Name of the person you are voting for: ")

if person_name in voting:
    voting[person_name] += 1
else:
    voting[person_name] = 1

# Save voting data to json file
with open("voting.json", "w", encoding="utf-8") as file:
    json.dump(voting, file, indent=4)

print(voting)