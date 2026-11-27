def reverse_string(text):
    stack = []

    for char in text:
        stack.append(char)

    reversed_text = ""

    while len(stack) > 0:
        reversed_text += stack.pop()

    return reversed_text


text = input("Enter text: ")

result = reverse_string(text)

print("Reversed text:", result)