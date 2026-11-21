# Transpose matrix
def transpose_matrix(m):
    result = []

    for i in range(len(m[0])):
        row = []
        for j in range(len(m)):
            row.append(m[j][i])
        result.append(row)

    return result


# Print matrix
def print_matrix(m):
    for row in m:
        for element in row:
            print(element, end=" ")
        print()


# First matrix
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Second matrix
matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

# Third matrix
matrix3 = [
    [5, 6, 7, 8]
]

print("Matrix 1:")
print_matrix(transpose_matrix(matrix1))

print("Matrix 2:")
print_matrix(transpose_matrix(matrix2))

print("Matrix 3:")
print_matrix(transpose_matrix(matrix3))