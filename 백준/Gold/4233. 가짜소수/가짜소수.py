def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def pow(a, p, n):
    for _ in range(n):
        a = (a * a) % p
    return a

def check(p, a):
    val = 1
    pp = bin(p)[2:]
    for i in range(len(pp)):
        if pp[i] == '1':
            val *= pow(a, p, len(pp) - i - 1)
            val %= p
    if val == a:
        return True
    return False

while True:
    p, a = map(int, input().split())
    if p == 0 and a == 0:
        break
    if is_prime(p):
        print("no")
    else:
        if check(p, a):
            print("yes")
        else:
            print("no")