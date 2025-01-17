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

n = int(input())
m = int(input())
arr = [i for i in range(n + 1)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1:
            union(i + 1, j + 1)

plan = list(map(int, input().split()))
check = set([find(i) for i in plan])
if len(check) == 1:
    print("YES")
else:
    print("NO")