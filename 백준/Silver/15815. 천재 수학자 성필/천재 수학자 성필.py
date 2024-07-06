expression = input()
stack = []
for ch in expression:
    if ch not in '+-*/':
        stack.append(ch)
    else:
        num2 = int(stack.pop())
        num1 = int(stack.pop())
        if ch == '+':
            num = num1 + num2
        elif ch == '-':
            num = num1 - num2
        elif ch == '*':
            num = num1 * num2
        else:
            num = num1 // num2
        stack.append(num)
print(stack[0])