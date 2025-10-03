primes = []
check = [False, False] + [True] * 118
for i in range(2, 119):
    if check[i]:
        primes.append(i)
        for j in range(i * 2, 119, i):
            check[j] = False

def solv(num):
    for i in range(len(primes)):
        if num - primes[i] in primes:
            return True
    return False

for _ in range(int(input())):
    a = int(input())
    if solv(a):
        print("Yes")
    else:
        print("No")