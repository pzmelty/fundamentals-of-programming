def bubblesort(array):
    n = len(array)

    for i in range(n):
        for j in range(n -1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j +1] = array[j+1], array[j]
    return array

# Test 1
arr1 = [7, 3, 9, 1, 5]
print(bubblesort(arr1))

# Test 2
arr2 = [12, 4, 8, 2, 6]
print(bubblesort(arr2))

# Test 3
arr3 = [15, 10, 3, 20, 1]
print(bubblesort(arr3))