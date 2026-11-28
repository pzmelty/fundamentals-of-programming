class Statistics:

    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def display_numbers(self):
        print("Numbers:", *self.numbers)

    def get_maximum(self):
        return max(self.numbers)

    def get_minimum(self):
        return min(self.numbers)

    def calculate_mean(self):
        return sum(self.numbers) / len(self.numbers)

    def calculate_median(self):
        sorted_numbers = sorted(self.numbers)
        n = len(sorted_numbers)

        if n % 2 == 1:
            return sorted_numbers[n // 2]
        else:
            middle1 = sorted_numbers[n // 2 - 1]
            middle2 = sorted_numbers[n // 2]
            return (middle1 + middle2) / 2

    def display_statistics(self):
        print("Minimum:", self.get_minimum())
        print("Maximum:", self.get_maximum())
        print("Arithmetic mean:", self.calculate_mean())
        print("Median:", self.calculate_median())


# Main program

stats = Statistics()

# Add numbers
stats.add_number(12)
stats.add_number(37)
stats.add_number(6)
stats.add_number(9)
stats.add_number(17)

# Display numbers
stats.display_numbers()

# Display statistics
stats.display_statistics()