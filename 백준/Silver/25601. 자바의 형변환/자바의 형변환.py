n = int(input())
graph = dict()
for _ in range(n - 1):
    b, a = input().split()
    graph[a] = graph.get(a, []) + [b]
    if b not in graph:
        graph[b] = []

visited = set()
a, b = input().split()
stack = [a]
visited.add(a)
while stack:
    curr = stack.pop()
    flag = False
    for next in graph[curr]:
        if next == b:
            print(1)
            flag = True
            break
        if next not in visited:
            stack.append(next)
            visited.add(next)
    if flag:
        break
else:
    stack = [b]
    visited = set()
    visited.add(b)
    while stack:
        curr = stack.pop()
        flag = False
        for next in graph[curr]:
            if next == a:
                print(1)
                flag = True
                break
            if next not in visited:
                stack.append(next)
                visited.add(next)
        if flag:
            break
    else:
        print(0)
