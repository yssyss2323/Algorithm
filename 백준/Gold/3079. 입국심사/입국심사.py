import sys
input = sys.stdin.readline

n,m = map(int, input().split())
need_time = [int(input()) for _ in range(n)]
need_time.sort()
min_time, max_time = need_time[0], need_time[-1] * m
ans = float('inf')
while min_time <= max_time:
    cnt = 0
    this_time = (min_time + max_time) // 2
    cnt += sum([this_time // need_time[i] for i in range(n)])
    if cnt >= m:
        max_time = this_time - 1
        ans = min(ans, this_time)
    else:
        min_time = this_time + 1
print(ans)