arr = [8,2,5,1,9]
print(arr)
for i in range(len(arr)-1):
    arr[i] = arr[i]**2

print(arr)