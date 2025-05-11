n = int(input())

def find_factor(x):
    i = 2
    factors = []
    while i ** 2 <= x:
        if x % i == 0:
            factors.append(i)
            while x % i == 0:
                x //= i
        i += 1
    if x > 1:
        factors.append(x)
    return factors

def find_divs(x):
    i = 2
    divs = [1]
    while i ** 2 <= x:
        cnt = 0
        tmp = []
        while x % i == 0:
            cnt += 1
            tmp.append(i ** cnt)
            x //= i
        tmp2 = []
        for d in divs:
            for t in tmp:
                tmp2.append(d * t)
        divs += tmp2
        i += 1
    if x > 1:
        tmp = []
        for d in divs:
            tmp.append(d * x)
        divs += tmp
    divs.sort()
    return divs


if (n % 2 == 0) or (n % 5 == 0):
    print(-1)
else:
    n *= 9
    pi = n

    factors = find_factor(n)
    for f in factors:
        pi *= (f - 1)
        pi //= f

    divs = find_divs(pi)
    for div in divs:
        if (10 ** div - 1) % n == 0:
            print(div)
            break