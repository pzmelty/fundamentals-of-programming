# Converts 2D array into 1D array
def convert_2d_to_1d(arr):
    result = []

    for row in arr:
        for element in row:
            result.append(element)

    return result


# First array
arr1 = [
    [2, 3],
    [1, 5]
]

# Second array
arr2 = [
    [0, 5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

# Third array
arr3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

print(convert_2d_to_1d(arr1))
print(convert_2d_to_1d(arr2))
print(convert_2d_to_1d(arr3))