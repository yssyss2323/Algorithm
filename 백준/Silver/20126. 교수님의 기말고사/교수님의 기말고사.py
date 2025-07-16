import sys
input = sys.stdin.readline

n, m, s = map(int, input().split())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort()

if times[0][0] >= m:
    print(0)
else:
    for i in range(n - 1):
        gap = times[i + 1][0] - (times[i][0] + times[i][1])
        if gap >= m:
            print(times[i][0] + times[i][1])
            break
    else:
        gap = s - (times[-1][0] + times[-1][1])
        if gap >= m:
            print(times[-1][0] + times[-1][1])
        else:
            print(-1)
