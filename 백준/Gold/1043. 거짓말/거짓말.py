import sys
input = sys.stdin.readline


def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    if find(x) != find(y):
        arr[find(x)] = find(y)


n, m = map(int, input().split())
arr = [i for i in range(n + 1)]
know = list(map(int, input().split()))[1:]
for i in range(1, len(know)):
    union(know[0], know[i])

party = [list(map(int, input().split()))[1:] for _ in range(m)]

for par in party:
    for i in range(1, len(par)):
        union(par[0], par[i])

ans = m
for par in party:
    if know and find(par[0]) == find(know[0]):
        ans -= 1
print(ans)
