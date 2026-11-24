# Creates a two-dimensional array filled with zeros
def create_2d_arr(x, y):
    arr = []

    for i in range(x):
        row = []
        for j in range(y):
            row = row + [0]
        arr = arr + [row]

    return arr


# Creates an array with 3 rows and 5 columns
array = create_2d_arr(3, 5)

# Prints the array
for row in array:
    print(row)