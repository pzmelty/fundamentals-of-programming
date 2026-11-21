arr = [2,6,4,9,7]

def star(n):
    result ='*' * n
    return result

for i in arr:
    print(i, ":", star(i))