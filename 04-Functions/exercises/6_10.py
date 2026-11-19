def f(x, y):
    total = 0

    for number in range(x, y):
        if number < 0 and number % 2 == 0:
            total += 1

    return total

def main():
    x = int(input("Enter lower range: "))
    y = int(input("Enter upper range: "))

    print(f(x, y))

if __name__ == "__main__":
    main()