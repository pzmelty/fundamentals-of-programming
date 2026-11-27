import json


# Read reservations from JSON file
def load_reservations():
    with open('09-DictionariesStacksAndQueues/reservations.json', "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["reservations"]


# Count number of rooms
def count_rooms(reservations):
    return len(set(reservation["room_number"] for reservation in reservations))


# Count paid reservations
def count_paid_reservations(reservations):
    return sum(1 for reservation in reservations if reservation["paid"])


# Count unpaid reservations
def count_unpaid_reservations(reservations):
    return sum(1 for reservation in reservations if not reservation["paid"])


# Calculate total value of reservations
def calculate_total_value(reservations, paid):
    total = 0

    for reservation in reservations:
        if reservation["paid"] == paid:
            total += reservation["nights"] * reservation["price_per_night"]

    return total


# Main program
reservations = load_reservations()

print("Number of rooms:", count_rooms(reservations))
print("Number of paid reservations:", count_paid_reservations(reservations))
print("Number of unpaid reservations:", count_unpaid_reservations(reservations))
print("Total value of paid reservations:", calculate_total_value(reservations, True))
print("Total value of unpaid reservations:", calculate_total_value(reservations, False))
