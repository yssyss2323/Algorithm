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
    divs = []
    for i in range(1, int(x ** 0.5)):
        if x % i == 0:
            divs.append(i)
            divs.append(x // i)
    if int(x ** 0.5) ** 2 == x:
        divs.append(int(x ** 0.5))
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