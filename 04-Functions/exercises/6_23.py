def f(password):
    if len(password) < 6:
        return False

    if len(password) != len(set(password)):
        return False

    return True

def main():
    password = input("Enter password: ")
    print(f(password))

if __name__ == "__main__":
    main()