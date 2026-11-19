def f(number):
    total = 0
    number = str(number)

    for digit in number:
        if number.count(digit) > 1:
            total += int(digit)

    return total

def main():
    number = int(input("Enter number: "))
    print(f(number))

if __name__ == "__main__":
    main()