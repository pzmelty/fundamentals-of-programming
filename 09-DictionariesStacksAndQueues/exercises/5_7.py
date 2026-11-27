hotels_in_Krakow = [
    {"name": "Sky", "price": 320.00},
    {"name": "Metropol", "price": 480.00},
    {"name": "New Port", "price": 420.00},
    {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
    {"name": "Focus", "price": 510.00},
    {"name": "Aqua", "price": 345.00},
    {"name": "La Boutique", "price": 390.00},
    {"name": "Marina", "price": 410.00}
]


# Returns a list of hotel names
def hotel_list(hotels):
    return ", ".join(hotel["name"] for hotel in hotels)


# Returns average hotel price
def avg_price(hotels):
    total = sum(hotel["price"] for hotel in hotels)
    return round(total / len(hotels))


# Calculates average prices
krakow_price = avg_price(hotels_in_Krakow)
sopot_price = avg_price(hotels_in_Sopot)

# Displays results
print("Hotels in Krakow:", hotel_list(hotels_in_Krakow))
print("Average hotel price in Krakow:", krakow_price)

print("Hotels in Sopot:", hotel_list(hotels_in_Sopot))
print("Average hotel price in Sopot:", sopot_price)

if krakow_price < sopot_price:
    print("Cheaper hotels in: Krakow")
elif sopot_price < krakow_price:
    print("Cheaper hotels in: Sopot")
else:
    print("Hotel prices are equal")