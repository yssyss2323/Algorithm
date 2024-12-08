test_num = 0
while True:
    test_num += 1
    string = input()
    if '-' in string:
        break

    stack = []
    for ch in string:
        if ch == '{':
            stack.append(0)
        else:
            if stack and stack[-1] == 0:
                stack.pop()
            else:
                stack.append(1)

    ans = 0
    for i in range(len(stack)):
        if i % 2 != stack[i]:
            ans += 1

    print(f"{test_num}. {ans}")