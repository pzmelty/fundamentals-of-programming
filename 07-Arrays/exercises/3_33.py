arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# print array before changes
print("BEFORE:")
for row in arr:
    print(row)

# swap first and last column
for i in range(len(arr)):
    arr[i][0], arr[i][-1] = arr[i][-1], arr[i][0]

# print array after changes
print("AFTER:")
for row in arr:
    print(row)