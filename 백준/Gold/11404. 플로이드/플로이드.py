import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[float('inf') if i !=j else 0 for i in range(n + 1)] for j in range(n + 1)]


for _ in range(m):
    a, b, c = map(int, input().split())
    if arr[a][b] > c:
        arr[a][b] = c

for k in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if arr[s][e] > arr[s][k] + arr[k][e]:
                arr[s][e] = arr[s][k] + arr[k][e]



for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == float('inf'):
            arr[i][j] = 0
    print(*arr[i][1:])
