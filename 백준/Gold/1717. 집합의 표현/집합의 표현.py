import sys

input = sys.stdin.readline


def find(x):
    if x == arr[x]:
        return x
    else:
        arr[x] = find(arr[x])
        return arr[x]


def union(x, y):
    xx = find(x)
    yy = find(y)
    if xx != yy:
        arr[yy] = xx


n, m = map(int, input().split())
arr = [i for i in range(n + 1)]
for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union(a, b)
    else:
        if find(a) != find(b):
            print("NO")
        else:
            print("YES")
