import sys
input = sys.stdin.readline

n, m = map(int, input().split())
checkpoint = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            checkpoint.append((i, j))
checkpoint.sort(key=lambda x: x[0] - x[1])

ans = [2 * n + m - i for i in range(n)] + [2 * n + 2 * m - i for i in range(m)] + [0] * (n + m)
for i, j in checkpoint:
    ans[i], ans[j + n] = ans[j + n], ans[i]
for i in range(n + m):
    ans[ans[i] - 1] = i + 1
print(*ans)