def f(sentence):
    return sentence.replace(" ", "")

def main():
    sentence = input("Enter sentence: ")
    print(f(sentence))

if __name__ == "__main__":
    main()