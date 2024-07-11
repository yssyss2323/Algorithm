def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        prev1, prev2 = 1, 1
        for _ in range(n - 2):
            tmp = prev1 + prev2
            prev1 = prev2
            prev2 = tmp
    return prev2

n = int(input())
if n <= 2:
    print(1, 1)
else:
    print(fibo(n),n - 2)