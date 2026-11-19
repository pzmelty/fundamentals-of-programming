def f(product_code):
    total = 0

    for digit in product_code[:3]:
        total += int(digit)

    return total % 7 == int(product_code[3])

def main():
    product_code = input("Enter product code: ")
    print(f(product_code))

if __name__ == "__main__":
    main()