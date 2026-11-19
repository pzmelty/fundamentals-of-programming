def f(n):
    return "*/" * (n - 1) + "*"

def main():
    n = int(input("Enter number: "))
    print(f(n))

if __name__ == "__main__":
    main()