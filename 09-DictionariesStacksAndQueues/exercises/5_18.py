import json

with open('09-DictionariesStacksAndQueues/dogs.json', 'r', encoding='utf-8') as file:
    dogs = json.load(file)

for dog in dogs:
    if dog["age"] < 5:
        print(dog["name"], dog["age"])