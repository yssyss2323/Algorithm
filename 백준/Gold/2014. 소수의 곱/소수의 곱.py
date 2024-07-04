import heapq
k, n = map(int, input().split())
primes = list(map(int, input().split()))
pq = []
for prime in primes:
    heapq.heappush(pq, prime)
for _ in range(n):
    curr = heapq.heappop(pq)
    for i in range(k):
        tmp = curr * primes[i]
        #print(curr, primes[i], tmp)
        heapq.heappush(pq, tmp)
        if curr % primes[i] == 0:
            break
print(curr)