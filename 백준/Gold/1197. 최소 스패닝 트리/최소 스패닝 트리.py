import sys
input = sys.stdin.readline

def set_find(x):
    if vert_set[x] != x:
        vert_set[x] = set_find(vert_set[x])
    return vert_set[x]

def union(x, y):
    x_root = set_find(x)
    y_root = set_find(y)
    if x_root != y_root:
        vert_set[x_root] = y_root

v, e = map(int, input().split())
vert_set = [i for i in range(v + 1)]
edges = [list(map(int, input().split())) for _ in range(e)]
edges.sort(key=lambda x: x[2])

ans = 0
cnt = 0
for v1, v2, c in edges:
    v1_root = set_find(v1)
    v2_root = set_find(v2)
    if v1_root == v2_root:
        continue
    else:
        vert_set[v1_root] = v2_root
        ans += c
        cnt += 1
    if cnt == v - 1:
        break
print(ans)