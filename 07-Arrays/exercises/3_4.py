arr = [-15,8,-31,47,-2,19]
min = arr[0]
for i in range(len(arr)-1):
    if arr[i] < min:
        min = arr[i]
print(min)