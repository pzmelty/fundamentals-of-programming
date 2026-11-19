def f(expression):
    total = 0
    sign = 1

    for char in expression:
        if char == "+":
            sign = 1
        elif char == "-":
            sign = -1
        else:
            total += sign * int(char)

    return total

def main():
    expression = input("Enter expression: ")
    print(f(expression))

if __name__ == "__main__":
    main()