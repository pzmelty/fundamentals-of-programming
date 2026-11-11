###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
volume = a * b * c
surface = 2 * (a * b + a * c + b * c)
print(f'Objętość prostopadłościanu o bokach {a}, {b} i {c}, to {volume}')
print(f'Pole powierzchni prostopadłościanu o bokach {a}, {b} i {c}, to {surface}')