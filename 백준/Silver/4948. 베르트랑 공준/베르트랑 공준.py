def primecount(x):
    primecheck = [False, False] + [True] * (2 * x - 1)
    length = len(primecheck)
    for i in range(2, length):
        if primecheck[i]:
            for j in range(2 * i, length, i):
                primecheck[j] = False
    count = 0
    for i in range(x + 1, 2 * x + 1):
        if primecheck[i]:
            count += 1
    return count

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(primecount(n))
