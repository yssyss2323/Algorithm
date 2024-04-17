n = int(input())

prime = [False] * 2 + [True] * (n - 1)
for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(i * 2, n + 1, i):
            prime[j] = False

factor = []
for i in range(1, n + 1):
    if prime[i]:
        factor.append(i)
for i in range(len(factor)):
    k = 1
    while factor[i] ** (k + 1) <= n:
        k += 1
    factor[i] **= k

answer = 1
for i in factor:
    answer *= i
    answer %= 987654321
print(answer)
