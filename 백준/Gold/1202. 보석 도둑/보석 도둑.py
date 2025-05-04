import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
diamonds = [list(map(int, input().split())) for _ in range(n)]
heapq.heapify(diamonds)
weights = [int(input()) for _ in range(k)]
weights.sort()

ans = 0
curr = []
for w in weights:
    while diamonds and w >= diamonds[0][0]:
        tmp = -1 * heapq.heappop(diamonds)[1]
        heapq.heappush(curr, tmp)
    if curr:
        ans -= heapq.heappop(curr)
    else:
        if not diamonds:
            break
print(ans)