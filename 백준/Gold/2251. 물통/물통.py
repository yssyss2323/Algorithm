a, b, c = map(int, input().split())

ans = set()
stack = [(0, c)]
visited = set([(0, c)])
while stack:
    curr = stack.pop()
    now = [curr[0], c - sum(curr), curr[1]]
    if curr[0] == 0:
        ans.add(curr[1])

    case1 = [now[0] - min(b - now[1], now[0]), now[1] + min(b - now[1], now[0]), now[2]]
    if (case1[0], case1[2]) not in visited:
        stack.append((case1[0], case1[2]))
        visited.add((case1[0], case1[2]))

    case2 = [now[0] + min(a - now[0], now[1]), now[1] - min(a - now[0], now[1]), now[2]]
    if (case2[0], case2[2]) not in visited:
        stack.append((case2[0], case2[2]))
        visited.add((case2[0], case2[2]))

    case3 = [now[0] - min(c - now[2], now[0]), now[1], now[2] + min(c - now[2], now[0])]
    if (case3[0], case3[2]) not in visited:
        stack.append((case3[0], case3[2]))
        visited.add((case3[0], case3[2]))

    case4 = [now[0] + min(a - now[0], now[2]), now[1], now[2] - min(a - now[0], now[2])]
    if (case4[0], case4[2]) not in visited:
        stack.append((case4[0], case4[2]))
        visited.add((case4[0], case4[2]))

    case5 = [now[0], now[1] - min(c - now[2], now[1]), now[2] + min(c - now[2], now[1])]
    if (case5[0], case5[2]) not in visited:
        stack.append((case5[0], case5[2]))
        visited.add((case5[0], case5[2]))

    case6 = [now[0], now[1] + min(b - now[1], now[2]), now[2] - min(b - now[1], now[2])]
    if (case6[0], case6[2]) not in visited:
        stack.append((case6[0], case6[2]))
        visited.add((case6[0], case6[2]))

print(*sorted(ans))
