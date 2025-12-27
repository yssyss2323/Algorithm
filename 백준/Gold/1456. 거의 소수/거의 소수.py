def check(n):
    end = int(n ** 0.5)
    primes = [False] * 2 + [True] * (end - 1)
    candid = []
    for i in range(2,end+1):
        if primes[i]:
            candid.append(i)
            for j in range(i*2, end+1, i):
                primes[j] = False
    cnt = 0
    for i in candid:
        x = 2
        while i ** x <= n:
            cnt += 1
            x += 1
    return cnt


a, b = map(int, input().split())
print(check(b) - check(a - 1))