my_tuple = (50, 20, 40, 50, 30, 50)

value = int(input("Value: "))

print("Tuple:", *my_tuple)
print("Number of occurrences:", my_tuple.count(value))