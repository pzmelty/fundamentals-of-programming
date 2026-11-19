def f(binary_number):
    for digit in binary_number:
        if digit != "0" and digit != "1":
            return False

    return True

def main():
    binary_number = input("Enter binary number: ")

    print(f(binary_number))

if __name__ == "__main__":
    main()