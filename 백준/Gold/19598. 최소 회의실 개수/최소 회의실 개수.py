import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
check = [arr[0][1]]

ans = 1
for i in range(1, n):
    stand = heapq.heappop(check)
    curr = arr[i]
    if curr[0] >= stand:
        heapq.heappush(check, curr[1])
    else:
        ans += 1
        heapq.heappush(check, curr[1])
        heapq.heappush(check, stand)
print(ans)