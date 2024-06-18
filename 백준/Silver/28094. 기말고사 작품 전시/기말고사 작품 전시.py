from itertools import permutations
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ab = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        v, a, b = map(int, input().split())
        ab[a][b] += v

    maximum = -1
    cnt = 0
    for case in list(permutations(range(1, n + 1), n)):
        score = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                score += ab[case[i]][case[j]]
        if score > maximum:
            maximum = score
            cnt = 1
        elif score == maximum:
            cnt += 1

    print(maximum, cnt)
