import json
import requests
import webbrowser

# API address
url = "https://api.nbp.pl/api/exchangerates/rates/c/eur/last/10/?format=json"

# Display JSON data in web browser
webbrowser.open(url)

# Download exchange rate data
response = requests.get(url)
data = response.json()

# Save data to JSON file
with open("euro.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("Data has been saved to euro.json")

# Read data from JSON file
with open("euro.json", "r", encoding="utf-8") as file:
    euro = json.load(file)

# Display exchange rates
print()
print("Date        Buying Rate    Selling Rate")

for rate in euro["rates"]:
    print(
        rate["effectiveDate"],
        "   ",
        rate["bid"],
        "       ",
        rate["ask"]
    )
