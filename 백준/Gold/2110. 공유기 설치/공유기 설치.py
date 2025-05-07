import sys
input = sys.stdin.readline

n, c = map(int, input().split())
points = [int(input()) for _ in range(n)]
points.sort()

def check_dist(arr, d, c):
    curr = 0
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] - arr[curr] >= d:
            curr = i
            cnt += 1
        if cnt == c:
            return True
    return False

l, r = 0, points[n - 1]
ans = 0
while l <= r:
    m = (l + r) // 2
    if check_dist(points, m, c):
        if ans < m:
            ans = m
        l = m + 1
    else:
        r = m - 1
print(ans)