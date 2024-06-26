n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    tmp = input().split()
    for j in range(n):
        if tmp[j] == '1':
            graph[i].append(j)

anslist = [[0] * n for _ in range(n)]
for i in range(n):
    stack = [i]
    visited = [False] * n
    while stack:
        now = stack.pop()
        for j in graph[now]:
            if not visited[j]:
                stack.append(j)
                visited[j] = True
                anslist[i][j] = 1
for ans in anslist:
    print(*ans)