max_num = 318137

primes = []
check = [False] * 2 + [True] * (max_num - 1)
for i in range(2, max_num + 1):
    if check[i]:
        primes.append(i)
        for j in range(2 * i, max_num + 1, i):
            check[j] = False

super_prime = []
for i in range(2, len(primes) + 1):
    if check[i]:
        super_prime.append(primes[i - 1])

for _ in range(int(input())):
    print(super_prime[int(input()) - 1])
