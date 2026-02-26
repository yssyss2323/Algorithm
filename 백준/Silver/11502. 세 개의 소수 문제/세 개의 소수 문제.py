import sys
input = sys.stdin.readline

primes = []
check = [False, False] + [True] * 999
for i in range(2, 1001):
    if check[i]:
        primes.append(i)
        for j in range(i * 2, 1001, i):
            check[j] = False

two_primes = [[]] * 1001
for i in range(len(primes)):
    for j in range(i):
        if primes[i] + primes[j] <= 1000:
            two_primes[primes[i] + primes[j]] = [primes[i], primes[j]]

for _ in range(int(input())):
    n = int(input())
    for p in primes:
        if p >= n:
            print(0)
            break
        if len(two_primes[n - p]) == 2:
            ans = sorted(two_primes[n - p] + [p])
            print(*ans)
            break
    else:
        print(0)
