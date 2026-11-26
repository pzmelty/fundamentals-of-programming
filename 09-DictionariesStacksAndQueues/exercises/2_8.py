price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

# Prints products and prices before discount
for product, price in price_list.items():
    print(product, price)

# Prints total value before discount
total = sum(price_list.values())
print("Total before discount:", round(total, 2))

# Reduces prices by 10%
for product in price_list:
    price_list[product] = round(price_list[product] * 0.9, 2)

# Prints products and prices after discount
for product, price in price_list.items():
    print(product, price)

# Prints total value after discount
total_after = sum(price_list.values())
print("Total after discount:", round(total_after, 2))