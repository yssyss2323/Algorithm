import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    dist = [1e9] * (n + 1)

    arr = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        arr.append((s, e, t))
        arr.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        arr.append((s, e, -t))

    ans = 'NO'
    for x in range(n):
        for s, e, t in arr:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if x == n - 1:
                    ans = 'YES'
    print(ans)