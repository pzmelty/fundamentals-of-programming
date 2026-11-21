def occurs(number, array):
    for i in array:
        if i == number:
            return True
    return False

arr = [15, 38, 7, 23, 14]

number = int(input("Number: "))

print("Array:", *arr)

if occurs(number, arr):
    print("Result: number", number, "appears in the array")
else:
    print("Result: number", number, "does not appear in the array")