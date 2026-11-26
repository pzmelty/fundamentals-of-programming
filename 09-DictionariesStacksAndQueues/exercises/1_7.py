products = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

# Displays list of products and quantity
for product, quantity in products.items():
    print(product, quantity)

# Displays total number of products
total = sum(products.values())

print("Total number of products:", total)