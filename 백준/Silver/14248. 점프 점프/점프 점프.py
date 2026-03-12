n = int(input())
arr = list(map(int, input().split()))
mat = [[] for _ in range(n)]
for i in range(n):
    if 0 <= i - arr[i] < n:
        mat[i].append(i - arr[i])
    if 0 <= i + arr[i] < n:
        mat[i].append(i + arr[i])

s = int(input()) - 1
visited = [False for _ in range(n)]
stack = [s]
visited[s] = True

while stack:
    curr = stack.pop()
    for x in mat[curr]:
        if not visited[x]:
            stack.append(x)
            visited[x] = True
print(visited.count(True))
