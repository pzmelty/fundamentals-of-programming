def f(n):
    a = 0
    b = 1

    for i in range(n - 1):
        a, b = b, a + b

    return a

def main():
    n = int(input("Enter n: "))
    print(f(n))

if __name__ == "__main__":
    main()