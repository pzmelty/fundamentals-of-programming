def f(amount_to_pay):
    coins = 0

    coins += amount_to_pay // 5
    amount_to_pay %= 5

    coins += amount_to_pay // 2
    amount_to_pay %= 2

    coins += amount_to_pay

    return coins

def main():
    amount_to_pay = int(input("Enter amount to pay: "))

    print(f(amount_to_pay))

if __name__ == "__main__":
    main()