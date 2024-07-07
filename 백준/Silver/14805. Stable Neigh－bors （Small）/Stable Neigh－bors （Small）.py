t = int(input())
for i in range(t):
    n, r, o, y, g, b, v = map(int, input().split())
    if r >= y >= b:
        order = 'RYB'
    elif r >= b >= y:
        order = 'RBY'
    elif y >= r >= b:
        order = 'YRB'
    elif y >= b >= r:
        order = 'YBR'
    elif b >= r >= y:
        order = 'BRY'
    else:
        order = 'BYR'
    ans = ""
    tmplist = sorted([r, y, b])
    ttmp = tmplist[1] - tmplist[0]
    ans += (order[0] + order[1]) * (ttmp)
    tmplist[1] -= ttmp
    tmplist[2] -= ttmp
    ans += (order[0] + order[1] + order[0] + order[2]) * min(tmplist[2]//2, tmplist[1])
    if tmplist[1] <= tmplist[2] // 2:
        tmplist[2] -= tmplist[1] * 2
        if tmplist[2] >= 1:
            ans = "IMPOSSIBLE"
    else:
        tmplist[0] -= tmplist[2] // 2
        tmplist[1] -= tmplist[2] // 2
        tmplist[2] -= (tmplist[2] // 2) * 2
        if tmplist[2]:
            ans += order[0]
        ans += (order[1] + order[2]) * tmplist[0]
    print(f"Case #{i + 1}: {ans}")
