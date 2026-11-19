def f(palindrome):
    return palindrome == palindrome[::-1]

def main():
    word = input("Enter word: ")
    print(f(word))

if __name__ == "__main__":
    main()