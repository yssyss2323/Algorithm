a, b = map(int, input().split())
prime = [False] * 2 + [True] * (b - 1)
for i in range(2, b + 1):
    if prime[i]:
        for j in range(i * 2, b + 1, i):
            prime[j] = False

def underprime(n):
    i = 2
    count = 0
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            count += 1
    if n > 1:
        count += 1
    return prime[count]

answer = 0
for i in range(a, b + 1):
    if underprime(i):
        answer += 1
print(answer)
