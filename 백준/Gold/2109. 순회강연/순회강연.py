import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.append([0, 0])
arr.sort(key=lambda x: (-x[1], -x[0]))

day = arr[0][1]
stack = []
ans = 0
for i in range(n):
    curr = arr[i]
    next = arr[i + 1]
    heapq.heappush(stack, -curr[0])
    if day != next[1]:
        gap = day - next[1]
        for _ in range(gap):
            if stack:
                ans += -heapq.heappop(stack)
            else:
                break
        day = next[1]
print(ans)