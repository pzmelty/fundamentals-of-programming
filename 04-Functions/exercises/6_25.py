def f(x, y):
    total = 0

    for number in range(x, y + 1):
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            total += number

    return total

def main():
    print(f(1, 20))
    print(f(10, 30))

if __name__ == "__main__":
    main()