import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
arr = list(map(int, input().split()))
snail = arr[v - 1:]

for _ in range(m):
    k = int(input())
    if k + 1 <= n:
        print(arr[k])
    else:
        tmp = (k - 1) % (n - v + 1)
        print(snail[tmp - 1])