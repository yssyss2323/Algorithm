import sys
input = sys.stdin.readline

max_num = 2 * 10 ** 6
primes = set()
check = [False] * 2 + [True] * (max_num - 1)
for i in range(2, max_num + 1):
    if check[i]:
        primes.add(i)
        for j in range(2 * i, max_num + 1, i):
            check[j] = False

for _ in range(int(input())):
    curr = sum(list(map(int, input().split())))
    if curr == 2 or curr == 3:
        print("NO")
    elif curr % 2 == 0:
        print("YES")
    else:
        curr -= 2
        if curr <= max_num:
            if curr in primes:
                print("YES")
            else:
                print("NO")
        else:
            for prime in primes:
                if curr % prime == 0:
                    print("NO")
                    break
            else:
                print("YES")