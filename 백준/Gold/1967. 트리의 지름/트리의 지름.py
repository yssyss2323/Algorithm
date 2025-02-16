import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, c, v = map(int, input().split())
    arr[p].append((c, v))
    arr[c].append((p, v))

stack = [(1, 0)]
visited = [False] * (n + 1)
visited[1] = True
check = (0, 1)
while stack:
    now, val = stack.pop()
    for i, x in arr[now]:
        if not visited[i]:
            stack.append((i, val + x))
            visited[i] = True
            if val + x > check[0]:
                check = (val + x, i)

ans = 0
visited = [False] * (n + 1)
visited[check[1]] = True
stack = [(check[1], 0)]
while stack:
    now, val = stack.pop()
    for i, x in arr[now]:
        if not visited[i]:
            stack.append((i, val + x))
            visited[i] = True
            if val + x > ans:
                ans = val + x
print(ans)