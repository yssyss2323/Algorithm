import heapq
import sys
input = sys.stdin.readline

n = int(input())
size = [int(input()) for _ in range(n)]
if n == 1:
    print(0)
else:
    size.sort()
    ans = 0
    for _ in range(n - 1):
        tmp1 = heapq.heappop(size)
        tmp2 = heapq.heappop(size)
        ans += tmp1 + tmp2
        heapq.heappush(size, tmp1 + tmp2)
    print(ans)