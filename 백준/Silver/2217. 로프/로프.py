n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=True)

ans = ropes[0]
for i in range(1, n):
    tmp = (i + 1) * ropes[i]
    if tmp > ans:
        ans = tmp
print(ans)
