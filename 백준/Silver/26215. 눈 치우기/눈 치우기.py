import heapq

n = int(input())
tmp = list(map(int, input().split()))
if len(tmp) < 3:
    tmp += [0] * (3 - len(tmp))
snows = [-i for i in tmp]
heapq.heapify(snows)

ans = 0
while True:
    snow1 = heapq.heappop((snows))
    snow2 = heapq.heappop((snows))
    if not snow1 and not snow2:
        break
    elif not snow1 or not snow2:
        ans -= min(snow1, snow2)
        break
    else:
        gap = snows[0] - snow2
        if snows[0]:
            gap += 1
        ans += gap
        snow1 += gap
        snow2 += gap
        heapq.heappush(snows, snow1)
        heapq.heappush(snows, snow2)
print(ans if ans <= 1440 else -1)
