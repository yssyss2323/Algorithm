n, m = map(int, input().split())
ans = list(range(1, n + 1))

for _ in range(m):
    i, j, k = map(int, input().split())
    ans[i - 1:j] = ans[k - 1:j] + ans[i - 1:k - 1]
print(*ans)