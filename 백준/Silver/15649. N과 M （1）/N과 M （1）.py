def p(n, m):
    tmp = []
    if m == 1:  # nP1
        for i in range(1, n + 1):
            tmp.append([i])
        return tmp
    else:  # nPm = n-1Pm-1 * m + n-1Pm
        for i in p(n - 1, m - 1):
            for j in range(m):
                tmp.append(i[:j] + [n] + i[j:])
        if n - 1 >= m:
            tmp += p(n - 1, m)
        tmp.sort()
        return tmp

N, M = map(int, input().split())
for i in p(N, M):
    print(*i)