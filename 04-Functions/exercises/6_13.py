def f(n):
    result = ""

    for i in range(1, n + 1):
        result += str(i)

    return result

def main():
    n = int(input("Enter number: "))
    print(f(n))

if __name__ == "__main__":
    main()