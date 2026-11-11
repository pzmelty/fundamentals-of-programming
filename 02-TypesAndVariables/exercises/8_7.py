liczba = int(input('Enter number: '))
#transformacja liczby na liczbę binarną
bin = bin(liczba)
#transformacja liczby na liczbę szesnastkową
hex = hex(liczba)
print(f'Liczba {liczba} w systemie binarnym to: {bin}')
print(f'Liczba {liczba} w systemie szesnastkowym to: {hex}')