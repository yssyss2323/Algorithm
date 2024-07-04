t = int(input())
for _ in range(t):
    n = int(input())
    coordinates = []
    relations = [[] for _ in range(n + 2)]
    for i in range(n + 2):
        x, y = map(int, input().split())
        coordinates.append((x, y))
        for j in range(i):
            if abs(coordinates[i][0] - coordinates[j][0]) + abs(coordinates[i][1] - coordinates[j][1]) <= 1000:
                relations[i].append(j)
                relations[j].append(i)

    visited = [True] + [False] * (n + 1)
    stack = [0]
    while stack:
        curr = stack.pop()
        if curr == n + 1:
            print("happy")
            break
        for x in relations[curr]:
            if not visited[x]:
                visited[x] = True
                stack.append(x)
    else:
        print("sad")
