def fibo(n):
    tmp = [0, 1]
    for _ in range(n - 1):
        tmp = [tmp[1], tmp[0] + tmp[1]]
    return tmp[-1]


n = int(input())
if n == 0:
    print(0)
else:
    print(fibo(n))