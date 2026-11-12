name = input('Enter a name: ')
n = len(name)
if ord(name[n-1]) == 97:  # 97 is the ASCII value of 'a'
    print(f'{name} -- Polish female name')
else:
    print(f'{name} -- foreign name')