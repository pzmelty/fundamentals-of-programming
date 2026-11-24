arr = [2, 3, 2, 5, 8, 1, 9, 8]

print("Array:", *arr)

print("Unique elements: ")
for i in arr:
    if arr.count(i) == 1:
        print(i, end=" ")