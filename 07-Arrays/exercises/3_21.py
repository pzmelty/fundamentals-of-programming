arr1 = [2, 4, 6]
arr2 = [1, 2, 3, 4, 5, 6, 7]

is_subset = True

for i in arr1:
    if i not in arr2:
        is_subset = False

if is_subset:
    print("First array is a subset of the second array")
else:
    print("First array is not a subset of the second array")