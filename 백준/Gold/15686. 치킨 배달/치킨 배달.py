from itertools import combinations

n, m = map(int, input().split())
homes, chickens = [], []
city = []
for i in range(n):
    tmp = list(map(int, input().split()))
    city.append(tmp)
    for j in range(n):
        if tmp[j] == 1:
            homes.append((i, j))
        elif tmp[j] == 2:
            chickens.append((i, j))

distances = []
for hx, hy in homes:
    distances.append([abs(hx - cx) + abs(hy - cy) for cx, cy in chickens])

ans = float('inf')
for arr in combinations(range(len(chickens)), m):
    tot = 0
    for i in range(len(homes)):
        tot += min(distances[i][j] for j in arr)
    if ans > tot:
        ans = tot
print(ans)
