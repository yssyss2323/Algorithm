t = int(input())
for _ in range(t):
    a, b, c, p = map(int, input().split())
    if a % p and b % p and c % p:
        print(0)
    elif (a % p and b % p) or (a % p and c % p) or (b % p and c % p):
        print(0)
    else:
        print(1)