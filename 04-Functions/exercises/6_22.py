def f(name):
    words = name.split()
    result = ""

    for word in words:
        result += word[0]

    return result

def main():
    name = input("Enter name: ")
    print(f(name))

if __name__ == "__main__":
    main()