n = int(input())
prev = input()
after = input()

check = []
for i in range(n):
    check.append(prev[i] == after[i])
check.append(True)


if check[0]:
    tmpcheck = check[:]
    ans = []
    tmp = 0
    for i in range(1, n - 1):
        if not tmpcheck[i]:
            tmpcheck[i] = True
            tmpcheck[i + 1] = not tmpcheck[i + 1]
            tmpcheck[i + 2] = not tmpcheck[i + 2]
            tmp += 1
    if tmpcheck[n - 1]:
        ans.append(tmp)

    tmpcheck = check[:]
    tmpcheck[2] = not tmpcheck[2]
    tmp = 2
    for i in range(1, n - 1):
        if not tmpcheck[i]:
            tmpcheck[i] = True
            tmpcheck[i + 1] = not tmpcheck[i + 1]
            tmpcheck[i + 2] = not tmpcheck[i + 2]
            tmp += 1
    if tmpcheck[n - 1]:
        ans.append(tmp)

    if not ans:
        print(-1)
    else:
        print(min(ans))

else:
    tmpcheck = check[:]
    tmpcheck[0] = not tmpcheck[0]
    tmpcheck[1] = not tmpcheck[1]
    ans = []
    tmp = 1
    for i in range(1, n - 1):
        if not tmpcheck[i]:
            tmpcheck[i] = True
            tmpcheck[i + 1] = not tmpcheck[i + 1]
            tmpcheck[i + 2] = not tmpcheck[i + 2]
            tmp += 1
    if tmpcheck[n - 1]:
        ans.append(tmp)

    tmpcheck = check[:]
    tmpcheck[0] = not tmpcheck[0]
    tmpcheck[1] = not tmpcheck[1]
    tmpcheck[2] = not tmpcheck[2]
    tmp = 1
    for i in range(1, n - 1):
        if not tmpcheck[i]:
            tmpcheck[i] = True
            tmpcheck[i + 1] = not tmpcheck[i + 1]
            tmpcheck[i + 2] = not tmpcheck[i + 2]
            tmp += 1
    if tmpcheck[n - 1]:
        ans.append(tmp)

    if not ans:
        print(-1)
    else:
        print(min(ans))
