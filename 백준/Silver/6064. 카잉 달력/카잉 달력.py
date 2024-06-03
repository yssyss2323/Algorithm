def lcm(a, b):
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)

    return a * b // gcd(a, b)

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    end_num = lcm(M, N)
    if x == M and y == N:
        print(end_num)
    else:
        x %= M
        y %= N
        for i in range(end_num // M + 1):
            test_num = (i * M) + x
            if test_num % N == y:
                print(test_num)
                break
        else:
            print(-1)
