import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for _ in range(m):
    a1 = heapq.heappop(arr)
    a2 = heapq.heappop(arr)
    heapq.heappush(arr, a1 + a2)
    heapq.heappush(arr, a1 + a2)
print(sum(arr))