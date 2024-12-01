import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    ans = 0
    for _ in range(k - 2):
        tmp1 = heapq.heappop(arr)
        tmp2 = heapq.heappop(arr)
        ans += tmp1 + tmp2
        heapq.heappush(arr, tmp1 + tmp2)
    print(ans + sum(arr))