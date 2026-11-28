import random


class Thermometer:

    def __init__(self):
        self.is_on = False
        self.temperature = 0.0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure_temperature(self):
        if self.is_on:
            self.temperature = round(random.uniform(34.0, 42.0), 1)
        else:
            print("Thermometer is off.")

    def display_temperature(self):
        if self.is_on:
            if self.temperature >= 41.0:
                print(f"Temperature: {self.temperature}C (fever)")
                print("CRITICAL TEMPERATURE!!")
            elif self.temperature >= 37.0:
                print(f"Temperature: {self.temperature}C (fever)")
            else:
                print(f"Temperature: {self.temperature}C")
        else:
            print("Thermometer is off.")


# Main program

# Create a thermometer
thermometer = Thermometer()

# Turn thermometer on
thermometer.turn_on()

# Measure temperature
thermometer.measure_temperature()

# Display temperature
thermometer.display_temperature()

# Turn thermometer off
thermometer.turn_off()
