import heapq
import sys
input = sys.stdin.readline

n = int(input())
lecture = []
for _ in range(n):
    _, s, e = map(int, input().split())
    lecture.append((s, e))
lecture.sort()

arr = [lecture[0][1]]

ans = 0
for i in range(1, n):
    curr = lecture[i]
    if arr[0] <= curr[0]:
        heapq.heappop(arr)
    heapq.heappush(arr, curr[1])
print(len(arr))