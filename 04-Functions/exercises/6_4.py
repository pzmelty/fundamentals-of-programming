def count(sent):
    total = 0
    for char in sent:
        if char == "e":
            total += 1
    return total

def main():
    sent = input("Napisz zdanie: ")
    print(f'W tym zdaniu jest {count(sent)} liter e')

if __name__ == "__main__":
    main()