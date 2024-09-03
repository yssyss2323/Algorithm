n, m, k = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(n)]
check_row = [sum(row) for row in garden]
check_col = []
for i in range(m):
    tmp = 0
    for j in range(n):
        tmp += garden[j][i]
    check_col.append(tmp)
# print(check_row, check_col)

if k == 1:
    if sum(check_row) == 2:
        print(0)
    else:
        print(1)
        x = check_row.index(1) + 1
        y = check_col.index(1) + 1
        print(x, y)
else:
    zx = sum([1 if x >= k else 0 for x in check_row])
    zy = sum([1 if y >= k else 0 for y in check_col])
    #print(zx , zy)
    if zx == 2:
        print(0)
    elif zx == 1:
        if zy == 1:
            if sum(check_row) < k * 2:
                print(1)
                for i in range(n):
                    if check_row[i] >= k:
                        x = i + 1
                        break
                for j in range(m):
                    if check_col[j] >= k:
                        y = j + 1
                        break
                print(x, y)
            else:
                print(0)
        else:
            x = 0
            for i in range(n):
                if check_row[i]:
                    x = i + 1
                    break
            y = check_col.index(1) + check_row[x - 1] - k + 1
            print(k * 2 - check_row[x - 1])
            for i in range(k * 2 - check_row[x - 1]):
                print(x, y + i)
    else:
        if zy == 2:
            print(0)
        else:
            y = 0
            for i in range(m):
                if check_col[i]:
                    y = i + 1
                    break
            x = check_row.index(1) + check_col[y - 1] - k + 1
            print(k * 2 - check_col[y - 1])
            for i in range(k * 2 - check_col[y - 1]):
                print(x + i, y)
