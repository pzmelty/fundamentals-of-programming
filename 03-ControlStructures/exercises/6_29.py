N = int(input('Enter number:' ))
i = 2
c = 0
while c < N:
    is_prime = True #2 jest pierwsza liczba pierwsza
    d = 2
    while d < i:    
        if i % d == 0:
            is_prime = False    #sprawdzenie po kolei kazdej liczby nie wiekszej niz i
            break
        d += 1
    if is_prime:
        print(i, end = ' ')     #wypisanie liczb pierwszych
        c += 1

    i += 1          # kolejna liczba