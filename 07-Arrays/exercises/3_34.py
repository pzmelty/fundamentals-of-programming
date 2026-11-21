# creates identity matrix
def identity_matrix(n):
    arr = []

    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        arr.append(row)

    return arr


# prints 2D array
def print_matrix(arr):
    for row in arr:
        for element in row:
            print(element, end=" ")
        print()


# prints three identity matrices
matrix3 = identity_matrix(3)
matrix5 = identity_matrix(5)
matrix8 = identity_matrix(8)

print("Identity matrix 3:")
print_matrix(matrix3)

print("Identity matrix 5:")
print_matrix(matrix5)

print("Identity matrix 8:")
print_matrix(matrix8)