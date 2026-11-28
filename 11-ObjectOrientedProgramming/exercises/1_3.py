class TaxiRide:

    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km  # price per kilometer
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print("TAXI RECEIPT")
        print("--------------------")
        print("Distance:", self.distance, "km")
        print("Rate per km:", self.rate_per_km, "€")
        print("Fare:", self.fare, "€")
        print()

def main():

    # Create two taxi rides
    taxi1 = TaxiRide(2)
    taxi2 = TaxiRide(3)

    # Calculate fares
    taxi1.calculate_fare(10)
    taxi2.calculate_fare(15)

    # Print receipts
    taxi1.print_receipt()
    taxi2.print_receipt()


if __name__ == "__main__":
    main()
