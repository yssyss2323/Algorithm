n, m, h = map(int, input().split())
ladders = [[None] * (n - 1) for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    ladders[a - 1][b - 1] = True
    if b - 1 > 0:
        ladders[a - 1][b - 2] = False
    if b - 1 < n - 2:
        ladders[a - 1][b] = False

checklist = []
for i in range(h):
    for j in range(n - 1):
        if ladders[i][j] is None:
            checklist.append((i, j))


def simulate(ladders):
    start = list(range(len(ladders[0]) + 1))
    for i in range(len(ladders)):
        for j in range(len(ladders[0])):
            if ladders[i][j]:
                start[j], start[j + 1] = start[j + 1], start[j]
    return start


target = list(range(n))
if simulate(ladders) == target:
    print(0)
else:
    for i in range(len(checklist)):
        x, y = checklist[i]
        ladders[x][y] = True
        if simulate(ladders) == target:
            print(1)
            break
        ladders[x][y] = None
    else:
        flag1 = False
        for i in range(1, len(checklist)):
            x1, y1 = checklist[i]
            ladders[x1][y1] = True
            for j in range(i):
                x2, y2 = checklist[j]
                if x1 == x2 and abs(y1 - y2) == 1:
                    continue
                ladders[x2][y2] = True
                if simulate(ladders) == target:
                    print(2)
                    flag1 = True
                    break
                ladders[x2][y2] = None
            if flag1:
                break
            ladders[x1][y1] = None
        else:
            flag2 = False
            for i in range(2, len(checklist)):
                x1, y1 = checklist[i]
                ladders[x1][y1] = True
                for j in range(1, i):
                    x2, y2 = checklist[j]
                    if x1 == x2 and abs(y1 - y2) == 1:
                        continue
                    ladders[x2][y2] = True
                    for k in range(j):
                        x3, y3 = checklist[k]
                        if (x1 == x3 and abs(y1 - y3) == 1) or (x2 == x3 and abs(y2 - y3)) == 1:
                            continue
                        ladders[x3][y3] = True
                        if simulate(ladders) == target:
                            print(3)
                            flag2 = True
                            break
                        ladders[x3][y3] = None
                    if flag2:
                        break
                    ladders[x2][y2] = None
                if flag2:
                    break
                ladders[x1][y1] = None
            else:
                print(-1)
