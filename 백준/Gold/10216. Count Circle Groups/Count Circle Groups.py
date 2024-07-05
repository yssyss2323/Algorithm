import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    places = [list(map(int, input().split())) for _ in range(n)]
    relations = [[] for _ in range(n)]#[[False] * n for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (places[i][0] - places[j][0]) ** 2 + (places[i][1] - places[j][1]) ** 2 \
                <= (places[i][2] + places[j][2]) ** 2:
                relations[i].append(j)
                relations[j].append(i)
    #print(relations)
    visited = set()
    stack = []
    cnt = 0
    for i in range(n):
        if i not in visited:
            visited.add(i)
            stack.append(i)
            cnt += 1
            while stack:
                curr = stack.pop()
                for x in relations[curr]:
                    if x not in visited:
                        visited.add(x)
                        stack.append(x)
    print(cnt)