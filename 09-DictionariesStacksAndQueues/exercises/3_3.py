expression1 = "[(2+3)*4+5]/6-({7*8}+[4])"
expression2 = "[(2+3)/4)"
expression3 = "(2-3*4+(5/6)"

def brackets_ok(expression):
    stack = []

    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if len(stack) == 0:
                return False

            if stack.pop() != brackets[char]:
                return False

    return len(stack) == 0


if brackets_ok(expression1):
    print("Expression 1: brackets are OK")
else:
    print("Expression 1: brackets are NOT correct")


if brackets_ok(expression2):
    print("Expression 2: brackets are OK")
else:
    print("Expression 2: brackets are NOT correct")


if brackets_ok(expression3):
    print("Expression 3: brackets are OK")
else:
    print("Expression 3: brackets are NOT correct")