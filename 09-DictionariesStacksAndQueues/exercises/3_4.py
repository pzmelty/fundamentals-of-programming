stack = []

number = int(input("Natural number: "))

n = number

while n > 0:
    remainder = n % 2
    stack.append(remainder)
    n = n // 2

binary_number = ""

while len(stack) > 0:
    binary_number += str(stack.pop())

print("Binary number:", binary_number)