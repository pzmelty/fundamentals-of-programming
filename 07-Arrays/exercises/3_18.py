import MyArrays

numbers = [7, 3, 8, 5, 2]

print("Numbers:", *numbers)

print("Second largest number:", MyArrays.second_largest(numbers))

print("Median:", MyArrays.median(numbers))

result = MyArrays.smallest_largest(numbers)
print("Smallest and largest number:", *result)

print("Numbers as a string:", MyArrays.array_to_string(numbers))