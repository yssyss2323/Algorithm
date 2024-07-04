from queue import PriorityQueue

k, n = map(int, input().split())
primes = list(map(int, input().split()))
goat = max(primes)
q = PriorityQueue()
visited = set()
for prime in primes:
    q.put(prime)

for _ in range(n - 1):
    curr = q.get()
    for i in range(k):
        tmp = curr * primes[i]
        #print(curr, tmp, q.qsize())
        if q.qsize() < n or tmp < goat:
            if tmp not in visited:
                visited.add(tmp)
                q.put(tmp)
                if tmp > goat:
                    goat = tmp
print(q.get())