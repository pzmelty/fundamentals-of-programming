def f(number, even):
    total = 0

    for digit in str(number):
        digit = int(digit)

        if even and digit % 2 == 0:
            total += digit

        elif not even and digit % 2 != 0:
            total += digit

    return total

def main():
    number = int(input("Enter number: "))
    even = input("Even? (True/False): ") == "True"

    print(f(number, even))

if __name__ == "__main__":
    main()