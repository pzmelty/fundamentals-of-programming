def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False

    return True


arr1 = ["water", "book", "sky"]
arr2 = ["water", "book", "sky"]

print("Array1:", *arr1)
print("Array2:", *arr2)

if compare(arr1, arr2):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are different")