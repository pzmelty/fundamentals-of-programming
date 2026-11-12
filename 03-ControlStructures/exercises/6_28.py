a = 0
b = 1
c = 0 #licznik

while c < 20:
    print (a, end = ' ')
    nn = a + b #suma dwoch kolejnych liczb
    a = b   #pierwsza staje sie druga
    b = nn #druga zamienia sie w trzecia
    c += 1