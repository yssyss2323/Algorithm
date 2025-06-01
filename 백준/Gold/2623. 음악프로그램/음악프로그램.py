import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj_arr = [[] for _ in range(n + 1)]
in_rank = [float('inf')] + [0] * n
for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0]):
        adj_arr[tmp[i]].append(tmp[i + 1])
        in_rank[tmp[i + 1]] += 1

topology_sort = []
for _ in range(n):
    for i in range(1, n + 1):
        if in_rank[i] == 0:
            in_rank[i] = -1
            topology_sort.append(i)
            for x in adj_arr[i]:
                in_rank[x] -= 1
            break
    else:
        print(0)
        break
else:
    for x in topology_sort:
        print(x)