nb = int(input('Enter decimal number: '))
nbb = nb
binary = ''
while nbb > 0:
    r = nbb % 2
    binary = str(r) + binary
    nbb = nbb// 2

print(f'{nb}(10) = {binary}(2)')