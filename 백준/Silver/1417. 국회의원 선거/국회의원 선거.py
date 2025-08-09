import heapq

n = int(input())
me = int(input())
arr = []
for _ in range(n - 1):
    heapq.heappush(arr, - int(input()))

if n == 1:
    print(0)
else:
    ans = 0
    while True:
        curr_max = - heapq.heappop(arr)
        if curr_max >= me:
            me += 1
            curr_max -= 1
            ans += 1
            heapq.heappush(arr, - curr_max)
        else:
            print(ans)
            break