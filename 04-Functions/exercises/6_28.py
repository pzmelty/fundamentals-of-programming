def f(dice):
    current_digit = dice[0]
    current_count = 1

    best_digit = dice[0]
    best_count = 1

    for digit in dice[1:]:
        if digit == current_digit:
            current_count += 1
        else:
            current_digit = digit
            current_count = 1

        if current_count > best_count:
            best_count = current_count
            best_digit = current_digit

    return int(best_digit)

def main():
    dice = input("Enter dice results: ")
    print(f(dice))

if __name__ == "__main__":
    main()