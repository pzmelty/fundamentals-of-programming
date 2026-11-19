def f(n):
    count = 0
    number = 1

    while count < n:
        number += 1

        if number > 1:
            is_prime = True

            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break

            if is_prime:
                count += 1

    return number

def main():
    n = int(input("Enter n: "))
    print(f(n))

if __name__ == "__main__":
    main()