from range import range

x = int(input("Wpisz dolną granicę: "))
y = int(input("Wpisz górną granicę: "))
n = int(input("Wpisz liczbę: "))

print(f'Number {n} in the range <{x},{y}>: {range(x, y, n)}')