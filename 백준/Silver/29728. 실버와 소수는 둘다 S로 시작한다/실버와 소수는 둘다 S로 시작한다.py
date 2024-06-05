N = int(input())
prime = [False] * 2 + [True] * (N - 1)
for i in range(2, N + 1):
    if prime[i]:
        for j in range(i * 2, N + 1, i):
            prime[j] = False

prime_cnt = prime.count(True)
if N == 1:
    print(1, 0)
elif N == 2:
    print(0, 2)
else:
    s = prime_cnt * 2 - 1
    b = N - s
    print(b,s)