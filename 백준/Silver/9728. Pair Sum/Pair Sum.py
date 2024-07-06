import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t + 1):
    n, m = map(int, input().split())
    numlist = list(map(int, input().split()))
    l, r = 0, n - 1
    cnt = 0
    while l < r:
        if numlist[l] + numlist[r] < m:
            l += 1
        elif numlist[l] + numlist[r] > m:
            r -= 1
        else:
            cnt += 1
            l += 1
            r -= 1
    print(f"Case #{i}: {cnt}")