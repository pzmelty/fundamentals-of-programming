arr = [34, 7, 19, 4, 21, 8]

i = len(arr) - 1
total = 0

while i >= 0:
    if arr[i] % 2 == 0:
        total = total + arr[i]
    i -= 1

print("Sum of even numbers:", total)