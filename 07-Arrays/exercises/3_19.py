arr = [1, 2, 3, 4, 34, 56]
nb = int(input('Enter a number: '))
result = 0
for i in arr:
    if i > nb:
        result += 1

print(result)