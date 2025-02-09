def check(arr):
    val = arr[0] + arr[-1]
    for i in range(1, len(arr)):
        val += abs(arr[i] - arr[i - 1])
    return val

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
ans = 2 * n * m
for i in range(n):
    ans += check(field[i])
for i in range(m):
    ans += check([field[j][i] for j in range(n)])
print(ans)
