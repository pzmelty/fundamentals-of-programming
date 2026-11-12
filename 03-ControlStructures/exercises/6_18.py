x = int(input("x = "))
y= int(input('y = '))

if x < 0:
    if y < 0:
        q = 'third'
    elif y > 0:
        q = 'second'
if x > 0:
    if y < 0:
        q = 'fourth'
    elif y > 0:
        q = 'first'

if x == 0 or y == 0:
    print('The point is in beetween quadrants')
else:
    print(f'Point P({x},{y}) is in the {q} quadrant of the coordinate system')