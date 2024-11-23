import heapq
import sys
input = sys.stdin.readline

n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
lectures.sort()

arr = [lectures[0][1]]

for i in range(1, n):
    curr = lectures[i]
    if arr and arr[0] <= curr[0]:
        heapq.heappop(arr)
    heapq.heappush(arr, curr[1])
print(len(arr))