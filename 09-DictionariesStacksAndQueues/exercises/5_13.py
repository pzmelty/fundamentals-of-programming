def calculate_rpn():
    stack = []

    while True:
        value = input("Enter number, operator (+, -, *, /) or =: ")

        if value == "=":
            if len(stack) == 1:
                print("Result:", stack.pop())
            else:
                print("Incorrect expression")
            break

        elif value in ["+", "-", "*", "/"]:
            if len(stack) < 2:
                print("Not enough numbers")
                break

            b = stack.pop()
            a = stack.pop()

            if value == "+":
                result = a + b
            elif value == "-":
                result = a - b
            elif value == "*":
                result = a * b
            elif value == "/":
                result = a / b

            stack.append(result)

        else:
            stack.append(float(value))


calculate_rpn()