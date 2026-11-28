
class Phone:

    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def make_call(self):
        print("Making a phone call...")

    def charge(self):
        self.battery_level = 100
        print("Phone is charging. Battery level:", self.battery_level, "%")

    def take_photo(self):
        print("Taking a photo...")

    def display_info(self):
        print("Phone information:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Battery level:", self.battery_level, "%")


# Create a smartphone object
my_phone = Phone("Apple", "iPhone 15", 65)

# Call methods
my_phone.make_call()
my_phone.take_photo()
my_phone.charge()

# Display object properties
my_phone.display_info()
