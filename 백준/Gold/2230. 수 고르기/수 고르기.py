import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

ans = float('inf')
s, e = 0, 0
while True:
    if arr[e] - arr[s] < m:
        if e == n - 1:
            print(ans)
            break
        e += 1
    elif arr[e] - arr[s] > m:
        if arr[e] - arr[s] < ans:
            ans = arr[e] - arr[s]
        s += 1
    else:
        print(m)
        break