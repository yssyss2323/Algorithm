n = int(input())
k = int(input())

prime = [False, False] + [True] * (n - 1)
check = []
for i in range(2, n + 1):
    if prime[i]:
        if i >= k:
            check.append(i)
        for j in range(2 * i, n + 1, i):
            prime[j] = False

sejun = [False] + [True] * n
for i in range(k + 1, n + 1):
    if prime[i]:
        for j in range(i, n + 1, i):
            sejun[j] = False

print(sejun.count(True))