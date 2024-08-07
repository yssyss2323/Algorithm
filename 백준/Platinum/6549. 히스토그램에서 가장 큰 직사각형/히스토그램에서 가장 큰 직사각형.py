while True:
    test_case = input()
    if test_case[0] == '0':
        break

    n = int(test_case.split()[0])
    heights = list(map(int, test_case.split()[1:]))
    stack = []
    ans = 0
    for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            if h * w > ans:
                ans = h * w
        stack.append(i)

    while stack:
        h = heights[stack.pop()]
        w = n if not stack else n - stack[-1] - 1
        if h * w > ans:
            ans = h * w

    print(ans)