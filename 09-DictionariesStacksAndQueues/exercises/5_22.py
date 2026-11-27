import json

product = {}

# Read product data from keyboard
product["name"] = input("Enter product name: ")
product["price"] = round(float(input("Enter product price: ")), 2)

paid = input("Has the product been paid for? (yes/no): ").lower()
product["paid"] = paid == "yes"

# Save product data to JSON file
with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product, file, indent=4)

print("Product data has been saved to product.json")
