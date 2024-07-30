a,b,c = map(int, input().split())
tot = a + b + c
if tot % 3:
    print(0)
else:
    visited = [[False] * (tot + 1) for _ in range(tot + 1)]
    stack = [(a,b)]
    visited[a][b] = True
    while stack:
        curr1, curr2 = stack.pop()
        if curr1 == curr2 == tot // 3:
            print(1)
            break
        curr3 = tot - curr1 - curr2
        for tmp1, tmp2 in (min(curr1, curr2), max(curr1, curr2)), (min(curr2, curr3), max(curr2, curr3)), (min(curr1, curr3), max(curr1, curr3)):
            if tmp1 < tmp2:
                tmp2 -= tmp1
                tmp1 *= 2
            nex_a, _ , nex_b = sorted((tmp1, tmp2, tot- tmp1 - tmp2))
            if not visited[nex_a][nex_b]:
                stack.append((nex_a, nex_b))
                visited[nex_a][nex_b] = True
    else:
        print(0)
